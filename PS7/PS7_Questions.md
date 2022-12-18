# PS-7 Questions

### **Q1) Inverted dictionary**

Write a function that takes in a dictionary and returns a new dictionary where the keys are the 
values from the original dictionary and the values are the keys from the original dictionary.

{'a': 1, 'b': 2, 'c': 3} → {1: 'a', 2: 'b', 3: 'c'}

### **Q2) Data Collection**

Write a program that reads lines from the input. 
Each line will be composed of 4 words, name of the game, genre of the game, year of release and the producer respectively. 

If a line is equal to "exit", stop reading. Store the games in a dictionary. Their values should also correspond to dictionaries composed of their genre, release date and producer.

Input | Output
--- | ---
RDR2 Action 2018 Rockstar <br> Fifa14 Sports 2013 EA <br> Borderlands Shooter 2009 Gearbox <br> Skyrim RPG 2011 Bethesda <br> Wall-E Platform 2008 THQ <br> exit | {'RDR2': {'genre': 'Action', 'release date': '2018', 'producer': 'Rockstar'}, <br> 'Fifa14': {'genre': 'Sports', 'release date': '2013', 'producer': 'EA'}, <br> 'Borderlands': {'genre': 'Shooter', 'release date': '2009', 'producer': 'Gearbox'}, <br> 'Skyrim': {'genre': 'RPG', 'release date': '2011', 'producer': 'Bethesda'}, <br> 'Wall-E': {'genre': 'Platform', 'release_date': '2008', 'producer': 'THQ'}}

### **Q3) Order filler**

You are running an e-commerce business. Write a program to control your stocks. If the request is higher than the amount of merchandise, print `unsuccessful`. If not, print `successful`.

Take requests until the user gives the input `exit`. Finally, print the last version of stocks as given below.

Take the stocks as `s = {"socks": 14, "pants": 6, "shoes": 7}`

Hint: Give the inputs one by one.

Input | Output
--- | ---
socks 13 <br> socks 4 <br> pants 2 <br> shoes 5 <br> exit | successful <br> unsuccessful <br> successful <br> successful <br> socks 1 <br> pants 4 <br> shoes 2