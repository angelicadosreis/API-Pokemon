# API-Pokemon
API Pokemon consumida em Python / Flask

Procedimentos para executar:


# 1. INSTALE O PYTHON EM SUA MÁQUINA

# Windows: 

Efetue download do Python e execute a instalação:

https://www.python.org/downloads/

Selecione "Add Python 3.X to PATH".

Digite no cmd:

`$ python --version`

`$ pip --version`

# Linux:

Digite no terminal:

`$ sudo apt-get install python3-pip`

`$ sudo apt-get update`

# Mac OS:

Digite no terminal:

`$ xcode-select --install`

`$ sudo easy_install pip`

`$ sudo pip install --upgrade pip`

`$ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"`

`$ brew install python3`



# 2. CRIE UM AMBIENTE VIRTUAL

# Windows:

No cmd, digite:

`$ pip install virtualenv`

`$ cd (caminho-para-diretório-onde-será-criado-ambiente-virtual)`
    
`$ python -m virtualenv (nomedoambientevirtual)`
    
`$ (caminho)\nomedoambientevirtual\Scripts\activate`

`(nomedoambientevirtual) $ python --version`

# Linux/Mac OS:

No terminal, digite:

`$ sudo pip install virtualenv`

`$ python3 -m virtualenv nomedoambientevirtual`
    
`$ cd nomedoambientevirtual`
    
`$ source bin/activate`

`(nomedoambientevirtual) $ python --version`



# 3. INSTALE AS BIBLIOTECAS

No cmd / terminal, digite:

`$ pip install -r requirements.txt`



# 4. CLONE O REPOSITÓRIO:

`$ git clone <https://github.com/angelicadosreis/API-Pokemon.git>`




# 5. ABRA O ARQUIVO APP.PY EM SUA IDE


Caso esteja utilizando VS Code, pode ser necessário realizar os seguintes passos:

View > Command Pallete > Python: Select interpreter

Selecione o interpretador: 
python 3.8.5 64-bit 
nomedoambientevirtual/bin/python

Se o interpretador acima não estiver disponível, acessar o arquivo {}settings.json vscode e altere o PATH indicado para Python:

Antes:
{
    "terminal.explorerKind": "external",
    "python.pythonPath": "/usr/bin/python2"
}


Depois:
{
    "terminal.explorerKind": "external",
    "python.pythonPath": "path to/nomedoambientevirtual/bin/python"
}



# 6. EXECUTE

Digite no terminal de sua IDE:

`$ source nomedoambientevirtual/bin/activate`
    
`$ cd (caminho-para-arquivo-app.py)`
    
`$ python app.py`

