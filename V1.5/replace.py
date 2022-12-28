def replace(string,a,b):
    string = string.replace(a,b)
    print(type(string))
    if type(string) != float:
        string = float(string)
    print(type(string))
    return string


def average(list):
    total = 0
    average_grade = 0
    for grade in list:
        total += grade
    average_grade = total/ len(list)
    return average_grade