#!/usr/bin/env bash

# install swatch
echo '% sudo apt install swatch'
sudo apt update && sudo apt install -y swatch

# copy original script and swatch config
echo '% sudo mkdir /etc/swatch'
sudo mkdir /etc/swatch
echo '% sudo cp -R ./* /etc/swatch'
sudo cp -R ./* /etc/swatch
echo '% sudo chmod -R +x /etc/swatch'
sudo chmod -R +x /etc/swatch

# autostart setting to cron
echo "% echo '@reboot root /usr/bin/swatchdog -c /etc/swatch/conf.d/auth.log.conf -t /var/log/auth.log > /dev/null' | sudo tee /etc/cron.d/swatch"
echo '@reboot root /usr/bin/swatchdog -c /etc/swatch/conf.d/auth.log.conf -t /var/log/auth.log > /dev/null' | sudo tee /etc/cron.d/swatch
