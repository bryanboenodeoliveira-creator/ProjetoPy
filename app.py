from flask import Flask, render_template, request, redirect
from db import get_connection

app = Flask(__name__)

# ==========================
# PÁGINA LOGIN
# ==========================

@app.route("/")
def login_page():
    return render_template("login.html")


# ==========================
# LOGIN
# ==========================

@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    senha = request.form["password"]

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    sql = "SELECT * FROM usuarios WHERE email=%s AND senha=%s"
    cursor.execute(sql, (email, senha))

    usuario = cursor.fetchone()

    cursor.close()
    conexao.close()

    if usuario:
        return "Login realizado com sucesso!"
    else:
        return "Email ou senha incorretos"


# ==========================
# TELA CADASTRO USUÁRIO
# ==========================

@app.route("/cadastro_usuario")
def cadastro_usuario():
    return render_template("cadastro-usuario.html")


# ==========================
# SALVAR USUÁRIO
# ==========================

@app.route("/salvar_usuario", methods=["POST"])
def salvar_usuario():

    nome = request.form["nome"]
    email = request.form["email"]
    cpf = request.form["cpf"]
    senha = request.form["senha"]
    telefone = request.form["telefone"]
    genero = request.form["genero"]

    conexao = get_connection()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO usuarios
    (nome,email,cpf,senha,telefone,genero)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    valores = (nome,email,cpf,senha,telefone,genero)

    cursor.execute(sql,valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/")


# ==========================
# TELA CADASTRO EMPRESA
# ==========================

@app.route("/cadastro_empresa")
def cadastro_empresa():
    return render_template("cadastro-empresa.html")


# ==========================
# SALVAR EMPRESA
# ==========================

@app.route("/salvar_empresa", methods=["POST"])
def salvar_empresa():

    nome_empresa = request.form["nome_empresa"]
    email = request.form["email"]
    senha = request.form["senha"]
    telefone = request.form["telefone"]
    numero_registro = request.form["numero_registro"]
    id_empresa = request.form["id_empresa"]

    conexao = get_connection()
    cursor = conexao.cursor()

    sql = """
    INSERT INTO empresas
    (nome_empresa,email,senha,telefone,numero_registro,id_empresa)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    valores = (nome_empresa,email,senha,telefone,numero_registro,id_empresa)

    cursor.execute(sql,valores)
    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect("/")


# ==========================

app.run(debug=True)