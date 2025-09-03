from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Start browser
browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

# Select the page body
html_elem = browser.find_element("tag name", "body")

# Loop until game over
while True:
    # Send key moves
    html_elem.send_keys(Keys.UP)
    html_elem.send_keys(Keys.RIGHT)
    html_elem.send_keys(Keys.DOWN)
    html_elem.send_keys(Keys.LEFT)

    time.sleep(0.1)  # small delay for the game to register moves

    # Check if game over
    try:
        game_over = browser.find_element("class name", "game-over")
        if game_over.is_displayed():
            print("Game Over!")
            break
    except:
        pass

# Close browser
browser.quit()


