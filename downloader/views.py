from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.views import generic
from django.template import Template,Context		
class MainView(generic.TemplateView):
	template_name='main.html'
	def get_queryset(self):
		return HttpResponse('o')     
 
 
 
 
 
def imagelist(request):
	 url_tag=request.POST.get("url","")
	 import requests
	 try:
		 requests.get(url_tag)
		 request.session['url']=url_tag
		 with open("log.txt","a") as file:
			 file.write(url_tag)
			 file.write("\n")
			 file.close()
		 return render(request,"list.html",{"url":"    Downloading From :           "+url_tag},)
	 except:
		 return render(request,"list.html",{"url":"","error":" The link is either invalied or damaged . Please copy and paste a link directly from url tab of browser for best results "},)
def listitems(request):
	url_type=request.POST.get("type","")
	#python power
	url_tag=request.session['url']
	import requests
	from bs4 import BeautifulSoup as bs
	soup=bs(requests.get(url_tag).text,"html.parser")
	if url_type=="Images":
		imagelinks=soup.find_all("img")
		imgw=[]
		template="imglist.html"
		for link in imagelinks:
			hr=link.get("src")
			imgurl=requests.compat.urljoin(url_tag,hr)
			imgw=imgw+[imgurl]
		if len(imgw)==0:
			return render(request,template,{"notfound":"No image Found","url":"Downloading from : "+url_tag,"namee":url_tag,},)
		else:
			return render(request,template,{"imgw":imgw,"url":"Downloading from : "+url_tag,"namee":url_tag,},)
	elif url_type=="Videos":
		videolinks=soup.find_all("source")
		vidw=[]
		template="vidlist.html"
		for link in videolinks:
			hr=link.get("src")
			vodurl=requests.compat.urljoin(url_tag,hr)
			vidw=vidw+[vodurl]
		if len(vidw)==0:
			return render(request,template,{"notfound":"No Videos found","url":"Downloading from : "+url_tag,"namee":url_tag,},)
		else:
			return render(request,template,{"vidw":vidw,"url":"Downloading from : "+url_tag,"namee":url_tag,},)
	elif url_type=="Scripts":
		csslinks=soup.find_all("script")
		cssw=[]
		cssone=[]
		for link in csslinks:
			hr=link.get("src")
			cssurl=requests.compat.urljoin(url_tag,hr)
			cssw=cssw+[cssurl]
			cssone=cssone+[requests.get(cssurl).text]
		if len(cssw)==0:
			return render(request,"csslist.html",{"url":"Downloading from "+url_tag,"namee":url_tag,"notfound":"No scripts found"},)
		else:
			return render(request,"csslist.html",{"url":"Downloading from "+url_tag,"namee":url_tag,"cssw":cssw,"cssone":cssone,},)
	elif url_type=="Audios":
		audiolinks=soup.find_all('source')
		audw=[]
		for link in audiolinks:
			hr=link.get('src')
			audurl=requests.compat.urljoin(url_tag,hr)
			audw=audw+[audurl]
		if len(audw)==0:
			return render(request,"audiolist.html",{"url":"Downloading from "+url_tag,"namee":url_tag,"notfound":"No Audio Found",},)
		else:
			return render(request,"audiolist.html",{"url":"Downloading from "+url_tag,"namee":url_tag,"audw":audw,},)
	elif url_type=="CSS":
		csslinks=soup.find_all("link")
		cssw=[]
		cssone=[]
		for link in csslinks:
			hr=link.get("href")
			cssurl=requests.compat.urljoin(url_tag,hr)
			cssw=cssw+[cssurl]
			cssone=cssone+[requests.get(cssurl).text]
		if len(cssw)==0:
			return render(request,"csslist.html",{"url":"Downloading from "+url_tag,"namee":url_tag,"notfound":"No Css Scripts Found"},)
		else:
			
			return render(request,"csslist.html",{"url":"Downloading from "+ url_tag,"namee":url_tag,"cssw":cssw,"cssone":cssone,},)
	elif url_type=="Source":
		from pygments import highlight
		from pygments.formatters import HtmlFormatter
		from pygments.lexers import HtmlLexer
		#html lexer
		he=highlight(soup.prettify(),HtmlLexer(),HtmlFormatter())
		return render(request,"linklist.html",{"source":format_html(he),"url":"Source of : "+url_tag,},)
	elif url_type=="Tags":
		return render(request,"linklist.html",{"url":"Coming soon"})
	elif url_type=="Help":
		return render(request,"help.html",{},)
	elif url_type=="About":
		return render(request,"about.html",{},)
	else:
		ty="404"

def helpview(request):
	print("fd")


