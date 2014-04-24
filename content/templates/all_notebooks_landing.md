Title: Notebooks Versions
url: notebooks.html
save_as: notebooks.html

{% for v in versions %}
  - [{{ v }}](|filename|/pages/notebook_versions/{{ v }}.md)
{% endfor %}
