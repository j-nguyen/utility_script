#!/usr/bin/env python
# Releases the branch to either QA/Staging/Master
# Created by: Johnny Nguyen

import subprocess
import util

def show_menu():
	""" Shows a menu """
	print '================== ' + util.HEADER + 'WORKFLOW MENU' + util.ENDC + ' =================='
	print '1) Release to Master'
	print '2) Exit'
	print '==================================================='

	choice = -1
	while choice not in [1,2]:
		try:
			choice = int(raw_input('Enter in a number (1-2): '))
		except ValueError:
			print util.FAIL + "Invalid Input" + util.ENDC + ": Please enter a number between (1-3)"

	return choice

def release():
	""" Releases to master """
	# Before doing anything, make sure we've committed
	status = subprocess.check_output(['git', 'status', '--porcelain'])
	if status != '':
		print util.FAIL + util.BOLD + 'Your branch needs to be committed.' + util.ENDC 
		return
	# Checkout to staging
	print '=== Checking out to Staging'
	print subprocess.check_output(['git', 'checkout', 'staging'])
	# Make sure that everything is up-to-date
	print '=== Making sure both the local and remote branches are up-to-date'
	print subprocess.check_output(['git', 'pull', 'origin', 'staging'])
	# Checkout to master, and makes sure it's up to date
	print '=== Checking out to Master'
	print subprocess.check_output(['git', 'checkout', 'master'])
	print subprocess.check_output(['git', 'pull', 'origin', 'master'])
	# Merge & Push
	print '=== Merging staging to master'
	print subprocess.check_output(['git', 'merge', 'master'])
	print subprocess.check_output(['git', 'push', 'origin', 'master'])
	# Ouptut
	print '=== Finished merging and pushed to master.'

def main():
	""" Executes our main function """
	options = show_menu()

	# Use the traditional if statements to get through
	if options == 1:
		release()
	else:
		quit()

# Run the function if this python file gets called
if __name__ == "__main__":
	main()