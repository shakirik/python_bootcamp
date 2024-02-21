names =  ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

# min (len(name) for name in names)

# max(names, key=lambda n: len(n))


# songs = [
#     {'title': 'happy birthday', 'playcount': '1'},
#     {'title': 'gummy bear', 'playcount': '14'},
#     {'title': 'rivers', 'playcount': '82'},
#     {'title': 'ymca', 'playcount': '99'}
# ]

# max(songs, key=lambda s: s['playcount'])
# min(songs, key=lambda s: s['playcount'])['title']



def extremes (itr):
    return (min(itr), max(itr)) 

print(extremes([1,9,87,3,4]))


def max_magnitude(lst):
    return max(lst)