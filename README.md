# Para inicializar

## Pré-requisitos
- Python 3.8+
- MySQL
- Git

## Primeira Configuração
```bash
git clone https://github.com/jeff-lf/PI-Barbearia.git
cd PI-Barbearia
python -m venv venv
venv\Scripts\activate  # no Windows
pip install -r requirements.txt
->> Crie o .env e prrencha as credenciais
```


## SEMPRE ANTES DE INICIALIZAR

```bash
git pull origin main
python manage.py migrate
python manage.py runserver
```