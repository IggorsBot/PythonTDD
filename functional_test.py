from selenium import webdriver
# from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


# binary = FirefoxBinary('/usr/lib/firefox')
# browser = webdriver.Firefox(firefox_binary=binary, executable_path="/usr/local/bin/")
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
