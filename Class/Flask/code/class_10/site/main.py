from blog import app, models, db

@app.shell_context_processor
def make_shell_context():
	vars = {
			'app':app,
			'models':models,
			'db':db
			}
	return vars
	
app.run(port=5000)