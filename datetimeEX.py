#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     24/10/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# imprts the date/time module #
import datetime

# creates a cariable called "currentDateTime" and assigns it to the current



##print(currentDateTime)
##print(currentDateTime.year)
##print(currentDateTime.strftime("%A"))
##print(currentDateTime.strftime("%a"))
##print(currentDateTime.strftime("%w"))
##print(currentDateTime.strftime("%d"))
##print(currentDateTime.strftime("%b"))
##print(currentDateTime.strftime("%B"))
##print(currentDateTime.strftime("%m"))
##print(currentDateTime.strftime("%y"))
currentDateTime = datetime.datetime.now()
print(currentDateTime.strftime("%Y"))
##print(currentDateTime.strftime("%H"))
##print(currentDateTime.strftime("%h"))
##print(currentDateTime.strftime("%p"))
##print(currentDateTime.strftime("%a"))
##print(currentDateTime.strftime("%H %p"))
##print(currentDateTime.strftime("%Z"))
##print(currentDateTime.strftime("%c"))
##print(currentDateTime.strftime("%x"))
##print(currentDateTime.strftime("%X"))
##print(currentDateTime.strftime("%U"))
##print(currentDateTime.strftime("%W"))

date = datetime.datetime(2019, 10, 24)
##print(date)