## Instagram Bot

[app.py](app.py) will let you scrap through all instagram posts containing a hashtag, and like them for you!

Set username and password through environment variable: :tada:

```Shell
vim ~/.bash_profile

# Linux/MacOS
export username=username
export pass=password

# Windows
set username=username
set pass=password
```

exit terminal to reflect the changes.


Replace ```user.LikePhotos('hashtag-to-search')``` with the hashtag to search, and run the function.

----
Prefer older method using hardcoded username and password?  Refer [here](https://github.com/shreyasgaonkar/Instagram-Bot/tree/3a86f120770e8abc3b028b5e9167a15c71b89dad)

**Note**: Instagram will probably shut down your account, if you are liking posts more than average. I would not let this run for more than 100 posts a day to not get banned.

---
### Pre-req:

1. ```$ pip install selenium```
2. [Gecko driver](https://github.com/mozilla/geckodriver/releases) installed in python's directory (```$ which python``` to check the installed directory)

---
### Issues:

- :cold_sweat: Something broken? [Open an issue](https://github.com/shreyasgaonkar/Instagram-Bot/issues)
