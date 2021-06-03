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

def process_field_list(field_dict, mongo_conn):
    for value in field_dict.values():
        if type(value) is dict:
            process_field_list(value, mongo_conn)
        elif type(value) is list:
            for sub_field in value:
                if sub_field["field_type"] in ["multiselect", "select", "spec_grid"]:
                    if ("options_type" in sub_field and sub_field["options_type"] == "table") or sub_field["field_type"] == "spec_grid":
                        options_table = mongo_conn.db[sub_field["table_name"]].find()
                        sub_field["options"] = []
                        for option in options_table:
                            sub_field["options"].append(option["name"])
                    
                