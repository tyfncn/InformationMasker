"""Masking Logic"""


def alpha_numeric_masker(value):
    alphanumeric_letters = "abcçdefgğhıijklmnoöpqrsştuüvwxyz" \
                           "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZ" \
                           "0123456789"
    masked_value = ""
    for current_char in value:
        if current_char in alphanumeric_letters :
            masked_value += "X"
        else:
            masked_value += current_char
    return masked_value
