from AppKit import NSWorkspace


def get_active_app_name() -> str:
    shared_workspace = NSWorkspace.sharedWorkspace()
    active_app = shared_workspace.activeApplication()
    active_app_name = active_app["NSApplicationName"]
    return active_app_name
