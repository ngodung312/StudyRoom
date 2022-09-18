from django.http import StreamingHttpResponse
import cv2
from django.shortcuts import render
# from chat import ADC_2022_MediaPipe_Pose as ADC

# Create your views here.

def main_view(request):
    if request.method == "GET":
        context = {'data': 'username'}
        return render(request, 'chat_index.html', context=context)

def stream():
    cap = cv2.VideoCapture(0) 

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: failed to capture image")
            break

        cv2.imwrite('demo.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + open('demo.jpg', 'rb').read() + b'\r\n')

def video_feed(request):
    return StreamingHttpResponse(stream(), content_type='multipart/x-mixed-replace; boundary=frame')
