import string
import zxcvbn
import getpass
import re
import random
import requests
import hashlib
from faker import Faker


class PasswordController:

    @staticmethod
    def generate_passphrase(number):
        fake = Faker()
        passphrase = "".join(fake.words(nb=int(number)))
        return passphrase

    @staticmethod
    def generate_letters(number):
        if number is None:
            return ''
        letters = ''
        for _ in range(number):
            letters += random.choice(string.ascii_letters)
        return letters

    @staticmethod
    def generate_digits(number):
        if number is None:
            return ''
        digits = ''
        for _ in range(number):
            digits += random.choice(string.digits)
        return digits

    @staticmethod
    def generate_symbols(number):
        if number is None:
            return ''
        symbol = ''
        for _ in range(number):
            symbol += random.choice("#?@%^&*-")
        return symbol

    @staticmethod
    def generate_full_password(digits, letters, symbols):
        result = ''
        if digits is not None:
            result += digits
        if letters is not None:
            result += letters
        if symbols is not None:
            result += symbols

        result = list(result)
        random.shuffle(result)
        result = ''.join(result)
        return result

    @staticmethod
    def generate_password(number):
        password_regex = re.compile(
            "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$")
        password = None
        while password is None or not password_regex.fullmatch(password):
            password = random.choice(string.ascii_letters + string.digits)
            password += ''.join(random.choice(string.ascii_letters + string.digits + "#?!@$%^&*-")
                                for _ in range(number - 1))
            while password[0] in "#?!@$%^&*-":
                password = password[1:] + password[0]
        return password

    @staticmethod
    def ask_hidden_password():
        return getpass.getpass("Enter your password : \n - ")

    @staticmethod
    def calculate_details(password):
        strenght = zxcvbn.zxcvbn(password)
        return strenght

    @staticmethod
    def store_details(details):
        feed_back_result = []
        strenght = f"{details['score']}/4"
        crack_time = details['crack_times_display'][
            'offline_slow_hashing_1e4_per_second']
        feedback = details['feedback']
        warning = feedback.get('warning')
        suggestions = feedback.get('suggestions')
        if warning is not None:
            feed_back_result.append(warning)

        if suggestions is not None and len(suggestions) > 0:
            feed_back_result.append(suggestions[0])

        result = [strenght, crack_time, feed_back_result]
        return result

    @staticmethod
    def check_pwned_password(password):
        sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = sha1_password[:5]
        suffix = sha1_password[5:]

        url = f"https://api.pwnedpasswords.com/range/{prefix}"

        response = requests.get(url)

        # need to manage bad request

        hashes = response.text.splitlines()

        for h in hashes:
            if suffix in h:
                return True
        return False

    @staticmethod
    def calculate_pass_element(password):
        pass_length = len(password)
        lower = sum(1 for e in password if e in string.ascii_lowercase)
        upper = sum(1 for e in password if e in string.ascii_uppercase)
        digit = sum(1 for e in password if e in string.digits)
        symbol = sum(1 for e in password if e in "#?!@$%^&*-")
        pass_element_list = {
            "lower": lower,
            "upper": upper,
            "digit": digit,
            "symbol": symbol,
            "total_length": pass_length,
        }
        return pass_element_list
