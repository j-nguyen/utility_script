#!/usr/bin/env python

# Import some stuff
import subprocess
import util
import branch
import merge

def show_menu(results):
    """ Shows a menu """
    print '================== ' + util.HEADER + 'WORKFLOW MENU' + util.ENDC + ' =================='
    print '1) Create a git branch'
    print '2) Rebase your contents'
    print '3) Exit - Exits workflow'
    print '==================================================='

    choice = -1
    while choice not in results:
        try:
            choice = int(raw_input('Enter in a number (1-3): '))
        except ValueError:
            print util.FAIL + "Invalid Input" + util.ENDC + ": Please enter a number between (1-3)"

    return choice

def rebase_contents():
    """ Pulls from staging, and assumes """
    print subprocess.check_output(['git', 'fetch'])
    print subprocess.check_output(['git', 'pull', 'origin', 'staging'])

def main():
    """ Main function """
    results = {
        1: branch.main,
        2: rebase_contents,
        3: quit
    }
    options = show_menu(results)

    # Invoke the command
    results[options]()

# Run command
if __name__ == "__main__":
    main()
