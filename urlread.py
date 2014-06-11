import urllib, urllib.request
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

list_a = []
##list_name = []
list_link = []
##list_rating = []
##list_imageurl = []
##list_review = []
##list_user_rating = []
##list_rank = []


list_det=[]

##t=time.process_time()
t=time.time()
##url = "http://www.tripadvisor.in/Hotels-g294217-Hong_Kong-Hotels.html"
url = input("Enter URL: ")
start = url
##p = urllib.request.urlopen(url)
check=0

while True:
    try:
        p = urllib.request.urlopen(url)
        source = p.read()
        p.close()
        soup = BeautifulSoup(source)
        r = soup.find_all('div', class_="orphan   hotelsCount")[0].select('b')[0].string
##        print(r)
##        print(type(r))
        check=int(r.replace(" ", ""))
##        print(check)
        break
    except:
        print("URL exception")
##        print(o)
##        o=o+1
        continue
        
        
i=0
print(check)

while True:
##    if(i==1):
##        break
##    
    try:
        p = urllib.request.urlopen(url)
    except IOError:
        print("URL exception")
        continue
        
    
    source = p.read()
    
    p.close()

    soup = BeautifulSoup(source)
    a=soup.prettify()
    
    x = a.split("var lazyImgs = [")[1].split("]")[0]
    ##for i in x:
    ##    if i == ',':
    ##        x.remove(i)

    ##print(x)
            





    list_divs = soup.find_all("div", class_="listing wrap")
    ##print(list_divs[0].find_all('a', class_='property_title')[0].string)
    ##print(list_divs[0].find_all('a', class_='property_title')[0]['href'])

    

    for item in list_divs:

        b=item.find_all('a', class_='property_title')[0]['href']
        if(b in list_link):
            continue
        
        dict_det = {}
        a=item.find_all('a', class_='property_title')
        
        if(a == []):
##            list_name.append(None)
            dict_det['Hotel name'] = None
        else:
##            list_name.append(a[0].string.replace("\n", ""))
            dict_det['Hotel name'] = a[0].string.replace("\n", "")
            
        
        
        if(b==None):
            list_link.append(None)
            dict_det['Details URL'] = None
        else:
            list_link.append( b)
            dict_det['Details URL']  = urllib.parse.urljoin('http://www.tripadvisor.in/Hotels-g294217-Hong_Kong-Hotels.html', b)
            

        c=item.find_all('img', class_='sprite-ratings-gry')
        if(c==[]):
##            list_rating.append(None)
            dict_det['Star rating'] = None
        else:
##            list_rating.append(c[0]['alt'].replace("\n", ""))
            dict_det['Star rating'] = c[0]['alt'].replace("\n", "")

        d=item.find_all('img', class_='photo_image')
        if(d==[]):
##            list_imageurl.append(None)
            dict_det['Image URL'] = None
        else:
##            list_imageurl.append(x.split(d[0]['id'])[1].split('"data":"')[1].split('"}')[0])
            dict_det['Image URL'] = x.split(d[0]['id'])[1].split('"data":"')[1].split('"}')[0]
        
        e=item.find_all('span', class_='more')
        if(e == []):
##            list_review.append(None)
            dict_det['Number of reviews'] = None
        else:
##            list_review.append(e[0].find_all('a')[0].string.replace("\n", ""))
            dict_det['Number of reviews'] = e[0].find_all('a')[0].string.replace("\n", "")
        
        f=item.find_all('img', class_='sprite-ratings')
        if(f==[]):
##            list_user_rating.append(None)
            dict_det['User rating'] = None
        else:
##            list_user_rating.append(f[0]['alt'].replace("\n", ""))
            dict_det['User rating'] = f[0]['alt'].replace("\n", "")

        g=item.find_all('div', class_='slim_ranking')
        if(g == []):
##            list_rank.append(None)
            dict_det['Ranking'] = None
        else:
##            list_rank.append(g[0].string.replace("\n", ""))
            dict_det['Ranking'] = g[0].string.replace("\n", "")


##        print(dict_det)
        list_det.append(dict_det)

        
    if(int(len(list_det)) == int(check)):
##        i=1
        break
    if(soup.find_all('span', class_='guiArw pageEndNext')!=[]):
        n=start
        print(len(list_name))
        print("again")
    else:
        n=soup.find_all('a', class_='guiArw sprite-pageNext ')[0]['href']
##    print(n)
    url = urllib.parse.urljoin(url,n)
##    print(url)
##    p = urllib.request.urlopen(url)


##time = time.process_time() - t
time = time.time() - t

for i in range(len(list_det)):
    print(list_det[i])
    print("\n")

    
##    print("Hotel name: ", list_name[i])
##    print("Details Page URL: ", list_link[i])
##    print("Star Rating: ",list_rating[i])
##    print("Image URL: ",list_imageurl[i])
##    print("Number of reviews: ",list_review[i])
##    print("User Rating: ",list_user_rating[i])
##    print("Rank of Hotel: ", list_rank[i])
##    print('\n')


##print(type(len(list_name)))

##print("Hotel name: ", list_name)
##print(list_link)
##print("Star Ratings: ",list_rating)
##print("Image URLs: ",list_imageurl)
##print("Number of reviews: ",list_review)
##print("User Ratings: ",list_user_rating)
##print(list_rank)
##
##print(len(list_name))
##print(len(list_link))
##print(len(list_rating))
##print(len(list_imageurl))
##print(len(list_review))
##print(len(list_user_rating))
##print(len(list_rank))

print(len(list_det))
print(time)

##print(list_divs[2].find_all('img', class_='photo_image'))
"""
##print(list_divs[4].find_all('img', class_='sprite-ratings-gry'))

##list = soup.find_all('a', class_='property_title')
##print(list[0].string)
##a=list[0]['href']
##print(list[0]['href'])
##print(urllib.parse.urljoin('http://www.tripadvisor.in/Hotels-g294217-Hong_Kong-Hotels.html', a))

##i=0

##
##for item in list:
##    list_name.append(list[i].string)
##    list_link.append(urllib.parse.urljoin('http://www.tripadvisor.in/Hotels-g294217-Hong_Kong-Hotels.html', item['href']))
##    try:
##        if soup.find_all("img", class_="sprite-ratings-gry")[i]['alt']:
##            print ('yes')
##        else:
##            print ('no')
##    except Exception as e:
##        print (e)
##    list_rating.append(soup.find_all("img", class_="sprite-ratings-gry")[i]['alt'])
##    i=i+1
##
##                        
##
##print(len(list_name))
##print(len(list_link))
##print(len(list_rating))


##rating = soup.find_all("img", class_="sprite-ratings-gry")
##for a in rating:
##    list_rating.append(a['alt'])
##print(len(list_rating))

####print(rating)
##print(rating[0]['alt'])


#for item in s:
#    list_a = item.find_all('a', class_='property_title')
#    print(list_a)


##s = "<html><div>test</div><ul><li>1</li><li>2</li><li>3</li></ul></html>"
##
##soup = BeautifulSoup(s)
####print(soup.prettify())
##list = []
##i=1
##for child in (soup.ul.find_all()):
####    print(child.text)
##    list.insert(int(child.text), i)
##    i=i+1

"""
