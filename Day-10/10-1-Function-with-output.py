# Function with output

def format_name(f_name, l_name):
    """This function takes two parameter f_name and l_name and return the full name formatted as
    title-cased string"""
    if f_name == "" or l_name == "":
        return "invalid Input"
    formatted_name = (f_name + ' ' + l_name).title()
    return formatted_name


print(format_name("Zaphkiel", ""))
