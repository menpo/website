Title: Notebooks
url: notebooks.html
save_as: notebooks.html

{% for project in projects %}
  - **{{ project }} {{ latest_versions[project] }}** - [browse online](http://nbviewer.jupyter.org/github/menpo/{{ project }}-notebooks/tree/{{ latest_versions[project] }}/notebooks/) - [download](https://github.com/menpo/{{ project }}-notebooks/archive/{{ latest_versions[project] }}.zip)
{% endfor %}

As part of the project, we maintain a set of Jupyter notebooks that help
illustrate how Menpo should be used.

The notebooks for each of the core four Menpo Libraries are kept inside their
own Github repositories.
If you wish to view the static output of the notebooks, feel free to browse
them online using the provided links. This gives a great way to passively read
the notebooks without needing a full Python environment. Note that these copies
of the notebook contain only static output and thus cannot be run directly - to
execute them you need to download them, install menpo, and open the notebook in
Jupyter.

### Running The Notebooks Locally
In order to experiment with the Menpo codebase, we suggest you download the
notebooks and run them yourself. Before being able to run the notebooks you
**must install menpo**. Head to the
[installation instructions]({filename}/pages/installation/index.md) before
continuing.

 1. Start by downloading the notebooks and extracting the zip somewhere on your
    local disk. Please substitute **NOTEBOOKS_PATH** with this path in the
    following instructions.
 2. We then need to run the notebooks using the `jupyter notebook` application.
    Begin by opening a command prompt/terminal and changing to the directory
    where you extracted the notebooks:

    **OSX/Linux**

        ::console
        $ cd NOTEBOOKS_PATH
        $ source activate menpo
        (menpo) $ jupyter notebook

    **Windows**

        ::console
        C:\>cd NOTEBOOKS_PATH
        NOTEBOOKS_PATH>activate menpo
        [menpo] NOTEBOOKS_PATH>jupyter notebook

 3. A browser should open and show the Jupyter notebook browser. Click a
    notebook to open it. You can now run the notebooks by executing each code
    cell and following the documentation provided inside the notebook. If you
    are unfamiliar with the Jupyter notebook environment, please consult
    their [documentation](http://jupyter.org).

### Previous Notebooks
These notebooks are versioned in an identical manner
to the main Menpo project. Therefore, you should make sure to use the version
of the notebooks that matches the version of Menpo you are using.

To check which version of Menpo you are using, run:

    :::python
    >>> import menpo
    >>> print(menpo.__version__)


inside of a Python interpreter.

{% for project in projects %}
#### {{ project }}
{% for v in previous_versions[project] %}
  - **{{ v }}** [browse](http://nbviewer.jupyter.org/github/menpo/{{ project }}-notebooks/tree/{{ v }}/notebooks/) [download](https://github.com/menpo/{{ project }}-notebooks/archive/{{ v }}.zip)
{% endfor %}

{% endfor %}
