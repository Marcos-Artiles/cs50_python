#declaring a list
results = ["Mario", "Luigi"]

#add elemnts to a list
results.append("Princess")
results.append("Yoshi")

#adding multiple enemies to a list
results.extend(["Koopa Troopa", "Toad"])

#remove the element form the list
results.remove("Toad")
#insert the element into the dessired possition on the list
results.insert(0, "Toad")

#reverse the order of the list
results.reverse()

#print the list
print(results)