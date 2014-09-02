import dataset
from bottle import route, run, post, request, redirect, static_file
from bottle import jinja2_view as view

db = dataset.connect('sqlite:///ikr.db')
table = db['ikr']

HIDE_THRES = -10

@route('/<file:re:ikr\.(js|css)>')
def server_static(file):
    return static_file(file, root=".")

@route("/<list_name>")
@route("/")
@view('ikr')
def index(list_name='default'):
    hide_thres = int(request.params.get('hide_thres', HIDE_THRES))

    list = table.find(list_name=list_name)
    list = sorted(list, key=lambda x: x['votes'], reverse=True)
    list = [x for x in list if x['votes'] > hide_thres]

    return {
        'list': list,
        'list_name': list_name,
    }

@post("/")
def go_to_list(list_name=None):
    if not list_name:
        list_name = request.forms['list_name']
    return redirect("/" + list_name)

@post("/<list_name>/add")
def add(list_name):
    row = dict(list_name=list_name, name=request.forms['item'], votes=0)

    row['id'] = table.insert(row)

    if request.params.get('format', '') == 'json':
        return dict(row)
    else:
        return go_to_list(list_name)

@route("/<list_name>/<action:re:(up|down)vote>/<id>")
def vote(list_name, action, id):
    row = table.find_one(list_name=list_name, id=id)
    row['votes'] += 1 if action == 'upvote' else -1
    table.update(row, ['id'])
    if request.params.get('format', '') == 'json':
        return dict(row)
    else:
        return go_to_list(list_name)


run(reloader=True, debug=True)
