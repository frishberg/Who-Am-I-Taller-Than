from data_collection import *
from time import sleep
import os

famous_people = [
    "Taylor Swift",
    "Justin Bieber",
    "Katy Perry",
    "Rihanna",
    "Beyonce",
    "Lady Gaga",
    "Miley Cyrus",
    "Kanye West",
    "Kendrick Lamar",
    "Obama",
    "Donald Trump",
    "Kim Kardashian",
    "Selena Gomez",
    "Ariana Grande",
    "Ellen DeGeneres",
    "Chris Brown",
    "Drake",
    "Nicki Minaj",
    "Kylie Jenner",
    "Kourtney Kardashian",
    "Khloe Kardashian",
    "Robert Downey Jr.",
    "Chris Pratt",
    "Chris Evans",
    "Scarlett Johansson",
    "Chris Hemsworth",
    "Mark Ruffalo",
    "Tom Holland",
    "Tom Hiddleston",
    "Benedict Cumberbatch",
    "Arnold Schwarzenegger",
    "Dwayne Johnson",
    "Vin Diesel",
    "Jason Statham",
    "Will Smith",
    "Tom Cruise",
    "Brad Pitt",
    "Leonardo DiCaprio",
    "Jennifer Lawrence",
    "Emma Stone",
    "Megan Fox",
    "Angelina Jolie",
    "Halle Berry",
    "Jennifer Aniston",
    "Shakira",
    "Paul Rudd",
    "Ryan Reynolds",
    "Chris Pine",
    "Paul McCartney",
    "Elton John",
    "Bono",
    "Bruce Springsteen",
    "Bob Dylan",
    "David Bowie"
]

for name in famous_people :
    try :
        if (not os.path.exists("data/" + name + ".txt")) : #if data doesn't already exists
            write_data(name)
            print("Successfully fetched data for " + name)
            sleep(2)
        else : #if data already exists
            print("Data already exists for " + name)
    except ValueError :
        print("Error fetching data for " + name)