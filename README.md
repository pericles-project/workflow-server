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

      sudo brew install python # if not already installed

- [pip](http://pip.readthedocs.org/)

  Debian:

      sudo apt-get install python-pip

  RedHat:

      sudo yum install python-pip

  OSX:

      sudo easy_install pip


## Install

I recommend that you use [virtualenv](http://virtualenv.readthedocs.org/) to
isolate your development environment from system [Python](https://python.org)
and any packages that may be installed there.

    mkdir ~/venvs
    virtualenv ~/venvs/pericles
    source ~/venvs/pericles/bin/activate
    pip install -r requirements.txt

Run
---

    PLANK_HOST=localhost PLANK_PORT=7000python mock_workflow_server.py
