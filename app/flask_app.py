from app.factories.application import setup_app

app = setup_app()

if __name__ == '__main__':
    app.run(debug=True)
