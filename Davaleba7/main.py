        
# 1. კონსოლიდან შეიტანეთ მიმდევრობა. 
# დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე (set).

# x = input("sheiyvanet mimdevroba: ")


# print(set(x.split()))

# 2. პირობა იგივეა, რაც პირველ დავალებაში,
# ოღონდ დაბეჭდეთ უნიკალური მონაცემებიანი სიმრავლე, 
# რომლის შეცვლაც შეუძლებელი იქნება (frozenset).

# x = input("sheiyvanet mimdevroba: ")


# print(frozenset(x.split()))

# 3. აიღეთ set ტიპის ორი მონაცემი. ელემენტები თავად განსაზღვრეთ. 
# დაბეჭდეთ გაერთიანებული მონაცემები კორტეჟის სახით (tuple).


# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# tuple = tuple(set1 | set2)

# print(tuple)

# 4. კონსოლიდან შევიტანოთ რიცხვების მიმდევრობა
# როგორც კორტეჟი (tuple). დავბეჭდოთ მხოლოდ
# უნიკალური ელემენტები სიის სახით (list).

# tuple = tuple(input("sheiyvanot ricxvebis mimdevroba: ").split())

# list = list(set(tuple))

# print(list)


# 5. მოცემულია სია, რომლის ელემენტები წარმოადგენენ კორტეჟს:
# [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

# დაბეჭდეთ შემდეგი ფორმატით:

# Name: Gega, Age: 24
# Name: Gaga, Age: 21
# Name: Goga, Age: 19
# Name: Giga, Age: 27
# Name: Gagi, Age: 11


# students = [("Gega", 24), ("Gaga", 21), ("Goga", 19), ("Giga", 27), ("Gagi", 11)]

# for name, age in students:
#     print(f"Name: {name}, Age: {age}")


# 6. მოცემულია მომხმარებლების სია: ["Irakli", "Giorgi", "Nona", "Oto"].
# ასევე გვაქვს სხვა მომხმარებლებიც: ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]
# დავბეჭდოთ თანხვედრა.


# list1 = ["Irakli", "Giorgi", "Nona", "Oto"]
# list2 = ["Kato", "Levani", "Nino", "Dato", "Irakli", "Nemo"]

# set1 = set(list1)
# set2 = set(list2)

# print(set1.intersection(set2))