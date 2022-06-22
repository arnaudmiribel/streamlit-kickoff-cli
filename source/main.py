import io
import os
import re
import subprocess
import sys
import webbrowser
from pathlib import Path
from urllib.parse import urlparse

import click
import pandas as pd
from cookiecutter.main import cookiecutter
from validators import url

DEFAULT_REPOSITORY = (
    "https://github.com/arnaudmiribel/st-template/blob/main/streamlit_app.py"
)

COOKIECUTTER_DEFAULT_DIRECTORY = "app"
COOKIECUTTER_REPOSITORY = (
    "https://github.com/arnaudmiribel/st-cookiecutter.git"
)


def get_webbrowser(os="macos"):
    return webbrowser.get()


def header():
    click.echo(
        click.style("\n\n🎈 Welcome to st 🎈\n\n", fg="red", bold=True),
        nl=True,
    )


def choice(text):
    click.echo(
        click.style(f"{text}", fg="red", bold=False),
        nl=True,
    )


def new_step(text):
    click.echo(click.style(f"➕ {text}", fg="green", bold=True), nl=True)


def warning(text):
    click.echo(click.style(f"{text}", fg="red", bold=True), nl=True)


def error(text):
    click.echo(click.style(f"💀💀💀 {text}", fg="red", bold=True), nl=True)


def success(text):
    click.echo(
        click.style(f"\n\n🎉 {text}\n\n", fg="green", bold=True), nl=True
    )


def _target_is_valid(target: str) -> bool:
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


@click.group()
def main():
    pass


def get_list() -> pd.DataFrame:
    lsof = subprocess.check_output(
        "lsof -nP -iTCP -sTCP:LISTEN",
        shell=True,
        stderr=subprocess.STDOUT,
    )

    df = pd.read_fwf(io.BytesIO(lsof))
    df = df[df.COMMAND.eq("Python")]
    df["PORT"] = df.NAME.apply(lambda d: d.split("(LISTEN)")[0].split(":")[1])
    df = df[df.PORT.str.startswith("85")]
    df["URL"] = "http://localhost:" + df.PORT
    df = df.rename(columns={"PID": "App ID", "URL": "App URL"})
    return df


@main.command()
def list():
    """🤯 List running Streamlit apps under ports 85**"""

    header()

    choice("Let's look at your apps running locally...")

    df = get_list()
    if df.empty:
        click.echo("Found no app running!")
    else:
        click.echo(
            df[["App ID", "App URL"]].set_index("App ID").drop_duplicates()
        )


@main.command()
def go():
    """😎 Open VS Code and your app in Chrome!"""
    click.echo("WIP")


@main.command()
@click.option(
    "-id", "--id", default=None, help="Kill a given app ID", type=int
)
@click.option(
    "-a",
    "--all",
    is_flag=True,
    default=False,
    help="Kill all Streamlit apps",
    type=bool,
)
def kill(id: int, all: bool):
    """🔫 Kill a given Streamlit app running locally!"""

    df = get_list()

    all_ids = df["App ID"].unique()
    if id is not None:
        if id in all_ids:
            click.echo(f"Killing {id}...")
            os.system(f"kill -9 {id}")
        else:
            error(
                f"This app ID is not valid. Valid IDs are {all_ids}. Use `st"
                " list` to learn more."
            )

    if all:
        click.echo(f"Killing all apps...")
        os.system(f"kill -9 {' '.join(all_ids)}")


@main.command()
def new():
    """🆕 Create a new Streamlit project from an empty template"""

    header()
    choice("You just asked for a `new` Streamlit project. Let's go!")

    path = click.prompt(
        "New directory name",
        type=str,
        default=COOKIECUTTER_DEFAULT_DIRECTORY,
    )

    if click.confirm("Want to customize the template?", default=False):
        app_title = click.prompt(
            "Title of your app", type=str, default="Balloons"
        )
        app_uses_secrets = click.confirm(
            "Will you be using secrets?", default=True
        )
        app_is_multi_page = click.confirm(
            "Will your app use more than one page?", default=True
        )
        app_uses_snowflake = click.confirm(
            "Are you connecting to Snowflake in this app?", default=False
        )

        cookiecutter(
            COOKIECUTTER_REPOSITORY,
            no_input=True,
            extra_context={
                "app_name": path,
                "app_title": app_title,
                "app_uses_secrets": int(app_uses_secrets),
                "app_is_multi_page": int(app_is_multi_page),
                "app_uses_snowflake": int(app_uses_snowflake),
            },
        )

    else:
        click.echo(
            "Fine! We will use default values and create your new Streamlit"
            f" app in '{path}'"
        )
        cookiecutter(
            COOKIECUTTER_REPOSITORY,
            no_input=True,
        )

    success(
        f"Successfully created your new Streamlit app in directory '{path}'!"
    )


@main.command()
@click.argument(
    "target",
    # help="Target GitHub repository URL.",
    default=DEFAULT_REPOSITORY,
)
@click.option(
    "-p",
    "--path",
    help="Path where you want to create your Streamlit project.",
    default="app",
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
def clone(
    target: str,
    path: str,
    open_project_in_vs_code: bool,
    open_app_in_browser: bool,
    run_app: bool,
):
    """👯 Clone an existing Streamlit project"""

    if target is not None:

        target_is_valid(target)

        (
            repository_url,
            project_path,
            streamlit_script_path,
            requirements_path,
        ) = parse_target(target)

        if path:
            project_path = Path(path)

        # Clone repo
        new_step(f"Cloning repo {repository_url}")
        os.system(f"git clone {repository_url} {project_path} -q")

        # Change directory to repo
        if path != ".":
            new_step(f"Changing directory to '{project_path}/'")
            os.chdir(project_path.name)

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


if __name__ == "__main__":
    main()
