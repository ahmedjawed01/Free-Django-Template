from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext,render
import json
from .models import *
from django.http import HttpResponseRedirect
import re
import time

from django.views.generic import ListView

from django.shortcuts import get_object_or_404

class BaseView(ListView):   
    context_object_name = 'data'
    template_name='page.html'
    meta_title="Home"
    meta_descr="my description"
    header_title=Settings.objects.get(id=1)
    all_data=Pages.objects.filter(active=True).order_by('-date')
   

    def get_context_data(self, **kwargs):
     
        context = super(BaseView, self).get_context_data(**kwargs)
        context['meta_title'] = self.meta_title
        context['meta_descr'] = self.meta_descr
        context['header_title'] = self.header_title
        context['all_data'] = self.all_data
        
        return context



class home(BaseView):
  
    
    queryset =  Pages.objects.filter(active=True).order_by('-date')[0]
    
   
class article(BaseView):
    
    def get_queryset(self,**kwargs):
       
        queryset=get_object_or_404(Pages, slug="/"+self.kwargs["page_slug"])
        self.meta_title=queryset.title
        self.meta_descr=queryset.short_descr
        return queryset






def generate_sitemap(request):
    sitemap_data='<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
    sitemap_data+='<url><loc>http://www.djangotutsme.com/</loc><lastmod>2014-10-10</lastmod><changefreq>monthly</changefreq><priority>1.0</priority></url>'
    pages=Pages.objects.filter(active=True)
    for data in pages:
        sitemap_data+='<url><loc>http://www.djangotutsme.com'+data.slug+'</loc><lastmod>'+str(data.date).split()[0]+'</lastmod><changefreq>monthly</changefreq><priority>0.5</priority></url>'

    sitemap_data+='</urlset>'
    return HttpResponse(sitemap_data,content_type="application/xhtml+xml")



