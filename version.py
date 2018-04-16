#!/usr/bin/env python
# Created by: Johnny Nguyen
# Last modified: March 1st 2018
# Creates versioning based on the branch. The delimiter set would probably be _ 

import subprocess
import util
import merge

def show_menu(results):
    """ Shows a menu """
    print '================== ' + util.HEADER + 'VERSIONING MENU' + util.ENDC + ' =================='
    print '1) New Version - Creates a new version'
    print '2) Merge - Merge your version into staging'
    print '3) Exit - Exits workflow'
    print '==================================================='

    choice = -1
    while choice not in results:
        try:
            choice = int(raw_input('Enter in a number (1-3): '))
        except ValueError:
            print util.FAIL + "Invalid Input" + util.ENDC + ": Please enter a number between (1-3)"

    return choice

def new_version():
    pass

def main():
    """ The main function """
        # Save option
    results = {
        1: new_version,
        2: merge.main,
        3: quit,
    }
    option = show_menu(results)

if __name__ == "main":
  main()