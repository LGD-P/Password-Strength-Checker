import rich_click as click
from click_controller import test_pass, passphrase, generate_password


click.rich_click.COMMAND_GROUPS = {
    "cli": [
        {
            "commands": ["generate-password", "passphrase", "test-pass"],
            "table_styles": {
                "show_lines": True,
                "row_styles": ["magenta", "yellow", "cyan", "green"],
                "border_style": "red",
                "box": "DOUBLE",
            },
        },
    ],
}


@click.group()
def cli():
    pass


cli.add_command(test_pass)
cli.add_command(passphrase)
cli.add_command(generate_password)

if __name__ == "__main__":
    cli()
