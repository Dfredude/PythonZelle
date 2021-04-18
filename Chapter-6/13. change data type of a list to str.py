def modifyListToNumbers(str_list):
    for i in range(len(str_list)):
        str_list[i] = int(str_list[i])

strList = ['25', '590', '88']
(modifyListToNumbers(strList))
print(strList)
