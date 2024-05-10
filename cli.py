import typer

app = typer.Typer()


@app.command()
def hello(name: str) -> None:
    print(f"Hello {name}!")


@app.command()
def goodbye(name: str) -> None:
    print(f"Goodbye {name}!")


if __name__ == "__main__":
    app()
