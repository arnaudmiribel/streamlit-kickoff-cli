import click
from cookiecutter.main import cookiecutter

from ..custom_logging import choice, success

DEFAULT_REPOSITORY = (
    "https://github.com/arnaudmiribel/st-template/blob/main/streamlit_app.py"
)

COOKIECUTTER_DEFAULT_DIRECTORY = "app"
COOKIECUTTER_REPOSITORY = (
    "https://github.com/arnaudmiribel/st-cookiecutter.git"
)

def _new(ctx: click.Context):
    choice("🆕 You just asked for a `new` Streamlit project. Let's go!")

    directory_name = click.prompt(
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
                "app_name": directory_name,
                "app_title": app_title,
                "app_uses_secrets": int(app_uses_secrets),
                "app_is_multi_page": int(app_is_multi_page),
                "app_uses_snowflake": int(app_uses_snowflake),
            },
        )

    else:
        click.echo(
            "Fine! We will use default values and create your new Streamlit"
            f" app in '{directory_name}'"
        )
        cookiecutter(
            COOKIECUTTER_REPOSITORY,
            no_input=True,
            extra_context={
                "app_name": directory_name,
            },
        )

    success(
        "Successfully created your new Streamlit app in directory"
        f" '{directory_name}/'!"
    )

    return directory_name


@click.command()
@click.pass_context
def new(ctx: click.Context,):
    """🆕 Create a new Streamlit project"""
    return _new(ctx)
