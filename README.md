# CitiesBot-public
Bot for production of equipment and sale of excess resources in browser game "Cities War" by WillyBBBC


INSTALLATION:


1. Download python (!!!MAKE SURE TO CHECK "ADD TO PATH" OR THIS WILL NOT WORK!!!)

https://www.python.org/downloads/

2. Download the web driver for your browser (This is what the script uses to talk to the browser)


FIREFOX: https://github.com/mozilla/geckodriver

CHROME: https://chromedriver.chromium.org/downloads

OPERA GX: https://github.com/operasoftware/operachromiumdriver/releases (ew)


2.1. After download put the web driver file in a place you know the path of, something like


C:\web-drivers\geckodriver.exe


For others you can just look up "[BROWSER NAME] Web driver"



3. Install selenium:

I know this all sounds complicated, but we are almost done


Selenium is what is called a framework, to keep it simple its sort of a toolbox, this one is for interacting with browsers

Python has pip, package installer for python, and guess what? That's right, you cant answer a static text file, but i suppose you have seen that selenium might be one of these fancy packages for python


Python allows you to use a very cool command line to do stuff, if you feel like it you can use it for mundane math, but today we will install something with it

if you look up a program called python in your computer and run it, a scary command line appears, if you chant this arcane spell it will get selenium into your machine


The arcane command is:

pip install -U selenium



4. Download this script


If you scroll up, you'll see a green button called code, click it, the last thing in the pop us is a download zip button, yeah click it


5. Final configuration


After download and unzipping just go into the bot.py file, change the PATH to where your web browser is


Then go into botsettings.py and edit the username, password (what you change is inbetween the "") and according to instructions on the file, what weapons and type you want to produce


If something does not work submit an issue using the issues tab above, or send me a report of the problem on discord (im not putting it here lmao)
