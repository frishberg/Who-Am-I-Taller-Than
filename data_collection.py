from googlesearch import search
import requests



#param: url
#return: source code of url
#this method takes in a url and outputs the source code of the url
def source_code(url) :
    r = requests.get(url)
    return r.text



#param: search query string
#return: first link that shows up in google search
#this method takes in a search query string and outputs the first link that shows up in google search
def first_result(query) :
    x = list(search(query, stop=1, pause=2))
    return(x[0])



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
    url = first_result(celeb_name + " celebheights.com")
    height = extract_height(url)
    return height



#param: url of networth page
#return: networth of celebrity
#this method takes in the url of a networth page and outputs the net worth of the celebrity.
# it uses the request library to get the source code of the inputted url page and then returns the net worth of the celebrity
def extract_networth(url) :
    sc = source_code(url)
    sc = sc[sc.index("$")+1:]
    sc = sc[:sc.index('.')]
    if (len(sc)>20) :
        sc=sc[:sc.index('"')]
    sc = sc.replace(" billion", "000000000")
    sc = sc.replace(" million", "000000")
    sc = sc.replace(" thousand", "000")
    sc = sc.replace(" dollars", "")
    networth = int(sc)
    return networth



#uses: extract_networth
#param: name of celebrity
#return: networth of celebrity
#this method takes in the name of a celebrity and outputs the net worth of the celebrity
def get_networth(celeb_name) :
    url = first_result(celeb_name + " celebritynetworth.com")
    net_worth = extract_networth(url)
    return net_worth



#uses: get_networth, get_height
#param: name of celebrity
#return: networth and height of celebrity
#this method takes in the name of a celebrity and outputs the net worth and height of the celebrity
def get_data(celeb_name) :
    return get_networth(celeb_name), get_height(celeb_name)



#uses: get_data
#param: name of celebrity
#return: none
#this method takes in the name of a celebrity and writes the net worth and height of the celebrity to a file
def write_data(celeb_name) :
    celeb_name = celeb_name.lower()
    networth, height = get_data(celeb_name)
    f = open("data/" + celeb_name + ".txt", "w")
    s = ""
    s += "networth: " + str(networth) + "\n"
    s += "height: " + str(height) + "\n"
    f.write(s)
    f.close()