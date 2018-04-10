#!/usr/bin/env python

# Created by: Johnny Nguyen
# Last modified: March 1st 2018

import util
import merge
import build
import devmenu

def show_menu(results):
    """ Shows a menu """
    print '================== ' + util.HEADER + 'WORKFLOW MENU' + util.ENDC + ' =================='
    print '1) Development - Create a git branch off of staging'
    print '2) Merge - Merge your development branch to staging (GitHub)'
    print '3) Exit - Exits workflow'
    print '==================================================='

    choice = raw_input('Enter in a number (1-5): ')

    while choice not in results:
        choice = raw_input(util.FAIL + 'Invalid Input! ' + util.ENDC + 'Please enter in a number (1-5): ')

    return choice 


def main():
    # Save option
    results = [
        1: devmenu.main,
        2: merge.main,
        3: quit,
    ]
    option = int(show_menu(results))
    
    # Invoke the function
    results[option]()

# Run the class
main()
