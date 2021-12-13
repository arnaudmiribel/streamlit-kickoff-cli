import click
import os
import webbrowser
from pathlib import Path
import subprocess

SCRIPT_TEMPLATE = """import streamlit as st

st.title("🎈 My new app!")
st.write("Welcome to your new app. Have fun editing it")
st.balloons()
"""

README_TEMPLATE = """
[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](DEPLOYED_APP_URL)

# 🎈 My new app

Some super description of my app
"""

GITIGNORE_TEMPLATE = """# Byte-compiled / optimized / DLL files
__pycache__/

# Notebook
.ipynb_checkpoints
profile_default/
ipython_config.py

# Streamlit secrets
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
    default=".",
)
@click.option(
    "--open_project_in_vs_code",
    default=True,
    help="Open VS code with the newly created file.",
)
@click.option(
    "--run_app",
    default=True,
    help="Run Streamlit script",
)
@click.option(
    "--open_app_in_browser",
    default=True,
    help="Open Streamlit app in browser",
)
def go(
    path: str,
    open_project_in_vs_code: bool,
    open_app_in_browser: bool,
    run_app: bool,
):

    header()

    project_path = Path(path)
    streamlit_script_path = Path(path) / "streamlit_app.py"

    # Create `streamlit_app.py`
    if not os.path.exists(streamlit_script_path):
        new_step(f"Creating new Streamlit script at {streamlit_script_path}...")
        with open(streamlit_script_path, "w") as f:
            f.write(SCRIPT_TEMPLATE)
    else:
        click.echo(click.style("Streamlit script already exists!"))

    # Create secrets
    new_step(f"Adding secrets to {streamlit_script_path}...")
    (project_path / ".streamlit").mkdir(parents=False, exist_ok=False)
    (project_path / ".streamlit" / "secrets.toml").touch()

    # Create requirements
    new_step(f"Adding requirements to {streamlit_script_path}...")
    (project_path / "requirements.txt").touch()

    # Create .gitignore
    new_step(f"Adding .gitignore to {streamlit_script_path}...")
    with open(project_path / ".gitignore", "w") as f:
        f.write(GITIGNORE_TEMPLATE)

    # Create README
    new_step(f"Adding README.md to {streamlit_script_path}...")
    with open(project_path / "README.md", "w") as f:
        f.write(README_TEMPLATE)

    # Open project in VS Code.
    if open_project_in_vs_code:
        new_step("Opening project in VS Code...")
        os.system(f'code "{project_path}"')
        os.system(f'code "{streamlit_script_path}"')

    # Run app.
    if run_app:
        new_step("Running Streamlit app")
        out = subprocess.check_output(["streamlit", "run", streamlit_script_path])
        new_step(out)

    # Open app in browser.
    if open_app_in_browser:
        browser = get_webbrowser()
        new_step("Opening app in the browser...")
        browser.open_new_tab()

    new_step("Closing...")