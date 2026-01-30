import re 

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number): #функция по нормализации телефона
    new_number = re.sub(r"[^\d]", "", phone_number) # получаем отфильтрованный номер который состоит только из чисел (\d) и объединяем через "" 

    if len(new_number) == 10 and new_number[0] == "0": # если номер состоит из 10 символов и начинается с 0 то добавляем +38
            new_number = "+38" + new_number
    elif len(new_number) == 12 and  new_number[0] == "3": # если номер состоит из 12 символов и начинается с 3 то добавляем +
            new_number = "+" + new_number
    else:
        return "+" + new_number #исключение на случай если не прошел проверки выше


    return new_number # возвращаем номер

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)