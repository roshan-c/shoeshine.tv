# Shoeshine.tv
'Shoeshine.tv’, a place to upload short videos/clips to then get a URL generated for easy sharing to friends, much like outplayed.tv, but self-hosted so never have to worry about it being shutdown. You can find the Trello board here: PLACEHOLDER.

## Installation

Installation per different systems and OS are not that different from one another, with the program being designed to be as platform-fluid as possible. 

For Windows host installs, you must have the following dependencies:
 
 * [XAMPP Web Server](https://www.apachefriends.org/xampp-files/8.1.4/xampp-windows-x64-8.1.4-1-VS16-installer.exe)

For Windows user installs, you must have the following depedencies:

  * [Python 3](https://www.python.org/downloads/) (3.7 or newer)
  * [pyvideothumbnailer](https://github.com/hhtznr/pyvideothumbnailer) 
  * You must install all the libraries found (here). This can be done by running the following command in a command prompt that is inside the folder where requirements.txt is found.
  ```
  pip install -r requirements.txt
  ```

For Debian-based Linux host installs:

 * First you should install apache2:
 ```
 sudo apt-get install apache2 -y
 ```
 ![image](https://user-images.githubusercontent.com/65707039/162407431-0955da57-1abc-49c1-9cef-4390fabb71c6.png)

 * Then, install PHP:
 ```
 sudo apt-get install php -y
 ```
 ![image](https://user-images.githubusercontent.com/65707039/162407556-eeb4dc47-2ae6-42b5-9719-c01acc2c8b17.png)

 * After, install MySQL:
 ```
 sudo apt-get install mariadb-server php-mysql -y
 ```
 ![image](https://user-images.githubusercontent.com/65707039/162407802-a70de771-9023-48ee-a8a7-62a2d1b4011a.png)

 * Finally, restart apache2:
 ```
 sudo service apache2 restart
 ```

For Arch-based Linux host installs:

 * [Linode's guide on setting up a LAMP stack on Arch Linux](https://www.linode.com/docs/guides/how-to-install-a-lamp-stack-on-arch-linux/)

## Usage

Windows-Based Server:
Once installed, open XAMPP Control Panel. You should be greeted with this screen.

![image](https://user-images.githubusercontent.com/65707039/162401715-f8cc0045-e713-4702-90d1-64905de08a99.png)

Start both Apache and MySQL.

![image](https://user-images.githubusercontent.com/65707039/162401908-948573ba-d50f-4338-9b6a-3b4db17e65f2.png)



Windows-Based GUI User:
The GUI to upload clips without using the website can be ran either in executable form or as the base Python script. To run the executable, just right click 'GUI.exe' and then 'Run as Administrator'

![image](https://user-images.githubusercontent.com/65707039/162193646-ca7f36dc-73bc-40db-a592-41e47a22d7dd.png)

or to run the base script itself, open a command prompt in the same directory and type: python gui.py

![image](https://user-images.githubusercontent.com/65707039/162193352-47f2b3b4-ce1b-4f76-a310-161b3436d551.png)


Debian-Based Server:
To start the server, you must repalce the default 'index.html' that apache2 uses with the 'index.php' found in the [Website](https://github.com/roshan-c/shoeshine.tv/tree/main/website) directory of the repositiory. This will load the front page of 'Shoeshine.tv'.

Debian-Based User:

 
