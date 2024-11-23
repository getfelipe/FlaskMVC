
# CRUD MVC em FLASK DASH 

Aplicação CRUD de Filmes em python implementada usando o modelo MVC ( Model - View - Controller), permitindo que o usuario possa adicionar, alterar, visualizar e deletar filmes ao banco de dados com os campos titulo, duracao, diretor, avaliação, genero.




## Features
  CRUD
- Criar (Adicionar filme - titulo, duracao, diretor, avaliação, genero)
- Atualizar (Alterar informações do Filme)
- Ler (Vizualizar os filmes)
- Deletar (Deletar os filmes)


## Tech Stack

**Cliente:** Navegador Web Local
**Servidor:** Flask

**IDE:** Visual Studio Code
**SGBD:** SQLite

**Linguagem de Programação:** Python 3.12


## 🛠Instalação

### Instalar as bibiotecas com o gerenciador de pacotes PIP

### Bibliotecas usadas :
```bash
 pip install
      Flask==3.0.3
      dash==2.18.2
      pandas==2.2.3
      dash-bootstrap-components==1.6.0
```


### Fazer o dowload da aplicação / codigo com o comando :
 ```bash
  git clone https://github.com/getfelipe/FlaskMVC.git 
```
### Indicar o caminho do banco de dados no arquivo model.py , atualizando a seguinte variavel :
 ```bash
 #model.py/

  file_path_db = 'Coloque aqui o caminho da base de dados filmes.db'
```
### Digitar o comando no terminal 
 ```bash
  python app.py
```
### Acessar o seguinte endereço para visualizar a aplicação :
 ```bash
 http://127.0.0.1:8050/
```



### Para ver a tabela atualizada , basta apertar o botão de "VISUALIZAR FILME" conforme imagem abaixo:

![App Screenshot](https://i.ibb.co/L6dKj4c/Screenshot-from-2024-11-22-21-22-24.png)

### Como resultado do acesso, aparecerá uma tabela semelhante  a esta: 

![App Screenshot](https://i.ibb.co/rbBQfm4/Screenshot-from-2024-11-22-21-39-48.png)

## Authors

- [@Felipe Machado](https://github.com/getfelipe)
- [@ Flavio S F](https://github.com/flavionesz)
