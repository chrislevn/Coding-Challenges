isbn_input = input()
split_list = isbn_input.split("-")
list_isbn = []

for i in range(len(split_list) - 1): 
    tmp_list = []
    for d in split_list[i]: 
        tmp_list.append(int(d))
    for j in tmp_list: 
        list_isbn.append(j)

if split_list[-1] == "X": 
    list_isbn.append(10)
else:
    last = int(split_list[-1])
    list_isbn.append(last)

s1, s2 = [], []
temp_s1, temp_s2 = 0, 0 

for i in range(len(list_isbn)): 
    tmp_1 = list_isbn[i] + temp_s1
    s1.append(tmp_1) 
    temp_s1 = tmp_1

res = sum(s1)

if res % 11 == 0: 
    print(isbn_input + " is correct.")
else: 
    print(isbn_input + " is incorrect.")