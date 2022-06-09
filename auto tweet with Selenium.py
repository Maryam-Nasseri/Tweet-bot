

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec


## hide your browser with headless mode
chromeOptions = Options()
chromeOptions.add_argument('--headless')
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chromeOptions)

#OR

# maximize browser window
chromeOptions = Options()
chromeOptions.add_argument("--start-maximized")

# web driver constructor
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=chromeOptions)

# get the tweeter url
tweeter_url = "https://twitter.com/login"
driver.get(tweeter_url)


# explicit wait:
wait = WebDriverWait(driver, 10)

# locate the username element; can be by XPath
username_input = wait.until(ec.visibility_of_element_located((By.NAME, "session[username_or_email]")))


# send login ID
username_input.send_keys(username)


# locate the password field and send the pw
password_input = wait.until(ec.visibility_of_element_located((By.NAME, "session[password]")))
password_input.send_keys(password)


# locate the login button and click it
login_button = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@data-testid='LoginForm_Login_Button']")))
login_button.click()


# locate the span of text area
tweet_text_span = driver.find_element_by_xpath("//div[@data-testid='tweetTextarea_0']/div/div/div/span")


# the tweet text
tweet_text_span.send_keys("My first auto tweet with selenium?")


# locate the tweet button and send the post
tweet_button = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@data-testid='tweetButtonInline']")))
tweet_button.click()


driver.close()





