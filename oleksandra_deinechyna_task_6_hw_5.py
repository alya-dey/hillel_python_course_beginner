set1 = {1, 2, 3}
# add
set1.add(4)
print(set1)
#  clear
set1.clear()
print(set1)
# update
set1.update([1, 2, 3, 4, 5])
print(set1)
#  copy
set1.copy()
print(set1)
#  difference
set2 = {4, 5, 6, 7}
set3 = set1.difference(set2)
set3 = set1 - set2
print(set3)
#  discard
set3.discard(2)
print(set3)
#  intersection
set4 = set1.intersection(set3)
set4 = set1 & set3
print(set4)
#  isdisjoint
print(set4.isdisjoint(set1))
#  issubset
print(set3.issubset(set1))
#  issuperset
print(set1.issuperset(set3))
#  pop
set4.pop()
print(set4)
#  remove
print(set2)
set2.remove(4)
print(set2)
#  union
set5 = set3 | set4
print(set5)
set6 = set5.union(set2)
print(set6)


'''
Написать примеры всех методов из set объекта.
Пример
set1 = {1,2,3}
# add
set1.add(4)
# update
set1.update([2,3,4,5])
'''