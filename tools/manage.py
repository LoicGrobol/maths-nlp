import pathlib
import shutil

import click
import pathspec
from livereload import Server, shell


@click.group()
def cli():
    pass


@cli.command(help="Watch and serve the book")
@click.argument(
    "book_path",
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
)
@click.option(
    "--path-output",
    default=pathlib.Path.cwd(),
    show_default=True,
    type=click.Path(writable=True, file_okay=False, path_type=pathlib.Path),
)
def serve(book_path: pathlib.Path, path_output: pathlib.Path):
    # TODO: find a way to reload the patterns if the ignore file changes
    # TODO: support nested gitignores
    if (ignores_file := book_path / ".gitignore").exists():
        with open(ignores_file) as in_stream:
            ps = pathspec.PathSpec.from_lines("gitwildmatch", in_stream)
        ignore = ps.match_file
    else:
        ignore = None

    cmd_args = [
        "jupyter-book",
        "build",
        str(book_path),
        "--path-output",
        str(path_output),
        "--verbose",
    ]
    shell([*cmd_args, "--all"])()
    server = Server()
    server.watch(book_path, shell(cmd_args), delay=1, ignore=ignore)
    server.serve(root=path_output / "_build/html")


@cli.command(help="Cleanup build files etc.")
@click.argument(
    "book_path",
    type=click.Path(exists=True, file_okay=False, path_type=pathlib.Path),
)
@click.option(
    "--path-output",
    default=pathlib.Path.cwd(),
    show_default=True,
    type=click.Path(writable=True, file_okay=False, path_type=pathlib.Path),
)
def clean(book_path: pathlib.Path, path_output: pathlib.Path):
    for p in (
        book_path / ".jupyterlite.doit.db",
        book_path / "_contents",
        path_output / "_build",
    ):
        if p.exists():
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()


if __name__ == "__main__":
    cli()
