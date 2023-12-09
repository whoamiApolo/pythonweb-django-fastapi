# Módulo Introdutório > Desenvolvimento Backend > Aula 2


## Rodando a API Produtos utilizando o framework Django

Acessar o diretório fastapi-produtos

```
cd /referencial/src/django-produtos
```

Criar o ambiente virtual

```
python -m venv ./venv
```

Para ativar o ambiente virtual

```
source venv/bin/activate
```

Instalar o Django

```
pip install django
```

Criar um arquivo txt com as dependências do projeto

```
pip freeze > requirements.txt
```

Para executar o servidor Django

```
python manage.py runserver 0.0.0.0:8000
```

Para criar um app no Django

```
python  manage.py startapp produto
```

Criar a migração dos modelos Django no banco de dados

```
python manage.py makemigrations
```

```
python manage.py migrate
```

Criar um super usuário para o Django Admin

```
python manage.py createsuperuser
```

## Rodando a API Produtos utilizando o framework FastAPI

Acessar o diretório fastapi-produtos

```
cd /referencial/src/fastapi-produtos
```

Para instalar os pacotes necessários para rodar o servidor FastAPI

```
pip install fastapi uvicorn
```

Para executar o servidor FastAPI

```
uvicorn app:app --host 0.0.0.0 --port 8080 --reload
```





# Subir ambiente de desenvolvimento
## Django
docker-compose up -d --build

### Docker - Containers
attach shell

### criando estrutura de pasta
mkdir django-produtos
cd django-produtos

### criando uma venv
python -m venv ./venv

### ativando o ambiente virtual
. venv/bin/activate (. substituirá o source)

### desativando o ambiente virtual
deactivate

### instalando o django com pip
pip install django

### atualizar o gerenciador de pacotes
pip install --upgrade pip

### validar a instalação do django
pip freeze

### salvando as dependencias necessárias para o projeto funcionar
pip freeze > requirements.txt

### startproject cria um projeto, onde todas as configurações do projeto estarão
django-admin startproject setup .

#### manage.py subir o servidor 
python manage.py runserver 0.0.0.0:8000

#### alterando horário e idioma do projeto setting.py
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'

### parar aplicação
ctrl + c

### Criando um app
python manage.py startapp produto

#### criando uma tabela no banco de dados em models.py
class Product inserida no arquivo models.py

#### inserir o app produto na pasta setup no arquivo settings.py no campo installed_apps
'produto',

### criar a migração dos modelos Django no banco de dados
python manage.py makemigrations

### para as migrações serem reconhecidas
python manage.py migrate

#### manage.py subir o servidor novamente
python manage.py runserver 0.0.0.0:8000

#### acessar admin
localhost:8000/admin

### criando um user para acessar
python manage.py createsuperuser

### usando os produtos que usamos no nosso modelo (models.py)
na pasta produto em admin.py, conseguimos registrar esses produtos para usar no admin. Para isso, basta inserir:
from produto.models import Product

admin.site.register(Product)

### exibindo o titulo dos produtos usando str
basta adicionar uma função str ao models.py


# Extras
start container
attach shell
cd django-produtos
. venv/bin/activate
python manage.py runserver 0.0.0.0:8000
Acesso via localhost:8000

## FastAPI
mkdir fastapi-produtos
cd fastapi-produtos
python -m venv ./venv
. venv/bin/activate
pip freeze

pip install fastapi uvicorn
pip install --upgrade pip
pip freeze
pip freeze > requirements.txt

### desenvolvimento da API no arquivo app.py
touch app.py

### executar a aplicação
uvicorn app:app --host 0.0.0.0 --port 8080 --reload (cada alteração realizada, ele atualiza)

### models - responsavel por manter a estrutura das nossas classes
product.py

### app.py import product

#### swagger
http://localhost:8080/docs