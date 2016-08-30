import datetime as date
import subprocess


#cur = date.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
cur = date.datetime.now().strftime('%H:%M:%S.%f')[:-3]
cmd = "ffmpeg -y -i rtsp://192.168.1.88:554/stander/livestream/0/0 -r 10 -f image2 /home/santosh/Music/%s.jpg" %(cur)

p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE)

print cmd
