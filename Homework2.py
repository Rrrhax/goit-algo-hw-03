import random

def get_numbers_ticket(min:int, max:int, quantity:int): #Функция получает на ввод 3 числа, минимальное ч., максиммально ч., и кол-во.
    try: #Обработка исключений  
        if not (1 <= min <= max <= 1000 and 1 <= quantity <= (max - min + 1)): # проверка на условия.(мин не менее 1, макс не более 1000, quantity в диапазоне min-max и больше чем 1)
            return [] # в ином случае(если не подходит по условиям) - возврат пустого списка
        list_of_num = list(range(min, max +1)) # создаем список от мин, до макс включительно
        generated_numbers = sorted(random.sample(list_of_num, quantity)) # сортироованная генерация случайного уникального(через sample) числа из списка list_of_num, в кол-ве quantity
        return generated_numbers
    except TypeError: # Если введено не число(int) 
        return "Expected min number, max number, quantity!"
    

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)