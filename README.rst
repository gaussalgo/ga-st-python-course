
ga-st-python-course
===================

Install requirements:

.. code-block:: shell

    pip install -U pip setuptools wheel
    pip install -r requirements.txt -r requirements-dev.txt


Rebuild requirements:

.. code-block:: shell

    pip install -U pip setuptools wheel pip-tools
    make requirements


Check *.py sources & run tests

.. code-block:: shell

    make
