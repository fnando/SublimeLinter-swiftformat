from SublimeLinter.lint import Linter, util
import sublime
import os.path


class SwiftFormat(Linter):
    """Provides an interface to swiftformat."""

    regex = r"^:(?P<line>\d+):(?P<col>\d+): (?:(?P<error>error)|(?P<warning>warning)): (?P<message>.+)$"
    defaults = {"selector": "source.swift"}
    error_stream = util.STREAM_STDERR

    def cmd(self):
        command = ["swiftformat", "--lint"]
        folders = sublime.active_window().folders()
        file_name = sublime.active_window().active_view().file_name()
        project_root = [x for x in folders if file_name.startswith(x + "/")][0]

        if project_root:
            config_path = os.path.join(project_root, ".swiftformat")

            if os.path.isfile(config_path):
                command.append("--config")
                command.append(config_path)

        command.append("stdin")

        return command
