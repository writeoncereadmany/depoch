#!/usr/bin/python

import fileinput
import datetime 
import re

def isPlausibleDate(date):
  return datetime.datetime(2000, 1, 1) < date < datetime.datetime(2100, 1, 1)

def depoch(match):
  try:
    maybe_timestamp = int(match.group())
    from_millis = datetime.datetime.fromtimestamp(maybe_timestamp)
    from_seconds = datetime.datetime.fromtimestamp(maybe_timestamp / 1000)
    if isPlausibleDate(from_millis):
      return '{' + from_millis.isoformat() + '}'
    elif isPlausibleDate(from_seconds):
      return '{' + from_seconds.isoformat() + '}'
    else:
      return match.group()
  except:
     return match.group()

for line in fileinput.input():
   print re.sub('\\d+', depoch, line).rstrip()
