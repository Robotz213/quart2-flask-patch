Unreleased
----------

* Support Quart 0.23.1 and its unified application/request/websocket context.
* Run the test matrix on Python 3.14, the project's minimum supported version.
* Use Greenback to await Quart operations from synchronous Flask-compatible accessors.

0.3.0 2023-11-19
----------------

* Bugfix use iscoroutinefunction from inspect (rather than Quart's).
* Support 3.12 drop 3.7.

0.2.0 2023-10-22
----------------

* Add click and request.values to patch.
* Support Quart 0.19 onwards.

0.1.0 2023-05-14
----------------

* Basic initial release.
