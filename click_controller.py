import rich_click as click
from logic_controller import PasswordController
from message_views import UserMessage


@click.command()
@click.option("--password", "-p", help="Specify the password")
def test_pass(password):
    """- Test your password here. Make sure it hasn't been leaked thanks to the haveibeenpwn api"""
    if password is None:
        click.echo("Please specify the password you want to test")
        return

    pawned = PasswordController.check_pwned_password(password)
    element = PasswordController.calculate_pass_element(password)
    strength = PasswordController.calculate_details(password)
    stored_strength = PasswordController.store_details(strength)

    UserMessage.display_pass_build(element)
    UserMessage.display_pass_strenght(stored_strength)
    UserMessage.display_pawn(pawned)


@click.command()
@click.option("--passphrase", "-pph", help="Specify number of words")
def passphrase(passphrase):
    """- Use -pph and to generate passphrases. A simple and effective way of generating secure passwords."""

    if passphrase and not passphrase.isdigit():
        raise click.BadParameter('The --passphrase option must be a digit.')

    pass_phrase = PasswordController.generate_passphrase(int(passphrase))
    UserMessage.display_passphrase(pass_phrase)


@click.command()
@click.option("--letters", "-l", help="Number of letters")
@click.option("--digits", "-d", help="Number of digits")
@click.option("--symbols", "-s", help="Number of symbols")
def generate_password(letters, digits, symbols):
    """- Choose the elements : letters -l numbers -d symbols -s and the number want to generate a secure password."""

    if letters and not letters.isdigit():
        raise click.BadParameter('The --letters option must be a digit.')
    if digits and not digits.isdigit():
        raise click.BadParameter('The --digits option must be a digit.')
    if symbols and not symbols.isdigit():
        raise click.BadParameter('The --symbols option must be a digit.')

    letters = None if not letters else PasswordController.generate_letters(
        int(letters))

    digits = None if not digits else PasswordController.generate_digits(
        int(digits))

    symbols = None if not symbols else PasswordController.generate_symbols(
        int(symbols))

    password = PasswordController.generate_full_password(letters, digits,
                                                         symbols)

    UserMessage.color_result(password)
