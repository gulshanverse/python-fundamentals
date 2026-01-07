s1 = {1,3,5,7}
s2 = {0,2,4,6}
print(s1.union(s1))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.issuperset(s2))
print(s1.issubset(s2))
print(s1.isdisjoint(s2))
print(s1.symmetric_difference(s2))
print(s1.symmetric_difference_update(s2))
s3 = {6,10,14,18}
s3.clear()
print(s3)
len(s3)
s4 = {1,2,3,4,5}
print(len(s4))