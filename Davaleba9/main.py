# 1. შექმენით გლობალური ცვლადი int_list = [10,20,30,40] 
# და დაწერეთ პითონის ფუნქცია, რომელიც  მიიღებს რიცხვს პარამეტრად 
# და გლობალურ int_list სიაში ჩაამატებს პარამეტრად მიღებულ რიცხვს.


# int_list = [10,20,30,40]
# shemotanili_ricxvi = int(input("sheiyvanet ricxvi romelic gindat daematos sias: "))
# def damateba(ricxvi):
#     global int_list
    
#     int_list.append(ricxvi)

# damateba(shemotanili_ricxvi)

# print(int_list)

# 2. დაწერეთ პითნის ფუნქცია რომელიც პარამეტრად იღებს რიცხვების 
# სიას (ლისტს) და აბრუნებს რიცხვების ჯამს. პარამეტრად უნდა მიიღოს 
# შემდეგი სია [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10].

# arr1 = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
# raodenoba = len(arr1)
# jami = 0
# def dajameba(x):
#     global jami
#     for i in range(raodenoba):
#         jami += x[i]
#     return jami

# print(dajameba(arr1))

# 3. შექმენით გლობალური ცვლადი gl_str = "Global" და დაწერეთ 
# პითონის ფუნქცია რომელიც ქმნის ლოკალურ ცვლადს იგივე
# სახელით რაც გლობალურ ცვლადს აქვს  (gl_str) და აბრუნებს
# ლოკალური ცვლადის მნიშვნელობას.

# gl_str = "Global"

# def shecvla():
#     gl_str = "local"
#     return gl_str

# print(shecvla()) # ეს იქნება ლოკალური ცვლადი 
# print(gl_str) # ეს ჩვეულებრივად გლობალური gl_str = "Global" 

# 4. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია, 
# რომელიც მიიღებს ერთ პარამეტრს number და დააბრუნებს  
# ციფრების ჯამს (მაგალითად თუ ფუნქციამ 
# მიიღო რიცხვი 12345, უნდა დააბრუნოს 15.
#  რადგან 1+2+3+4+5 უდრის 15-ს).


# def recursive(number):
#     if number == 0:
#         return 0
    
#     bolo_cifri = number % 10
#     danarcheni = number // 10
    
#     return bolo_cifri + recursive(danarcheni)

# result = recursive(12345)
# print(result)  




# 5. რეკურსიის გამოყენებით დაწერეთ პითონის ფუნქცია,
# რომელიც მიიღებს პარამეტრად სტრიქონს და დააბრუნებს მის შებრუნებულ 
# (revers) სტრიქონს (მაგალითად  input: Hello   Output: olleH


# def recursive(striqoni):
#     if striqoni == "":
#         return ""
    
#     return recursive(striqoni[1:]) + striqoni[0]

# result = recursive("Hello")
# print(result) 



def fibo(n):
    if n in (0,1):
        return n

    return fibo(n-1) + fibo(n-2)

result = fibo(4)

print(result)

# fib0 2 gaxda 1 
# fibo 1 1 
# fibo 0 0 
# 1 1
# 1 0 1 1