from __future__ import unicode_literals

from django.db import models
from django import forms

# Create your models here.
class Scholarship(models.Model):
	name = models.CharField(max_length=120,blank=True,null=True)
	amount_in_rupees = models.IntegerField()
	deadline = models.DateTimeField("Deadline")
	created = models.DateTimeField(auto_now_add = True)
	procedure = models.TextField()#forms.CharField(widget=forms.Textarea)#models.CharField(max_length = 120,blank = True,null = True)
	eligibility = models.TextField()#forms.CharField(widget=forms.Textarea)#models.CharField(max_length = 120,blank = True,null = True)    ##forms.CharField( widget=forms.TextArea )



	def __unicode__(self):
	 return self.name