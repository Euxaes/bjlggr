#!/usr/bin/env python

"""
Author: Eva Rachel Retuya (https://github.com/Euxaes)
Bullet Journal Logger

This script allows for continuous enumeration of "items" taken from my actual
bullet journal for digital filing without having to worry about markdown syntax.
"""

import webbrowser

# https://stackoverflow.com/questions/9573244
def isNotBlank(ans):
    if ans and ans.strip():
        return True
    return False

def mdWriter(mdFile, ans):
    """ Keep writing until 'blank' """
    while isNotBlank(ans):
        if ans[0] != '-':
            sentence = "- %s\n" % ans
            mdFile.write(sentence)
        else:
            # add two spaces for nesting bullets
            sentence = "  %s\n" % ans
            mdFile.write(sentence)
        ans = raw_input()
    mdFile.write("\n")
        
def placeCategory(mdFile, category, ans):
	if isNotBlank(ans):
	    header = "# %s\n" % category
	    mdFile.write(header)
	    mdWriter(mdFile, ans)

# Set filename
filename = "yesterday.md"
# Open yesterday.md for writing
target = open(filename, 'w')

print("Writing yesterday's journal entry: \n")
prompt = raw_input("When did you wake up? ")
wakeTime = "## %s\n\n" % prompt
target.write(wakeTime)

print("Enter an empty string to move on otherwise keep on listing items.\n")
prompt = raw_input("Yesterday's events are: \n")
placeCategory(target, "Events", prompt)

prompt = raw_input("Tasks you did: \n")
placeCategory(target, "Tasks", prompt)

prompt = raw_input("Took note of the following: \n")
placeCategory(target, "Notes", prompt)

prompt = raw_input("Thought-provoking stuff: \n")
placeCategory(target, "Thoughts", prompt)

prompt = raw_input("When did you slept? ")
bedTime = "## %s" % prompt
target.write(bedTime)

# Close the file
target.close()
# Open file for review and additional formatting
print "Opening file, \"yesterday.md\"..."
webbrowser.open(filename)
