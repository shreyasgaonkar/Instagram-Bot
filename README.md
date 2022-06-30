## Instagram Bot

[app.py](app.py) will let you scrap through all instagram posts containing a hashtag, and like them for you. If you want to organically grow your profile, engaging with posts similar to what you have been sharing in the past will increase the likelihood of others following you back. 

Set username and password through environment variable:

```Shell
vim ~/.bash_profile

# Linux/MacOS
export username=username
export pass=password
```
exit terminal or `source` to reflect the changes.

```Shell
# Windows
set username=username
set pass=password
```

Replace ```hashtag = 'hashtag-to-search'``` with the hashtag to search or provide it with `--hashtag "hashtag-to-search"`, and run the function.

Run:
```Shell
git clone https://github.com/shreyasgaonkar/Instagram-Bot.git
cd Instagram-Bot

# Override the hashtag with the --hashtag argument
python app.py --hashtag hashtag-to-search

# Or hardcode the value in the app.py
python app.py
```

This will open new Firefox window, run through the login clicking on any optional modals and cycle through the first 50 posts as per the hashtag searched; and exit once done.

----

**Note**: Instagram will probably shut down your account, if you are liking posts more than average. I would not let this run for more than 100 posts a day to not get deactivated.

---
### Pre-req:

0. Install Firefox
1. ```$ pip install selenium```
2. [Gecko driver](https://github.com/mozilla/geckodriver/releases) installed in python's directory (```$ which python``` to check the installed directory)

---
### Issues:

- :cold_sweat: Something broken? [Open an issue](https://github.com/shreyasgaonkar/Instagram-Bot/issues)
