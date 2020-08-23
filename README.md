# NOVAOutreachEmail
## Environmental Setup
To use this code, make sure you have a version of > Python 3.7 running on your environment.

Go to your Princeton Gmail Settings -> Manage Your Google Account -> Security -> Turn on Less Secure Apps (you can turn off after you run the script).

Copy the names you are supposed to email in the first column of a new excel file, and the emails in the second column. See example.csv for the correct format. Save your csv with names in the same directory as the send_email.py script with the name "names.csv"

Install the correct requirements. The easiest way to do this is run "pip install -r requirements.txt" if you have pip setup.

## Customize Script
Fill in sender_email as your own email address in send_email.py.

Write your own message within send_email.py. There are two places to do this. Text is the plaintext version, and html is the html version. The html should be enough, but if for some reason a person has their email set up to only receive plaintext, the plaintext version will make sure it is delivered.

## Debugging
I would reccomend debugging you email by sending it to yourself a couple times before running it on all of the names. Make a csv with your own name and email to debug fully and run the script.

## Running
Run it on the command line with ```python send_email.py```. You will be prompted to enter your email password on the commandline. Do it and hit enter. It should send your email to every person with a customized name :)
