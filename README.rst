SQL schema registry
======================================

.. docincludebegin

sql_schema_registry process and records a deployment DDL code execution
The module is compatible with Python 3.5+ and released under the terms of the
`MIT license`.

Visit the project page at https://github.com/alex-liz/sql-schema-registry for
further information about this project.


Quick Start
-----------

.. code-block:: sh

   $ pip install sql_schema_registry

.. code-block:: python
    sql_schema_registry.deploy(schema_name, db_name, user_name, files_path, schema_restart, db_conn)


Parameters
-----------
schema_name
~~~~~~~~~~~~~~~~~~~~~~
Name of the schema to deploy. Same name as the folder where sql files are.

db_name
~~~~~~~~~~~~~~~~~~~~~~
Name of the database. Same name as the folder where schemas folders are.

user_name
~~~~~~~~~~~~~~~~~~~~~~

Name of the user (optional)

files_path
~~~~~~~~~~~~~~~~~~~~~~
Path to the schema folder

schema_restart
~~~~~~~~~~~~~~~~~~~~~~
Restart from scratch (optional)

db_conn
~~~~~~~~~~~~~~~~~~~~~~
Connection to database

Links
-----

Project page
   https://github.com/alex-liz/sql-schema-registry

Bug tracker
   https://github.com/alex-liz/sql-schema-registry/issues

Documentation
   WIP
