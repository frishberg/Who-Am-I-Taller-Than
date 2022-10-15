from googlesearch import search
from selenium import webdriver
import json



#param: url
#return: source code of url
#this method takes in a url and outputs the source code of the url
def source_code(url) :
    driver = webdriver.Chrome(executable_path="Python/chromedriver.exe")
    driver.implicitly_wait(0.5)
    driver.get(url)
    s = driver.page_source
    return s



#param: search query string
#return: first link that shows up in google search
#this method takes in a search query string and outputs the first link that shows up in google search.  it also takes in a required website, 
# so that it only returns a link from the desired website.  there have been occurences where the desired website wouldn't
# be the first result, so I implemented this to fix that.
def first_result(query, website) :
    x = list(search(query, stop=3, pause=2))
    for y in x : #sometimes the first result is a random website, so this now gets top 3 results and returns the desired page
        if (website in y) :
            return y



#param: url of height page
#return: height of celebrity
#this method takes in the url of a height page and outputs the height of the celebrity.
# it uses the request library to get the source code of the inputted url page and then returns the height of the celebrity
def extract_height(url) :
    sc = source_code(url)
    sc = sc[sc.index("nameH3"):]
    sc = sc[sc.index("(") + 1:]
    height = float(sc[:sc.index(" cm)")])
    return height



#uses: extract_height
#param: name of celebrity
#return: height of celebrity (in cm)
#this method takes in the name of a celebrity and outputs the height of the celebrity
def get_height(celeb_name) :
    url = first_result(celeb_name + " celebheights.com", "celebheights.com")
    height = extract_height(url)
    return height



#param: url of networth page
#return: networth of celebrity
#this method takes in the url of a networth page and outputs the net worth of the celebrity.
# it uses the request library to get the source code of the inputted url page and then returns the net worth of the celebrity
def extract_networth(url) :
    sc = (source_code(url)).lower()
    sc = sc[sc.index('class="value"')+15:]
    sc = sc[:sc.index("<")]
    sc = sc.replace(" billion", "000000000")
    sc = sc.replace(" million", "000000")
    sc = sc.replace(" thousand", "000")
    sc = sc.replace(" dollars", "")
    networth = int(sc)
    return networth



#uses: extract_networth
#param: name of celebrity
#return: networth of celebrity
#this method takes in the name of a celebrity and outputs the net worth of the celebrity.
def get_networth(celeb_name) :
    url = first_result(celeb_name + " celebritynetworth.com", "celebritynetworth.com")
    net_worth = extract_networth(url)
    return net_worth


#param: url of pageviews api call
#return: number of views
#this method takes in the url of a pageviews api call and outputs the number of views
def extract_views(url) :
    sc = source_code(url)
    n = 0
    while("views" in sc) :
        sc = sc[sc.index("views") + 7:]
        n += int(sc[:sc.index("}")])
    return n


#uses: extract_views
#param: name of celebrity
#return: number of wikipedia page views of celebrity between January 1st 2021 and October 11th 2022.  This uses the constant date
# ending at October 11th because that is when I coded this method.  I considered using the current data, however that would require to rewrite 
# all of the generated data every time you want to add a new profile, otherwise, the data range (and thus data) would be different for people, 
# and would not be an accurate metric of popularity.
def get_popularity(celeb_name) :
    wikipedia_url = first_result(celeb_name + " wikipedia", "wikipedia.org")
    wikipedia_sub_url = wikipedia_url[wikipedia_url.index("wiki/") + 5:] #ex. ("wikipedia.org/wiki/John_Cena") -> ("John_Cena")
    url = "https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia.org/all-access/all-agents/" + wikipedia_sub_url + "/monthly/20210101/20221011"
    views = extract_views(url)
    return views



#uses: get_networth, get_height
#param: name of celebrity
#return: networth and height of celebrity
#this method takes in the name of a celebrity and outputs the net worth and height of the celebrity
def get_data(celeb_name) :
    return get_networth(celeb_name), get_height(celeb_name), get_popularity(celeb_name)



#uses: get_data
#param: name of celebrity
#return: none
#this method takes in the name of a celebrity and writes the net worth, height and popularity of the celebrity to a file
def write_data(celeb_name) :
    celeb_name = celeb_name.lower()
    networth, height, popularity = get_data(celeb_name)
    data = {"name" : celeb_name, "networth": networth, "height": height, "popularity": popularity}
    json_append(data, "Webpage/data.json")

def json_append(data, file_name) :
    f = open(file_name, "r")
    file_data = json.load(f)
    file_data.append(data)
    with open(file_name, "w") as f :
        json.dump(file_data, f, indent=4)
    f.close()

#param: name of celebrity, json file location
#this method takes in the name of a celebrity and checks if the celebrity is already in the json file
def json_includes(name, file_name) :
    f = open(file_name, "r")
    file_data = json.load(f)
    for i in file_data :
        if (i["name"] == name) :
            return True
    return False