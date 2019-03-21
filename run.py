import cv2
import numpy as np
from classifier import classify
import tools
from Conversation.text_to_speech import TextToSpeech
from Conversation.sound_rec_demo import SpeechToText
import take_photo
from datetime import datetime
import os
COUNT = 0
NAME = ''
PRE_NAME = ''
NAME_LIST = []
START = datetime.now()


def face_detection():
    global COUNT
    global NAME
    global START
    global NAME_LIST
    cv2.namedWindow("test")
    cap=cv2.VideoCapture(0)
    success,frame=cap.read()
    classifier=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
    prelen = ''
    while success:
        success,frame=cap.read()
        size=frame.shape[:2]
        image=np.zeros(size,dtype=np.float16)
        image=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.equalizeHist(image,image)
        divisor=8
        h,w=size
        minSize=(w//divisor,h//divisor)
        faceRects=classifier.detectMultiScale(image,1.2,2,cv2.CASCADE_SCALE_IMAGE,minSize)
        print(len(faceRects))
        if prelen == len(faceRects) and len(faceRects) != 0:
            print('equal')
            for faceRect in faceRects:
                x,y,w,h=faceRect
                image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame, NAME, (x + 30, y + 30), font, 1, (255, 0, 255), 4)
            COUNT += 1
        else:
            print('classify')
            if len(faceRects) > 0:
                for faceRect in faceRects:
                    x,y,w,h=faceRect
                    image = frame[y - 10: y + h + 10, x - 10: x + w + 10]
                    cv2.imwrite('1.jpg', image)

                    NAME = classify('1.jpg')
                    voice = TextToSpeech()
                    end = datetime.now()
                    #print((end - START).seconds)
                    if (end - START).seconds > 60:
                        NAME_LIST = []
                        START = datetime.now()
                    #print(NAME_LIST)
                    if NAME == 'unknown people':
                        if tools.check_status() == False:
                            voice.play(voice.get_audio_bytes(
                                'Hi'))  
                        else:
                            time = 0
                            voice.play(voice.get_audio_bytes('I never meet you before. Can you spell your name? Just say your name. I will remember you. Make sure you are the only person that in front of me'))
                            speaking = SpeechToText()
                            name = SpeechToText().record_to_file()
                            voice.play(voice.get_audio_bytes('So, your name is ' + name + 'Is it right? Please answer yes or no.'))
                            while 'yes' not in answer:
                                voice.play(voice.get_audio_bytes('Can you spell your name again?')) 
                                voice.play(voice.get_audio_bytes('So, your name is ' + name +
                                                                 'Is it right? Please answer yes or no.')) 
                                answer = SpeechToText().record_to_file()
                                answer = answer[:-1]
               
                            name = name.replace('.', '')
                            name = name.replace(' ', '')
                            # Take 10 photo of this guy, and turn it to file.

                            while time <= 10:
                                print('here')
                                cv2.imwrite('YOU DIRECTORY\\update\\' + str(time) + '.jpg', image)
                                time += 1
                            files = ['1.jpg','2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '0.jpg']
                            zip_file = name + '.zip'
                            take_photo.zip_files(files, zip_file)
                            for file in files:
                                os.remove(file)
                            os.chdir(r'D:\Queens\fourth\cisc499\facetracking\final_version')
                            ##tools.update([zip_file])  # to update the classifier
                            os.remove('update//' + zip_file)
                            NAME_LIST.append(name)


                    else:
                        if NAME not in NAME_LIST:
                            voice.play(voice.get_audio_bytes('Hi,'+NAME))
                            NAME_LIST.append(NAME)



                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    font = cv2.FONT_HERSHEY_SIMPLEX
                    cv2.putText(frame, NAME, (x + 30, y + 30), font, 1, (255, 0, 255), 4)
                    COUNT += 1
                    prelen = len(faceRects)
            else:
                prelen = len(faceRects)

            #print(len(image))

        cv2.imshow("test",frame)
        key=cv2.waitKey(10)
        c=chr(key&255)
        if c in ['q','Q',chr(27)]:
            break
    cv2.destroyWindow("test")

face_detection()
