# 1. დაწერეთ პითონის ფუნქცია, რომელიც იღებს პარამეტრად 
# ერთიდაიგივე ზომის სიას (list)
#  და zip ფუნქციის გამოყენებით დააჯგუფეთ სიების ელემენტები.
# params: [1, 2, 3], ['a', 'b', 'c']  
# outputs: ["(1, 'a')", "(2, 'b')", "(3, 'c')"]


# def dajgufeba(*args):
#     return [str(x) for x in zip(*args)]

# result = dajgufeba([1, 2, 3], ['a', 'b', 'c'])
# print(result)


# 2. დაწერეთ პითონის ფუნქცია, რომელიც პარამეტრად იღებს
#  რიცხვების სიას და აბრუნებს ელემენტების ნამრავლს. 
# ფუნქციაში გაითვალისწინეთ გამონაკლისები (Exceptions), 
# თუ მიიღეთ არასწორი ტიპის პარამეტრს (TypeError).
# ფუქნციის დასაწერად გამოიყენეთ lambda და  functools-ის reduce მეთოდი.  

# params:[1, 2, 3, 4, 5]
# output: 120

# from functools import reduce

# def namravlis_povna(numbers):
#     try:
#         return reduce(lambda x, y: x * y, numbers)
#     except TypeError:
#         print(f"araswori parametrebi")

# result = namravlis_povna([1, 2, 3, 4, 5])
# print(result) 



# 3. დაწერეთ lambda ფუნქცია რომელიც იღებს მთელი რიცხვების 
# სიას (list) და აბრუნებს მხოლოდ სიის კენტ ელემენტებს.

# params: [1, 2, 3, 4, 5, 6, 7]
# outputs: [1, 3, 5, 7]

# kentebi = lambda numbers: list(filter(lambda x: x % 2 != 0, numbers))

# result = kentebi([1, 2, 3, 4, 5, 6, 7])
# print(result)


# 4. დაწერეთ პითნის ფუნქცია, რომელიც იღებს ორ პარამეტრს, სტრიქონების სიასა და სტრიქონს 
# (ending). დააბრუნეთ მხოლოდ სიის ის ელემენტები რომელიც მთავრდება, მეორე პარამეტრად 
# მიწოდებული სტრიქონით. გამოიყენეთ lambda და filter ფუნქცია. გაითვალისწინეთ გამონაკლისები (TypeError),
#  თუ სხვა გამონაკლისიც აღმოჩნდა ისიც გაითვალისწინეთ.

# მინიშნება: გადაავლეთ თვალი string მეთოდებს, მონახეთ ისეთი მეთოდი,
#  რომელიც აბრუნებს სიტყვას, რომელიც მთავრდება რაღაც სიმბოლოებით...

# params: ['hello', 'world', 'coding', 'nod'], 'ing'  
# outputs: ['coding']

def daboloebit_povna(sia, daboloeba):
  
    try:
        return list(filter(lambda x: x.endswith(daboloeba), sia))
    except TypeError as ex:
        print(f"shecdoma: {ex}")
    except Exception as ex:
        print(f"shecdoma: {ex}")


result = daboloebit_povna(['hello', 'world', 'coding', 'nod'], 'ing')
print(result)
