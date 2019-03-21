# Robot
I just comment out ##tools.update([zip_file]) in run.py, which can update new people to classifier, but the funtion can work.



Python:
sudo apt-get install build-essential checkinstall
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
cd /usr/srcsudo 
wget https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz
sudo tar xzf Python-3.5.2.tgz
cd Python-3.5.2 
sudo ./configure 
sudo make altinstall

IBM Watson API:
pip install --upgrade "watson-developer-cloud>=2.8.0"

OpenCV: # can only work if there is UI for the system.
sudo apt-get install python-opencv
import cv2 as cv
print(cv.__version__)


Pyaudio:
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install ffmpeg libav-tools
Sudo pip install pyaudio


