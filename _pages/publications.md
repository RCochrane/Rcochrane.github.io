---
permalink: /pages/publications.md
title: "Publications"
author_profile: true
redirect_from: 
  - /publications/
  - /pages/publications.md
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

'https://rcochrane.github.io/markdown_generator/publications.py'
