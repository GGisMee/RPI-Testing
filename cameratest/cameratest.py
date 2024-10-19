from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FileOutput
from time import sleep

# Initiera kameran
camera = Picamera2()

# Ställ in för att visa förhandsvisningen
camera.start_preview(Preview.QT)

# Konfigurera kameran för video
camera.configure(camera.create_video_configuration())

# Starta kameran
camera.start()

# Skapa encoder för H264-video
encoder = H264Encoder()

# Skapa utdata för att spara videon till en fil
output = FileOutput("video_test.h264")

# Starta inspelningen med encoder och utdata
camera.start_recording(encoder, output)

# Filma i 10 sekunder
sleep(10)

# Stoppa inspelningen
camera.stop_recording()
