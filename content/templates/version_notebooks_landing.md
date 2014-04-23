Title: {{ version }}: Notebooks
url: notebooks/{{ version }}
save_as: notebooks/{{ version }}/index.html

{% for folder in notebooks %}
{{ '##' }} {{ folder.header }}
    {% for n in folder.notebooks %}
  - [{{ n.text }}]({{ n.url }})
    {% endfor %}
{% endfor %}