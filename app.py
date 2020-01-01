import re
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class InstagramBot:
    def __init__(self, username, password):
        self.username = username,
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        email = bot.find_element_by_name("username")
        password = bot.find_element_by_name("password")
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(4)

    def LikePhotos(self, hashtag):
        time.sleep(1)
        count = 0
        bot = self.bot
        bot.get("https://www.instagram.com/explore/tags/" + hashtag)
        time.sleep(2)

        # simulate scroll for lazy loading
        for i in range(3):
            bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            time.sleep(2)

        # Get all links, which will be later cleaned for the posts
        links = bot.find_elements_by_xpath('//div/a')
        links_hrefs = []
        for link in links:
            # if links have href tag, add it to the list
            try:
                links_hrefs.append(link.get_attribute('href'))
            except:
                pass

        for image in links_hrefs:
            try:
                # Check if the links contains posts
                val = re.search(r'^https://www.instagram.com/p/', image)
                bot.get(val.string)
                # random sleep between 1 - 3 secs for any 'unusual activity'
                time.sleep(random.choice([i for i in range(3)]))
                # Like post
                # If a post is already liked, this class will not be in the DOM
                bot.find_element_by_class_name('glyphsSpriteHeart__outline__24__grey_9').click()
                count += 1

                # Don't like more than 50 posts
                if(count > 50):
                    break
                time.sleep(1)
            except:
                pass

        print("liked {} posts".format(count))
        bot.quit()


# Magic!
user = InstagramBot('username', 'password')
user.login()
user.LikePhotos('hashtag-to-search')
