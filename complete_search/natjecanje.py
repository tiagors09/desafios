def verifying_neighborhood(me, neighbor):
    i_have_a_spare_kayak = me["has_reserve_kayak"] 
    neighbor_has_a_broken_kayak = neighbor["is_damaged_kayak"]

    return i_have_a_spare_kayak and neighbor_has_a_broken_kayak

def helping_the_neighborhood(me, neighbor,counter):
    me["has_reserve_kayak"] = False
    neighbor["is_damaged_kayak"] = False
    counter = counter - 1
    return counter
        
_input = [int(i) for i in input().split()]
n_count = _input[0]
s_count = _input[1]
r_count = _input[2]

s = [int(i) for i in input().split()]
r = [int(i) for i in input().split()]

data = {}

for i in range(1, n_count + 1):
    data[i] = {
        "team": i,
        "is_damaged_kayak": i in s,
        "has_reserve_kayak": i in r,
        "neighborhood": [i-1, i+1],
    }

for d in range(1, n_count + 1):
    me = data[d]
    left_neighbor_index = me["neighborhood"][0]
    right_neighbor_index = me["neighborhood"][1]

    if verifying_neighborhood(me, me):
        s_count = helping_the_neighborhood(me, me, s_count)
    elif left_neighbor_index > 0 and verifying_neighborhood(me, data[left_neighbor_index]):
        s_count = helping_the_neighborhood(me, data[left_neighbor_index], s_count)
    elif right_neighbor_index <= n_count and verifying_neighborhood(me, data[right_neighbor_index]):
        s_count = helping_the_neighborhood(me, data[right_neighbor_index], s_count)

print(s_count)
