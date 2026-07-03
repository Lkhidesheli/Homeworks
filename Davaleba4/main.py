# 1. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს და აბრუნებს 
# სტრიქონის UTF-8 დაშიფრულ ვერსიას.\


# x = input("Seiyvanet text romelic unda daishifros: ")

# #ვერსია 1
# # Text = x.encode()     # დიფოლთადაც იშიფრებე უტფ 8 ასე.
# # ვერისა 2 
# Text = x.encode("utf-8")

# print("Dashifruli tekstia : ", Text)

# 2. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# ჩამოაშორეთ ზედმეტი ინტერვალები.
# ყველა სიმბოლო გადაიყვანეთ პატარა ასოებში და
# დაუმატეთ ქვესტრიქონი 'Python'.
# თუ შეყვანილ სტრიქონში არსებობს სიტყვა
# "python", ჩაანაცვლეთ "Python"-ით.

# text = "            Me vswavlob python 's IT STEP Academy -Shi            "

# text = text.lower()
# text = text.strip()

# if "python" in text:
#     text = text.replace("python", "Python")
# else:
#     text = text + " Python"

# print(text)

# 3. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# პროგრამამ უნდა დააბრუნოს ახალი სტრიქონი,
# რომელიც შედგება შეყვანილი სტრიქონის პირველი ნახევრისაგან.

# text = "Me vswavlob Python's"

# textnaxevari = len(text) // 2
# print(text[0:textnaxevari])

# 4. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს.
# string მოდულის გამოყენებით დაწერეთ შემოწმება.
# სტრიქონი ვალიდურია მაშინ, როდესაც ის შეიცავს მინიმუმ ერთ
# ლათინურ ასოსა და
# მინიმუმ ერთ ციფრს და ამავე დროს არ შეიცავს დამატებით 
# სიმბოლოებს: '!', '~', '#', '$' და ა.შ.





# from string import ascii_letters, digits, punctuation

# text = "LukaKhidesheli17!"

# latinuriaso = False
# cifrebi = False
# punctuacia = False

# for char in text:
#     if char in ascii_letters:
#         latinuriaso = True
#     elif char in digits:
#         cifrebi = True
#     elif char in punctuation:
#         punctuacia = True

# if latinuriaso == True and cifrebi == True and punctuacia == True:
#     print("სტრიქონი ვალიდურია!")
# else:
#     print("სტრიქონი არავალიდურია!")



# 5. დაწერეთ პითონის კოდი, რომელიც იღებს სტრიქონს,
# სტრიქონი გადაყავს ბაიტებში, ბეჭდავს მნიშვნელობას და შემდეგ კი
# გადაყავს ბაიტებიდან სტრიქონში და ბეჭდავს სტრიქონს.

# text = input("შეიყვანეთ ტექსტი: ")

# bytetext = text.encode()
# print("ბაიტების ვერსია:", bytetext)

# text2 = bytetext.decode()
# print("ბაიტებიდან სტრიქონში:", text2)