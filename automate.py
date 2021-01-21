from selenium import webdriver 


"""options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

driver = webdriver.Chrome(options=options)"""
driver=webdriver.Chrome()
driver.get('https://amazon.com')

signIn = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
signIn.click()
username = driver.find_element_by_xpath('//*[@id="ap_email"]')
username.send_keys('9557637442')
button1 = driver.find_element_by_xpath('//*[@id="continue"]')
button1.click()
password = driver.find_element_by_xpath('//*[@id="ap_password"]')
password.send_keys('Webster1')
button2 = driver.find_element_by_xpath('//*[@id="signInSubmit"]')
button2.click()

searchBox = driver.find_element_by_xpath('//*[@id="twotabsearchtextbox"]')
searchBox.send_keys('earphones')
searchButton = driver.find_element_by_xpath('//*[@id="nav-search"]/form/div[2]/div/input')
searchButton.click()

"""
flipkart
username = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input')
username.send_keys('Your_username')
password = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input')
password.send_keys('Your_password')
login = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[2]/div/form/div[3]/button')
login.click()
searchbox = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
searchbox.send_keys('earphones')
searchbutton = driver.find_element_by_xpath('//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
searchbutton.click()""" 


"""
Google Search
searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
searchbox.send_keys("Sandeep Maheshwari") 

searchbutton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
searchbutton.click()"""



