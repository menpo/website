Title: Notebooks
url: notebooks.html
save_as: notebooks.html

As part of the project, we maintain a set of notebooks that help illustrate how
Menpo should be used.

The notebooks are kept inside their
[own Github repository](http://www.github.com/menpo/menpo-notebooks).
If you wish to view the static output of the notebooks, feel free to browse
them online using the provided links. This gives a great way to passively read
the notebooks without needing a full Python environment. Note that these copies
of the notebook contain only static output and thus cannot be run.

To download the notebooks and use them within your copy of Menpo, use the
links provided.

#### **({{ latest_version }}) - Latest Notebooks**
  - **[Browse Online](http://nbviewer.ipython.org/github/menpo/menpo-notebooks/tree/{{ latest_version }}/notebooks/)**
  - **[Download](https://github.com/menpo/menpo-notebooks/archive/{{ latest_version }}.zip)**

#### Previous Notebooks
These notebooks are versioned in an identical manner
to the main Menpo project. Therefore, you should make sure to use the version
of the notebooks that matches the version of Menpo you are using.

To check which version of Menpo you are using, run:

```python
import menpo
print(menpo.__version__)
```

inside of a Python interpreter.

##### Versions
{% for v in previous_versions %}
  - {{ v }}
    - [Browse](http://nbviewer.ipython.org/github/menpo/menpo-notebooks/tree/{{ v }}/notebooks/)
    - [Download](https://github.com/menpo/menpo-notebooks/archive/{{ v }}.zip)
{% endfor %}