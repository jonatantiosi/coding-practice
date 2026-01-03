# count - iterator sem fim

from itertools import count

c1 = count(16, 8)
# start, step
r1 = range(16, 50, 4)


print('c1', hasattr(c1, '__iter__'))
print('c1', hasattr(c1, '__next__'))
print()
print('r1', hasattr(r1, '__iter__'))
print('r1', hasattr(r1, '__next__'))

print('count')
for i in c1:
    if i >= 50:
        break
    print(i)
print()
print('range')
for i in r1:
    print(i)