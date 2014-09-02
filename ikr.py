import dataset
from bottle import route, run, post, request, redirect
from bottle import jinja2_view as view

db = dataset.connect('sqlite:///ikr.db')
table = db['ikr']

@route("/<list_name>")
@route("/")
@view('index')
def index(list_name='default'):
    return {
        'list': sorted(table.find(list_name=list_name),
                       key=lambda x: x['votes'],
                       reverse=True),
        'list_name': list_name,
    }

@post("/")
def go_to_list(list_name=None):
    if not list_name:
        list_name = request.forms['list_name']
    return redirect("/" + list_name)

@post("/<list_name>/add")
def add(list_name):
    table.insert(dict(list_name=list_name, name=request.forms['item'], votes=0))
    return go_to_list(list_name)

@route("/<list_name>/<action:re:(up|down)vote>/<id>")
def vote(list_name, action, id):
    row = table.find_one(list_name=list_name, id=id)
    row['votes'] += 1 if action == 'upvote' else -1
    table.update(row, ['id'])
    return go_to_list(list_name)


run(reloader=True, debug=True)
