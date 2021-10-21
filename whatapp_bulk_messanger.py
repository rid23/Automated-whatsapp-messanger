from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def send_whatsapp(number):
	#opening whatsapp web
	driver.get(f'https://web.whatsapp.com/send?phone=+91{number}')
	#driver.find_element_by_xpath("//div[@title='Attach']")

	try:
		#to bypass alert pop-up when a number is invalid
		alert = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//div[text() = 'OK']")))
		alert.click()
	except:
		attach = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,"//div[@title='Attach']")))
		sleep(0.5)
		attach.click()
		sleep(2)
		image_attach = driver.find_element_by_xpath("//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']")
		sleep(0.5)
		image_attach.send_keys('C:\\Users\\riddhi\\Desktop\\PYTHON\\tst.jpg')
		sleep(2)
		send_key = driver.find_element_by_xpath("//span[@data-testid='send']")
		sleep(0.5)
		send_key.click()

def main():
	with open('numbers.txt','r') as f:
		nums = f.readlines()
	
	for number in nums:
		send_whatsapp(number)
		sleep(2)

	
if __name__ == '__main__':
	options = webdriver.ChromeOptions()
	options.add_argument("--user-data-dir=C:/Users/riddhi/AppData/Local/Google/Chrome/for_rid")
	driver = webdriver.Chrome(executable_path = 'C:\\Users\\riddhi\\Desktop\\PYTHON\\chromedriver.exe',options = options)
	main()
	driver.quit()
	print('operation successful')