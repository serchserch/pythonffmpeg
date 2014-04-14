
import requests
import json
import subprocess


from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpResponse

from django.views.decorators.http import condition

#
#
#
def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'hi': "This is Python!"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('index.html', context_dict, context)
    #return HttpResponse("Rango says hello world!")
    



#
# Streaming de video en mp4 utilizando ffmpeg
# deps[ffmpeg, subprocess]
def videomp4(request):
    urlRTSP = 'rtsp://root:ozhkarsucks@172.19.0.201:9014/axis-media/media.amp'  

    
    # mp4
    attr = [
      'ffmpeg',
      '-i', urlRTSP,
      '-vcodec', 'copy',
      '-r', '100',
      '-f', 'mp4',
      '-movflags', 'frag_keyframe+empty_moov',
      'pipe:1'
    ]       
    pipe = subprocess.Popen(attr, stdout=subprocess.PIPE)        
    resp = HttpResponse(pipe.stdout, mimetype='video/mp4')
    
    return resp


#
# Streaming de video en ogg utilizando ffmpeg
# deps[ffmpeg, subprocess]
def videoogg(request):
    urlRTSP = 'rtsp://root:chinitossucks@172.19.0.202:554/axis-media/media.amp'
    attr = [
      'ffmpeg',
      '-i', urlRTSP,                       
      '-acodec', 'libvorbis',                  
      '-f' , 'ogg',                            
      'pipe:1'  
    ]    
    pipe = subprocess.Popen(attr, stdout=subprocess.PIPE)        
    resp = HttpResponse(pipe.stdout, mimetype='video/ogg')
    
    return resp


#
# Streaming de video en ogg utilizando ffmpeg
# deps[ffmpeg, subprocess]
def videowebm(request):
    urlRTSP = 'rtsp://root:chinitossucks@172.19.0.202:554/axis-media/media.amp'  
    attr = [
      'ffmpeg',
      '-i', urlRTSP,
      '-vcodec', 'libvpx',                     
      '-g', '0',                              
      '-me_method' , 'zero',                  
      '-flags2','fast',                    
      '-preset','ultrafast',                 
      '-tune','zerolatency',                
      '-r', '100',                            
      '-f', 'webm',                           
      '-b:v', '1M',                            
      '-crf', '20',                          
      'pipe:1' 
    ]    
    pipe = subprocess.Popen(attr, stdout=subprocess.PIPE)        
    resp = HttpResponse(pipe.stdout, mimetype='video/webm')
    
    return resp





        
        
#
# Ejemplo de request a servicios de bd 
# deps [requests]
def login(request):
    
    payload = {'idCorreo': 'sergio.morlan@globalcorporation.cc', 'pass': 'sergio', 'tipoSesion': 'w'}
    
    r = requests.post('http://172.19.0.123/Services/Json/eClaroUsuarios/ControlUsuarios.svc/mostrarDatosUsuario/', 
                     headers={'content-type': 'application/json'}, data=json.dumps(payload))

    return HttpResponse((r))



    #resp = urllib2.urlopen(req)
    #content = resp.read()
    #return HttpResponse(content)