
def getLongestChain(chain, dominos, maxChain): 
    for i in range(len(dominos)): 
        curr_dom = dominos[i]
        if chain.isEmpty() or chain[len(chain) - 1][1] == curr_dom[0]: 
            chain.append(curr_dom)
            if len(chain) > maxChain: 
                dominos.remove(i)
            maxChain = getLongestChain(chain, dominos, maxChain)
            dominos.append(i, curr_dom)
            chain.remove(len(chain) - 1)

        currDomFlipped = (curr_dom[1], curr_dom[0])

        if chain.isEmpty() or chain[len(chain) - 1][1] == currDomFlipped[0]: 
            chain 

dominos  = []

tile = input()

while tile !=  "-1":
    a, b = map(int, tile.split(" "))
    a, b = int(a), int(b)
    
    dominos.append((a,b))

    tile = input()



