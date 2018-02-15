---
title: Editor Tutorials
date: 2018-02-08 06:39:00 Z
---
<h1>{{ page.title }}</h1>

<p>These tutorials were forked from <a href="https://github.com/Blizzard/s2editor-tutorials">https://github.com/Blizzard/s2editor-tutorials</a> </p>

<h2>Introduction</h2>

<ul>
{% assign items = site.editor_tutorials | where: "category", "01_Introduction" %}
{% for item in items %} 	
  	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>

<h2>Terrain Editor</h2>

<ul>
{% assign items = site.editor_tutorials | where: "category", "02_Terrain_Editor" %}
{% for item in items %}
 	<li><a href="{{ item.url }}">{{ item.title }}</a></li>	
{% endfor %}
</ul>

<h2>Trigger Editor</h2>

<ul>
{% assign items = site.editor_tutorials | where: "category", "03_Trigger_Editor" %}
{% for item in items %}
 	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>

<h2>Data Editor</h2>

<ul>
{% assign items = site.editor_tutorials | where: "category", "04_Data_Editor" %}
{% for item in items %}
 	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>

<h2>Text Editor</h2>

<ul>
{% assign items = site.editor_tutorials | where: "category", "05_Text_Editor" %}
{% for item in items %}
 	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>

<h2>Cutscene Editor</h2>

<ul>
{% assign items = site.editor_tutorials | where: "category", "06_Cutscene_Editor" %}
{% for item in items %}
 	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>

<h2>Lessons</h2>

<ul>
{% assign items = site.editor_tutorials | where: "category", "07_Lessons" %}
{% for item in items %}
 	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>