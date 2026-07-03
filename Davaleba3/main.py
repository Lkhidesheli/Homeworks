#1. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს "n" და ბეჭდავს 1-დან "n"-მდე რიცხვების ჯამს.
# n = int(input("შეიყვანეთ რიცხვი: "))
# #პირველი ვარიანტი
# print(f"1 დან  {n} მდე რიცხვების ჯამი არის: {sum(range(1,n+1))}")
# #მეორე ვარიანტი
# print(f"1 დან {n} მდე რიცხვების ჯამი არის: {(1+n)*n/2}")

#2. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მომხმარებლისგან რიცხვს
#  და შემდეგ იყენებს "while" ციკლს რომ რევესრულად დაბეჭდოს რიცხვები 0-მდე. 
# მაგალითად თუ შეიყვანს 4, დაიბეჭდოს 4, 3, 2, 1

# x = int(input("sheiyvane ricxvi : "))

# while x != 0:
#     print(x)
#     x -= 1


# 3. დაწერეთ პითონის პროგრამა თამაშისთვის, რომელიც მუდმივად სთხოვს მომხმარებელს
# გამოიცნოს წინასწარ განსაზღვრული რიცხვი.როდესაც მომხმარებელი გამოიცნობს სწორ რიცხვს,
# დაასრულებს პროგრამა მუშაობას.


# x = 7
# print("gamoicani damaxsovrebuli cifri")
# while True:
#     n = int(input("Chawere sheni varianti: "))

#     if x == n:
#         print("Gilocav, Shen gamoicani")
#         break
#     elif x < n:
#         print("Chafikrebuli ricxvi naklebia tkvens ricxvze")
#     else:
#         print("Chafikrebuli ricxvi metia tkvens ricxvze")
        
# print("Game over")



# 4. დაწერეთ პითონის პროგრამა, რომელიც მიიღებს მუდმივად რიცხვებს. შექმენით საწყისი ცვლადი 
# total_sum = 0, შეამოწმეთ რიცხვი თუ დადებითია, მხოლოდ მაშინ დაუმატეთ total_sum ცვლადს.
#  ეს პროცესი გაგრძელდეს იქამდე სანამ მომხმარებელი არ შეიყვანს 'sum' ტექსტს, რის შემდეგაც 
# დაიბეჭდება შეყვანილი დადებითი რიცხვების ჯამი.



# total_sum = 0 
# while True:
#     x = input("chaweret ricxvi an sum : ")
#     if x.lower() == "sum":
#         break
#     num = int(x)
#     if num > 0 :
#         total_sum += num
#     elif num <= 0:
#         print("es araris dadebiti ricxvi, gtxovt chawerot dadebiti ricxvi")
# print("ricxvebis jamia: ", total_sum)



arr = [1,23,2,1,2,3,11,2,3,4,3,4]

# arr1 = arr
# arr.reverse()
# arr.sort(reverse=True)
# print(arr)
# print(sorted(arr))
# print(sorted(arr, reverse=True))

# print(sorted(arr)[::-1])

students = {"grades": [
    {"Luka": "A" }, 
    {"sandro": "B"}
    ]
    }
print(students["grades"][0]["Luka"])
