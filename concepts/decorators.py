def decorator_function(function):
    
    def wrapper():
        print('This is the first message')
        function()
        print('This is the last message')
    return wrapper

@decorator_function
def buzzing():
    print('Buzzz')

#buzzing = decorator_function(buzzing)

buzzing()
