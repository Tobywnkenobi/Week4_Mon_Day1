# #Dylan's whiteboard

# def find_pairs(alist):
#     count, hash_map = 0, {}
#     for color in alist:
#         hash_map[color] = hash_map.get(color, 0) + 1
#     for k, v in hash_map.items():
#         count += alist.count(color)
#     return count

# print(find_pairs(['red','red','red','red','red','red']))
# print(find_pairs(['red','green','red','blue','blue','blue']))


def logn(number):
    output = []
    count = 1
    while count < number:
        output.append(count)
        count *= 2
    return output

len(logn(100))