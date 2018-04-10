#!/usr/bin/env python

# Created by: Johnny Nguyen
# Last modified: March 1st 2018

import util
import merge
import devmenu

def show_menu(results):
    """ Shows a menu """
    print '================== ' + util.HEADER + 'WORKFLOW MENU' + util.ENDC + ' =================='
    print '1) Development - Create a git branch off of staging'
    print '2) Merge - Merge your development branch to staging (GitHub)'
    print '3) Exit - Exits workflow'
    print '==================================================='

    choice = -1
    while choice not in results:
        try:
            choice = int(raw_input('Enter in a number (1-3): '))
        except ValueError:
            print util.FAIL + "Invalid Input" + util.ENDC + ": Please enter a number between (1-3)"

    return choice


def main():
    # Save option
    results = {
        1: devmenu.main,
        2: merge.main,
        3: quit,
    }
    option = show_menu(results)
    
    # Invoke the function
    results[option]()

if __name__ == "__main__":
    main()
