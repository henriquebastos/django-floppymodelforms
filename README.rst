=============================
django-floppymodelforms
=============================

.. image:: https://badge.fury.io/py/floppymodelforms.png
    :target: http://badge.fury.io/py/floppymodelforms

.. image:: https://travis-ci.org/henriquebastos/floppymodelforms.png?branch=master
        :target: https://travis-ci.org/henriquebastos/floppymodelforms

.. image:: https://pypip.in/d/floppymodelforms/badge.png
        :target: https://crate.io/packages/floppymodelforms?version=latest


A hack to force Django's ModelForm to use floppyforms' fields.


Installation
------------

Install the package::

    pip install django-floppymodelforms

Then use it in a project::

	import floppymodelforms


Usage
-----

To activate django-floppymodelforms in a project, add it to `INSTALLED_APPS`
after the `floppyforms` app.::

    INSTALLED_APPS = (
        # ...
        'floppyforms',
        'floppymodelforms',
    )


Features
--------

* Add support for Django's extra form fields.


License
-------

BSD License
