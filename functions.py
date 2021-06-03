from datetime import datetime

def date_to_string(conv_dict):
    for field, value in conv_dict.items():
        if isinstance(value, datetime):
            conv_dict[field] = value.strftime("%d %B, %Y")
        elif isinstance(value, dict):
            date_to_string(value)

def product_mark(product):
    if (product["start_date"].date() < (datetime.now()).date() + timedelta(days=7)):
        if product["status"] == "Completed - Production Ready":
            product["colour"] = "green"
        else:
            product["colour"] = "red"
    elif (product["start_date"].date() < (datetime.now()).date() + timedelta(days=14)):
        if product["status"] != "Completed - Production Ready":
            product["colour"] = "yellow"

    # Check if the product was created in the last day, 
    # if it was mark it to add a badge to it in the table
    if (product["created_on"]).date() + timedelta(days=1) > (datetime.now()).date():
        product["new"] = True

