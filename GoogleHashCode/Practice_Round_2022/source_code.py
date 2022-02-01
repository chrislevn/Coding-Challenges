class Client: 
    def __init__(self, id):
        self.id = id 
        self.likes = []
        self.dislikes = []
    
    def add_like(self, like):
        self.likes.append(like)
    
    def add_dislike(self, dislike):
        self.dislikes.append(dislike)

    def __str__(self):
        return str(self.id) + " " + str(self.likes) + " " + str(self.dislikes)

def solve(input, output):
    with open(input) as f:
        lines = f.readlines()
        c = int(lines[0])
        customer_list = []
        likes_dict = set()
        dislikes_dict = set()

        for i in range(c):
            # print(lines[i])

            customer = Client(i)
            l = list(lines[i*2+1].replace("\n", "").split(" "))
            d = list(lines[i*2+2].replace("\n", "").split(" "))


            if int(l[0]) > 0: 
                for j in range(1, len(l)): 
                    customer.add_like(l[j])
                    likes_dict.add(l[j])
            
            if int(d[0]) > 0:
                for j in range(1, len(d)):
                    customer.add_dislike(d[j])
                    dislikes_dict.add(d[j])

            customer_list.append(customer)
        
        for item in dislikes_dict: 
            if item in likes_dict: 
                likes_dict.remove(item)
            
        result_len = len(likes_dict)
        result = sorted(list(likes_dict))
        result = " ".join(str(x) for x in result)

        final = str(result_len) + " " + result
        curr_max = test(final, customer_list)
        print("curr max", curr_max)

        for i in range(len(customer_list)):
            temp_count = 0
            check_likes = set(customer_list[i].likes)
            check_dislikes = set(customer_list[i].dislikes)

            for j in range(len(customer_list)):
                temp_check = True
                if i == j:
                    continue
                else: 
                    for item in customer_list[j].dislikes:
                        if item not in check_likes: 
                            temp_check = False 
                    if temp_check is False:
                        temp_count += 1
            print(temp_count)
                        
        # print(final)

        with open(output, 'w') as f:
            f.write(final)


def test(result, customer_list): 
    result = list(result.split(" "))
    count = 0
    result_num = result[0]
    ingredient_list = result[1:]

    for customer in customer_list:
        check_like = all(item in ingredient_list for item in customer.likes)
        check_dislike = any(item in ingredient_list for item in customer.dislikes)

        if check_like and not check_dislike: 
            count += 1

    return count



# solve("GoogleHashCode/Practice_Round_2022/a_an_example.in.txt", "GoogleHashCode/Practice_Round_2022/part_a.txt")
# solve("GoogleHashCode/Practice_Round_2022/b_basic.in.txt", "GoogleHashCode/Practice_Round_2022/part_b.txt")
solve("GoogleHashCode/Practice_Round_2022/c_coarse.in.txt", "GoogleHashCode/Practice_Round_2022/part_c.txt")
# solve("GoogleHashCode/Practice_Round_2022/d_difficult.in.txt", "GoogleHashCode/Practice_Round_2022/part_d.txt")
# solve("GoogleHashCode/Practice_Round_2022/e_elaborate.in.txt", "GoogleHashCode/Practice_Round_2022/part_e.txt")

