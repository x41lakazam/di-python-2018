from coffee import app, db, models, forms, routes

@app.shell_context_processor
def shell_context():
    vars = {'db': db,
            'models':models,
            'forms':forms,
            'routes':routes
           }

    return vars

if __name__ == "__main__":
    app.run(port=5000, debug=True)
