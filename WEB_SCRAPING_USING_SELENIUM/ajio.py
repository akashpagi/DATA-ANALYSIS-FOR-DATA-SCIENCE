# url : https://www.ajio.com/men-backpacks/c/830201001

# import time
# from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service

# s = Service()
# o = webdriver.EdgeOptions()

# # to protect form closing the window automatically
# o.add_experimental_option('detach', True)

# # # Create a WebDriver instance with ChromeDriverManager
# driver = webdriver.Edge(options=o,)



from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Navigate to the url
driver.get('https://www.ajio.com/men-backpacks/c/830201001')

# Wait for the page to load (optional)
time.sleep(2)

# Scroll down using JavaScript
old_height = driver.execute_script("return document.body.scrollHeight;")

counter = 1
while True:
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for a moment to let the page scroll 
    time.sleep(2)  
    new_height = driver.execute_script("return document.body.scrollHeight;")
   
    print("counter: ", counter)
    counter = counter + 1
    print("old_height: ",old_height)
    print("new_height: ",new_height)
    
    if new_height == old_height:
        break
    old_height = new_height 

ajio_html_page = driver.page_source
with open('ajio_backpacks.html', 'w', encoding='utf-8') as f:
    f.write(ajio_html_page)