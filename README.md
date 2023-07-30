# saybah-bot
Yet Another Open Source Discord Bot

## Prerequistes
I made this bot in Linux, so I don't know what problems will occur running it on 
Windows or MacOS. Also, make sure you are running Python 3.8 or later. As of
writing this, I am currently using Python 3.10.6.

We also need to make sure the following packages are installed on your system:

- [ffmpeg](https://ffmpeg.org/)
- [libffi](https://github.com/libffi/libffi)
- [python3-dev](https://packages.debian.org/sid/python3-dev) 

These packages are all needed for discord voice support and music playing.
Unfortunately, none of those links tell you how to install these packages,
so here is a quick guide:

### Installing Required Packages
#### Debian Based Distros
``` Bash
sudo apt update && sudo apt install ffmpeg libffi-dev python3-dev
```

#### Arch Based Distros
``` Bash
sudo pacman -S ffmpeg libffi
```
> *Note: Arch ships header files with the regular package, so there are no -dev
> packages to worry about. More info [here](https://bbs.archlinux.org/viewtopic.php?pid=299628#p299628).*

#### Fedora
First, you need to configure the RPMfusion repository in order to install ffmpeg.
To do so, you can use the two commands from [this article:](https://computingforgeeks.com/how-to-install-ffmpeg-on-fedora/?expand_article=1)
``` Bash
sudo dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm
sudo dnf -y install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm
```
Then, dnf should be able to handle the rest:
``` Bash
sudo dnf updateinfo && sudo dnf install ffmpeg libffi-devel python3-devel
```

## Setting Up and Running the Bot
First we need to create a simple virtual environment.

``` Bash
python3 -m venv bot-env
source bot-env/bin/activate
```

Then install the modules in `requirements.txt`:
``` Bash
pip install -r requirements.txt
```
> *Note: I want to also make an optional conda install, since I prefer conda to venv,
> and since some packages like libffi are available through conda, which might make
> everyone's lives easier. However, I found that some of the needed packages were not
> available through conda, so whether this will ever be implemented is up in the air.*


One more step. Create a file named `.env` with variable `token` equal to your 
Discord Bot code.

Example:
```
File: .env
----------
token = 42069694206969.42069694206969.42069694206969
```

Now we're ready. Just run `main.py` and you should be all set
``` Bash
python3 main.py
```