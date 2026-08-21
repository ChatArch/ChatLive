"""CLI entrypoint for chatlive."""

from __future__ import annotations

import click
from chatstyle import add_tree_option

from chatlive import __version__


@click.group(name="chatlive", invoke_without_command=True)
@click.version_option(__version__, prog_name="chatlive")
@add_tree_option(renderer_options={"root_name": "chatlive"})
@click.pass_context
def main(ctx: click.Context) -> None:
    """ChatArch live tooling entrypoint."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


if __name__ == "__main__":
    main()
