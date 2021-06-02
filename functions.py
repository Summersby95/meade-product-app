from datetime import datetime

def date_to_string(conv_dict):
    for field, value in conv_dict.items():
        if isinstance(value, datetime):
            conv_dict[field] = value.strftime("%d %B, %Y")
        elif isinstance(value, dict):
            date_to_string(value)