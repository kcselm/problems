def digital_root(number):
    numbers = map(int,str(number))
    answer = 0
    for n in numbers:
        answer += n
    # print(answer)

    if (answer > 10):
        return digital_root(answer)
    else:
        return answer

    #--better--
    # return number if number < 10 else digital_root(sum(map(int,str(number))))
    
print(digital_root(942))
