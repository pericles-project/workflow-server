"""Mock Workflow Server.

Delivers dummy JSON for workflows that it reads from workflows.json
"""

from __future__ import with_statement

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
        return (
            json.dumps(workflows[identifier]),
            200,
            {'Content-Type': "application/json"}
        )
    except KeyError:
        abort(404)


@app.route('/workflows/<identifier>/<int:step>', methods=['GET'])
def get_workflow_step(identifier, step):
    """Get and return the requested workflow step."""
    global workflows
    try:
        return (
            json.dumps(workflows[identifier]['wf'][step]),
            200,
            {'Content-Type': "application/json"}
        )
    except (KeyError, IndexError):
        abort(404)


# Load dummy workflows from json
with open('workflows.json') as fh:
    workflow_list = json.load(fh)

workflows = {wf['id']: wf for wf in workflow_list}


app.debug = False


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
