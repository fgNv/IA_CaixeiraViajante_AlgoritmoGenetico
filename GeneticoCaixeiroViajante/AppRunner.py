activate_this = 'ENV_CBR/Scripts/activate_this.py'

import runpy
file_globals = runpy.run_path(activate_this)

from App.Model.Runner import run
from App.Web.ModelBuilder import buildModel
from App.Web.CustomEncoder import CustomEncoder
from flask import *

app = Flask(__name__)
app.debug = True

@app.route('/calculus', methods=['POST'])
def calculus():
	requestData = request.get_json()
	data = buildModel(requestData)
	result = run(data.graph, data.populationSize, data.mutationRate, data.iterationsQuantity)
	return Response(json.dumps(result, cls=CustomEncoder), mimetype='text/json') 

if __name__ == '__main__':
	app.run()