Title: Windows Expert Installation
url: installation/windows/expert.html
save_as: installation/windows/expert.html

We assume you are very familiar with the Windows environment and with entering
commands in to the command prompt. If you feel uncomfortable with this, or at
any time you feel confused, please refer to the
[novice instructions.]({filename}/pages/installation/windows/novice.md)

  1. Download and install
     [Miniconda for Python 2.7](http://conda.pydata.org/miniconda.html)
     on Windows. Make sure to choose the correct architecture (32/64) for your
     copy of Windows.
  2. After following the instructions you should be able to access `python`
     and `conda` from a command prompt.
  3. Create a fresh conda environment by using

        :::console
        C:\>conda create -n menpo python

  4. Activate the environment by executing:

        :::console
        C:\>activate menpo
        [menpo] C:\>

  5. Install Menpo and **all** of it's dependancies:

        :::console
        [menpo] C:\>conda install -c menpo menpo

  6. Download the notebooks from [here]({filename}/pages/notebooks.md):
    - Make sure you choose the version of the notebooks that corresponds to
      your copy of Menpo.
  7. In a command prompt, navigate to where the notebooks were downloaded, make
     sure the Menpo conda environment is activated, and run:

        :::console
        [menpo] C:\>ipython notebook

  8. Open any of the notebooks to begin learning how to use Menpo. For a more
     in-depth user guide, head to the
     [documentation](http://menpo.readthedocs.org).