# Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


x=bool(input('Введите 0 или 1(x) '))
y=bool(input('Введите 0 или 1(y) '))
z=bool(input('Введите 0 или 1(z) '))
f1=not(x and y and z)
f2=not x or not y or not z
if f1==f2:
    print('yes')
else:
    print('no')
