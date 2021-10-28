"""Masking Logic"""


def alpha_numeric_masker(value):
    masked_value = ""
    for x in value:
        if x.isalnum():
            masked_value += "X"
        else:
            masked_value += x
    return masked_value
