from django.shortcuts import render
from .mathdro_api_py import country
from .mathdro_api_py import news
import json

news= news.news()
news_list=news.get_news(4)
final_news_list=[]
final_news_link=[]
for news_i in news_list:
    final_news_list.extend(news_i.keys())
    final_news_link.extend(news_i.values())
wo = country.worldwide()
global_data = wo.worldwide_data()
world_li =[j for i,j in global_data.items()]
country_li = wo.country_list()
wo.get_country_data("india")
update_date =str(wo.last_date())
country_name=""
state_name=""


def home(request):
    return render(request, "home.html",{"dict":world_li, "c_list":country_li, "news_list":final_news_list, "news_link":final_news_link , "date1":update_date})

def country(request):
    global country_name
    country_name = request.GET['select']
    country_data = wo.get_country_data(country_name)
    li=[x for x in country_data.values()]
    state_data = wo.state_list(country_name)
    return render(request, "country.html",{"dict":li,"c_list":state_data,"date1":update_date, "news_list":final_news_list, "news_link":final_news_link})

def state(request):
    global state_name
    state_name = request.GET['select']
    state_data = wo.get_state_data(country_name,state_name,latest=True)
    state_data=state_data[0]
    li = [y for x,y in state_data.items()]
    return render(request, "state.html", {"dict":li,"date1":update_date, "news_list":final_news_list, "news_link":final_news_link})

def cdetail(request):
    country_name = request.GET["select"]
    state_data = wo.get_state_data(country_name)
    print(state_data)
    return render(request,"country_detail.html")