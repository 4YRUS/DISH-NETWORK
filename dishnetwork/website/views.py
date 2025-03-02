from django.shortcuts import render
from django.http import JsonResponse
import json 

from .models import imagefield
from django.core.files.base import ContentFile
import base64

from .readimage import read_image_for_blind
from .readaudio import read_audio_for_deaf

from .models import audiofield


def home(request):
	if request.method=='POST':
		try:
			data = json.loads(request.body)
			imagedata = data.get('image')
			a,imagestring = imagedata.split(';base64,')

			image = ContentFile(base64.b64decode(imagestring),name='firstimage.png')

			obj1 = imagefield.objects.create(image = image)

			
			print(obj1.image.url)
			try:
				message = (read_image_for_blind("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\DJANGO\\DISH\\dishnetwork\\" + obj1.image.url))

				print('\n',message)

				obj1.delete()

				return JsonResponse({"message": message})
			except:
				obj1.delete()
				return JsonResponse({"message":"Sorry, There was an error. "})
		except:
			return JsonResponse({"Error" : "Not Valid Form"})
		
	return render(request,'home.html',{})

def mute(request):
	return render(request,'mute.html',{})

def deaf(request):
	if request.method=='POST':

		audio = request.FILES.get('audio',[])

		obj1 = audiofield.objects.create(audio=audio)

		print(obj1.audio.url)
		
		try:
			message = read_audio_for_deaf("C:\\Users\\bss22\\OneDrive\\Desktop\\Don't Open\\DJANGO\\DISH\\dishnetwork\\" + obj1.audio.url)

			print(message)
			obj1.delete()

			return JsonResponse({"message":message})

		except:
			obj1.delete()

			return JsonResponse({"message":"Error &@& Error"})
	return render(request,'deaf.html',{})


