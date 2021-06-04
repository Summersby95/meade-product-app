from datetime import datetime, timedelta


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


def update_dict_builder(field_list, request_pass, mongo_conn):
    details = {}
    if isinstance(field_list, list):
        for field in field_list:
            if field["field_type"] == "input" or field["field_type"] == "select":
                details[field["field_name"]] = request_pass.form.get(field["field_name"])
            elif field["field_type"] == "multiselect":
                details[field["field_name"]] = []
                for value in request_pass.form.getlist(field["field_name"]):
                    details[field["field_name"]].append(value)
            elif field["field_type"] == "date":
                details[field["field_name"]] = datetime.strptime(request_pass.form.get(field["field_name"]), '%d %B, %Y')
            elif field["field_type"] == "spec_grid":
                grid_options = []
                grid_table = mongo_conn.db[field["table_name"]].find()

                for option in grid_table:
                    grid_options.append(option["name"].lower().replace(" ", "_"))
                
                for option in grid_options:
                    details[option] = {
                        "rag":request_pass.form.get(option+"_rag"),
                        "tolerance":request_pass.form.get(option+"_tol"),
                        "comments":request_pass.form.get(option+"_com")
                    }
    elif isinstance(field_list, dict):
        for sub_field, sub_val in field_list.items():
            details[sub_field] = update_dict_builder(sub_val, request_pass, mongo_conn)
    
    return details
