ilMioSet = set ({"roma", "torino", "genova", "livorno"})

print(ilMioSet)

ilMioSet.add("milano")
print(ilMioSet)

ilMioSet.remove("torino")
print(ilMioSet)

ilMioSet2 = {"Nicola", "Luca", "Marco"}

ilMioSet2.symmetric_difference(ilMioSet)
print(ilMioSet2)