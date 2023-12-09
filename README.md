# Servidor Django x Crud FastAPI
## Django
```
docker-compose up -d --build
```

### Docker - Containers
```
attach shell
```

### Criando estrutura de pasta
```
mkdir django-produtos
cd django-produtos
```

### Criando uma venv
```
python -m venv ./venv
```

### Ativando o ambiente virtual
```
. venv/bin/activate (. substituirá o source)
```

### Desativando o ambiente virtual
```
deactivate
```

### Instalando o django com pip
```
pip install django
```

### Atualizar o gerenciador de pacotes
```
pip install --upgrade pip
```

### Validar a instalação do django
```
pip freeze
```

### Salvando as dependencias necessárias para o projeto funcionar
```
pip freeze > requirements.txt
```

### Startproject cria um projeto, onde todas as configurações do projeto serão salvas
```
django-admin startproject setup .
```

#### Executar o servidor 
```
python manage.py runserver 0.0.0.0:8000
```

#### Alterando horário e idioma do projeto setting.py
```
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
```

### Parar aplicação
```
ctrl + c
```

### Criando um app
```
python manage.py startapp produto
```

#### Criando uma tabela no banco de dados em models.py
```
class Product inserida no arquivo models.py
```

#### Inserir o app produto na pasta setup no arquivo settings.py no campo installed_apps
```
'produto',
```

### Criar a migração dos modelos Django no banco de dados
```
python manage.py makemigrations
```

### Reconhecendo as migrações
```
python manage.py migrate
```

#### Executar o servidor
```
python manage.py runserver 0.0.0.0:8000
```

#### Admin
```
localhost:8000/admin
```

### Criando um user
```
python manage.py createsuperuser
```

### Usando os produtos que usamos no nosso modelo (models.py)
```
na pasta produto em admin.py, conseguimos registrar esses produtos para usar no admin. Para isso, basta inserir:
from produto.models import Product

admin.site.register(Product)
```


### Exibindo o titulo dos produtos usando str
```
basta adicionar uma função str ao models.py
```

### Extras
```
start container
attach shell
cd django-produtos
. venv/bin/activate
python manage.py runserver 0.0.0.0:8000
Acesso via localhost:8000
```

## FastAPI
```
mkdir fastapi-produtos
cd fastapi-produtos
python -m venv ./venv
. venv/bin/activate
pip freeze

pip install fastapi uvicorn
pip install --upgrade pip
pip freeze
pip freeze > requirements.txt
```

### Desenvolvimento da API no arquivo app.py
```
touch app.py
```

### Executar a aplicação
```
uvicorn app:app --host 0.0.0.0 --port 8080 --reload (cada alteração realizada, ele atualiza)
```

### Models - responsavel por manter a estrutura das nossas classes
```
product.py
```

### App.py import product
```
from models.product import Product
```

#### swagger
```
http://localhost:8080/docs
```