---
title: Home
author: Alexander Laut
date: November 25, 2021
---

## Projects

### [sylt](https://alaut.github.io/sylt) 

A longitudinal tracker for modeling synchrotron beam dynamics with intensity effects

### [apres](https://alaut.github.io/apres)

A toolkit used to reconstruct accelerator apertures using ray-casting.

## Notes

<!-- <ul> -->
{% for item in site.notes %}
<!--     <li><a href="{{ item.url }}">{{ item.title }}</a></li> -->
    - [{{item.title}}]({{item.url}})
{% endfor %}
<!-- </ul> -->
