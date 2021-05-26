#3.4嘉宾名单
Guests = ["binbinwang", "stone", "nanhu", "shuaishuai"]
message = "\n"+Guests[0].title() + ", I invite you to dinner with me."
print(message)
message = "\n"+Guests[1].upper() + ", I invite you to dinner with me."
print(message)
message = "\n"+Guests[2].title() + ", I invite you to dinner with me."
print(message)
message = "\n"+Guests[3].title() + ", I invite you to dinner with me."
print(message)

#3.5修改嘉宾名单
message = "\n"+Guests[2] + " can`t attend the dinner"
print(message)
Guests.pop(2)
Guests.insert(2 , "Stars")
message = "\n"+Guests[0].title() + ", I invite you to dinner with me."
print(message)
message = "\n"+Guests[1].upper() + ", I invite you to dinner with me."
print(message)
message = "\n"+Guests[2].title() + ", I invite you to dinner with me."
print(message)
message = "\n"+Guests[3].title() + ", I invite you to dinner with me."
print(message)

#3.6添加嘉宾
print("\nDear guests" + "\n  I found a bigger table")
Guests.insert(0,"Mr Right")
Guests.insert(2,"Miss C")
Guests.append("Mr Wu")
print(Guests)
message = "\n"+Guests[0].title() + ", I invite you to dinner with me."
print(message)
message = "\n"+Guests[1].title() + ", I invite you to dinner with me."
print(message)
message = "\n"+Guests[2].title() + ", I invite you to dinner with me."
print(message)
message = "\n"+Guests[3].title() + ", I invite you to dinner with me."
print(message)
message = "\n"+Guests[4].title() + ", I invite you to dinner with me."
print(message)

#3.7缩减名单
print("\nDistinguished guests," + "\n  I’m sorry, the newly purchased table cannot be delivered,"
"so I can only invite two guests to complete it together")
Guests_sorry=Guests.pop(0)
print("\n" + Guests_sorry +" \n   I'm sorry, I can't invite you to dinner")
Guests_sorry=Guests.pop(0)
print("\n" + Guests_sorry +" \n   I'm sorry, I can't invite you to dinner")
Guests_sorry=Guests.pop(0)
print("\n" + Guests_sorry +" \n   I'm sorry, I can't invite you to dinner")
Guests_sorry=Guests.pop(-1)
print("\n" + Guests_sorry +" \n   I'm sorry, I can't invite you to dinner")
Guests_sorry=Guests.pop(-1)
print("\n" + Guests_sorry +" \n   I'm sorry, I can't invite you to dinner")
print(Guests)

print(Guests[0].title() + "\n   You are still among my invitees")
print(Guests[1].title() + "\n   You are still among my invitees")
del Guests[1]
print(Guests)
del Guests[0]
print(Guests)






