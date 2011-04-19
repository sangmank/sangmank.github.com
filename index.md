---
title: Home
layout: default 
---

Sangman Kim's Blog
==================

This is Sangman's official blog. You may also want to take a look at [http://cs.utexas.edu/~sangmank](my academic page) or [http://www.cerc.utexas.edu/~jiwoo/](my wife Jiwoo's page). 

Writing
-------
 {% for post in site.posts %}
 * {{ post.date | date_to_string }} - [{{ post.url }}]({{ post.title }})
 {% endfor %}

Things I like
-------------
 * [http://www.github.com](github)
 * [http://orgmode.org/](Emacs org mode)
 *


