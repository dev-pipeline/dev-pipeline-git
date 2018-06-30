dev-pipeline-git
================
|codacy|
|code-climate|

A git_ plugin for `dev-pipeline`_


Installation
------------
The simplest way to install is using pip_.

.. code:: bash

    $ cd /path/to/dev-pipeline-git
    $ pip3 install

If you don't have pip available, you can run :code:`setup.py` directly.

.. code:: bash

    $ cd /path/to/dev-pipeline-git
    $ python3 setup.py install

You'll need git installed.  Doing that is beyond the scope of this document,
but it should be available for pretty much every operating system.


Using
-----
You can use :code:`git` as an option for :code:`scm` in a :code:`build.config`.
Information about options you can set are in the documentation_.


.. |codacy| image:: https://api.codacy.com/project/badge/Grade/b2b62cb231324e34b257993e01069df7
    :target: https://www.codacy.com/app/snewell/dev-pipeline-git?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=dev-pipeline/dev-pipeline-git&amp;utm_campaign=Badge_Grade

.. |code-climate| image:: https://api.codeclimate.com/v1/badges/2964d5af32e85e382e98/maintainability
   :target: https://codeclimate.com/github/dev-pipeline/dev-pipeline-git/maintainability
   :alt: Maintainability

.. _dev-pipeline: https://github.com/dev-pipeline/dev-pipeline
.. _documentation: docs/scm-git.rst
.. _git: https://git-scm.com
.. _pip: https://pypi.python.org/pypi/pip
