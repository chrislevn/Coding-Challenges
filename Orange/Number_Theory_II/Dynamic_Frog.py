
if __name__ == "__main__": 
    t = int(input())
    for i in range(t): 
        n, d = map(int, input().split())

        if n < 1: 
            rock_input = input()
            print("Case {}: {}".format(i+1, d))
        else:
            stones = [['B', 0]]
            rock_input = input().split(" ")

            for rock in rock_input: 
                rock_tmp = rock.split("-")
                rock_type = rock_tmp[0]
                rock_distance = int(rock_tmp[1])

                stones.append([rock_type, rock_distance])

            stones.append(['B', d])

            max_leap = 0

            for j in range(1, len(stones)): 
                if stones[j][0] == 'B': 
                    if stones[j-1][0] == 'B': 
                        max_leap = max(max_leap, stones[j][1] - stones[j-1][1])
                    elif j > 1: 
                        max_leap = max(max_leap, stones[j][1] - stones[j-2][1])
                else: 
                    if j > 1 and stones[j-1][0] == 'S': 
                        max_leap = max(max_leap, stones[j][1] - stones[j-2][1])
                    # max_leap = max(max_leap, d)
            print("Case {}: {}".format(i+1, max_leap))
