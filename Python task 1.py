
def check_number(num):
    if isinstance(num, (int, float)):
        if num % 2 == 0:
            return "Парне число"
        else:
            return "Непарне число"
    else:
        return ""
       