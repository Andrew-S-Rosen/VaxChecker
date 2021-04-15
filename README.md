# Purpose
The website [vaxxmax.com](http://vaxxmax.com/) automatically checks CVS, Walgreens, Walmart, and Rite-Aid for available COVID-19 vaccines. However, it doesn't have a way to notify you if an appointment opens up in your area. This script will check vaxxmax on your behalf and notify you when a suitable appointment opens up!

# Setup
1. Download ChromeDriver from [here](https://chromedriver.chromium.org) (the latest stable release is recommended).
2. Install the Python dependencies (see below).
3. Edit the web settings in `check_vaxxmax.py`. You will have to tell it where the ChromeDriver executable is located (`webdriver`), how frequently you want to query vaxxmax (`sleeptime`), the maximum distance you'd like to travel for the shot (`max_distance`), the state you live in (`state`), and if you'd like an email to be sent (`send_email`). 
4. Optional: Edit the notification settings in `check_vaxxmax.py` if you want an email notification (otherwise it just prints to the screen). This calls `smtplib` to send an email to a user of your choosing from your e-mail account. Caution is always advised whenever storing credentials in a paintext file. Feel free to set `send_email` to `False` if you don't want to set up email notifications, in which case you can ignore these settings.

# How to Run
Simply call `python check_vaxxmax.py` once you have set everything up. Leave it running until you've found an appointment.

# Debugging
If you want to make sure it's running okay, do a quick test on a location with plenty of vaccines (e.g. `state = 'CA'`) and set `max_distance` to something large (e.g. `max_distance = 10000`) to make sure that you get properly notified.

# Dependencies
This code is written in Python 3 (tested on Python 3.8.5), which you can install via [Anaconda](https://anaconda.com/). The code has the following dependencies, which can be readily installed via `pip install <PackageName>`:
- Selenium (tested on 3.141.0)
- NumPy (tested on 1.19.2)
- Pandas (tested on 1.1.5)

# Notes on Use
- The [vaxxmax.com](http://vaxxmax.com/) website gets regularly updated with new features and formatting, which can occasionally break the code. If you notice an error, please [raise an issue](https://github.com/arosen93/VaxChecker/issues) on this GitHub page so that it can be addressed (or [submit a pull request](https://github.com/arosen93/VaxChecker/pulls) if you know how to fix it).
- Please be courteous when setting `sleeptime` so that you don't stress the [vaxxmax.com](http://vaxxmax.com/) servers. Personally, I would set it to something like `sleeptime = 120` (120 s) if you want frequent checks or `sleeptime = 300` (300 s) for something a little less frequent.
- To avoid a large number of notifications, `check_vaxxmax.py` will not send you repeat notifications if there have been no changes since the last time you were notified. However, that means if an appointment opened, you checked, but it filled up before you could book it, then you should re-run `check_vaxxmax.py` so that the previous message history is cleared.

# General Vaccine Finding Tips
- Large blocks of appointments tend to open up in the early morning. If you're awake around 1 AM local time, do a quick check. Maybe you'll get lucky! Also check in the mornings when you wake up. As the day goes by, it will likely become harder to find an appointment near you.
- Even before you go to book a real slot, pretend as if you are currently booking a vaccine appointment on the pharmacy websites of your choosing. Go through the process as far as you can. This will help familiarize yourself with the system because your brain turns to mush when you're racing to book a slot.
- Select your state [here](https://www.cvs.com/immunizations/covid-19-vaccine) to see the list of CVS stores that are providing the vaccine in your area. Not all CVS locations are currently providing the COVID-19 vaccine.
- There are several other sites besides [vaxxmax.com](http://vaxxmax.com/), such as [vaccinespotter.org](https://www.vaccinespotter.org/) and [ilvaccine.org](https://www.ilvaccine.org/) (for those in the IL area).
- Not all pharmacies are regularly checked via the aforementioned trackers, so I still encourage manually checking every now and then.
