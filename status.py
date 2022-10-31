from datetime import datetime
from sys import stdout
from time import sleep
from subprocess import check_output
from json import loads as json_loads


def write(data: str) -> None:
    stdout.write(data)
    stdout.flush()


def get_date() -> str:
    now = datetime.now()
    return now.strftime("%d.%m.%Y %H:%M:%S")


def get_keyboard_layout() -> str:
    json_result = check_output(["swaymsg", "-t", "get_inputs"])
    layout: str = json_loads(json_result)[-1]["xkb_active_layout_name"]
    return "Русский" if layout == "Russian" else "English"


def update() -> None:
    date = get_date()
    layout = get_keyboard_layout()
    write(f"{layout}    {date}")


while True:
    update()
    sleep(0.5)
