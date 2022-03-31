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

## [filter-pack](https://alaut.github.io/filter-pack/)

A toolkit used to characterize the X-Ray energy spectrum of thomson photons by transmission analysis through a filter pack on a single shot basis.

## Notes

<ul>
{% for item in site.notes %}
    <li><a href="{{ item.url }}">{{ item.title }}</a></li>
{% endfor %}
</ul>

<!-- - [The Space Charge Geometry Factor](/g)
- [The **Effective** Space Charge Geometry Factor](/g_bar)
- [Closed Quasi-Elliptical Shapes](/shapes)
- [Generalized Quasi-Normal Distributions](/distributions)
- [Ray Tracing Intersection Algorithm](/ray_casting) -->
