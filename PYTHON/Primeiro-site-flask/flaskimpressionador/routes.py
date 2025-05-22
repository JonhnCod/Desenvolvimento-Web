from flask import render_template,flash,redirect,url_for,request
from flaskimpressionador import app, database,bcrypt
from flaskimpressionador.forms import LoginForm, RegisterForm, FormEditprofile, FormPost
from flaskimpressionador.models import Usuario, Post
from flask_login import login_user, logout_user,current_user,login_required
import secrets
import os
from PIL import Image




# ---------------------------------- PÁGINA HOME ------------------------------------------

@app.route('/')
@login_required
def home():
    posts = Post.query.order_by(Post.id.desc()).all()
    return render_template('paginas/home.html', posts=posts)



# ---------------------------------- PÁGINA LOGIN ------------------------------------------

@app.route('/login',methods=['GET','POST'])
def login():
    form_login = LoginForm()
    if form_login.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.password.data):
            login_user(usuario,remember=form_login.remember_me.data)
            flash(f'sucesso Login: {form_login.email.data}', 'alert-success')
            par_next = request.args.get('next')
            if par_next:
                return redirect(par_next)
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Falha Login: email Não existe ou senha incorreta', 'alert-danger')


    return render_template('paginas/login.html',form_login=form_login)


# ---------------------------------- PÁGINA CADASTRO ------------------------------------------


@app.route('/cadastro',methods=['GET','POST'])
def cadastro():
    form_cadastro = RegisterForm()
    if form_cadastro.validate_on_submit():
        senha_cript = bcrypt.generate_password_hash(form_cadastro.senha.data)
        usuario = Usuario(username=form_cadastro.username.data,email=form_cadastro.email.data,senha=senha_cript)
        database.session.add(usuario)
        database.session.commit()
        flash(f'Cadastrado: {form_cadastro.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('paginas/cadastro.html',form_cadastro=form_cadastro)


# ---------------------------------- PÁGINA usuarios ------------------------------------------

@app.route('/usuarios')
@login_required
def usuarios():
    lista = Usuario.query.all()
    return render_template('paginas/usuario.html',lista=lista)


# ---------------------------------- PÁGINA SAIR ------------------------------------------

@app.route('/sair')
@login_required
def sair():
    logout_user()
    return redirect(url_for('home'))


# ---------------------------------- PÁGINA PERFIL ------------------------------------------

@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename='imageprofile/{}'.format(current_user.foto_perfil))
    return render_template('paginas/perfil.html',foto_perfil=foto_perfil)


# ---------------------------------- PÁGINA EDITAR PERFIL ------------------------------------------

@app.route('/perfil/editar', methods=['GET','POST'])
@login_required
def editar_perfil():
    form_perfil = FormEditprofile()
    if form_perfil.validate_on_submit():
        current_user.username = form_perfil.username.data
        current_user.email = form_perfil.email.data
        if form_perfil.foto_perfil.data:
            nome_image = salvar_imagem(form_perfil.foto_perfil.data)
            current_user.foto_perfil = nome_image
        current_user.cursos = atualizar_cursos(form_perfil)
        database.session.commit()
        flash(f'Perfil editado: {form_perfil.username.data}', 'alert-success')
        return redirect(url_for('perfil'))
    elif request.method == 'GET':
        form_perfil.username.data = current_user.username
        form_perfil.email.data = current_user.email
    foto_perfil = url_for('static', filename='imageprofile/{}'.format(current_user.foto_perfil))
    return render_template('paginas/editarperfil.html' ,foto_perfil=foto_perfil,form_perfil=form_perfil)


# ---------------------------------- PÁGINA CRIAR POST ------------------------------------------

@app.route('/post/criar',methods=['GET','POST'])
@login_required
def criar_post():
    post_form = FormPost()
    if post_form.validate_on_submit():
        post = Post(titulo=post_form.titulo.data,corpo=post_form.corpo.data,autor_post=current_user)
        database.session.add(post)
        database.session.commit()
        flash('post criado com sucesso', 'alert-success')
        return redirect(url_for('home'))
    return render_template('paginas/criarpost.html',post_form=post_form)



# ---------------------------------- PÁGINA CADA POST ------------------------------------------

@app.route('/post/<post_id>',methods=['GET','POST'])
@login_required
def exibir_post(post_id):
    post = Post.query.get(post_id)
    if current_user == post.autor_post:
        form = FormPost()
        if request.method == 'GET':
            form.titulo.data = post.titulo
            form.corpo.data = post.corpo
        elif form.validate_on_submit():
            post.titulo = form.titulo.data
            post.corpo = form.corpo.data
            database.session.commit()
            flash('post editado com sucesso', 'alert-success')
            return redirect(url_for('home'))
    else:
        form = None

    return render_template('paginas/post.html', post=post, form=form)


# ------------- Funções -----------------------------

def salvar_imagem(foto_perfil):
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(foto_perfil.filename)
    nome_arquivo = nome  + codigo + extensao
    caminho_salvar = os.path.join(app.root_path, 'static/imageprofile', nome_arquivo)
    tamanho = (400,400)
    foto_reduz = Image.open(foto_perfil)
    foto_reduz.thumbnail(tamanho)
    foto_reduz.save(caminho_salvar)
    return nome_arquivo


def atualizar_cursos(form_perfil):
    lista_cursos = []
    for campo in form_perfil:
        if 'curso_' in campo.name:
            if campo.data:
                lista_cursos.append(campo.label.text)
    return ";".join(lista_cursos)


