from django.db import models
from django.utils.text import slugify


class Settings(models.Model):

    title = models.CharField(max_length=256) 
    value = models.TextField(null=True,default=None,blank=True)
  
    

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural="Settings"





class Pages(models.Model):

    title = models.CharField(max_length=256,null=True) 
    short_descr = models.CharField(max_length=256,null=True,blank=True) 
    content=models.TextField(null=True,default="")
    slug = models.CharField(max_length=256,null=True,default="",blank=True) 
    active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)
  
    

    def slug_link(self):
        return '<a target="_blank" href="%s">%s</a>' % (self.slug,self.slug)
    slug_link.allow_tags = True


    def __unicode__(self):
        return self.title 

    
    def save(self):
    
        if Pages.objects.filter(title=self.title).count()>0:
            title=self.title+str(self.id)
        else:
            title=self.title
        
        self.slug = '/%s' % (slugify(self.title))
        
        super(Pages, self).save()


    class Meta:
        verbose_name_plural="Pages"




         