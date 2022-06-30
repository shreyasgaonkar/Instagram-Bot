import argparse
import os
import random
import re
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class InstagramBot:
    """Class to define login and like photo methods"""

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        """User login using credentials"""
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)

        # Click optional "Accept cookies from Instagram on this browser?"
        try:
            bot.find_element(By.CSS_SELECTOR, 'button.aOOlW').click()
        except Exception as exp:
            print("No element to click: Accept cookies from Instagram. Skipping..")

        time.sleep(2)

        email = bot.find_element(By.NAME, "username")
        password = bot.find_element(By.NAME, "password")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(4)

        # Click optional "Bypass save login info"
        try:
            bot.find_element(By.CSS_SELECTOR, '.cmbtv > button').click()
        except Exception as exp:
            print("No element to click: save login info. Skipping..")

        time.sleep(1)
        # Click optional "Turn on Notification"
        try:
            bot.find_element(
                By.CSS_SELECTOR, '.mt3GC > button:last-of-type').click()
        except Exception as exp:
            print("No element to click: Turn on Notification. Skipping..")

    def like_posts(self, hashtag):
        """Search hashtag URL and like first 50 posts"""
        time.sleep(5)
        count = 0
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/" + hashtag)
        time.sleep(2)

        # simulate scroll for lazy loading
        for i in range(3):
            bot.execute_script(
                'window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(1+i)

        # Get all links, which will be later cleaned for the posts
        links = bot.find_elements(By.XPATH, "//div/a")
        links_hrefs = []
        for link in links:
            # if links have href tag, add it to the list
            try:
                links_hrefs.append(link.get_attribute('href'))
            except Exception as unhandled_exception:
                pass

        for image in links_hrefs:
            try:
                # Check if the links contains posts
                val = re.search(r'^https://www\.instagram\.com/p/', image)
                bot.get(val.string)

                # random sleep between 1 - 3 secs for any 'unusual activity'
                time.sleep(random.choice([1, 2, 3]))

                # Like post
                bot.set_page_load_timeout(10)
                bot.find_element(By.CSS_SELECTOR, '._aamu button').click()
                count += 1

                # Don't like more than 50 posts
                if count > 49:
                    break
                time.sleep(1)
            except Exception as unhandled_exception:
                print(unhandled_exception)

        print("liked {} posts".format(count))
        bot.quit()


def parse_hashtag() -> str:
    """Parse required and optional arguments"""

    parser = argparse.ArgumentParser()
    parser.add_argument("--hashtag",
                        required=False,
                        help="Optional: Override hashtag")

    args = parser.parse_args()

    try:
        hashtag = args.hashtag.lower()
    except Exception as exp:
        hashtag = "None"

    return hashtag


def main():
    """Main function to like posts"""

    hashtag = parse_hashtag()
    if hashtag == "None":
        hashtag = 'hashtag-to-search'  # fall back to this hashtag if not in CLI arguments

    USER = InstagramBot(os.environ.get('username'), os.environ.get('pass'))
    USER.login()
    USER.like_posts(hashtag)


if __name__ == "__main__":
    main()
