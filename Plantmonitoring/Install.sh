#!/bin/sh

enter_full_setting()
{
lua - "$1" "$2" <<EOF > "$2.bak"
local key=assert(arg[1])
local fn=assert(arg[2])
local file=assert(io.open(fn))
local made_change=False
for line in file:lines() do
  if line:match("^#?%s*"..key) then
    line=key
    made_change=True
  end
  print(line)
end
if not made_change then
  print(key)
end
EOF
mv "$2.bak" "$2"
}

toggle_setting_on_off()
{
lua - "$1" "$2" "$3" <<EOF > "$3.bak"
local key=assert(arg[1])
local value=assert(arg[2])
local fn=assert(arg[3])
local file=assert(io.open(fn))
local made_change=False
for line in file:lines() do
  if line:match("^#?%s*"..key.."=.*$") then
    line=key.."="..value
    made_change=True
  end
  print(line)
end
if not made_change then
  print(key.."="..value)
end
EOF
mv "$3.bak" "$3"
}

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo 'Welcome to the Plantmonitoring setup'
echo 'Please note that the initial setup requires an active internet connection.'
echo 'First, we will update the apt-get database'
sudo apt-get -qq update
echo '----------------'
echo 'Installing prerequisites for the Plantmonitoring Software: pip, i2c tools, python-smbus, web.py, redis-py'
sudo apt-get -qq -y install python-pip i2c-tools python-smbus
sudo pip install web.py redis peewee
echo '----------------'
echo 'Activating needed settings using raspi-config: I2C, Camera and the default boot behaviour'
sudo raspi-config nonint do_i2c 0
sudo raspi-config nonint do_camera 0
sudo raspi-config nonint do_boot_behaviour B1
echo '----------------'
echo 'Making the pi ready to read DHT11 Sensors'
sudo apt-get -qq -y install build-essential python-dev
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
(cd $DIR/Adafruit_Python_DHT && exec sudo python setup.py install) >> /dev/null
echo '----------------'
echo 'Registering as a service for systemctl'
echo 'For this, we follow the instructions from https://www.raspberrypi.org/documentation/linux/usage/systemd.md'
SERVICE_FILE="/etc/systemd/system/Plantmonitoring.service"
sudo echo "[Unit]" > $SERVICE_FILE
sudo echo "Description=Plantmonitoring" >> $SERVICE_FILE
#sudo echo "After=network-online.target" >> $SERVICE_FILE
sudo echo "[Service]" >> $SERVICE_FILE
sudo echo "ExecStart=/usr/bin/python -u ${DIR}/Plantmonitoring.py" >> $SERVICE_FILE
sudo echo "WorkingDirectory=${DIR}" >> $SERVICE_FILE
sudo echo "StandardOutput=inherit" >> $SERVICE_FILE
sudo echo "StandardError=inherit" >> $SERVICE_FILE
sudo echo "Restart=always" >> $SERVICE_FILE
sudo echo "User=pi" >> $SERVICE_FILE
sudo echo "[Install]" >> $SERVICE_FILE
sudo echo "WantedBy=multi-user.target" >> $SERVICE_FILE

sudo systemctl daemon-reload
sudo systemctl start Plantmonitoring.service
sudo systemctl enable Plantmonitoring.service
echo 'Plantmonitoring is now installed as Plantmonitoring.service in systemctl'
echo 'You can check the output by using systemctl status Plantmonitoring.service'
echo '----------------'
echo 'Lastly, let us Install Redis'
echo 'This will install reids with the standard Installation. Redis will be available on port 6379 afterwards.'
#We could install redis from the official sources:
#sudo apt-get -qq install redis-server
#Unfortunately, these are usually not providing the current release, so we will download the latest release directly:
cd /../tmp
wget http://download.redis.io/redis-stable.tar.gz
tar xvzf redis-stable.tar.gz
cd redis-stable
make -s
make test 
sudo make -s install

#Here, we run the setup of redis server. It will generate the config files and register redis as a service.
#Unfortunately, it still uses update-rc.d and not systemctl.
#If you want to manually install it, check this script:
#http://download.redis.io/redis-stable/utils/install_server.sh
sudo REDIS_PORT=6379 \
REDIS_CONFIG_FILE=/etc/redis/6379.conf \
REDIS_LOG_FILE=/var/log/6379.log \
REDIS_DATA_DIR=/var/lib/redis/6379 \
REDIS_EXECUTABLE=`command -v redis-server` ./utils/install_server.sh 

echo 'Redis Installation completed'
echo '-------------------'
echo 'It is recommended to reboot now.'