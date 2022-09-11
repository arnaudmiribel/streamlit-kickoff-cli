import os
import sys

import click
from custom_logging import error
from list.command import get_list


@click.command()
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
@click.pass_context
def kill(ctx: click.Context, id: int, all: bool):
    """🔫 Kill a given Streamlit app running locally!"""

    if (id is not None and all) or (id is None and not all):
        error(
            "You must either input the app process ID --id or choose --all to"
            " kill all apps at once."
        )
        sys.exit()

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
        os.system(f"kill -9 {' '.join(map(str, all_ids))}")
        click.echo(f"Succesfully killed ")
