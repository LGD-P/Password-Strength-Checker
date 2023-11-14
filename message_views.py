from rich.console import Console


class UserMessage():
    c = Console()

    @staticmethod
    def display_pawn(password):

        if password:
            UserMessage.c.print(
                "\n[bold red] According to [blue]https://haveibeenpwned.com/Passwords[/blue] Your password has been "
                "compromised in a data breach.\n\n Please change it immediately.[bold red]"
            )
        else:
            UserMessage.c.print(
                "\n[green]According to [blue]https://haveibeenpwned.com/Passwords[/blue], your password has not been "
                "leaked.\n "
                "\nHowever, please remain vigilant, use strong passwords, and change them regularly.[green]"
            )

    @staticmethod
    def display_pass_build(pass_element):
        UserMessage.c.print("\n [blue]Password constitution: \n\n"
                            f" - Length : [green]{pass_element['total_length']}[/green]\n"
                            f" - Lower : [green]{pass_element['lower']}[/green]\n"
                            f" - Upper : [green]{pass_element['upper']}[/green]\n"
                            f" - Digit : [green]{pass_element['digit']}[/green]\n"
                            f" - Symbol : [green]{pass_element['symbol']}[/green]")

    @staticmethod
    def score_message(score):
        score_result = {
            "0/4": "[red]❌ Respect yourself... don't do that[/red]",
            "1/4": "[dark_orange3]Very weak you can do better ![/dark_orange3]",
            "2/4": "[gold3]Medium we are close to something interesting ![/gold3]",
            "3/4":
                "[dark_olive_green3]Good password but can be stronger[/dark_olive_green3]",
            "4/4":
                "[green_yellow] This is a strong one congratulations[/green_yellow]"
        }
        return score_result.get(score, "None")

    @staticmethod
    def display_pass_strenght(score):
        UserMessage.c.print(
            "\n [blue]Password strenght: \n\n"
            f" - Strength : {UserMessage.score_message(score[0])}\n"
            f" - Common Crack Time : [green]{score[1]}[/green]\n")
        if len(score[2][0]) > 1:
            UserMessage.c.print(
                f"[blue] - Feedback:  [green]{score[2]}[/green]  [/blue]")

    @staticmethod
    def color_result(result):
        output = ""
        for char in result:
            if char.isdigit():
                output += "[orange_red1]" + char + "[/orange_red1]"
            elif char.isalpha():
                output += "[yellow1]" + char + "[/yellow1]"
            else:
                output += "[bold red1]" + char + "[/bold red1]"
        return UserMessage.c.print(f"\n[blue]- Here your password ==> "
                                   f"{output}\n\n"
                                   f"- You should test it ! copy and past the following command : \n\n"
                                   f'[green]python main.py  test-pass -p "{output}"[green]\n')

    @staticmethod
    def display_passphrase(number):
        UserMessage.c.print(f"\n[blue]- Here your passphrase ==> " \
                            f"[green]{number}[/green]\n\n" \
                            f"- You should test it ! copy and past the following command : \n\n" \
                            f'[green]python main.py  test-pass -p "{number}"[green]\n')
