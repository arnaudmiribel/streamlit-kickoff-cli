import click
import os
import webbrowser
from pathlib import Path

SCRIPT_TEMPLATE = """import streamlit as st

st.title("🎈 My new app!")
st.write("Welcome to your new app. Have fun editing it")
st.balloons()
"""


def get_webbrowser(os="macos"):
    return webbrowser.get()


def header():
    click.echo(
        click.style("\n\n🎈 Welcome to `st` 🎈\n\n", fg="red", bold=True),
        nl=True,
    )


def new_step(text):
    click.echo(click.style(f"➕ {text}", fg="green", bold=True), nl=True)


def warning(text):
    click.echo(click.style(f"{text}", fg="red", bold=True), nl=True)


@click.command()
@click.option(
    "-p",
    "--path",
    help="Path where you want to create your Streamlit project.",
)
@click.option(
    "--open_project_in_vs_code",
    default=1,
    help="Open VS code with the newly created file.",
)
@click.option(
    "--run_app",
    default=1,
    help="Run Streamlit script",
)
@click.option(
    "--open_app_in_browser",
    default=1,
    help="Open Streamlit app in browser",
)
def go(
    path: str,
    open_project_in_vs_code: int,
    open_app_in_browser: int,
    run_app: int,
):

    header()

    streamlit_script_path = Path(path) / "streamlit_app.py"

    # Create `streamlit_app.py`
    if not os.path.exists(streamlit_script_path):
        new_step(f"Creating new Streamlit script at {streamlit_script_path}...")
        with open(streamlit_script_path, "w") as f:
            f.write(SCRIPT_TEMPLATE)
    else:
        click.echo(click.style("Streamlit script already exists!"))

    # Open project in VS Code.
    if open_project_in_vs_code:
        new_step("Opening project in VS Code...")
        os.system(f'code "{streamlit_script_path}"')

    # Run app.
    if run_app:
        new_step("Running Streamlit app")
        import subprocess

        out = subprocess.check_output(["streamlit", "run", streamlit_script_path])

        new_step(out)

    # Open app in browser.
    if open_app_in_browser:
        browser = get_webbrowser()
        new_step("Opening app in the browser...")
        browser.open_new_tab()

    new_step("Closing...")