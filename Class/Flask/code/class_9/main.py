from juices import app, db, models

@app.shell_context_processor
def my_shell_context():
    return {
        'app': app,
        'db': db,
        'models': models
    }

app.run(port=5000, debug=True)
