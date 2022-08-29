from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests
# Create your views here.


def index(request):
    # print(request.GET.get('q'))
    if request.GET.get('q') is not None:
        query = request.GET.get('q')
        url = 'https://www.ask.com/web?q='+query 
        res = requests.get(url) 
        soup = bs(res.text, 'lxml')
        # print(soup)
        container_lists = soup.find_all('div', {'class': 'PartialSearchResults-item'})
        results = []
        for container in container_lists :
            # HEADER LINK AND TEXT 
            container_header_title = container.find(class_='PartialSearchResults-item-title').text
            container_header_url = container.find('a').get('href')
            # SUBHEADER TEXT
            container_subheader_title = container.find(class_='PartialSearchResults-item-url').text
            container_desc = container.find(class_='PartialSearchResults-item-abstract').text
            results.append([container_header_title , container_header_url, container_subheader_title , container_desc ])
    context = { 'results': results }
    return render(request, 'index.html', context)

