
class Validator:
    @staticmethod
    def raise_if_len_is_empty_string(value, max_letters, message):
        if len(value.strip()) < max_letters:
            raise ValueError(message)

    @staticmethod
    def raise_if_len_is_out_of_range(value, max_value, message):
        if value < max_value:
            raise ValueError(message)

    @staticmethod
    def raise_if_name_is_not_unique(value, list_names, message):
        if value in list_names:
            raise ValueError(message)

    @staticmethod
    def return_if_len_is_out_of_range(value, max_value, message):
        if value < max_value:
            return message
