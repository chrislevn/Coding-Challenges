import queue


class ChangeZ:
    def __init__(self, id = 0, newZ = 1, changeZ = 2):
        self.id = id
        self.newZ = newZ
        self.changeZ = changeZ

    def __lt__(self, other):
        if self.changeZ == other.changeZ:
            return self.id > other.id
        return self.changeZ > other.changeZ

    def __str__(self):
        s = "{0} {1}".format(self.id, self.newZ)
        return s


pq = queue.PriorityQueue()

n = int(input())

arr = []
for i in range(n):
    topic, z, p, l, c, s = map(int, input().split())
    new_z = (p*50 + l*5 + c*10 + s*20)
    change_z = new_z - z
    arr.append(ChangeZ(topic, new_z, change_z))

for i in arr:
    pq.put(i)

for i in range(5):
    print(pq.get())