
class Validator:
    @staticmethod
    def raise_if_len_is_out_of_range(value, max_letters, message):
        if len(value) < max_letters:
            raise ValueError(message)

    @staticmethod
    def raise_if_speed_is_out_of_range(value, min_speed, max_speed, message):
        if value < min_speed or value > max_speed:
            raise ValueError(message)

    # @staticmethod
    # def
