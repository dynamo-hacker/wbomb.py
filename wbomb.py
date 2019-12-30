
from selenium import webdriver
import os
def banner():
	print('''
DDD      Y   Y     N   N      AA      M   M      OOO      
D  D      Y Y      NN  N     A  A     MM MM     O   O     
D  D       Y       N N N     AAAA     M M M     O   O     
D  D       Y       N  NN     A  A     M   M     O   O     
DDD        Y       N   N     A  A     M   M      OOO 
	                                                      
		''')
def main():
	driver = webdriver.Chrome()
	driver.get('https://web.whatsapp.com/')

	name = input('Enter the name of user or group: ')
	msg = input('Enter your message: ')
	count = int(input('Enter the count: '))

	input('Enter any key after scanning QR code')

	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()
	
	# The classname of message box may vary.
	msg_box = driver.find_element_by_class_name('_13mgZ') 
		
	for i in range(count):
		msg_box.send_keys(msg)
		# The classname of send button may vary.
		button = driver.find_element_by_class_name('_3M-N-')
		button.click() 
	print('Bombing Complete!!')

banner()
main()
