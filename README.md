# Pi Board

The first part of the instructions below adds the main shutdown script for the RemotePi Board to the autostart.sh file, which enables the script to run when the OS starts.

* Key in (mind the . in front of config !) :
  * _cd .config_
* Copy autostart.sh in the .config folder
* Key in
  * _chmod +x autostart.sh_

The next part creates the main RemotePi Board shutdown script. This script shuts down the OS safely, when the button on the RemotePi Board or the off button on the remote is pressed :

* Copy irswitch.sh in the .config folder
* Key in
  * _chmod +x irswitch.sh_

The following additional script enables the RemotePi Board to cut off the power, after OpenElec / LibreELEC has been shut down from the on-screen menu.

* Copy shutdown.sh in the .config folder
* Mark the script as executable by keying in
  * _chmod +x shutdown.sh_
* Reboot from the OpenElec or LibreELEC OS GUI.
* After reboot you can use the RemotePi Board to power cycle OpenElec / LibreELEC

# nuxii

## LibreELEC

* Key in (mind the . in front of config !) :
  * _cd .config_
* Copy autostart.sh in the .config folder
* Key in
  * _chmod +x autostart.sh_
* Copy shutdownBtn.sh in the .config folder
* Key in
  * _chmod +x irswitch.sh_

## Raspbian

* Key in :
  * _cd /etc/init.d_
* Copy shutdownBtn in the /etc/init.d folder
* Key in
  * _chmod +x shutdownBtn_
* Copy shutdownBtn.py in the /etc/init.d folder
* Key in
  * _chmod +x shutdownBtn.py_

## RecalBox

* Key in :
  * _cd /etc/init.d_
* Copy S99shutdownBtn in the /etc/init.d folder
* Key in
  * _chmod +x S99shutdownBtn_
* Copy shutdownBtn.py in the /etc/init.d folder
* Key in
  * _chmod +x shutdownBtn.py_
