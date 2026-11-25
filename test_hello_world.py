import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).with_name("hello_world.py")


def run(*args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        capture_output=True,
        text=True,
        check=True,
    ).stdout


def test_greets_a_name_given_on_the_command_line():
    assert run("Ada") == "Hello Ada!\n"


def test_greets_the_world_with_no_name():
    assert run() == "Hello World!\n"


def test_shout_with_a_name():
    assert run("--shout", "Ada") == "HELLO ADA!\n"


def test_shout_without_a_name():
    assert run("--shout") == "HELLO WORLD!\n"


def test_shout_after_the_name():
    assert run("Ada", "--shout") == "HELLO ADA!\n"
