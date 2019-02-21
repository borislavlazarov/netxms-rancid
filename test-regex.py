import csv, sys, re, time

with open('all-sys-descr.txt') as f:
    lines = f.readlines()

for line in lines:
 if re.match("^S[FG][35]0\d-", line, re.IGNORECASE):
  print line

