def logger(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper