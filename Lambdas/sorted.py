nums = [1,4,2,89,32,90,43]

print(sorted(nums, reverse=True))


users = [
         {"title": "song1", 
         "artist": "drake", 
         "duration": 2.9},
        {"title": "song2", 
         "artist": "boo", 
         "duration": 4.9},
        {"title": "song3",
          "artist": "crew", 
          "duration": 7.3}
         ]

print(sorted(users, key=len))

# key can be used to specify and can use lambdas as key