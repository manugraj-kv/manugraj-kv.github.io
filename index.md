---
title: Home
layout: default
nav_order: 1
---

# Welcome to Yggdrassl

Some intro text here.

## Recently Added
<ul>
  {% assign recent_pages = site.docs | sort: "date" | reverse %}
  {% for page in recent_pages limit:5 %}
    <li><a href="{{ page.url | relative_url }}">{{ page.title }}</a> — {{ page.date | date: "%b %-d, %Y" }}</li>
  {% endfor %}
</ul>
