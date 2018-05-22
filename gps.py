from geopy.geocoders import Nominatim
import webbrowser
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from decimal import Decimal
chrome_path_script = r"C:\Python34\Scripts\chromedriver"
geolocator = Nominatim()
address = input("enter address:\t")
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
location = geolocator.geocode(address)
url=''
distance =0
miles =0
my_url=''
given =''
def google_earth():
    g1 = address.split()
    g2=''
    for word in g1:
        g2+="+"+word
    gurl='https://earth.google.com/web/search/'+g2
    webbrowser.get(chrome_path).open(gurl)
def navigation():
    global given
    def google_maps_url():
        global url
        a1 = address.split()
        b=''
        for word in a1:
            b+="+"+word
        a2= address2.split()
        b2 =''
        for word in a2:
            b2+="+"+word
        url = 'https://www.google.com/maps/dir/'+b +'/'+ b2
    def here_we_go_url():
        global my_url
        location = geolocator.geocode(address)
        (a,b)=((location.latitude, location.longitude))
        location = geolocator.geocode(address2)
        (c,d)=((location.latitude, location.longitude))
        a= str(a)
        b= str(b)
        c= str(c)
        d= str(d)
        my_url = 'https://www.openstreetmap.org/directions?engine=osrm_car&route='+a +'%2C'+b+'%3B'+c+'%2C'+d

    def google_maps():
        global miles
        google_maps_url()
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()

        page_soup = soup(page_html,"lxml")

        match = page_soup.html
        match = str(match)

        if 'mile' in match:

            dis=(match.index('mile'))


        g = str((match[dis-6]))
        a=str((match[dis-5]))
        b=str((match[dis-4]))
        c=str((match[dis-3]))
        d=str((match[dis-2]))
        e=str((match[dis-1]))
        try:
            f = g+a+b+c+d+e
            miles = float(f)
            print("according to the googlemaps distance:\t",miles," miles")
        except:
            try:
                f =a+b+c+d+e
                miles = float(f)
                print("according to the googlemaps distance:\t",miles, " miles")
            except:
                f=b+c+d+e
                miles = float(f)
                print("according to the googlemaps distance:\t", miles, " miles")

    def here_we_go():
        global distance
        here_we_go_url()
        browser = webdriver.Chrome(chrome_path_script)
        browser.get(my_url)
        review = browser.find_elements_by_id("routing_summary")
        for post in review:
            e=(post.text)
        a=[]
        d=[e]
        for i in d:
            for j in i:
                a.append(j)
        space = a.index(' ')
        m= a.index('m')
        k =100
        try:
            k = a.index('k')
        except:
            pass
        distance=''
        if k<m:
            m=k
        while True:
            if space<(m-1):
                space=space+1
                distance+=a[space]
            else:
                break
        distance = int(distance)
        if k==m:
            distance =0.621371*distance
        else:
            distance =0.621371*distance/1000
        browser.quit()
        print("According to open street map distance is\t:",distance, " miles")
    def browser(link):
        webbrowser.get(chrome_path).open(link)
    if given == 'N' or given=='n':
        address2 = input("enter destination: \t")
        google_maps()
        here_we_go()
    x = input("Do you want to open shortest distance?: Y for yes or N for no:\t ")

    if x=="y" or x=="Y":

        if Decimal(distance)>Decimal(miles):
            browser(url)
        if Decimal(miles)>Decimal(distance):
            browser(my_url)
given = input("press E for google Earth  and N for navigation: \t")
if given == 'E' or given=='e':
    google_earth()
else:
    navigation()