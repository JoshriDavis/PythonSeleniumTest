from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Actions to finish the test
def finishTest():
    global driver
    time.sleep(5)
    print("Done!")
    driver.quit() 
  
# Create global elements  
def globalElements():
    global driver, actualResult
    driver=webdriver.Chrome()
    actualResult = 0
    
# Search specific results in Youtube search
def searchInYoutube(textToSearch):
    global driver
    driver.get("https://www.youtube.com/")
    driver.find_element_by_name("search_query").send_keys(textToSearch)
    driver.find_element_by_name("search_query").send_keys(Keys.ENTER)
    
# Test if the first Youtube search result is as expected
def TestFirstYoutubeSearchResult(expectedResult):
    global driver, actualResult
    driver.implicitly_wait(30)
    actualResult = driver.find_element_by_css_selector("#video-title > yt-formatted-string")
    try:
        assert actualResult.text == expectedResult
        print("Pass!")
        return 1
    except AssertionError:
        print("Fail!")
        return 0

######### Main script #########
globalElements() # Create and define global elements
searchInYoutube("X Factor")
TestFirstYoutubeSearchResult("BEST Singing Auditions EVER! (Got Talent, X Factor & Idols)")
actualResult.click() # Play the video
finishTest()