def cube (number):
    return number*number*number
def divi_by_3(number):
    if number % 3 == 0:
        return cube (number)
    else:
        return False
print(divi_by_3(8))
print(divi_by_3(27))