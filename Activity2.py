amount = int(input("Enter your amount:"))

notes_of_500 = amount // 500
amount = amount % 500
notes_of_200 = amount // 200
amount = amount % 200
notes_of_100 = amount // 100
amount = amount % 100
notes_of_50 = amount // 50
amount = amount % 50
notes_of_20 = amount // 20
amount = amount % 20
notes_of_10 = amount // 10
amount = amount % 10

print ("Number of notes of 500:" , notes_of_500)
print ("Number of notes of 200:" , notes_of_200)
print ("Number of notes of 100:" , notes_of_100)
print ("Number of notes of 50:" , notes_of_50)
print ("Number of notes of 20:" , notes_of_20)
print ("Number of notes of 10:" , notes_of_10)