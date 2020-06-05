---
layout: archive
title: "Publications"
permalink: https://rcochrane.github.io/publications/2019-06-17-Designer-Sinorhizobium-meliloti-strains-and-multi-functional-vectors-enable-direct-inter-kingdom-DNA-transfer
author_profile: true
---

---
layout: archive
title: "Publications"
permalink: https://rcochrane.github.io/publications/2019-12-19-Rapid-method-for-generating-designer-algal-mitochondrial-genomes
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}
