def numberToWordsV1(number):
    nat_num = ["Cero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    if number < 10: 
        new_list = [nat_num[number]]
        return new_list
    else:
        number_str = str(number)
        new_number = int(number_str[:-1])
        last_digit_of_num = int(number_str[-1])
        rslt = numberToWordsV1(new_number)
        rslt.append(nat_num[last_digit_of_num])
        return rslt

test1 = numberToWordsV1(78209)
print(test1)

def numberToWordsV2(number):
    numbers_words = ["Cero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    if number < 10:
        return [numbers_words[number]]
    else:
        new_number = number // 10
        last_digit_of_num = number%10
        rslt = numberToWordsV2(new_number)
        rslt.append(numbers_words[last_digit_of_num])
        return rslt

test2 = numberToWordsV2(78209)
print(test2)



