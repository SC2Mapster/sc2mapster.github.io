---
title: Tutorials
date: 2018-02-08 06:39:00 Z
---

<h1>{{ page.title }}</h1>
<h2>Blizzard Tutorials</h2>
<p>You can find blizzard written tutorials over <a href="https://s2editor-guides.readthedocs.io/">here</a>.</p>
<h2>UI</h2>
<ul>
  {% for post in site.categories.UI %}
  	{% assign author = site.data.authors[post.author] %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> by <a href="mailto:{{ author.email }}">{{ author.name | default: site.author }}</a>
    </li>
  {% endfor %}
</ul>

<h2>Data</h2>
<ul>
  {% for post in site.categories.Data %}
  	{% assign author = site.data.authors[post.author] %}
    <li>
      <a href="{{ post.url }}">{{ post.title }}</a> by <a href="mailto:{{ author.email }}">{{ author.name | default: site.author }}</a>
    </li>
  {% endfor %}
</ul>

