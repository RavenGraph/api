from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo1': {'task': 'Make Database Logic'},
    'todo2': {'task': 'Send To API'},
    'todo3': {'task': 'Make Front End'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task')


# Todo
# shows a single todo item and lets you delete a todo item
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201



class TodoList(Resource):
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return TODOS[todo_id], 201

#class RetrieveTableData(Resource):
    #def get(self):
        #var GetMainAssetAndCreatedVariable = query for main assets and associated nodes
        #return GetMainAssetAndCreatedVariable 
        #Example MATCH (p:AssetName { name:"BTC" }) - and get associated addresses
        #RETURN p
    
    #def get(self)
        #var GetCountNumberOfAssocatedNodes = query for how many of a single asset are in circulation
        #return GetCountNumberOfAssocatedNodes

    #def get(self)
    #var NumberOfTransaction = get the number of transactions associateed with a unique asset
    #return NumberOfTransaction


api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<todo_id>')

#api.add_resource(RetrieveTableData, '/Info')


if __name__ == '__main__':
    app.run(debug=True)
