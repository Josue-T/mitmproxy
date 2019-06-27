
def map(km):
    km.add(":", "console.command ", ["global"], "Command prompt")
    km.add("?", "console.view.help", ["global"], "View help")
    km.add("B", "browser.start", ["global"], "Start an attached browser")
    km.add("C", "console.view.commands", ["global"], "View commands")
    km.add("K", "console.view.keybindings", ["global"], "View key bindings")
    km.add("O", "console.view.options", ["global"], "View options")
    km.add("E", "console.view.eventlog", ["global"], "View event log")
    km.add("2", "console.view.http2", ["global"], "View the HTTP/2 flow")
    km.add("Q", "console.exit", ["global"], "Exit immediately")
    km.add("q", "console.view.pop", ["global"], "Exit the current view")
    km.add("-", "console.layout.cycle", ["global"], "Cycle to next layout")
    km.add("shift tab", "console.panes.next", ["global"], "Focus next layout pane")
    km.add("ctrl right", "console.panes.next", ["global"], "Focus next layout pane")
    km.add("P", "console.view.item @focus", ["global"], "View item details")

    km.add("g", "console.nav.start", ["global"], "Go to start")
    km.add("G", "console.nav.end", ["global"], "Go to end")
    km.add("k", "console.nav.up", ["global"], "Up")
    km.add("j", "console.nav.down", ["global"], "Down")
    km.add("l", "console.nav.right", ["global"], "Right")
    km.add("h", "console.nav.left", ["global"], "Left")
    km.add("tab", "console.nav.next", ["global"], "Next")
    km.add("enter", "console.nav.select", ["global"], "Select")
    km.add("space", "console.nav.pagedown", ["global"], "Page down")
    km.add("ctrl f", "console.nav.pagedown", ["global"], "Page down")
    km.add("ctrl b", "console.nav.pageup", ["global"], "Page up")

    km.add("I", "set intercept_active=toggle", ["global"], "Toggle intercept")
    km.add("i", "console.command.set intercept", ["global"], "Set intercept")
    km.add("W", "console.command.set save_stream_file", ["global"], "Stream to file")
    km.add("A", "item.resume @all", ["flowlist_http1", "flowlist_http2",
                                     "flowview_http1", "flowview_http2"], "Resume all intercepted items")
    km.add("a", "item.resume @focus", ["flowlist_http1", "flowlist_http2",
                                       "flowview_http1", "flowview_http2"], "Resume this intercepted items")
    km.add(
        "b", "console.command cut.save @focus response.content ",
        ["flowlist_http1", "flowlist_http2", "flowview_http1", "flowview_http2"],
        "Save response body to file"
    )
    km.add("d", "view.http1.items.remove @focus", ["flowlist_http1", "flowview_http1"], "Delete item from view")
    km.add("d", "view.http2.items.remove @focus", ["flowlist_http2", "flowview_http2"], "Delete item from view")
    km.add("D", "view.http1.items.duplicate @focus", ["flowlist_http1", "flowview_http1"], "Duplicate item")
    km.add("D", "view.http2.items.duplicate @focus", ["flowlist_http2", "flowview_http2"], "Duplicate item")
    km.add(
        "e",
        """
        console.choose.cmd Format export.formats
        console.command export.file {choice} @focus
        """,
        ["flowlist_http1", "flowlist_http2", "flowview_http1", "flowview_http2"],
        "Export this flow to file"
    )
    km.add("f", "console.command.set view_filter_http1", ["flowlist_http1"], "Set view filter")
    km.add("f", "console.command.set view_filter_http2", ["flowlist_http2"], "Set view filter")
    km.add("F", "set console_focus_follow=toggle", ["flowlist_http1", "flowlist_http2"], "Set focus follow")
    km.add(
        "ctrl l",
        "console.command cut.clip ",
        ["flowlist_http1", "flowlist_http2", "flowview_http1", "flowview_http2"],
        "Send cuts to clipboard"
    )
    km.add("L", "console.command view.load ", ["flowlist_http1", "flowlist_http2"], "Load flows from file")
    km.add("m", "item.mark.toggle @focus", ["flowlist_http1", "flowlist_http2"], "Toggle mark on this item")
    km.add("M", "view.http1.properties.marked.toggle", ["flowlist_http1"], "Toggle viewing marked items")
    km.add("M", "view.http2.properties.marked.toggle", ["flowlist_http2"], "Toggle viewing marked items")
    km.add(
        "n",
        "console.command view.flows.create get https://example.com/",
        ["flowlist_http1"],
        "Create a new flow"
    )
    km.add(
        "o",
        """
        console.choose.cmd Order view.http1.order.options
        set view_order_http1={choice}
        """,
        ["flowlist_http1"],
        "Set flow list order"
    )
    km.add(
        "o",
        """
        console.choose.cmd Order view.http2.order.options
        set view_order_http2={choice}
        """,
        ["flowlist_http2"],
        "Set flow list order"
    )
    km.add("r", "replay.client @focus", ["flowlist_http1", "flowlist_http2", "flowview_http1", "flowview_http2"], "Replay this flow")
    km.add("S", "console.command replay.server ", ["flowlist_http1", "flowlist_http2"], "Start server replay")
    km.add("v", "set view_order_http1_reversed=toggle", ["flowlist_http1"], "Reverse flow list order")
    km.add("v", "set view_order_http2_reversed=toggle", ["flowlist_http2"], "Reverse flow list order")
    km.add("U", "item.mark @all false", ["flowlist_http1", "flowlist_http2"], "Un-set all marks")
    km.add("w", "console.command save.file @shown ", ["flowlist_http1", "flowlist_http2"], "Save listed flows to file")
    km.add("V", "item.revert @focus", ["flowlist_http1", "flowlist_http2",
                                       "flowview_http1", "flowview_http2"], "Revert changes to this item")
    km.add("X", "item.kill @focus", ["flowlist_http1", "flowlist_http2"], "Kill this item")
    km.add("z", "view.http1.items.remove @all", ["flowlist_http1"], "Clear flow list")
    km.add("z", "view.http2.items.remove @all", ["flowlist_http2", "flowlist_http2"], "Clear flow list")
    km.add("Z", "view.http1.items.remove @hidden", ["flowlist_http1"], "Purge all flows not showing")
    km.add("Z", "view.http2.items.remove @hidden", ["flowlist_http2"], "Purge all flows not showing")
    km.add(
        "|",
        "console.command script.run @focus ",
        ["flowlist_http1", "flowlist_http2", "flowview_http1", "flowview_http2"],
        "Run a script on this flow"
    )

    km.add(
        "e",
        """
        console.choose.cmd Part console.edit.focus.options
        console.edit.focus {choice}
        """,
        ["flowview_http1", "flowview_http2"],
        "Edit a flow component"
    )
    km.add(
        "f",
        "view.http1.settings.setval.toggle @focus fullcontents",
        ["flowview_http1"],
        "Toggle viewing full contents on this item",
    )
    km.add(
        "f",
        "view.http2.settings.setval.toggle @focus fullcontents",
        ["flowview_http2"],
        "Toggle viewing full contents on this item",
    )
    km.add("w", "console.command save.file @focus ", ["flowview_http1", "flowview_http2"], "Save flow to file")
    km.add("space", "view.http1.focus.next", ["flowview_http1"], "Go to next flow")
    km.add("space", "view.http2.focus.next", ["flowview_http2"], "Go to next flow")

    km.add(
        "v",
        """
        console.choose "View Part" request,response
        console.bodyview @focus {choice}
        """,
        ["flowview_http1", "flowview_http2"],
        "View flow body in an external viewer"
    )
    km.add("p", "view.http1.focus.prev", ["flowview_http1"], "Go to previous flow")
    km.add("p", "view.http2.focus.prev", ["flowview_http2"], "Go to previous flow")
    km.add(
        "m",
        """
        console.choose.cmd Mode console.flowview.mode.options
        console.flowview.mode.set {choice}
        """,
        ["flowview_http1", "flowview_http2"],
        "Set flow view mode"
    )
    km.add(
        "z",
        """
        console.choose "Part" request,response
        item.encode.toggle @focus {choice}
        """,
        ["flowview_http1", "flowview_http2"],
        "Encode/decode flow body"
    )

    km.add("L", "console.command options.load ", ["options"], "Load from file")
    km.add("S", "console.command options.save ", ["options"], "Save to file")
    km.add("D", "options.reset", ["options"], "Reset all options")
    km.add("d", "console.options.reset.focus", ["options"], "Reset this option")

    km.add("a", "console.grideditor.add", ["grideditor"], "Add a row after cursor")
    km.add("A", "console.grideditor.insert", ["grideditor"], "Insert a row before cursor")
    km.add("d", "console.grideditor.delete", ["grideditor"], "Delete this row")
    km.add(
        "r",
        "console.command console.grideditor.load",
        ["grideditor"],
        "Read unescaped data into the current cell from file"
    )
    km.add(
        "R",
        "console.command console.grideditor.load_escaped",
        ["grideditor"],
        "Load a Python-style escaped string into the current cell from file"
    )
    km.add("e", "console.grideditor.editor", ["grideditor"], "Edit in external editor")
    km.add(
        "w",
        "console.command console.grideditor.save ",
        ["grideditor"],
        "Save data to file as CSV"
    )

    km.add("z", "eventstore.clear", ["eventlog"], "Clear")

    km.add(
        "a",
        """
        console.choose.cmd "Context" console.key.contexts
        console.command console.key.bind {choice}
        """,
        ["keybindings"],
        "Add a key binding"
    )
    km.add(
        "d",
        "console.key.unbind.focus",
        ["keybindings"],
        "Unbind the currently focused key binding"
    )
    km.add(
        "x",
        "console.key.execute.focus",
        ["keybindings"],
        "Execute the currently focused key binding"
    )
    km.add(
        "enter",
        "console.key.edit.focus",
        ["keybindings"],
        "Edit the currently focused key binding"
    )
