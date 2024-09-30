immutable_var= 1,2,3.0,'task'
print(immutable_var)
print(immutable_var[-1])
#immutable_var[-1]=20  # изменить последний элемент кортежа на 20
#print(immutable_var)  # операция выдала ошибку, так как кортеж относится к неизменяемым типам данных и не поддерживает обращение по элементам
mutable_var=[5, 3.0, 'список', False]
print(mutable_var)
mutable_var[-1]=True
print(mutable_var)