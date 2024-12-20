import unicodedata


class NVCommon:
    # Normalize function
    @staticmethod
    def remove_accents(input_str):
        nfkd_form = unicodedata.normalize('NFKD', input_str)
        return ''.join(c for c in nfkd_form if not unicodedata.combining(c))

    # Function to validate numeric input
    @staticmethod
    def validate_number_input(action, value_if_allowed):
        if action == "1":  # 1 means insertion
            return value_if_allowed.isdigit()  # Allow only digits
        return True
