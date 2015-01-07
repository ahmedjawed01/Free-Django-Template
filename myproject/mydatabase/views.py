from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext,render
import json
from .models import *
from django.http import HttpResponseRedirect
import re
import time








def home(request):

    
    meta_title="Home"
    meta_descr="my description"
    header_title=Settings.objects.get(id=1)
    all_data=Pages.objects.filter(active=True).order_by('-date')
    data=all_data[0]
    title=data.title
    content=data.content
    slug=data.slug
    article_id=data.id
    date=data.date
    
    return render_to_response('page.html', 
            { 
            "title":title,
            "content":content,
            "meta_title":meta_title,
            "meta_descr":meta_descr,
            "header_title":header_title,
            "all_data":all_data,
           
            }  
            ,context_instance=RequestContext(request))







def article(request,page_slug=""):

    header_title=Settings.objects.get(id=1)
    page_slug="/"+page_slug
    all_data=Pages.objects.filter(active=True).order_by('-date')
    try:
        data=Pages.objects.get(slug=page_slug,active=True)
    except:
        return HttpResponseRedirect("/notfound")

    title=data.title
    content=data.content
    slug=data.slug
    article_id=data.id
    date=data.date
  
    return render_to_response('page.html', 
            { 
            
           
            "meta_title":title,
            "meta_descr":data.short_descr,
            "title":title,
            "content":content,
            "slug":slug,
            "date":date,
            "all_data":all_data,
            "header_title":header_title,
           
           
            }  
            ,context_instance=RequestContext(request))









def generate_sitemap(request):
    sitemap_data='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'

    sitemap_data+='<url><loc>http://www.djangotutsme.com/</loc><lastmod>2014-10-10</lastmod><changefreq>monthly</changefreq><priority>1.0</priority></url>'
    
   

    pages=Pages.objects.filter(active=True)
    for data in pages:
        sitemap_data+='<url><loc>http://www.djangotutsme.com'+data.slug+'</loc><lastmod>'+str(data.date).split()[0]+'</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>'

    



    sitemap_data+='</urlset>'

    

    

    
    return HttpResponse(sitemap_data,content_type="application/xhtml+xml")



