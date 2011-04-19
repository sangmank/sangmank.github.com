---
title: Home
layout: main 
---

Sangman Kim's Page 
=====================

Well, this is a test page for github page. (한글이 나오나?) I just wonder if many aspect of github works as I expect.

Test (테스트)
-------------------------

Test does mean test. Don't expect too much from this. 한글도 나와야 되고.

그것도 잘 나와야 되고.

안나오기만 해봐라. 난 그래도 한글을 쓸거거등

<div id="home">
  <h1>Publications</h1>
  <ul class="pub">
  </ul>

  <h1>Writings</h1>
  <ul class="posts">
    {% for post in site.posts %}
      <li><span>{{ post.date | date_to_string }}</span> &raquo; <a href="{{ post.url }}">{{ post.title }}</a></li>
    {% endfor %}
  </ul>
  
  <h1>Things I like</h1>
  <ul>
</div>
