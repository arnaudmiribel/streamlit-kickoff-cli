import os
import subprocess
import webbrowser
from pathlib import Path

import click
from custom_logging import choice, error, new_step


def get_webbrowser(os="macos"):
    return webbrowser.get()

def _dev(ctx: click.Context, path: str = "streamlit_app.py"):
    choice("👩‍💻 Dev time! Let's open VS Code and your app in Chrome!")

    path_ = Path(path)
    # code_editor_command = ctx.obj["EDITOR_COMMAND"]

    if path_.is_file():

        # Open project in VS Code.
        new_step("Opening project in VS Code...")
        os.system(f"code . --new-window")
        os.system(f"code {path} --reuse-window")

        # Run app.
        new_step("Running app...")
        out = subprocess.check_output(["streamlit", "run", path])
        new_step(out)

        # Open app in browser.
        browser = ctx.obj["BROWSER"]
        click.echo(browser)
        new_step("Opening app in the browser...")
        browser.open_new_tab()

        # TODO: AppleScript to get the two windows side-by-side!

    else:
        error(
            f"Couldn't find the app script {path} in this directory. \nUse"
            " '-p' to specify a custom path"
        )


@click.command()
@click.option(
    "-p",
    "--path",
    default="streamlit_app.py",
    help="Path to the main script of the app (e.g. 'streamlit_app.py')",
    type=str,
)
@click.pass_context
def dev(ctx: click.Context, path: str):
    """👩‍💻 Dev time! Opens VS Code and your app in Chrome!"""
    _dev(ctx, path)
