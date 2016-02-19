Frequently Asked Questions (FAQ)
================================

  1. [What license is Menpo under?](#license)
  2. [How do I cite Menpo?](#citation)
  3. [How do I install a development version?](#development)

### What license is Menpo under? {: #license}
Menpo is under the 3-clause BSD license which can be found 
[here](https://github.com/menpo/menpo/blob/master/LICENSE.txt). This means
that you are free to use Menpo in commercial products as long as you retain
our copyright notice and do not use the *Imperial College London* name to
promote your product. A list of contributors is given within the
[authors file](https://github.com/menpo/menpo/blob/master/AUTHORS.txt).

### How do I cite Menpo? {: #citation}
Menpo has been accepted to appear at the 
[ACM Multimedia 2014](http://acmmm.org/2014/) conference.

<pre>
Joan Alabort-i-Medina, Epameinondas Antonakos, James Booth, Patrick Snape and Stefanos Zafeiriou, "Menpo: A Comprehensive Platform for Parametric Image Alignment and Visual Deformable Models.", In Proceedings of the international conference on Multimedia, ACM, 2014.
</pre> [[Bibtex](paper/menpo.bib)] [[pdf](paper/Menpo_ACM_MM_2014.pdf)]

Therefore, this publication is the reference paper to cite if you use Menpo 
within **any academic paper**. We request that you if do use Menpo for an
academic publication within any displicine that you cite Menpo!

### How do I install a development version? {: #development}
To install a development version of Menpo (or any of the libraries), we suggest
the following workflow:

  1. Install the latest *development* version of Menpo from conda. This will 
     install the most recently successful commit from the git repository and
     ensure you receive all the latest, correct dependencies:

        :::console
        $ conda create -n menpodev python
        $ source activate menpodev
        (menpodev) $ conda install -c menpo/channel/master menpo

  2. **Remove** Menpo so that we can install the development version from
     Github:

        :::console
        (menpodev) $ conda remove menpo

  3. Checkout the Menpo git repository. You may wish to fork the project
     on Github so that you can make pull requests back to the Menpo project. In
     this case, just replace ``https://github.com/menpo/menpo.git`` with
     ``https://github.com/GITHUB_USERNAME/menpo.git`` below:

        :::console
        (menpodev) $ git clone https://github.com/menpo/menpo.git

  4. Install *pip* **inside** the conda environment and then install an editable
     version of your Menpo repository inside:

        :::console
        (menpodev) $ conda install pip
        (menpodev) $ pip install -e ./menpo --no-deps

  5. Any edits you make within the ``./menpo`` folder will be reflected inside
     this conda environment! This procedure is identical for any of the Menpo
     libraries, primarily steps **3** and **4**.

The instructions above were specific to Unix operating systems, but Windows
should be identical outside of activating the conda environment.
