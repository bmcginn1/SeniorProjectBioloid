

echo Update apt-get lists and upgrade existing
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y dist-upgrade

echo Install vim and screen
sudo apt-get -y install vim screen


echo Installing Port Audio Stuff.
sudo apt-get -y install portaudio19-dev
sudo apt-get -y install python-all-dev
sudo apt-get -y install python3-dev
sudo apt-get -y install python3-pyaudio python-pyaudio

echo Installing stuff for the watson cloud connectors.
echo This one takes a while and seems like it stalls, but just let it run!
read  -n 1 -p "Press any key to continue....  BUT REMEMBER IT MAY TAKE A WHILE TO RUN!" mainmenuinput
sudo apt-get  -y install libssl-dev libffi-dev build-essential scons swig
sudo easy_install3 --upgrade watson-developer-cloud


echo Installing the RPi GPIO stuff
sudo pip3 install RPi.GPIO


echo Copying the confil files for asound
cp asound.conf /etc/asound.conf
cp .asoundrc ~/.asoundrc


echo Install VLC
sudo apt-get -y install vlc

echo Install the required Python3 Libraries
sudo easy_install3 websocket-client
sudo pip3 install colour
sudo pip3 install python-vlc

echo Installing Pypot Bioloid control
sudo pip3 install pypot
sudo apt-get --yes install libatlas-base-dev


echo install other stuff
sudo pip install requests
sudo pip install codecs
sudo pip install configparser


echo Install the Adafruit Led software
cd ~/
git clone https://github.com/jgarff/rpi_ws281x.git
cd rpi_ws281x
scons
cd python
sudo python3 setup.py install


cd ~/
git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
cd pyaudio
sudo python3 setup.py install
