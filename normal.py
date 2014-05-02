#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil

def copy_users():
	''' Does the normalization of users.txt->users table. 
	    No need to change, just copy the file.'''
	shutil.copyfile('projData/users.txt', 'normalData/users.txt')

def main():
	copy_users()
	return 0

if __name__ == '__main__':
	main()

