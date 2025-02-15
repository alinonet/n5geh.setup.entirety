#!/bin/bash
echo
echo Download N5GEH Platform...
git clone https://github.com/alinonet/n5geh.platform
mv n5geh.platform platform
echo
echo Download Entirety...
git clone https://github.com/alinonet/n5geh.entirety
mv n5geh.entirety entirety
echo
echo Setup Docker and N5GEH Platform...
chmod +x platform/scripts/installation_setup.sh
./platform/scripts/installation_setup.sh
echo
echo Press Enter to reboot...
read key
sudo reboot
