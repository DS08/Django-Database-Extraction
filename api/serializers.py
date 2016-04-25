from rest_framework import serializers

#from app1.models import Scholarship
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        #fields = ('name', 'deadline', 'created','amount_in_rupees','procedure','eligibility')
        fields= ('username','first_name','last_name','email')