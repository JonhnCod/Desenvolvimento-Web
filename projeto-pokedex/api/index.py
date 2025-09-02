# api/index.py
# Este arquivo serve como a porta de entrada para a Vercel.

# Importamos a variável 'app' do seu pacote 'app' (do __init__.py)
from app import app

# A Vercel vai procurar por uma variável chamada 'app' neste arquivo.
# Não é necessário usar app.run() aqui.