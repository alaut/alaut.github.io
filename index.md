---
layout: page
---

## Introduction

Hi! Here's my little math/physics blog!

## Notes

<ul>
{% for item in site.notes %}
    <li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>
