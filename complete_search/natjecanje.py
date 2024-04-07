def verifying_neighborhood(me, neighbor):
    return me["has_reserve_kayak"] and neighbor["is_damaged_kayak"]

def helping_the_neighborhood(me, neighbor,counter):
    me["has_reserve_kayak"] = False
    neighbor["is_damaged_kayak"] = False
    return counter - 1
        
_input = [int(i) for i in input().split()]
n_count = _input[0]
s_count = _input[1]
r_count = _input[2]

s = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]

data = {}

for i in range(1, n_count + 1):
    data[i] = {
        "is_damaged_kayak": i in s,
        "has_reserve_kayak": i in r,
        "neighborhood": [i-1, i+1],
    }

for d in range(1, n_count + 1):
    me = data[d]
    
    if verifying_neighborhood(me, me):
        s_count = helping_the_neighborhood(me, me, s_count)
        break

    left_neighbor_index = me["neighborhood"][0]
    if left_neighbor_index > 0 and verifying_neighborhood(me, data[left_neighbor_index]):
        s_count = helping_the_neighborhood(me, data[left_neighbor_index], s_count)
        break
        
    right_neighbor_index = me["neighborhood"][1]
    if right_neighbor_index <= (n_count + 1) and verifying_neighborhood(me, data[right_neighbor_index]):
        s_count = helping_the_neighborhood(me, data[right_neighbor_index], s_count)
        break

print(s_count)
