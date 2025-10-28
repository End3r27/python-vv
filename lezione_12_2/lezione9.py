#ancora sui set
#union(), update(),
#intersection_update(), intersection(),
#symmetric_difference_update(), symmetric_difference()

ilMioSet = {"roma", "torino", "genova", "livorno"}
print(ilMioSet)

ilMioSet2 = {"bari","taranto","roma","genova"}
print(ilMioSet2)

print("--------ilMioSet3--------")

ilMioSet3 = ilMioSet.union(ilMioSet2)
#ilMioSet3 = ilMioSet.u
print(ilMioSet3)
#quindi con update si uniscono due set
#con union se ne crea uno nuovo che ne contiene due vecchi
#inoltre vengono esclusi gli elementi uguali!

#vediamo ora: come mettere insieme i valori duplicati
#intersection_update(), che lavora aggiornando uno dei due set
#intersection(), che crea un nuovo set

print("-----------------...---------------")

ilMioSet.intersection_update(ilMioSet2)
print(ilMioSet)

ilMioSet4 = ilMioSet.intersection(ilMioSet2)
print(ilMioSet4)


print("------------------------------")
#vediamo ora: come mettere insieme i valori diversi
#symmetric_difference_update(),
#che lavora aggiornando uno dei due set
#symmetric_difference(), che crea un nuovo set
ilMioSet = {"roma", "torino", "genova", "livorno"}
print(ilMioSet)

ilMioSet2 = {"bari","taranto","roma"}
print(ilMioSet2)

print("----------------****-----------------")

ilMioSet.symmetric_difference_update(ilMioSet2)
print(ilMioSet)
ilMioSet = {"roma", "torino", "genova", "livorno"}
print(ilMioSet)
ilMioSet4 = ilMioSet.symmetric_difference(ilMioSet2)
print(ilMioSet4)

