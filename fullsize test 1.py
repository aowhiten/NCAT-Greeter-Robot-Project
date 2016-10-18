from selenium import webdriver

import os, sys, time



print "example with maximize_window()"
nav = webdriver.Firefox()
nav.get('https://www.youtube.com/watch?v=SD5UAqkQpXw')
nav.maximize_window()
time.sleep(10)
nav.quit()

print 'example with fixed set_window_size("1024", "768")'
nav = webdriver.Firefox()
nav.get('https://www.youtube.com/watch?v=SD5UAqkQpXw')
nav.set_window_size("1024", "768")
time.sleep(10)
nav.quit()
