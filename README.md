# Purpose
The website [vaxxmax.com](http://vaxxmax.com/) automatically checks CVS, Walgreens, and Rite-Aid for available COVID-19 vaccines. However, it doesn't have a way to notify you if an appointment opens up in your area. This script will check vaxxmax on your behalf and notify you when a suitable appointment opens up!

# Setup
1. Download ChromeDriver from [here](https://chromedriver.chromium.org) (the latest stable release is recommended). This will allow the [Selenium package](https://github.com/SeleniumHQ/selenium) to interact with vaxxmax.
2. Install the Python dependencies (see below).
3. Edit the web settings in `check_vaxxmax.py`. You will have to tell it where the ChromeDriver executable is located (`webdriver`), how frequently you want to query vaxxmax (`sleeptime`), the maximum distance you'd like to travel for the shot (`max_distance`), the state you live in (`state`), and if you'd like an email to be sent (`send_email`). 
4. Optional: Edit the notification settings in `check_vaxxmax.py` if you want an email notification (otherwise it just prints to the screen). This calls `smtplib` to send an email to a user of your choosing from your e-mail account. Caution is always advised whenever storing credentials in a paintext file. Feel free to set `send_email` to `False` if you don't want to set up email notifications, in which case you can ignore these settings.

# How to Run
Simply call `python check_vaxxmax.py` once you have set everything up.

# Dependencies
This code is written in Python 3 (tested on Python 3.8.5), which you can install via [Anaconda](https://anaconda.com/). The code has the following dependencies, which can be readily installed via `pip install <PackageName>` or `conda install <PackageName>` (if you are using Anaconda):
- Selenium (tested on 3.141.0)
- NumPy (tested on 1.19.2)
- Pandas (tested on 1.1.5)
