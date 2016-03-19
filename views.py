from django.shortcuts import render
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt 
import requests
import json
from django.http import HttpResponse
from random import shuffle
# Create your views here.



@csrf_exempt
def Ytrend(request):
	k=[]
	title=[]
	link=[]
	img=[]
	
	
	r=requests.get("https://www.youtube.com/feed/trending")
	soup=BeautifulSoup(r.content,"lxml")
	data=soup.find_all('h3',{'class':'yt-lockup-title'})
	idata=soup.find_all('div',{'class':'yt-thumb video-thumb'})
	for i in range(20):
		n={}
		try:

			title.append(str(data[i].a.text))
			link.append(str(data[i].a['href'])[9:])
			img.append(str(idata[i].img['src']))
			n['head']=title[i]
			n['link']="https://youtu.be/" +link[i]
			n['img']="http:"+img[i]
				
			k.append(n)
				#return HttpResponse(json.dumps(n), content_type='application/json' )
				
		except:
			pass
		#j_d=json.dumps(k)
		#return HttpResponse(json.dumps(k), content_type='application/json' )	
	title=[]
	link=[]
	img=[]
	
	q=requests.get("https://news.google.com/news")
	soup=BeautifulSoup(q.content,"lxml")
	data=soup.find_all('h2',{'class':'esc-lead-article-title'})
	idata=soup.find_all('div',{'class':'esc-thumbnail-image-wrapper '})
	for i in range(20):
		n={}
		try:
			
			title.append(str(data[i].a.text))
			link.append(str(data[i].a['href']))
			img.append(str(idata[i].img['src']))
			n['head']=title[i]
			n['link']=link[i]
			n['img']="http:"+img[i]
			k.append(n)
		except:
			pass
			
	img=[]
	b=0
	e=0
	title=[]
	link=[]
	
	z=0
	w=requests.get("http://9gag.com/")
	soup=BeautifulSoup(w.content,"lxml")
	c=soup.find_all('img',{'class':'badge-item-img'})
	d=soup.find_all('h2',{'class':'badge-item-title'})
	for i in range(10):
		n={}	
		try:	
			o=0
			new=""
			ntitle=""			
			img.append(str(c[i]['src']))
			title.append(str(d[i].text))
			
			








			l=len(title[i])
			n['head']=title[i][18:l-14]
			n['link']="http://www.9gag.com"
			n['img']=img[i]
			k.append(n)
											
		except:
			pass
	#shuffle(k)
	#j_d=json.dumps(k)



	title=[]
	link=[]
	img=[]
	w=requests.get("https://twitter.com/?lang=en")
	soup=BeautifulSoup(w.content,"lxml")
	c=soup.find_all('strong',{'class':'fullname js-action-profile-name show-popup-with-id'})
	p=soup.find_all("div",{'class':"AdaptiveMedia-photoContainer js-adaptive-photo "})
	l=soup.find_all("a",{'class':"account-group js-account-group js-action-profile js-user-profile-link js-nav"})

	
	for i in range(20):
		n={}
		try:
			title.append(str(c[i].text))
			img.append(str(p[i]['data-image-url']))
			link.append(str(l[i]['href']))
			n['head']=title[i]+" tweeted"
			n['link']="http://www.twitter.com"+link[i]
			n['img']=img[i]
			k.append(n)
			
		except:
			pass	
	#d=soup.find_all('h2',{'class':'badge-item-title'})


	#return HttpResponse(json.dumps(k), content_type='application/json' )	
	#return render(request,'scnd.html',{"link":img,"title":title})
	shuffle(k)
	j_d=json.dumps(k)
	return HttpResponse(json.dumps(k), content_type='application/json' )
	
		
		

			
