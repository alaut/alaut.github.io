---
layout: page
---

# Projects

## [sylt](alaut.github.io/sylt) 

A longitudinal tracker for modeling synchrotron beam dynamics with intensity effects


## [apres](alaut.github.io/apres)
A toolkit used to reconstruct accelertor apertures using ray-casting.


# Notes

<ul>
{% for item in site.notes %}
    <li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>
