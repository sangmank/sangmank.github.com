#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys, os, re
import datetime 
import krt

orig_title = raw_input("what is the title? (only alphabet or numbers or spaces)")

title = orig_title.replace(" ", "-")
title = krt.romanize(title)

title = re.sub("[^a-zA-Z0-9 -]", "-", title)

today = datetime.date.today()

filename = "%s-%s.textile"%(today.strftime("%Y-%m-%d"), title)

if filename in os.listdir("."):
	print "file %s already exists"%filename
	sys.exit(1)

entryf = open(filename, "w")
entryf.write("""---
layout: post
title: %s
---

h1. {{ page.title }}"""%orig_title)
entryf.close()

print "file %s has been created" % filename
