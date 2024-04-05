# Exercícios de Docker

_**EX1.**
Construa uma imagem a partir de um arquivo de instruções (Dockerfile) que execute o código carguru.py. Após, execute um container a partir da imagem criada._

_Registre aqui o conteúdo de seu arquivo Dockerfile e o comando utilizado para execução do container._

_**Resposta:**_

```python
# No Dockerfile foi colocado as seguintes instruções para a execução do código carguru.py:

FROM python

WORKDIR /app

COPY app/carguru.py .

CMD ["python", "carguru.py"]

# Com relação ao comandos (utilizados no Terminal) foram:

docker build -t carguru-image . # usado para iniciar uma imagem com base nas instruções do Dockerfile, onde a tag -t é usada para já nomearmos a imagem

docker run carguru-image # permite a execução do código python carguru.py
```

Abaixo é possível visualizar as saidas alcançadas no próprio programa Docker e pelo Visual Studio Code:

<div align="center">

![Output Docker](<../Images Sprint4/Output Docker.png>)

![Output VSC](<../Images Sprint4/Output VSC.png>)

</div>

&nbsp;

_**EX2.**
É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta._

_**Resposta:**_

```python
No Docker, é possível reutilizar containers que foram parados anteriormente, desde que esses containers não tenham sido removidos ( --rm ). Containers parados ainda existem no sistema Docker, e você pode reiniciá-los usando o comando docker start <container_id>.
```

&nbsp;

_**EX3.**
Agora vamos exercitar a criação de um container que permita receber inputs durante sua execução. Seguem as instruções._

**-- Criar novo script Python que implementa o algoritmo a seguir:**

**1 - Receber uma string via input**

**2 - Gerar o hash  da string por meio do algoritmo SHA-1**

**3 - Imprimir o hash em tela, utilizando o método hexdigest**

**4 - Retornar ao passo 1**

**-- Criar uma imagem Docker chamada mascarar-dados que execute o script Python criado anteriormente**

**--  Iniciar um container a partir da imagem, enviando algumas palavras para mascaramento**

**-- Registrar o conteúdo do script Python, arquivo Dockerfile e comando de inicialização do container neste espaço.**

_**Resposta:**_

```python
# O conteúdo do script de Python (hash_generator.py ) segue abaixo:

import hashlib

while True:
    input_string = input("Digite uma string (ou 'exit' para sair): ")
    
    if input_string.lower() == 'exit':
        break

    sha1_hash = hashlib.sha1(input_string.encode()).hexdigest()
    print("Hash SHA-1 da string:", sha1_hash)

# No Dockerfile foi colocado as seguintes instruções para a execução do código hash_generator.py:

FROM python

WORKDIR /app

COPY app/hash_generator.py .

CMD ["python", "hash_generator.py"]

# Com relação ao comandos (utilizados no Terminal) foram utilizados:

docker build -t mascarar-dados . # usado para iniciar uma imagem com base nas instruções do Dockerfile, onde a tag -t é usada para já nomearmos a imagem

docker run -it mascarar-dados # para iniciar um container a partir da imagem "mascarar-dados" e enviar strings para mascaramento interativamente.
```

<div align="center">

![Output VSC3](<../Images Sprint4/Output VSC3.png>)

</div>

---