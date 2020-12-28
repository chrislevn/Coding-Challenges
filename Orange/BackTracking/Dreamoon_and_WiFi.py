def permutaition(size_question, index): 
    global total_correct, total_created
    for i in range(2): 
        arr[index] = i
        if index == size_question - 1:
            temp_line = ''

            for ch in arr: 
                if ch == 0: 
                    temp_line += "-"
                elif ch == 1: 
                    temp_line += "+"
            temp = calSum(temp_line)
            total_created += 1

            if temp == delta:
                total_correct += 1
            
        else: 
            permutaition(size_question, index+1)


def calSum(line):
    result = 0 
    for ch in line: 
        if ch == "+":
            result += 1
        elif ch == "-": 
            result -= 1

    return result


if __name__ == "__main__":
    line_1 = input() 
    line_2 = input() 
    
    plus_1, minus_1  = 0, 0
    question_1 = 0

    plus_2, minus_2 = 0, 0
    question_2 = 0

    total_correct = 0
    total_created = 0

    check_1 = calSum(line_1)
    check_2 = calSum(line_2)

    delta = check_1 - check_2

    #line_1 check
    for ch in line_1: 
        if ch == "+":
            plus_1 += 1
        elif ch == "-": 
            minus_1 += 1

    for ch in line_2: 
        if ch == "+": 
            plus_2 += 1
        elif ch == "-": 
            minus_2 += 1
        else: 
            question_2 += 1

    if question_2 == 0: 
        if plus_1 == plus_2 and minus_1 == minus_2: 
            print("{0:.10f}".format(1))
        elif plus_1 > 0 and plus_2 == 0 and question_2 < (plus_1 + minus_1): 
            print("{0:.10f}".format(0))
        elif minus_1 > 0 and minus_2 == 0 and question_2 < (plus_1 + minus_1):  
            print("{0:.10f}".format(0))
        else:
            print("{0:.10f}".format(0))
    else: 
        remain_plus = plus_1 - plus_2
        remain_minus = minus_1 - minus_2
        # print(remain_plus, remain_minus)
        
        size_question = question_2
        arr = ['0'] * size_question
        if size_question > 0: 
            permutaition(size_question, 0)
    
        res = total_correct/total_created
        print("{0:.10f}".format(res))