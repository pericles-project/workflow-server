mock-workflow-server
====================

A Dummy Workflow Server for PERICLES

## Dependencies

- [Python](https://python.org) 2.7

  Debian:

      sudo apt-get install python-dev

  RedHat:

      sudo yum install python-devel

  OSX:

      brew?

- [pip](http://pip.readthedocs.org/)

  Debian:

      sudo apt-get install python-pip

  RedHat:

      sudo yum install python-pip

  OSX:

      brew?


## Install

I recommend that you use [virtualenv](http://virtualenv.readthedocs.org/) to
isolate your development environment from system [Python](https://python.org)
and any packages that may be installed there.

    mkdir virtualenvs
    virtualenv ~/venvs/pericles
    source ~/venvs/pericles/bin/activate
    pip install -r requirements.txt

Run
---

    python mock_workflow_server.py
