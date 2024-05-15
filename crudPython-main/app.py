from flask import Flask, render_template, request, redirect, url_for, flash
import galaxias_BD

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'img'


#rota para capa.html template principal
@app.route('/')
@app.route('/capa.html')
def capa():
    return render_template('capa.html')



#rota para index.html
@app.route('/index.html')
def home():
    galaxias = galaxias_BD.listar_galaxias()
    return render_template('index.html', dados=galaxias)

@app.route('/galeria')
def galeria():
    return render_template('galeria.html')

#rota para o video
@app.route('/video')
def video():
    return render_template('video.html')

@app.route('/sobreNos')
def sobreNos():
    return render_template('sobreNos.html')

@app.route('/sobre')
def sobre():
    
    return render_template('sobre.html')

 
@app.route('/cadastrar')
def criar():
    return render_template("cadastrar.html")

@app.route('/criar', methods=['POST'])
def criar_galaxia():
    nome = request.form['nome']
    estrelaPrincipal = request.form['estrela']
    distancia = request.form['distancia']
    imagem = request.form['imagem']

    galaxias_BD.inserir_galaxia(nome, estrelaPrincipal, distancia, imagem)
   
    return redirect(url_for('home'))

@app.route('/deletar/<int:id>', methods=['POST'])
def deletar_galaxia_route(id):
    galaxias_BD.deletar_galaxia(id)
    return redirect(url_for('home'))

@app.route('/editar/<int:id>', methods=['GET'])
def editar(id):
    galaxia = galaxias_BD.retornar_galaxia(id)
    if galaxia:
        return render_template('editar.html', id=id, galaxia=galaxia)
    return redirect(url_for('home'))

@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    if request.method == 'POST':
        nome = request.form['nome']
        estrelaPrincipal = request.form['estrela']
        distancia = request.form['distancia']
        imagem = request.form['imagem']
        
        if galaxias_BD.retornar_galaxia(id):
            galaxias_BD.atualizar_galaxia(id, nome, estrelaPrincipal, distancia, imagem)
            return redirect(url_for('home'))
        else:
            return 'Galáxia não encontrada!', 404

@app.route('/contato', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        mensagem = request.form['mensagem']

        # Enviar informações para o e-mail desejado
        # Aqui você pode implementar o envio de e-mail usando bibliotecas como smtplib
        return redirect(url_for('home'))
        return 'Mensagem enviada com sucesso!'
    return render_template('contato.html')

if __name__ == '__main__':
    galaxias_BD.criar_tabela()
    app.run(debug=True)



