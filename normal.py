#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os
import re

def clean_old_data():
	'''Removes the old files before executing'''
	os.system("rm -fr normalData/*")

def copy_users():
	''' Does the normalization of users.txt->users table. 
	    No need to change, just copy the file.'''
	shutil.copyfile('projData/users.txt', 'normalData/users.txt')

def normalize_friend():
	'''Does the normalization of the friends table'''
	filein = open("projData/friendList.txt", "r")
	fileout = open("normalData/friendList.txt", "w")
	for line in filein:
		count = 0
		for word in re.split(r'\t+', line.strip()):
			if count == 0:
				idleft = word
				count = 1
			else:
				fileout.write(idleft)
				fileout.write("\t")
				fileout.write(word)
				fileout.write("\n")
	filein.close()
	fileout.close()

def normalize_follow():
	'''Does the normalization of the follow table'''
	filein = open("projData/followList.txt", "r")
	fileout = open("normalData/followList.txt", "w")
	for line in filein:
		count = 0
		for word in re.split(r'\t+', line.strip()):
			if count == 0:
				idleft = word
				count = 1
			else:
				fileout.write(idleft)
				fileout.write("\t")
				fileout.write(word)
				fileout.write("\n")
	filein.close()
	fileout.close()
	
def normalize_checkins():
	'''Does the normalization of the checkins table'''
	filein = open("projData/checkins.txt", "r")
	fileout = open("normalData/checkins.txt", "w")
	for line in filein:
		count = 1
		for word in re.split(r'\t+', line.strip()):
			if count == 1:
				userid = word
			elif count == 2:
				date = word
			elif count == 3:
				time = word
			elif count == 6:
				locid = word
			count = count + 1
		newline = '%s\t%s\t%s\t%s\n' % (userid, date, time, locid)
		fileout.write(newline)
	filein.close()
	fileout.close()
	
def normalize_division_name():
	'''Normalize the devision name table'''
	filein = open("projData/checkins.txt", "r")
	fileout = open("normalData/div_name.txt", "w")
	for line in filein:
		count = 1
		for word in re.split(r'\t+', line.strip()):
			if count == 12:
				l1_ad_div = word
			elif count == 13:
				l1_div_code = word
			elif count == 14:
				l2_ad_div = word
			elif count == 15:
				l2_div_code = word
			elif count == 16:
				country_code = word
			count = count + 1
		newline = '%s\t%s\t%s\t%s\t%s\n' % (l1_ad_div, l2_ad_div, l1_div_code, l2_div_code, country_code)
		fileout.write(newline)
	filein.close()
	fileout.close()
	
def normalize_nearest_refer():
	'''Normalize the nearest refer table'''
	filein = open("projData/checkins.txt", "r")
	fileout = open("normalData/nearest_refer.txt", "w")	
	for line in filein:
		count = 1
		for word in re.split(r'\t+', line.strip()):
			if count == 11:
				placename = word
			elif count == 10:
				postal_code = word
			elif count == 7:
				la_of_nearest = word
			elif count == 8:
				lo_of_nearest = word
			elif count == 13:
				l1_div_code = word
			elif count == 15:
				l2_div_code = word
			elif count == 16:
				country_code = word
			count = count + 1
		newline = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t\n' \
					% (placename, postal_code, la_of_nearest, lo_of_nearest, l1_div_code, \
					    l2_div_code, country_code)
		fileout.write(newline)
	filein.close()
	fileout.close()
		
def normalize_locations():
	'''Normalizes the location table'''
	filein = open("projData/locations.txt", "r")
	fileout = open("normalData/location1.txt", "w")		
	for line in filein:
		count = 1
		for word in re.split(r'\t+', line.strip()):
			if count == 1:
				locid = word
			elif count == 2:
				name = word
			elif count == 3:
				adddate = word
			count = count + 1
		newline = '%s\t%s\t%s\n' % (locid, name, adddate)
		fileout.write(newline)
	filein.close()
	fileout.close()	
	
def get_all_locations():
	'''Does the second phase of location normalization'''
	filein = open("projData/checkins.txt", "r")
	fileout = open("normalData/location2.txt", "w")
	for line in filein:
		count = 1
		for word in re.split(r'\t+', line.strip()):
			if count == 6:
				locid = word
			elif count == 4:
				chkinlat = word
			elif count == 5:
				chkinlong = word
			elif count == 11:
				placename = word
			elif count == 10:
				postcode = word
			elif count == 9:
				distance = word
			count = count + 1
		newline = '%s\t%s\t%s\t%s\t%s\t%s\n' % (locid, chkinlat, \
				chkinlong, placename, postcode, distance)
		fileout.write(newline)
	filein.close()
	fileout.close()	
	
def main():
	clean_old_data()
	copy_users()
	normalize_friend()
	normalize_follow()
	normalize_checkins()
	normalize_division_name()
	normalize_nearest_refer()
	normalize_locations()
	get_all_locations()
	return 0

if __name__ == '__main__':
	main()

