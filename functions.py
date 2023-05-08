def get_user(name,:str, age:int, salary=10000, years=3) -> list:
    return f'Your name is {name}, age = {age}, salary = {salary}, years = {years} old.'

print(get_user('Maruche', 23, 20000, 2))