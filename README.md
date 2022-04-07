# Shoeshine.tv
'Shoeshine.tv’, a place to upload short videos/clips to then get a URL generated for easy sharing to friends, much like outplayed.tv, but self-hosted so never have to worry about it being shutdown. You can find the Trello board here: PLACEHOLDER.

## Installation

Installation per different systems and OS are not that different from one another, with the program being designed to be as platform-fluid as possible. 

For Windows host installs, you must have the following dependencies:
 
 * [XAMPP Web Server](https://www.apachefriends.org/index.html)

For Windows user installs, you must have the following depedencies:

  * [Python 3](https://www.python.org/downloads/) (3.7 or newer)
  * [MoviePy](https://github.com/Zulko/moviepy)
  * [MediaInfo](https://github.com/sbraz/pymediainfo)
  * PIL/[Pillow](https://python-pillow.org/)
  * PYTHON GUI EXAMPLE
  * [pyvideothumbnailer](https://github.com/hhtznr/pyvideothumbnailer) 

For Debian-based Linux host installs, you must install the following packages:

 * [apache2](https://httpd.apache.org/)
 * [MariaDB](https://mariadb.org/)
 * [PHP](https://www.php.net/)

For Arch-based Linux host installs, you must install the following packages:

 * [Linode's guide on setting up a LAMP stack on Arch Linux](https://www.linode.com/docs/guides/how-to-install-a-lamp-stack-on-arch-linux/)

## Usage

Windows-Based Server:

Windows-Based GUI User:
The GUI to upload clips without using the website can be ran either in executable form or as the base Python script. To run the executable, just right click 'GUI.exe' and then 'Run as Administrator'

![image](https://user-images.githubusercontent.com/65707039/162193646-ca7f36dc-73bc-40db-a592-41e47a22d7dd.png)

or to run the base script itself, open a command prompt in the same directory and type: python gui.py

![image](https://user-images.githubusercontent.com/65707039/162193352-47f2b3b4-ce1b-4f76-a310-161b3436d551.png)


Debian-Based Server:
To start the server, you must repalce the default 'index.html' that apache2 uses with the 'index.php' found in the [Website](https://github.com/roshan-c/shoeshine.tv/tree/main/website) directory of the repositiory. This will load the front page of 'Shoeshine.tv'.

Debian-Based User:

 
