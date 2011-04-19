---
title: Home
layout: default 
---

Sangman Kim's Blog
==================

This is Sangman's official blog. You may also want to take a look at [my academic page](http://cs.utexas.edu/~sangmank) or [my wife Jiwoo's page](http://www.cerc.utexas.edu/~jiwoo/). 

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


