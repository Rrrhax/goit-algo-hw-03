from datetime import datetime

def get_days_from_today(date:str) -> int | str: #Функция которая получает строку "date" и возвращает число или строку
    try: # Обработка исключений
        str_to_date = datetime.strptime(date, "%Y-%m-%d").date() #переводим строку в формат datetime и получаеи только дату из него
        today_date = datetime.today().date() # получаем сегодняшнюю дату

        return (today_date - str_to_date).days # функция возвращает разницу между сегодня и указаной датой в днях
    
    except ValueError: 
        return "Wrong date format. Use 'YEAR-MONTH-DAY'!" # исключение при получении неправильного формата даты на ввод

    
user_date = input("Type in your date in format 'YEAR-MONTH-DAY': ") # мини UI для ввода даты с помощью инпута 
result = get_days_from_today(user_date) 
print(result)