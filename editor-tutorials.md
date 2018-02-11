---
title: Editor Tutorials
date: 2018-02-08 06:39:00 Z
---

<h1>{{ page.title }}</h1>

<p>These tutorials were forked from <a href="https://github.com/Blizzard/s2editor-tutorials">https://github.com/Blizzard/s2editor-tutorials</a> </p>

<h2>Introduction</h2>

<ul>
{% for item in site.editor_tutorials %}
 	{% if item.category == "01_Introduction" %}
  	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
	{% endif %}
{% endfor %}
</ul>

<h2>Terrain Editor</h2>

<ul>
{% for item in site.editor_tutorials %}
 	{% if item.category == "02_Terrain_Editor" %}
  	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
	{% endif %}
{% endfor %}
</ul>

<h2>Trigger Editor</h2>

<ul>
{% for item in site.editor_tutorials %}
 	{% if item.category == "03_Trigger_Editor" %}
  	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
	{% endif %}
{% endfor %}
</ul>

<h2>Data Editor</h2>

<ul>
{% for item in site.editor_tutorials %}
 	{% if item.category == "04_Data_Editor" %}
  	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
	{% endif %}
{% endfor %}
</ul>

<h2>Text Editor</h2>

<ul>
{% for item in site.editor_tutorials %}
 	{% if item.category == "05_Text_Editor" %}
  	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
	{% endif %}
{% endfor %}
</ul>

<h2>Cutscene Editor</h2>

<ul>
{% for item in site.editor_tutorials %}
 	{% if item.category == "06_Cutscene_Editor" %}
  	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
	{% endif %}
{% endfor %}
</ul>

<h2>Lessons</h2>

<ul>
{% for item in site.editor_tutorials %}
 	{% if item.category == "07_Lessons" %}
  	<li><a href="{{ item.url }}">{{ item.title }}</a></li>
	{% endif %}
{% endfor %}
</ul>
