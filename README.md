Working log

(Fix error)
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock*
sudo dpkg --configure -a 
sudo apt update

(Setup venv)
sudo apt-get install python3.8
sudo apt-get install python3.8-venv
python3.8 -m venv venv
source venv/bin/activate

(Install pygame)
sudo apt-get install python-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev
sudo apt-get install mercurial
sudo apt install libfreetype6-dev
sudo apt-get install python3.8-dev
pip install pygame
pip freeze > requirements.txt


