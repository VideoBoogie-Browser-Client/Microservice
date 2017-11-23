from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http:127.0.0.1:5000')
body = browser.find_element_by_tag_name('body')
assert 'Hello' in body.text
