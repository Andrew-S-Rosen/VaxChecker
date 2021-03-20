from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import time
import numpy as np
import pandas as pd
import smtplib

# ----------Fill Me Out---------
# Web Settings
webdriver = r"C:\chromedriver.exe" # download: https://chromedriver.chromium.org
sleeptime = 300  # sleep time (s) between URL calls
max_distance = 120  # max distance (mi) from you
state = 'IL'  # state for shots
send_mail = True  # send email (otherwise just print to screen)
max_total_runtime = np.inf  # max time to run script

# Notification settings (can be ignored for send_mail == False)
email_acct = 'ILoveFauci@gmail.com' #email account to send from
email_pwd = 'Fauci123!' #password to email account
to_email = 'ILoveFauci@gmail.com' #email account to send to
subject = 'GO GET THAT JAB!' #subject line of email
smtp_server = 'smtp.gmail.com' #SMTP server
smtp_port = 587 #SMTP port
# -----------------------------

# Set up email credentials
if send_mail:
    auth = (email_acct, email_pwd)
    server = smtplib.SMTP(smtp_server, smtp_port)

# URLs to check of vaxxmax
urls = ['http://vaxxmax.com/cvs',
        'http://vaxxmax.com/walgreens',
        'http://vaxxmax.com/riteaid']

# Initialize variables
t0 = time.time()
df_rows = []
elapsed_time = 0
df_column_names = ['store', 'city', 'state', 'zip',
                   'county', 'last_updated', 'became_available',
                   'distance']
df_column_names_short = ['store', 'city', 'zip', 'distance']

# Launch virtual browser
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('log-level=3')
driver = Chrome(executable_path=webdriver,options=chrome_options)

# Search for shots!
while elapsed_time < max_total_runtime:
    for i, url in enumerate(urls):

        # Open URL
        driver.get(url)
        driver.get(url)

        # Select state
        if 'cvs' in url:
            name = 'cvs'
        elif 'walgreens' in url:
            name = 'walgreens'
        elif 'riteaid' in url:
            name = 'rite-aid'
        selector = Select(driver.find_element_by_xpath(
            '//*[@id="state-select-'+name+'"]'))
        try:
            selector.select_by_value(state)
        except:
            continue
        time.sleep(2)

        # Access table
        table = driver.find_element_by_xpath('//*[@id="locations"]/tbody')
        rows = table.find_elements_by_tag_name('tr')

        # Iterate through rows of table and parse
        for row in rows:
            entries = row.find_elements_by_tag_name('td')
            entries_text = [entry.text.strip() for entry in entries]
            if len(entries_text) == 1:
                break
            entries_text[0] = name
            entries_text[3] = int(entries_text[3].split('Copy')[0].strip())
            entries_text[5] = entries_text[5].split(
                'about')[-1].split('ago')[0].strip()
            entries_text[6] = entries_text[6].split(
                'about')[-1].split('ago')[0].strip()
            entries_text[7] = int(entries_text[7])
            df_rows.append(entries_text)

    # Send out the winners!
    if df_rows:

        # Construct DataFrame
        df = pd.DataFrame(df_rows, columns=df_column_names)
        df = df.sort_values('distance')
        df_close = df[df['distance'] <= max_distance]
        df_close = df_close[df_column_names_short]

        # If there are shots, notify!
        if len(df_close) > 0:
            message = "Get your jab here:\nStore, City, Zipcode, Distance (mi)\n"
            for idval, df_entries in df_close.iterrows():
                for df_entry in df_entries:
                    message += str(df_entry)+', '
                message += '\n'
            message += '\n'
            print(message)

            # Send email if requested
            if send_mail:
                server.starttls()
                server.login(auth[0], auth[1])
                email_message = 'Subject: {}\n\n{}'.format(subject, message)
                server.sendmail(auth[0], to_email, email_message)
                server.quit()

    # Update timer
    elapsed_time = time.time()-t0
    time.sleep(sleeptime)

driver.quit()
