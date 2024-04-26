person = ("Bob", 42, "Mechanic")
name, _, profession = person # we dont care about the age so we need to use _

print(name, profession)

#head, *tail = [1,2,3,4,5,6]
#print(head) # 1
#print(tail) # [2, 3, 4, 5, 6]

*tail, head = [1,2,3,4,5,6]
print(head) # 6
print(tail) # [1, 2, 3, 4, 5]
