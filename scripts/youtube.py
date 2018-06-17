def playback(url):
    from selenium import webdriver
    #from selenium.webdriver.chrome.options import Options
    #options = Options()
    driver = webdriver.Firefox()
    driver.set_window_size(width=150,height=400)
    driver.get(url)
    # For time out.
    driver.implicitly_wait(10) # seconds
    return True


def kiminonaha():
    url = 'https://www.youtube.com/watch?v=3qeAZLyBNQI'
    playback(url)


def aimer():
    url = 'https://www.youtube.com/watch?v=3p7W5r4t3As'
    playback(url)
