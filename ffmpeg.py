import subprocess


urlRTSP = 'rtsp://root:ozhkarsucks@172.19.0.201:9014/axis-media/media.amp'



# mp4
mp4 = [
  'ffmpeg',
  '-i', urlRTSP,
  '-vcodec', 'copy',
  '-r', '100',
  '-f', 'mp4',
  '-movflags', 'frag_keyframe+empty_moov',
  'pipe:1'
]


webm = [
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


ogg = [
  'ffmpeg',
  '-i', urlRTSP,                       
  '-acodec', 'libvorbis',                  
  '-f' , 'ogg',                            
  'pipe:1'  
]


args = ogg


subprocess.call(args)