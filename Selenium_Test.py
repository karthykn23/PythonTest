import time 
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = webdriver.chrome()

url="https://www.flightradar24.com/data/airports/pnq"
driver.get(url)
get_url = driver.current_url 
print(get_url)
driver.implicitly_wait(60)
driver.find_element_by_xpath('//a[text()="continue"]').click()

Alert alert = driver.switchTo().alert();
alert.dismiss();
    
  airports_code = 'PNQ'
  schedule = Schedule(airports_code)
  
  arrivals = schedule.arrivals
  
  desired_airports = ['BLR','DEL','GOX','IXC','HYD','NAG']
  for arrivals in arrivals:
      location = arrivals.get('location','').upper()
      
      if any (airports in location for airports in desired_airports):
        flight = arrival.get('flight','')
        status = arrival.get('status','data not available')
        print (f"From {location}: Flight {flight} - Status{status}")
        
schedule.close_browser()