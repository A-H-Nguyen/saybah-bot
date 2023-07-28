# saybah-bot
Yet Another Open Source Discord Bot

## Setting Up the Bot
"Step 0" is to make sure the PC you are running this bot on is using
Linux. I made this bot in Linux, so I don't know what problems will
occur running it on Windows or MacOS.

Next, make sure ffmpeg is installed on your system.
You can simply install it with your favorite package manager,
assuming you're running Linux. The install of ffmpeg will change based
on your distro. For example, if you are an Ubuntu normie, the world
favors you because it's a simple `sudo apt udate && sudo apt install fmpeg`.
But if you're on Fedora it's really annoying.

We also need to create a simple virtual environment.
This does assume you have Python 3. You *are* using Python 3 right?

```
python3 -m venv bot-env
source bot-env/bin/activate
```

Then install the modules in `requirements.txt`:
```
pip install -r requirements.txt
```

Almost done. Now, we need to install youtube-dl seperately,
otherwise the bot will not work. I need to look into this more.

Here is the current workaround:

```
pip install --force-reinstall https://github.com/yt-dlp/yt-dlp/archive/master.tar.gz
```

One more step. In the file called `.env` set the variable `token`
to be equal to your own Discord Bot code.

Example:
```
File: .env
----------
token = 42069694206969.42069694206969.42069694206969
```