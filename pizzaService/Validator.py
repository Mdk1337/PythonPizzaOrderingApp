import re


class Validator:
    @staticmethod
    def validateAddress(address):
        if len(address) == 0:
            return "Address"

        matchObj = re.match(r'[A-Za-z\s]+(\s|\,\s)\d*(\s|\,\s)?\w+', address)

        if not matchObj:
            return "Address (does not meet the requirements)"

    @staticmethod
    def validatePhone(phone):
        if len(phone) == 0:
            return "Phone number"

        matchObj = re.match(r'^(\d{8,11}|(\d{3}(\\|\/|-)\d{3,}(\\|\/|-)\d{3,}))$', phone)

        if not matchObj:
            return "Phone number (does not meet the requirements)"
