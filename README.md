The first part of the instructions below adds the main shutdown script for the RemotePi Board to the autostart.sh file, which enables the script to run when the OS starts.

* Key in (mind the . in front of config !) :
  cd .config
* Copy autostart.sh in the .config folder
* Press ctrl+x to exit the editor, y to confirm, enter to save the file
* Key in
  chmod +x autostart.sh

The next part creates the main RemotePi Board shutdown script. This script shuts down the OS safely, when the button on the RemotePi Board or the off button on the remote is pressed :

* Copy irswitch.sh in the .config folder
* Press ctrl+x to exit, y to confirm, enter to save the file
* Key in
  chmod +x irswitch.sh

The following additional script enables the RemotePi Board to cut off the power, after OpenElec / LibreELEC has been shut down from the on-screen menu.

* Copy shutdown.sh in the .config folder
* Press ctrl+x to exit, y to confirm, enter to save the file
* Mark the script as executable by keying in
  chmod +x shutdown.sh 
* Reboot from the OpenElec or LibreELEC OS GUI.
* After reboot you can use the RemotePi Board to power cycle OpenElec / LibreELEC