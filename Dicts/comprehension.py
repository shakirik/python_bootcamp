numbers = dict(first = 1, second = 2, third = 3 )

squared = {k:v ** 2 for k, v in numbers.items()}
print(squared)

str1 = "ABC"
str2 = "123"

combo = {str1[i]:str2[i] for i in range(0, len(str1))}
print(combo)

instructor = {
    "name": "shakir",
    "city": "london",
    "colour": "yellow"
}

yelling_instructor = {(k.upper() if k == "colour" else k): (v.upper() if v == "yellow" else v) for k,v in instructor.items()}
print(yelling_instructor)


logic = {num: "even" if num % 2 == 0 else "odd" for num in range(0,100)}
print(logic)