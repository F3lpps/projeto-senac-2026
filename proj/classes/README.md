# Lista de Exercícios: Classes e Objetos em Python

Esta lista contém 15 exercícios ordenados para guiar o aprendizado desde a estrutura mais básica de uma classe até a criação de sistemas e interações mais complexas entre múltiplos objetos.

---

### 1. O Primeiro Objeto (Fácil)
**Instruções:**
Crie uma classe chamada `Pessoa`.
* **Construtor (`__init__`)**: Deve receber e armazenar os atributos `nome` (string) e `idade` (inteiro).
* **Método**: Crie um método chamado `apresentar(self)` que retorna a string: `"Olá, meu nome é [nome] e eu tenho [idade] anos."`

---

### 2. Controle de Estoque de Livros (Fácil)
**Instruções:**
Crie uma classe chamada `Livro`.
* **Construtor**: Deve receber `titulo`, `autor` e `quantidade_copias` (inteiro).
* **Métodos**: 
  * `vender(self)`: Diminui a `quantidade_copias` em 1.
  * `reabastecer(self, quantidade)`: Aumenta a `quantidade_copias` baseado no número recebido por parâmetro.

---

### 3. O Interruptor Inteligente (Fácil a Médio)
**Instruções:**
Crie uma classe chamada `Lampada`.
* **Construtor**: Não recebe parâmetros extras além de `self`. Ela deve começar sempre com o atributo `ligada = False`.
* **Métodos**:
  * `clicar_interruptor(self)`: Se a lâmpada estiver desligada, ela liga. Se estiver ligada, ela desliga.
  * `status(self)`: Retorna uma string dizendo `"A lâmpada está ligada"` ou `"A lâmpada está desligada"`.

---

### 4. Modificando Atributos com Validação (Médio)
**Instruções:**
Crie uma classe chamada `ContaBancaria`.
* **Construtor**: Recebe `titular` e começa com o atributo `saldo = 0.0`.
* **Métodos**:
  * `depositar(self, valor)`: Adiciona o valor ao saldo apenas se o valor for maior que zero.
  * `sacar(self, valor)`: Se o saldo for suficiente, subtrai o valor do saldo e retorna `True`. Se o saldo for insuficiente ou o valor for inválido, não altera o saldo e retorna `False`.

---

### 5. Usando Condicionais no Objeto (Médio)
**Instruções:**
Crie uma classe chamada `Aluno`.
* **Construtor**: Recebe `nome` (string) e `notas` (que será uma lista de números).
* **Métodos**:
  * `calcular_media(self)`: Calcula e retorna a média aritmética das notas que estão na lista.
  * `verificar_situacao(self)`: Usa o método da média. Se a média for 7.0 ou mais, retorna `"Aprovado"`. Se for entre 5.0 e 6.9, retorna `"Recuperação"`. Se for menor que 5.0, retorna `"Reprovado"`.

---

### 6. Sistema de Clima (Médio)
**Instruções:**
Crie uma classe chamada `Termometro`.
* **Construtor**: Recebe a `temperatura_atual` (float).
* **Métodos**:
  * `aumentar(self, graus)` e `diminuir(self, graus)`: Alteram a temperatura atual de acordo com o valor passado.
  * `alerta_clima(self)`: Retorna `"Congelando"` se estiver abaixo de 0°C, `"Agradável"` se estiver entre 0°C e 25°C, e `"Muito Quente"` se estiver acima de 25°C.

---

### 7. Classe com Contador Interno (Médio)
**Instruções:**
Crie uma classe chamada `Carro`.
* **Controle de quilometragem**: O construtor deve receber `modelo` e `ano`. Internamente, crie o atributo `odometro = 0` (que marca os quilômetros rodados).
* **Métodos**:
  * `viajar(self, distancia)`: Recebe a distância da viagem (número positivo) e soma essa distância ao `odometro`. Se tentarem passar um número negativo, o método deve exibir um aviso e não alterar nada.

---

### 8. Gerenciador de Playlist (Médio a Difícil)
**Instruções:**
Crie uma classe chamada `Playlist`.
* **Construtor**: Recebe o `nome` da playlist e cria internamente um atributo `musicas` como uma lista vazia.
* **Métodos**:
  * `adicionar_musica(self, nome_musica)`: Adiciona a música na lista.
  * `remover_musica(self, nome_musica)`: Se a música existir na lista, remove ela. Se não existir, avisa que a música não foi encontrada.
  * `mostrar_playlist(self)`: Exibe o nome da playlist e lista todas as músicas linha por linha.

