from flaskimpressionador import app, database

with app.app_context():
    database.drop_all()
    database.create_all()
    print("Banco de dados criado com sucesso!")
