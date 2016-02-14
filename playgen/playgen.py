#! usr/bin/env python
import time
import os
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
class YoutubePlaylistTxt(object):
	def __init__(self):
		if not os.path.exists("YoutubePlaylistTxt"):
			os.makedirs("YoutubePlaylistTxt")
	def specification(self):
		print '1.Auto MP4\n2.Auto 3GP\n3.720P\n4.360P\n5.240P\n6.144P'
		self.quality = input("Quality: ")
		if(self.quality > 6):
			os.system('clear')
			self.specification()
		file_name = raw_input("File Name: ")
		if os.path.exists('YoutubePlaylistTxt/'+file_name+'.txt'):
			file_name = file_name + '_new'
			print 'Renamed to '+file_name
		self.playlist_file = open('YoutubePlaylistTxt/'+file_name+'.txt','a')
	def create_txt(self):
		browser = webdriver.Chrome()
		browser.get("http://youtubemultidownloader.com/list.php")
		#browser.set_window_size(10,10)
		if(self.quality == 1):
			quality_button = browser.find_element_by_id("quality1").click()
		elif(self.quality == 2):
			quality_button = browser.find_element_by_id("quality2").click()
		elif(self.quality == 3):
			quality_button = browser.find_element_by_id("quality3").click()
		elif(self.quality == 4):
			quality_button = browser.find_element_by_id("quality4").click()
		elif(self.quality == 5):
			quality_button = browser.find_element_by_id("quality5").click()
		elif(self.quality == 6):
			quality_button = browser.find_element_by_id("quality6").click()
		browser.refresh()
		playlist_url_field = browser.find_element_by_id("txtPlaylist")
		playlist_url_field.send_keys(Keys.CONTROL,'v')
		link_area = browser.find_element_by_id("txtDownload")
		time.sleep(60)
		link_area.send_keys(Keys.CONTROL,'a')
		link_area.send_keys(Keys.CONTROL,'c')
		link = pyperclip.paste()
		self.playlist_file.write(link)
		self.playlist_file.close()
		print 'File Created Successfully'
		browser.quit()
ypt = YoutubePlaylistTxt()
ypt.specification()
ypt.create_txt()