---

### 9. Tamagotchi / Bichinho Virtual (Médio)
**Instruções:**
Crie uma classe chamada `BichinhoVirtual`.
* **Construtor**: Recebe o `nome`. Cria os atributos `fome = 50` e `felicidade = 50`.
* **Métodos**:
  * `alimentar(self)`: Diminui a fome em 15 unidades e aumenta a felicidade em 5. (A fome nunca pode ser menor que 0).
  * `brincar(self)`: Aumenta a felicidade em 20 unidades e aumenta a fome em 10. (A felicidade nunca pode passar de 100).

---

### 10. Carrinho de Compras Interativo (Difícil)
**Instruções:**
Crie uma classe chamada `CarrinhoDeCompras`.
* **Estrutura**: O construtor não recebe parâmetros. Ele deve inicializar duas listas vazias internas: `itens` (para os nomes dos produtos) e `precos` (para os preços correspondentes).
* **Métodos**:
  * `adicionar_item(self, nome_produto, preco_produto)`: Adiciona o nome na lista de itens e o preço na lista de preços (garantindo que fiquem no mesmo índice).
  * `calcular_total(self)`: Percorre a lista de preços, soma todos eles e retorna o valor total do carrinho.

---

### 11. O Jogo do Alvo (Médio)
**Instruções:**
Crie uma classe chamada `Jogador`.
* **Construtor**: Recebe o `nome` do jogador e define `pontuacao = 0`.
* **Métodos**:
  * `acertou_alvo(self, distancia_do_centro)`: Recebe a distância em centímetros que o tiro ficou do centro do alvo. Se for menor que 5cm, ganha 100 pontos. Se for entre 5cm e 20cm, ganha 50 pontos. Se for maior que 20cm, ganha 10 pontos.

---

### 12. Cadastro de Funcionários (Médio a Difícil)
**Instruções:**
Crie uma classe chamada `Empresa`.
* **Estrutura**: O construtor recebe o `nome_empresa` e inicializa uma lista vazia chamada `funcionarios`.
* **Métodos**:
  * `contratar(self, nome_funcionario)`: Adiciona o nome do funcionário à lista.
  * `demitir(self, nome_funcionario)`: Remove o funcionário da lista.
  * `verificar_funcionario(self, nome_funcionario)`: Retorna `True` se a pessoa trabalha na empresa e `False` caso contrário.

---

### 13. Agenda de Contatos (Difícil)
**Instruções:**
Crie uma classe chamada `Agenda`.
* **Estrutura**: O construtor cria duas listas internas vazias: `nomes` e `telefones`.
* **Métodos**:
  * `salvar_contato(self, nome, telefone)`: Salva o nome e o telefone nas respectivas listas.
  * `buscar_telefone(self, nome_pesquisado)`: Procura pelo nome na lista de nomes. Se achar, descobre o índice e retorna o telefone correspondente da outra lista. Se não achar, retorna `"Contato não encontrado"`.

---

### 14. Interação entre Objetos: Transferência (Difícil)
**Instruções:**
Utilizando o conceito da classe `ContaBancaria` (criada no exercício 4):
* Adicione um novo método chamado `transferir(self, conta_destino, valor)`.
* **Lógica**: O método recebe como parâmetro um **outro objeto** do tipo conta (`conta_destino`) e o valor da transferência. Se a conta atual tiver saldo suficiente, ela retira o dinheiro de si mesma e usa o método `.depositar()` da `conta_destino` para colocar o dinheiro lá, retornando `True`. Caso contrário, a operação é cancelada e retorna `False`.

---

### 15. Sistema de Combate RPG (Difícil)
**Instruções:**
Crie uma classe chamada `Personagem`.
* **Construtor**: Recebe `nome`, `vida` (inteiro) e `ataque` (inteiro).
* **Métodos**:
  * `esta_vivo(self)`: Retorna `True` se a vida for maior que 0, e `False` caso contrário.
  * `receber_dano(self, quantidade)`: Subtrai a quantidade da vida do personagem. Se a vida ficar menor que zero, ajusta para 0.
  * `atacar(self, oponente)`: Recebe como parâmetro **outro objeto** `Personagem` (o oponente). Se o atacante estiver vivo, ele chama o método `oponente.receber_dano(self.ataque)` para tirar vida do oponente baseado no seu próprio poder de ataque.

---
