#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

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
		for word in line.split():
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
		for word in line.split():
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
		for word in line.split():
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
	
def main():
	clean_old_data()
	copy_users()
	normalize_friend()
	normalize_follow()
	normalize_checkins()
	return 0

if __name__ == '__main__':
	main()

