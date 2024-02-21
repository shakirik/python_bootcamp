# tuples are unique so can not add values once you have created a tuple
# you cannot remove values from tuples either as immutable
# created using normal brackets and just a list

alphabet = ('a', 'b', 'c', 'd')
print(type(alphabet))


# can use tuples within a dict 

locations = {
    (23930,22392): "London",
    (3923, 33231): "New York",
    (332, 3232): "Sydney"
}

print(locations[(23930,22392)])


# count method - tells you how many there is 

x = (1, 2, 3, 4, 4, 4)
x.count(1)
x.count(3)

# index method - will return the index at which a value is found in a tuple

t = (1,2,3,4,5,6,7,9)
t.index(3)
