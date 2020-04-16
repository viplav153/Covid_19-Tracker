from django.shortcuts import render, HttpResponse, redirect
import requests
from bs4 import BeautifulSoup
import time

# Create your views here.

def home(request):
    

    def webData(url): #Getting The Data From The Website
        r = requests.get(url)
        return r.text

    #if __name__ == "__main__":
        
    html_doc = webData('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(html_doc, 'html.parser') #Parsing The Data
            

    x= soup.find_all ('table')
    exc={'table':str (x)}
    #data=exc['table']
            
    return render(request, 'home.htm',exc) 
            
            







    
