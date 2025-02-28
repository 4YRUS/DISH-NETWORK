from django.shortcuts import render
from django.http import JsonResponse
import json 

from .models import imagefield
from django.core.files.base import ContentFile
import base64

from .readimage import read_image_for_blind


def home(request):
	if request.method=='POST':
		try:
			data = json.loads(request.body)
			imagedata = data.get('image')
			a,imagestring = imagedata.split(';base64,')

			image = ContentFile(base64.b64decode(imagestring),name='firstimage.png')

			obj1 = imagefield.objects.create(image = image)

			
			print(obj1.image.url)
			
			message = (read_image_for_blind("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\DJANGO\\DISH\\dishnetwork\\" + obj1.image.url))

			print('\n',message)

			obj1.delete()

			return JsonResponse({"message": message})
		except:
			return JsonResponse({"Error" : "Not Valid Form"})
		
	return render(request,'home.html',{})

def mute(request):
	return render(request,'mute.html',{})

def deaf(request):
	return render(request,'deaf.html',{})


