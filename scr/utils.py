def add(a,b):
    return a+b

def subtract(a,b):
    if(a <= 0 or a < b):
        return "There is an error!"
    else:
        return a-b

def devision(a,b):
    if (a <= 0):
        return "There can't be devisible value which is devided  by 0 or negative number"
    else:
     return a/b