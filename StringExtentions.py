def SnakeCaseToCamelCase(input):
    return input.replace("_","")

def CamelCaseToSnakeCase(input):
    result=""
    for char in input:
        if char.isupper():
            result+="_"+char
        else:
            result+=char
    if result[0]=="_":
        result = result[1:]
    return result

