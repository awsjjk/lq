count=0
def if_contains(x):
    string=str(x)
    if string.find('2') >= 0:
        string = string[string.find('2'):]
        if string.find('0') >= 0:
            string = string[string.find('0'):]
            if string.find('2') >= 0:
                string = string[string.find('2'):]
                if string.find('3') >= 0:
                    return True
for i in range(12345678,98765433):
    if not if_contains(i):
        count+=1
print(count)
85959030
