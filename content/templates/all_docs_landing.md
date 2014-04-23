Title: Documentation Versions
url: documentation.html
save_as: documentation.html

{% for v in versions %}
  - [{{ v }}](docs/{{ v }})
{% endfor %}