from django.http import HttpResponse
from django.template import Template, RequestContext
from django.shortcuts import render
from userDS.parser import user_page_parse, signed_list_parse
from userDS.spojUser import spojUser
from userDS.spojUserMulti import spojUserMulti
import urllib2
from google.appengine.api import urlfetch
def home(request):
	return render(request, 'home.html')

def get_user_info(user_name):
	result = urlfetch.fetch('http://www.spoj.com/SPOJ/users/'+user_name, deadline=30)
	encoding=result.headers['content-type'].split('charset=')[-1]
	html = result.content.decode('ISO-8859-2')
	html = html.replace('\n','')

	user_info = user_page_parse(html, user_name)

	signed_html = urlfetch.fetch('http://www.spoj.com/SPOJ/status/'+user_name+'/signedlist/', deadline=30).content
	problem_info = signed_list_parse(signed_html, user_info)
	user_info.probPool.calc_stats()
	user_info.get_classical_table()
        # new addition
	user_info.get_latest()
	return user_info

def single_user(request, user_name):
	user_info = get_user_info(user_name)
	return render(request, 'single.html',{'main': user_info})
	#html = get_user_info(user_name)
	#return HttpResponse(html)

def submit(request):
        return render(request, 'submit.html')
