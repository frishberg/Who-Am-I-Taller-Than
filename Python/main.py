from data_collection import *
from time import sleep
import selenium

famous_people = [  #list to be added to data, scraped from wikipedia
    "Mark Zuckerberg",
    "Jeff Bezos",
    "Bill Gates",
    "Elon Musk",
    "Jack Ma",
    "Steve Ballmer",
    "Michael Bloomberg",
    "Larry Summers",
    "Michael Dell",
    "Jim Walton",
    "Rob Walton",
    "Charles Koch",
    "David Koch",
    "Alice Walton",
    "MacKenzie Scott",
    "Phil Knight",
    "Jim Simons",
    "Jack Dorsey",
    "Jacqueline Mars",
    "Jim Breyer",
    "John Mars",
    "Ken Griffin",
    "Abigail Johnson",
    "John Roberts",
    "Clarence Thomas",
    "Samuel Alito",
    "Stephen Breyer",
    "Sonia Sotomayor",
    "Elena Kagan",
    "Neil Gorsuch",
    "Brett Kavanaugh",
    "Amy Coney Barrett",
    "Ketanji Brown Jackson",
    "Kevin O'Leary",
    "Barbara Corcoran",
    "Mark Cuban",
    "Daymond John",
    "Robert Herjavec",
    "Lori Greiner",
]

for name in famous_people :
    if ("." in name) :
        name = name[name.index(".")+2:]
    name = name.lower()
    try :
        if (not json_includes(name, "Webpage/data.json")) : #if data doesn't already exists
            try :
                write_data(name)
                print("Successfully fetched data for " + name)
                sleep(2)
            except selenium.common.exceptions.InvalidArgumentException :
                print("Failed to fetch data for " + name)
        else : #if data already exists
            print("Data already exists for " + name)
    except ValueError :
        print("Error fetching data for " + name)