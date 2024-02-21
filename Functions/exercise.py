def speak(animal="dog"):
    noises = {
        "pig": "oink",
        "duck": "quack",
        "cat": "meow"
    }
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

# keyword arguments