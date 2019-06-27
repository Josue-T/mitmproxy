import os.path
import typing

from mitmproxy import command
from mitmproxy import exceptions
from mitmproxy import flowfilter
from mitmproxy import io
from mitmproxy import ctx
from mitmproxy import flow
from mitmproxy import http2
from mitmproxy import viewitem
import mitmproxy.types


class Save:
    def __init__(self):
        self.stream = None
        self.filt = None
        self.active_flows: typing.Set[flow.Flow] = set()

    def load(self, loader):
        loader.add_option(
            "save_stream_file", typing.Optional[str], None,
            "Stream flows to file as they arrive. Prefix path with + to append."
        )
        loader.add_option(
            "save_stream_filter", typing.Optional[str], None,
            "Filter which flows are written to file."
        )

    def open_file(self, path):
        if path.startswith("+"):
            path = path[1:]
            mode = "ab"
        else:
            mode = "wb"
        path = os.path.expanduser(path)
        return open(path, mode)

    def start_stream_to_path(self, path, flt):
        try:
            f = self.open_file(path)
        except IOError as v:
            raise exceptions.OptionsError(str(v))
        self.stream = io.FilteredFlowWriter(f, flt)
        self.active_flows = set()

    def configure(self, updated):
        # We're already streaming - stop the previous stream and restart
        if "save_stream_filter" in updated:
            if ctx.options.save_stream_filter:
                self.filt = flowfilter.parse(ctx.options.save_stream_filter)
                if not self.filt:
                    raise exceptions.OptionsError(
                        "Invalid filter specification: %s" % ctx.options.save_stream_filter
                    )
            else:
                self.filt = None
        if "save_stream_file" in updated or "save_stream_filter" in updated:
            if self.stream:
                self.done()
            if ctx.options.save_stream_file:
                self.start_stream_to_path(ctx.options.save_stream_file, self.filt)

    @command.command("save.file")
    def save(self, viewitems: typing.Sequence[viewitem.ViewItem], path: mitmproxy.types.Path) -> None:
        """
            Save viewitems to a file. If the path starts with a +, viewitems are
            appended to the file, otherwise it is over-written.
        """

        try:
            f = self.open_file(path)
        except IOError as v:
            raise exceptions.CommandError(v) from v
        stream = io.FlowWriter(f)
        for i in viewitems:
            if isinstance(i, http2.HTTP2Frame):
                # Remove all other messages in the flow object
                i.flow.messages = [i]
            stream.add(i.flow)
        f.close()
        ctx.log.alert("Saved %s viewitems." % len(viewitems))

    def tcp_start(self, flow):
        if self.stream:
            self.active_flows.add(flow)

    def tcp_end(self, flow):
        if self.stream:
            self.stream.add(flow)
            self.active_flows.discard(flow)

    def websocket_start(self, flow):
        if self.stream:
            self.active_flows.add(flow)

    def websocket_end(self, flow):
        if self.stream:
            self.stream.add(flow)
            self.active_flows.discard(flow)

    def response(self, flow):
        if self.stream:
            self.stream.add(flow)
            self.active_flows.discard(flow)

    def request(self, flow):
        if self.stream:
            self.active_flows.add(flow)

    def done(self):
        if self.stream:
            for f in self.active_flows:
                self.stream.add(f)
            self.active_flows = set([])
            self.stream.fo.close()
            self.stream = None

    def http2_start(self, flow):
        if self.stream:
            self.active_flows.add(flow)

    def http2_frame(self, flow):
        """
        Save the last received frame
        """
        if self.stream:
            # Save only the last frame
            # it avoid to save many time the same frame
            flow_to_store = flow.copy()
            flow_to_store.messages = [flow.messages[-1]]
            self.stream.add(flow_to_store)

    def http2_end(self, flow):
        """
        Save the last flow state
        """
        if self.stream:
            # As we already saved each frame, just save the flow objet at his last state
            flow.messages = []
            self.stream.add(flow)
            self.active_flows.discard(flow)
