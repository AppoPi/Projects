from selenium import webdriver
d=webdriver.Chrome()
d.get('https://goo.gl/fkpkws')
print d.find_element_by_xpath('//*[@id="form-t3_5j6ggmfg3"]/div/div/pre[1]/code').text