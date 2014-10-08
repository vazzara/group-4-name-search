import google

def search(q):
    #takes question q, returns list of urls
    urlsList = []
    for url in google.search(q,tld='com',lang='en',num=10,start=0,stop=20):
        urlsList.append(url)
    return urlsList

def parse_urls(urlsList):
    #takes list of urls, returns only text
    #beautiful soup
    print ""

def name_occurrence(text):
    #finds names in text
    print ""

def analyse_list(namesList):
    #takes list of names, returns analysis + answer to question
    print ""

if __name__ == "__main__":
    urlsList = search("Who is the President of the United States?")
    parse_urls(urlsList)
