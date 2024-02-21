playlist = {
    "title": "patagonia bus", 
    "author": "shakir kabir",
    "songs":
    [
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
}


total_duration = 0
for s in playlist["songs"]:
    total_duration += s["duration"]
    
print(total_duration)