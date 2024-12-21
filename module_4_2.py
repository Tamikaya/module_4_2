#Создайте новую функцию test_function
def test_function():
    
# Создайте другую функцию внутри функции inner_function
    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()  # возвращает 0

#inner_function()  # ошибка,вызов вне функции test_function

test_function()     # работает

































