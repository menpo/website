Date: 2014-05-17
Title: Quick tip: Using line_profiler in an IPython notebook
Tagline: A quick guide up-to-date guide to setting up line_profiler with IPython.
Slug: line_profiler_ipython
Category: Blog
Tags: IPython, profiling, tip
Author: James Booth

### Installation

Install line profiler[^version]

```
> pip install --pre line_profiler
```
You can install line_profiler as a proper IPython extension, but I like the simplicity of just activating it when I need it. just run 

```python
import line_profiler
import IPython
ip = IPython.get_ipython()
ip.define_magic('lprun', line_profiler.magic_lprun)
```

in a cell and you're good for the session.

### Usage

Let's say we have a function call `foo()`which is taking a long time, and we strongly suspect that it's the `bar` function call inside it that's taking a while. We tell line profiler of all functions we are interested in with the `-f` flag (you can have multiple!) and finally tell it the function to actually execute at the end:

```python
from mypackage import foo, bar
%lprun -f bar foo()
```

This works perfectly well with objects and methods too, just specify the method you want to profile with it's full name (i.e. in it's class namespace)

```python
from mypackage import MyClass
instance = MyClass()
%lprun -f MyClass.bar instance.foo()
```

[^version]: As of May 2014 we need `--pre` because later versions of pip [won't install betas](http://pip.readthedocs.org/en/latest/reference/pip_install.html#pre-release-versions) by default, and the [current version](https://pypi.python.org/pypi/line_profiler/) of line_profiler is `1.0b3`. Once there's no longer a `b` at the end of the version string `pip install line_profiler` will be sufficient.
