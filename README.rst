pretalx view as raw table plugin
==========================

This is a plugin for `pretalx`_.

Current State
-------------

WIP -
a baisc static table version can be found in the `static_table branch`_
a first idea skeleton for a api-javascript based version can be found in the `API_version branch`_


Development setup
-----------------

1. Make sure that you have a working `pretalx development setup`_.

2. Clone this repository, eg to ``local/pretalx-view_as_raw_table``.

3. Activate the virtual environment you use for pretalx development.

4. Execute ``python setup.py develop`` within this directory to register this application with pretalx's plugin registry.

5. Execute ``make`` within this directory to compile translations.

6. Restart your local pretalx server. You can now use the plugin from this repository for your events by enabling it in
   the 'plugins' tab in the settings.


License
-------

Copyright 2019 Stefan Krüger

Released under the terms of the Apache License 2.0


.. _static_table branch: /s-light/pretalx-view_as_raw_table/blob/static_table/
.. _API_version branch: /s-light/pretalx-view_as_raw_table/blob/API_version/
.. _pretalx: https://github.com/pretalx/pretalx
.. _pretalx development setup: https://docs.pretalx.org/en/latest/developer/setup.html
