# PS-5 Questions

### **Q1) Baseball**

You are given a text file that shows several statistics about baseball players. Every line contains data coming from a single player.
Elements on these lines are separated by semicolons as follows:

Player's Name; Team Identifier; Games Played; At Bats; Runs Scored; Hits; Doubles; Triples; Homeruns

Write a program that takes a request and a positive integer (N) as inputs. Then, it should print the players who has top N maximum hits/batting average/slugging average.

Hint: 

* Singles = Hits - Doubles - Triples - Homeruns
* Total Bases = Singles + 2xDoubles + 3xTriples
* Batting Average = Hits / At Bats
* Slugging Average = Total Bases / At Bats

Input | Output
--- | ---
MAX HITS <br> 3 | Miguel Cabrera <br> Torii Hunter <br> Shin-Soo Choo
MAX BATTING <br> 2 | Miguel Cabrera <br> Torii Hunter
MAX SLUGGING <br> 2 | Torii Hunter <br> L.J. Hoes 

### **Q2) Movies**

You are given a CSV file that shows several movies' names, publishing years and genres. Every line contains data coming from a single movie.
Elements on these lines are separated by commas as follows:

1,Toy Story (1995),Animation

Write a program that takes a request as an input. If it is a movie, display its publishing year and genre. If it is a genre, display all movies in this genre.
If it is a year, display all movies published in this year. In this program you should get the raw data and turn it into a dictionary
that contains the keys "movie", "year" and "genre".

Input | Output
--- | ---
1992 | Waiting to Exhale <br> American President <br> Casino <br> Four Rooms
Toy Story | 1995 <br> Animation
Animation | Toy Story <br> Balto