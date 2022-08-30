import io
import subprocess

import click
import pandas as pd
from custom_logging import choice


def get_list() -> pd.DataFrame:
    """Listen to Python apps running on port 85** and collect their PID

    Returns:
        pd.DataFrame: Dataframe with Python apps and PID
    """
    lsof = subprocess.check_output(
        "lsof -nP -iTCP -sTCP:LISTEN",
        shell=True,
        stderr=subprocess.STDOUT,
    )

    df = pd.read_fwf(io.BytesIO(lsof))
    df = df[df.COMMAND.str.lower().str.contains("python")]
    df["PORT"] = df.NAME.apply(lambda d: d.split("(LISTEN)")[0].split(":")[1])
    df = df[df.PORT.str.startswith("85")]
    df["URL"] = "http://localhost:" + df.PORT
    df = df.rename(columns={"PID": "App ID", "URL": "App URL"})
    return df


@click.command()
@click.pass_context
def list(ctx: click.Context,):
    """🤯 List running Streamlit apps under ports 85**"""

    choice("Let's look at your apps running locally...")

    df = get_list()
    if df.empty:
        click.echo("Found no app running!")
    else:
        click.echo(
            df[["App ID", "App URL"]].set_index("App ID").drop_duplicates()
        )
