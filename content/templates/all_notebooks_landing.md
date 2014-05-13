Title: Notebooks Versions
url: notebooks.html
save_as: notebooks.html

* <big>[{{ latest_version }} - Latest Notebooks](http://nbviewer.ipython.org/github/menpo/menpo-notebooks/tree/{{ latest_version }}/notebooks/)</big>

#### Previous Notebooks
{% for v in previous_versions %}
  - [{{ v }}](http://nbviewer.ipython.org/github/menpo/menpo-notebooks/tree/{{ v }}/notebooks/)
{% endfor %}