import urllib, urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = "http://www.tripadvisor.in/Attractions-g304551-Activities-c42-New_Delhi_National_Capital_Territory_of_Delhi.html"
p = urllib.request.urlopen(url)

##source = p.read()
##p.close()
####print(source)
##
##soup = BeautifulSoup(source)
##a=soup.prettify()
####print(a)
##
##
##list_divs = soup.find_all('div', class_='listing')
####print(list_divs[0])
####print(len(list_divs))

list_name = []
list_imgurl = []
list_link = []
list_review = []
list_user_rating = []
list_rank = []
list_desc = []
list_desc_url = []
list_cat = []

while True:
    source = p.read()
    p.close()
    ##print(source)

    soup = BeautifulSoup(source)
    a=soup.prettify()
##  print(a)


    list_divs = soup.find_all('div', class_='listing')
##  print(list_divs[0])
    
    for item in list_divs:

        if(item.find_all('a', class_='property_title') == []):
                list_name.append(None)
        else:
                list_name.append(item.find_all('a', class_='property_title')[0].string.replace("\n", ""))

        if(item.find_all('a', class_='property_title')[0]['href']==None):
                list_link.append(None)
        else:
                list_link.append(urllib.parse.urljoin('http://www.tripadvisor.in/Hotels-g294217-Hong_Kong-Hotels.html', item.find_all('a', class_='property_title')[0]['href']))
                
            
        if(item.find_all('img', class_='photo_image') == []):
                list_imgurl.append(None)
        else:
                list_imgurl.append(item.find_all('img', class_='photo_image')[0]['src'])

         
        if(item.find_all('img', class_ = 'sprite-ratings')==[]):
            list_user_rating.append(None)
        else:
            list_user_rating.append(item.find_all('img', class_='sprite-ratings')[0]['alt'].replace("\n", ""))


        if(item.find_all('span', class_='onShow') == []):
            list_desc.append(None)
        else:
            list_desc.append(item.find_all('span', class_='onShow')[0].select("b")[0].find_all_next(text = True, limit=2)[1].replace("\n", ""))


        if(item.find_all('div', class_="popRanking wrap ") == []):
            
            list_rank.append(None)
        else:
            a=item.find_all('div', class_="popRanking wrap ")[0].string.replace("\n", "")
            list_rank.append(a)
                                        

        if(item.find_all('p', class_="information description")==[]):
                list_desc_url.append(None)
        else:
                list_desc_url.append(urllib.parse.urljoin('http://www.tripadvisor.in/Hotels-g294217-Hong_Kong-Hotels.html', item.find_all('p', class_='information description')[0].find_all('a')[0]['href']))


        if(item.find_all('span', class_='more')==[]):
            list_review.append(None)
        else:
            list_review.append(item.find_all('span', class_='more')[0].find_all('a')[0].string.replace("\n", ""))

        if(item.find_all('div', class_="information attraction-type")==[]):
            list_cat.append(None)
        else:
            list_cat.append(item.find_all('div', class_= 'information attraction-type')[0].select('span')[0].find_all_next(text=True, limit=2)[1].replace("\n", ""))


    if(soup.find_all('span', class_='guiArw pageEndNext')!=[]):
        break
    n=soup.find_all('a', class_="guiArw sprite-pageNext ")[0]['href']
    print(n)
    url = urllib.parse.urljoin(url,n)
    print(url)
    p = urllib.request.urlopen(url)


for i in range(len(list_name)):
    print("Tour name: ", list_name[i])
    print("Category: ", list_cat[i])
    print("Details Page URL: ", list_link[i])
    print("User Rating: ",list_user_rating[i])
    print("Image URL: ",list_imgurl[i])
    print("Description: ", list_desc[i])
    print("Description URL: ", list_desc_url[i])
    print("Number of reviews: ",list_review[i])
    print("Rank of tour: ", list_rank[i])
    print('\n')




##print(list_name)
##print(list_imgurl[0])
##print(list_link[0])
##print(list_user_rating[0])                                
##print(list_desc[0])
##print(list_rank)
##print(list_desc_url)
##print(list_review)
##print(list_cat)


print(len(list_name))
print(len(list_imgurl))
print(len(list_link))
print(len(list_user_rating))
print(len(list_desc))
print(len(list_rank))
print(len(list_desc_url))
print(len(list_review))
print(len(list_cat))

                        
##print(type(list_divs[15].find_all('p', class_='information description')[0].find('a')[0]))
