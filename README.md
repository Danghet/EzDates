# EzDates
A python module to reformat dates.
# How to Use
Use fixdates() to reformat
Two arguments: Date and format
# Date
For the month, it can either be a word like "oct" or "january" or a number below or equal to 12.
The date is determined by a number that is less than 32
The year requires all 4 characters: 2021 instead of 21.
# Format  
This is the format you want the date returned in
fixdates("mar 5 1986", "mdy") would return "3-5-1986"   
