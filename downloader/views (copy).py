from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.views import generic
from django.template import Template,Context		
class MainView(generic.TemplateView):
	template_name='base.html'
	def get_queryset(self):
		return HttpResponse('o')
def helpview(request):
	return render(request,'help.html',{},)
def imagelist(request):
        tag_entered=request.POST.get('tag','')
        type_wanted=request.POST.get('type','')
        #python power
        import requests
        from bs4 import BeautifulSoup as bs
        respond=requests.get(tag_entered)
        responds=respond.text
        payload=bs(responds,'html.parser')
        htmls=payload.prettify()
        if type_wanted=='source':
        	return render(request,'list.html',{'special':htmls},)
        elif type_wanted=='image':
        	imglinks=payload.find_all('img')
        	imgw=[]
        	for link in imglinks:
        		imgw=imgw+[link.get('src')]
        		
        	return render(request,'imglist.html',{'imgl':imgw,'namee':tag_entered},)
        elif type_wanted=='link':
        	imglinks=payload.find_all('a')
        	imgw=[]
        	for link in imglinks:
        		imgw=imgw+[link.get('href')]
        		
        	return render(request,'linklist.html',{'imgl':imgw,'namee':tag_entered,'nameee':type_wanted},)
        elif type_wanted=='script':
        	imglinks=payload.find_all('script')
        	imgw=[]
        	for link in imglinks:
        		imgw=imgw+[link.get('src')]
        		
        	return render(request,'linklist.html',{'imgl':imgw,'namee':tag_entered,'nameee':type_wanted},)
        elif type_wanted=='tags':
        	imglinks=payload.find_all('meta')
        	imgw=[]
        	for link in imglinks:
        		imgw=imgw+[link.get('keywords')]
        		imgw=imgw+[link.get('name')]
        		
        	return render(request,'linklist.html',{'imgl':imgw,'namee':tag_entered,'nameee':type_wanted},)
        	
        	
        
        


