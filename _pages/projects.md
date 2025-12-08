---
layout: archive
title: "Projects"
permalink: /projects/
author_profile: true
---

{% include base_path %}

Here are some of my selected projects.

{% for post in site.projects reversed %}
  {% include archive-single.html %}
{% endfor %}
