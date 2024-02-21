def ensure_correct_name (*args):
    if "Shakir" in args and "Kabir" in args:
        return "Hello Shakir"
    return "Who are you?"

print(ensure_correct_name("Shakir", "Kabir", 3, 5))
print(ensure_correct_name("Islam"))