from data_collection import *
from time import sleep
import selenium

famous_people = [
    
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
