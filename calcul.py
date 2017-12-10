'''
coucou c nous
'''

res = 0
for i in range(1, 3000):
    prev_res = res
    res = res+i
    print('{0} + {1} = {2}'.format(prev_res, i, res))

print("coucou")