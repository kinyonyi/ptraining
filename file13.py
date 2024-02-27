#modules
def changed(data):
    return f"{data[0]}{data[-1]}{data[3:5]}"

def multipleNumbers(array):
    result = 1
    for x in array:
        result = x * result
    return result

def reversedString(data):
    return data[::-1]