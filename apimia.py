from flask import Flask, request
from flask import jsonify


# Importamos nuestros módulos de funciones
import tools.get as get 
import tools.post as pos

app = Flask(__name__)


# Comprobamos que funciona 

@app.route("/hola")
def mundo():
    return "hola mundo"

# 1. ENDPOINTS GET


# Endpoint para obtener todos los usuarios + id

@app.route("/users")
def users():
    users = get.get_usu()
    return jsonify(users)


# Endpoint para obtener todos los grupos + id


@app.route("/groups")
def groups():
    group = get.get_group()
    return jsonify(group)

# Endpoint para obtener todos los mensajes de un grupo

@app.route("/message_gr/<gr_id>")
def groups_message(gr_id):
    group_men = get.get_men_gr_id(gr_id)
    return jsonify(group_men)



# Endpoint para que use el usuario sino sabe el id de un grupo, pero si su nombre
# LO SIENTO USUARIO PERO ESTE ENDPOINT AUN NO SE PUEDE EJECUTAR. POR ELLO SI QUIERE SABER EL ID A PARTIR DEL NOMBRE DEBE ACUDIR AL JUPYTER NOTEBOOH GET_ID.
# SIENTO LAS MOLESTIAS

@app.route("/gr_id/<gr_name>")
def gr_id_nombre(gr_name):
    id_nameg = get.get_id_from_grname(gr_name)
    return jsonify(id_nameg)



# Endpoint para obtener todos los mensajes de un usuario

@app.route("/message_usu/<usu_id>")
def usu_message(usu_id):
    usu_men = get.get_men_usu_id(usu_id)
    return jsonify(usu_men)

# Endpoint para que use el usuario sino si si su nombre
# LO SIENTO USUARIO PERO ESTE ENDPOINT AUN NO SE PUEDE EJECUTAR. POR ELLO SI QUIERE SABER EL ID A PARTIR DEL NOMBRE DEBE ACUDIR AL JUPYTER NOTEBOOH GET_ID.
# SIENTO LAS MOLESTIAS

@app.route("/usu_id/<usu_name>")
def gr_id_nombre(usu_name):
    id_nameu = get.get_id_from_usuname(usu_name)
    return jsonify(id_nameu)

# Endpoint para obtener el id del último usuario registrado
# LO SIENTO USUARIO PERO ESTE ENDPOINT AUN NO SE PUEDE EJECUTAR. POR ELLO SI QUIERE SABER EL ID A PARTIR DEL NOMBRE DEBE ACUDIR AL JUPYTER NOTEBOOH GET_ID.
# SIENTO LAS MOLESTIAS

@app.route("/usu_last_id")
def last_id_usu():
    last_id_usu = get.get_lastid_usu()
    return jsonify(last_id_usu)



# Endpoint para obtener el id del último grupp registrado
# LO SIENTO USUARIO PERO ESTE ENDPOINT AUN NO SE PUEDE EJECUTAR. POR ELLO SI QUIERE SABER EL ID A PARTIR DEL NOMBRE DEBE ACUDIR AL JUPYTER NOTEBOOH GET_ID.
# SIENTO LAS MOLESTIAS

@app.route("/gr_last_id")
def last_id_gr():
    last_id_gr = get.get_lastid_group()
    return jsonify(last_id_gr)




# 2. ENPOINTS POST 

# Enpoint para meter mensaje 


@app.route("/insert_message", methods=["POST"])
def insert_message():
    message = request.form.get("texto")
    group = request.form.get("gr_id")
    user = request.form.get("usu_id")
    pos.text_gr_usu(message, group, user)
    return "Mensaje se ha introducido"


# Endpoint para crear usuario 

@app.route("/insert_user", methods=["POST"])
def insert_user():
    name = request.form.get("usu_name")
    pos.create_user(name)
    return "User has been correctly created"


# Endpoint para crear un grupo

@app.route("/insert_group", methods=["POST"])
def insert_group():
    grupo = request.form.get("gr_name")
    pos.create_group(grupo)
    return "El grupo se ha creado"


# Endpoint para meter un usuario en un chat

@app.route("/usu_in_group", methods=["POST"])
def insert_usu_in_group():
    grupo = request.form.get("gr_id")
    user = request.form.get("usu_id")
    
    pos.create_conexion(grupo, user)
    return "Se ha creado la conexión usuario, grupo"




app.run()