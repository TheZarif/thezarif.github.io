---
permalink: /
title: "About Me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

<div class="home-intro">
  <p class="home-intro__kicker">PhD Student · Faculty of Information · University of Toronto</p>
  <p class="home-intro__lead">I study how digital information systems shape the ways migration and migrants are represented, understood, and made knowable.</p>
  <p class="home-intro__body">Drawing on migration and critical algorithm studies, I examine how computational systems, from search engines to generative AI, select, organize, and transform narratives about migration. Using computational methods alongside theories of framing and representation, my work investigates how emerging forms of algorithmic knowledge reshape the social and political imaginaries of migration.</p>
  <p class="home-intro__supervision">Co-supervised by Dr. Ebrahim Bagheri and Dr. Syed Ishtiaque Ahmed.</p>
</div>

{% include base_path %}

{% assign current_projects = site.projects | sort: "date" | reverse %}

<section class="home-section" aria-labelledby="home-projects-title">
  <div class="home-section__heading">
    <h2 id="home-projects-title">Selected Projects</h2>
    <a href="{{ base_path }}/projects/">Explore projects <span aria-hidden="true">→</span></a>
  </div>
  <div class="home-list">
{% for project in current_projects %}
    <article class="home-entry">
      <p class="home-entry__meta">{{ project.type }}{% if project.venue %} · {{ project.venue }}{% endif %}</p>
      <h3 class="home-entry__title"><a href="{{ base_path }}{{ project.url }}">{{ project.title }}</a></h3>
      <p class="home-entry__description">{{ project.excerpt }}</p>
    </article>
{% endfor %}
  </div>
</section>

{% assign recent_pubs = site.publications | sort: "year" | reverse %}

<section class="home-section" aria-labelledby="home-publications-title">
  <div class="home-section__heading">
    <h2 id="home-publications-title">Recent Publications</h2>
    <a href="{{ base_path }}/publications/">All publications <span aria-hidden="true">→</span></a>
  </div>
  <div class="home-list">
{% for pub in recent_pubs limit:3 %}
    <article class="home-entry">
      <p class="home-entry__meta">{{ pub.year }}{% if pub.status == 'accepted' %} · Accepted{% endif %}</p>
      <h3 class="home-entry__title"><a href="{{ base_path }}{{ pub.url }}">{{ pub.title }}</a></h3>
      {% if pub.authors %}<p class="home-entry__authors">{{ pub.authors }}</p>{% endif %}
      {% if pub.venue %}<p class="home-entry__description">{{ pub.venue }}</p>{% endif %}
    </article>
{% endfor %}
  </div>
</section>
