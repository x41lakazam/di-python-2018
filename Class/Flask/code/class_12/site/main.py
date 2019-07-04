from blog import app, models, db

@app.shell_context_processor
def shell_vars():
	vars = {
			'app':app,
			'models':models,
			'db':db
			}
	return vars

app.run(port=5000)
