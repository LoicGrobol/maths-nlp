import glob
import pathlib
import click
from livereload import Server, shell
import pathspec


@click.command(help="Watch and serve the book")
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
    ]
    shell([*cmd_args, "--all"])()
    server = Server()
    server.watch(book_path, shell(cmd_args), delay=1, ignore=ignore)
    server.serve(root=path_output / "_build/html")


if __name__ == "__main__":
    serve()
