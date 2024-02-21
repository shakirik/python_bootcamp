def colorise (text, color):
    if type(text) is not str:
        raise TypeError("text must be instace of str")
    
    
    print(f"Print {text} and {color}")
    
print(colorise("hello", "green"))
print(colorise(34, "hello"))