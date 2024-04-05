# Seção 4: Exercícios Python II - 1/2

_**EX21.**
Implemente duas classes, Pato e Pardal , que herdam de uma superclasse chamada Passaro as habilidades de voar e emitir som. Contudo, tanto Pato quanto Pardal devem emitir sons diferentes (de maneira escrita) no console, conforme o modelo a seguir._

_Imprima no console exatamente assim:_

_**Pato\
Voando...\
Pato emitindo som...\
Quack Quack\
Pardal\
Voando...\
Pardal emitindo som...\
Piu Piu**_

**_Resposta_**

```python
class Passaro:
    def voar(self):
        print("Voando...")
    
    def emitir_som(self, som):
        print(f"Emitindo som...\n{som}")

class Pato(Passaro):
    def emitir_som(self):
        super().emitir_som("Quack Quack")

class Pardal(Passaro):
    def emitir_som(self):
        super().emitir_som("Piu Piu")

pato = Pato()
pato.voar()
pato.emitir_som()

pardal = Pardal()
pardal.voar()
pardal.emitir_som()
```

&nbsp;

_**EX22.**
Crie uma classe chamada Pessoa, com um atributo privado chamado nome (declarado internamente na classe como \_\_nome) e um atributo público de nome id._

_Adicione dois métodos à classe, sendo um para definir o valor de \_\_nome e outro para retornar o valor do respectivo atributo._

_Lembre-se que o acesso ao atributo privado deve ocorrer somente através dos métodos definidos, nunca diretamente.  Você pode alcançar este comportamento através do recurso de properties do Python._

_Veja um exemplo de como seu atributo privado pode ser lido e escrito:_

_**pessoa = Pessoa(0)\
pessoa.nome = 'Fulano De Tal'\
print(pessoa.nome)**_

**_Resposta_**

```python
class Pessoa:
    def __init__(self, identificacao):
        self.id = identificacao
        self.__nome = None

    def nome(self):
        return self.__nome
    
    def nome(self, novo_nome):
        self.__nome = novo_nome

pessoa = Pessoa(0)

pessoa.nome = 'Fulano De Tal'

print(pessoa.nome)
```

&nbsp;

_**EX23.**
Crie uma classe  Calculo  que contenha um método que aceita dois parâmetros, X e Y, e retorne a soma dos dois. Nessa mesma classe, implemente um método de subtração, que aceita dois parâmetros, X e Y, e retorne a subtração dos dois (resultados negativos são permitidos)._

_Utilize os valores abaixo para testar seu exercício:_

_**x = 4\
y = 5\
imprima:**_

_**Somando: 4+5 = 9\
Subtraindo: 4-5 = -1**_

**_Resposta_**

```python
class Calculo:
    def soma(self, x, y):
        return x + y

    def subtracao(self, x, y):
        return x - y

x = 4
y = 5

calculo = Calculo()

print(f"Somando: {x}+{y} = {calculo.soma(x, y)}")
print(f"Subtraindo: {x}-{y} = {calculo.subtracao(x, y)}")
```

&nbsp;

_**EX24.**
Crie uma classe Ordenadora que contenha um atributo listaBaguncada e que contenha os métodos ordenacaoCrescente e ordenacaoDecrescente._

_Instancie um objeto chamado crescente dessa classe Ordenadora que tenha como listaBaguncada a lista [3,4,2,1,5] e instancie um outro objeto, decrescente dessa mesma classe com uma outra listaBaguncada sendo [9,7,6,8]._

_Para o primeiro objeto citado, use o método ordenacaoCrescente e para o segundo objeto, use o método ordenacaoDecrescente._

_Imprima o resultado da ordenação crescente e da ordenação decresce_

**[1, 2, 3, 4, 5]\
[9, 8, 7, 6]**

**_Resposta_**

```python
class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada

    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)

    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse=True)

crescente = Ordenadora([3, 4, 2, 1, 5])

decrescente = Ordenadora([9, 7, 6, 8])

print(crescente.ordenacaoCrescente())
print(decrescente.ordenacaoDecrescente())
```

&nbsp;

_**EX25.**
Crie uma classe Avião que possua os atributos modelo, velocidade_maxima, cor e capacidade. Defina o atributo cor de sua classe , de maneira que todas as instâncias de sua classe avião sejam da cor “azul”._

_Após isso, a partir de entradas abaixo, instancie e armazene em uma lista 3 objetos da classe Avião. Ao final, itere pela lista imprimindo cada um dos objetos no seguinte formato:_

_**“O avião de modelo “x” possui uma velocidade máxima de “y”, capacidade para “z” passageiros e é da cor “w”.**_

_Sendo x, y, z e w cada um dos atributos da classe “Avião”._

_Valores de entrada:_

+ _**modelo BOIENG456: velocidade máxima 1500 km/h: capacidade para 400 passageiros: Cor Azul**_
+ _**modelo Embraer Praetor 600: velocidade máxima 863km/h: capacidade para 14 passageiros: Cor Azul**_
+ _**modelo Antonov An-2: velocidade máxima de 258 Km/h: capacidade para 12 passageiros: Cor Azul**_

**_Resposta_**

```python
class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.capacidade = capacidade
        self.cor = "Azul"

entradas = [
    ("modelo BOIENG456", "velocidade máxima 1500 km/h", "capacidade para 400 passageiros"),
    ("modelo Embraer Praetor 600", "velocidade máxima 863 km/h", "capacidade para 14 passageiros"),
    ("modelo Antonov An-2", "velocidade máxima de 258 Km/h", "capacidade para 12 passageiros")
]
avioes = []

for entrada in entradas:
    modelo, velocidade, capacidade = entrada
    aviao = Aviao(modelo, velocidade, capacidade)
    avioes.append(aviao)

for aviao in avioes:
    print(f"O avião de {aviao.modelo} possui uma velocidade máxima de {aviao.velocidade_maxima},"
          f" capacidade para {aviao.capacidade} e é da cor {aviao.cor}.")
```

---