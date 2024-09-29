import copy

'''
2
3
4
5
6
7
8
9
10
11 walet
12 dama
13 król
14 as
'''
SIEDEM_KART = [[3,2],[7,4],[11,4],[13,1],[10,4],[14,4],[12,4]]
SIEDEM_KART_C = copy.deepcopy(SIEDEM_KART)
for x in SIEDEM_KART_C:
    x.reverse()
print(SIEDEM_KART_C)
SIEDEM_KART_C.sort()
print(SIEDEM_KART_C)

# SIEDEM_KART.sort()
# print(SIEDEM_KART)
x=1-2*.7*.3-.3*.3-.7*.7/2-.6*.6/2
print(x)
