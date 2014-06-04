"""Mock Workflow Server.

Delivers dummy JSON for workflows that it reads from workflows.json
"""

from __future__ import with_statement

import os

try:
    import json
except ImportError:
    import simplejson as json

from flask import Flask, abort

app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello():
    return ('<h1>Welcome to the workflow server</h1>'
            '<p>'
            '<a href="workflows/">List workflows</a>'
            '</p>'
    )

@app.route('/workflows/', methods=['GET'])
def list_workflows():
    """Return a list of existing workflows."""
    global workflows
    return (
        json.dumps(workflows.keys()),
        200,
        {'Content-Type': "application/json"}
    )


@app.route('/workflows/<identifier>', methods=['GET'])
def get_workflow(identifier):
    """Get and return the requested workflow."""
    global workflows
    try:
        wf = workflows[identifier]
    except KeyError:
        abort(404)
    else:
        # Replace URL with values from environment
        for i, wf_item in enumerate(wf['wf']):
            wf['wf'][i] = update_url(wf_item)
        return (
            json.dumps(wf),
            200,
            {'Content-Type': "application/json"}
        )


@app.route('/workflows/<identifier>/<int:step>', methods=['GET'])
def get_workflow_step(identifier, step):
    """Get and return the requested workflow step."""
    global workflows
    try:
        wf_item = workflows[identifier]['wf'][step]
    except (KeyError, IndexError):
        abort(404)
    else:
        # Replace URL with values from environment
        wf_item = update_url(wf_item)
        return (
            json.dumps(wf_item),
            200,
            {'Content-Type': "application/json"}
        )


def update_url(wf_item):
    """Update URL for a workflow step and return the step."""
    global COMPONENT_HOST, COMPONENT_PORT
    if COMPONENT_HOST is not None:
        if COMPONENT_PORT is not None:
            wf_item['url'] = wf_item['url'].replace(
                '://127.0.0.1',
                '://{0}:{1}'.format(COMPONENT_HOST, COMPONENT_PORT)
            )
        else:
            wf_item['url'] = wf_item['url'].replace(
                '://127.0.0.1',
                '://{0}'.format(COMPONENT_HOST)
            )
    if COMPONENT_PORT is not None:
        wf_item['url'] = wf_item['url'].replace(
                '://127.0.0.1',
                '://127.0.0.1:{0}'.format(COMPONENT_PORT)
            )
    return wf_item


# Load dummy workflows from json
with open('workflows.json') as fh:
    workflow_list = json.load(fh)

workflows = {wf['id']: wf for wf in workflow_list}


app.debug = False

COMPONENT_HOST = os.environ.get('PLANK_HOST')
COMPONENT_PORT = os.environ.get('PLANK_PORT')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
