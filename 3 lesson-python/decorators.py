def announce(f):
    def wrapper():
        print("Запускается функция")
        f()
        print("Завершилась")
    return wrapper()


@announce
def hello():
    print("Hello world") 