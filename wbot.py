from selenium import webdriver
browser=webdriver.Chrome()
browser.get('https://web.whatsapp.com/')
name=input('Enter the name')
msg=input('Enter your message')
count=int(input('Enter the count'))
input('Press enter after scanning qr code')
elem=browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))
elem.click()
msg_box=browser.find_element_by_class_name('_13mgZ')
for i in range (count):
    msg_box.send_keys(msg)
    button=browser.find_element_by_class_name('_3M-N-')
    button.click()
