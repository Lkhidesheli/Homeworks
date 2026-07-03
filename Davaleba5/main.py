# 1. დაწერეთ პითონის პროგრამა, რომელიც დასაწყისში შექმნის ცარიელ სიას ([]), 
# თუ მომხარებელი შეიყვანს სიმბოლო 'a'-ს, ნიშნავს რომ უნდა დაამატოთ სიაში რიცხვი;
# თუ აკრიფა 'r', სიიდან უნა წაიშალოს რიცხვი; 'e'-ს შეტანისას პროგრამამ უნდა 
# დაასრულოს მუშაობა. მიღებული შედეგი დაბეჭდეთ კონსოლში.

# a – append

# r – remove

# e – exit

# გამოიყენეთ მხოლოდ ეს ბრძანებები და მოახდინეთ სიაზე ზემოქმედება.


# sia = []

# while True:

#     text = input("Sheiyvanet a(damateba), r(washla),  e(procesis dasruleba) : ")
       
#     if text == "a":
#         text2 = int(input("romeli cifri gsurt rom daamatot sias: "))
#         sia.append(text2)
#         print("tkvens siashi aris shemdegi cifrebi: ",sia)
#     elif text == "r":
#         text2 = int(input("romeli cifri gsurt rom washalot siidan: "))
#         if text2 in sia:
#             sia.remove(text2)
#         else:
#             print("tkveni cifri ar aris siashi, scadet tavidan")
#         print("tkvens siashi darcha shemdegi cifrebi: ", sia)
#     elif text == "e":
#         print("tkven gamoxvedit sesiidan shedegi ki aris : ", sia)
#         break





# 2. დაწერეთ პითონის პროგრამა, რომელიც შექმნის სიას my_list_1
# = [43, '22', 12, 66, 210, ["hi"]], და შეასრულებს შემდეგ ნაბიჯებს:
# a. დაბეჭდავს 210-ის ინდექსს;
# b. დაამატებს ბოლო ელემენტში ტექსტს "hello";
# c. წაშლის მეორე ინდექსზე მდგომ ელემენტს და დაბეჭდავს სიას;
# d. შექმენით ახალი სია my_llist_2, რომელსაც ექნება my_llist_1-ის 
# მნიშვნელობა, გაასუფთავეთ my_llist_2-ის მნიშნველობა და დაბეჭდეთ ორივე სია.
# მინიშნება: სიის გასუფთავება – arr.clear()
    
# my_list_1 = [43, '22', 12, 66, 210, ["hi"]]

# print("210 is index aris: ",my_list_1.index(210))
# my_list_1[-1].append("hello")
# my_list_1.remove(my_list_1[1])
# print(my_list_1)

# my_list_2 = my_list_1.copy()
# my_list_2.clear()

# print("My_list_1 : ", my_list_1)
# print("My_list_2 : ",my_list_2)


# 3. დაწერეთ პითნის პროგრამა, რომელიც მიიღებს
# ტელეფონის ნომერს და regex-ით შეამოწმებს შეყვანილი 
# ნომერი იცავს თუ არა "(123) 456-789" ფორმატს, თუ იცავს 
# დააბრუნეთ შეყნვაილი ტელეფონის ნომერი, წინააღმდეგ შემთხვევაში
# გამოიტანეთ "Invalid format" ტექსტი.

# მინიშნება: სრული დამთხვევისთვის გამოიყენეთ .fullmatch() მეთოდი re მოდულიდან.

import re

nomeri = input("chaweret telefonis nomeri: ")

pattern = r"[0-9]{3} [0-9]{3}-[0-9]{3}"

if re.fullmatch(pattern,nomeri):
    print(nomeri)
else:
    print("invaild format")


# shedegi: 
# chaweret telefonis nomeri: 555 555-555
# 555 555-555


# chaweret telefonis nomeri: 232
# invaild format