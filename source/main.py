import os
import re
import subprocess
import sys
import webbrowser
from pathlib import Path
from urllib.parse import urlparse

import click
from validators import url


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


def error(text):
    click.echo(click.style(f"💀💀💀 {text}", fg="red", bold=True), nl=True)


def _target_is_valid(target: str):
    if target is not None and url(target):
        if "github" in target and target.endswith(".py"):
            return True

    return False


def target_is_valid(target: str):
    """Checks if target is valid. Otherwise throw exception and exit.

    Args:
        target (str): Target repository URL
    """
    if not _target_is_valid(target=target):
        error(
            "Input target must be a GitHub URL that points to the main .py"
            " script"
        )
        sys.exit()


def parse_target(target: str):
    """Parse the target repository URL into useful pieces

    Args:
        target (str): Target repository URL

    Returns:
        str: Repository GitHub URL
        pathlib.Path: Project path
        pathlib.Path: Streamlit main script path
        pathlib.Path: Requirements file path
    """
    repository_url = urlparse(target).path
    repository_url = re.split("/blob/", target)[0]
    project_path = Path(repository_url.strip("/").rsplit("/", 1)[-1])
    streamlit_script_path = (
        project_path / re.split("/blob/[a-z]+/", target)[-1]
    )
    requirements_path = project_path / "requirements.txt"

    return (
        repository_url,
        project_path,
        streamlit_script_path,
        requirements_path,
    )


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
@click.argument("target", required=False)
def go(
    target: str,
    path: str,
    open_project_in_vs_code: bool,
    open_app_in_browser: bool,
    run_app: bool,
):

    header()

    if target is not None:

        target_is_valid(target)

        (
            repository_url,
            project_path,
            streamlit_script_path,
            requirements_path,
        ) = parse_target(target)

        # Clone repo
        new_step(f"Cloning repo {repository_url}")
        os.system(f"git clone {repository_url} -q")

        # Change directory to repo
        new_step(f"Changing directory to {project_path}")
        os.chdir(project_path.name)

        # Create .gitignore
        new_step(f"Adding .gitignore to {project_path.name}...")
        with open(".gitignore", "w") as f:
            f.write(GITIGNORE_TEMPLATE)

        # Create a new environment with venv
        new_step("Creating a new environment with venv")
        os.system("python3 -m venv .venv")
        os.system("source .venv/bin/activate")

        # Install dependencies
        new_step("Installing dependencies")
        os.system(f"pip3 install --quiet -r {requirements_path.name}")

        # Open project in VS Code.
        if open_project_in_vs_code:
            new_step("Opening project in VS Code...")
            os.system(f"code .")
            os.system(f"code {streamlit_script_path.name}")

        # Run app
        if run_app:
            new_step("Running app...")
            out = subprocess.check_output(
                ["streamlit", "run", streamlit_script_path.name]
            )
            new_step(out)

        # Open app in browser.
        if open_app_in_browser:
            browser = get_webbrowser()
            new_step("Opening app in the browser...")
            browser.open_new_tab()

        new_step("Closing...")

    else:

        go(
            target="https://github.com/arnaudmiribel/st-template/blob/main/streamlit_app.py",
            path=path,
            open_project_in_vs_code=open_project_in_vs_code,
            open_app_in_browser=open_app_in_browser,
            run_app=run_app,
        )
