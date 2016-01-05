Title: Welcome to the Menpo project!
url:
save_as: index.html

<div style="display: table; margin: 0 auto; margin-bottom: 20px;">
	<img alt="Example Face Fitting 1" src="pages/images/face_examples/example_1.png" style="border:1px solid #021a40; margin-right: 2px;">
	<img alt="Example Face Fitting 2" src="pages/images/face_examples/example_2.png" style="border:1px solid #021a40; margin-right: 2px;">
	<img alt="Example Face Fitting 3" src="pages/images/face_examples/example_3.png" style="border:1px solid #021a40; margin-right: 2px;">
	<img alt="Example Face Fitting 4" src="pages/images/face_examples/example_4.png" style="border:1px solid #021a40; margin-right: 2px;">
	<img alt="Example Face Fitting 5" src="pages/images/face_examples/example_5.png" style="border:1px solid #021a40; margin-right: 2px;">
	<img alt="Example Face Fitting 6" src="pages/images/face_examples/example_6.png" style="border:1px solid #021a40;">
</div>
<div style="clear: both;"></div>

The Menpo project is a set of Python libraries for manipulating data
that is particularly useful for Machine Learning and Computer Vision. The core
``menpo`` library contains a number of powerful tools for manipulating
*annotated* image and mesh data. ``menpo`` focuses on making importing, 
manipulating and visualizing data as simple as possible. This makes us strong 
supporters of projects like the [Jupyter notebook](http://jupyter.org/).

The Menpo project also includes another tool that makes annotating new datasets
even easier! Freely available a [landmarker.io](https://www.landmarker.io), the 
landmarker is a tool that makes it simple to annotate new images.

On top of the core ``menpo`` library, we have implemented a number of other 
libraries that utilize ``menpo`` for more specific purposes. Currently, the
Menpo project libraries include:

  - ``menpo``: the core library containing all the essential classes for
    data manipulation including transforms, warping, landmarks, importing and
    exporting.  
    [![Github Release][m_shield]][m_gh] [![BSD License][bsd_shield]][m_lic]
  - ``menpofit``: a statistical modelling toolkit, providing all the tools 
    required to build, fit and test deformable models like
    **Active Appearance Models**, **Constrained Local Models** and
    **Supervised Descent Method**.  
    [![Github Release][mf_shield]][mf_gh] [![BSD License][bsd_shield]][mf_lic]
  - ``menpo3d``: specific tools for visualizing and manipulating 3D data such
    as meshes. This package contains a lot of complex dependencies, including
    an OpenGL based rasterizer.  
    [![Github Release][m3d_shield]][m3d_gh] [![BSD License][bsd_shield]][m3d_lic]
  - ``menpodetect``: wraps a number of existing projects that can perform
    object detection. Not all of the wrapped projects fall under the same
    BSD license and so care must be taken when using this project to adhere
    to the sub-project licenses.  
    [![Github Release][md_shield]][md_gh] [![BSD License][bsd_shield]][md_lic]
   - ``menpowidgets``: provides Jupyter notebook interactive widgets. These widgets
     are for all of the Menpo project subprojects including ``menpo`` and ``menpofit``.  
    [![Github Release][mw_shield]][mw_gh] [![BSD License][bsd_shield]][mw_lic]
    
  [bsd_shield]: http://img.shields.io/badge/License-BSD-green.svg
  [m_shield]: http://img.shields.io/github/release/menpo/menpo.svg
  [m_gh]: http://github.com/menpo/menpo
  [m_lic]: https://github.com/menpo/menpo/blob/master/LICENSE.txt
  [mf_shield]: http://img.shields.io/github/release/menpo/menpofit.svg
  [mf_gh]: http://github.com/menpo/menpofit
  [mf_lic]: https://github.com/menpo/menpofit/blob/master/LICENSE.txt
  [m3d_shield]: http://img.shields.io/github/release/menpo/menpo3d.svg
  [m3d_gh]: http://github.com/menpo/menpo3d
  [m3d_lic]: https://github.com/menpo/menpo3d/blob/master/LICENSE.txt
  [md_shield]: http://img.shields.io/github/release/menpo/menpodetect.svg
  [md_gh]: http://github.com/menpo/menpodetect
  [md_lic]: https://github.com/menpo/menpodetect/blob/master/LICENSE.txt
  [mw_shield]: http://img.shields.io/github/release/menpo/menpowidgets.svg
  [mw_gh]: http://github.com/menpo/menpowidgets
  [mw_lic]: https://github.com/menpo/menpowidgets/blob/master/LICENSE.txt

### Installation
The Menpo project is written in **Python** and we provide a simple and easy 
method of installation using [Conda](http://conda.pydata.org/). We suggest you 
head over to the 
[installation instructions]({filename}/pages/installation/index.md) to get 
started. We recommend the use of ``conda`` due to the fact that the Menpo projects also include compiled ``C/C++`` code which may be complicated to compile on various platforms.

### Citing the Menpo project
<pre>
Joan Alabort-i-Medina, Epameinondas Antonakos, James Booth, Patrick Snape and Stefanos Zafeiriou, "Menpo: A comprehensive platform for parametric image alignment and visual deformable models", In Proceedings of the ACM International Conference on Multimedia, MM ’14, pages 679-682, New York, NY, USA, 2014. ACM.
</pre> [[Bibtex]({filename}/pages/paper/menpo.bib)] [[pdf]({filename}/pages/paper/Menpo_ACM_MM_2014.pdf)]
