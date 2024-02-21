def special_greeting(**kwargs):
    if "David" in kwargs and kwargs["David"] == "special":
        return "Special greeting"
    elif "David" in kwargs:
        return f"{kwargs['David']} David"
    return "Not sure who this is"

print(special_greeting(David="Hello"))
print(special_greeting(Bob="Hello"))
print(special_greeting(David="special"))