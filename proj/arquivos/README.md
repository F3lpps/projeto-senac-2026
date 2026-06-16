# Lista Consolidada de Exercícios: Processamento de Arquivos em Python

Pratique a manipulação de dados externos, fluxos de leitura/escrita e tratamento de exceções robustas de forma progressiva.

---

## 🟢 Nível: Fácil (Conceitos Iniciais e Fluxos Básicos)

### 1. Criador de Diário Escrito
* **Objetivo:** Treinar escrita básica de strings em arquivos (`w`).
* **Instruções:** Crie uma função chamada `gravar_diario(mensagem)` que recebe uma string por parâmetro. A função deve abrir um arquivo chamado `diario.txt` em modo de escrita, salvando o texto recebido dentro dele e substituindo conteúdos anteriores.

### 2. O Leitor de Poemas Protegido
* **Objetivo:** Aplicar leitura estruturada (`r`) com prevenção de falhas de sistema.
* **Instruções:** Crie uma função chamada `ler_poema()`. Ela deve tentar abrir e extrair o conteúdo de um arquivo chamado `poema.txt` e exibi-lo na tela. Se o arquivo físico não for localizado na pasta, capture a exceção nativa `FileNotFoundError` e retorne um aviso amigável ao usuário.

### 3. Registro de Pontuação de Jogo (Modo Append)
* **Objetivo:** Compreender a persistência incremental de dados usando o modo de anexo (`a`).
* **Instruções:** Crie uma função chamada `registrar_pontuacao(nome_jogador, pontos)`. Toda vez que for executada, ela deve abrir o arquivo `ranking.txt` e adicionar uma linha inédita no final do texto mantendo o formato padrão `Nome: [nome_jogador] - Pontos: [pontos]`.

### 4. Contador de Linhas Crítico
* **Objetivo:** Percorrer e iterar por fluxos de texto linha por linha.
* **Instruções:** Crie uma função chamada `contar_linhas_arquivo(nome_arquivo)`. A função deve abrir o arquivo especificado no parâmetro, realizar a contagem exata de quebras de linhas existentes e retornar esse valor inteiro. Certifique-se de tratar o erro caso o arquivo passado não exista.

### 5. Filtrando Mensagens de Log (DEBUG vs ERROR)
* **Objetivo:** Analisar arquivos de texto aplicando regras condicionais simples de filtragem.
* **Instruções:** Suponha que haja um arquivo chamado `sistema.log` onde cada linha contém mensagens como `INFO: Conexão estabelecida` ou `ERROR: Falha no banco`. Crie a função `filtrar_erros()` para ler este arquivo, isolar apenas as linhas iniciadas com a palavra-chave `ERROR` e salvá-las em um arquivo novo chamado `alertas_criticos.txt`.

### 6. Somador de Números em Arquivo de Texto
* **Objetivo:** Converter tipos primitivos (`string` para `float`) durante a varredura do arquivo.
* **Instruções:** Crie uma função chamada `somar_valores_arquivo()`. Ela deve abrir um arquivo chamado `valores.txt` (que contém um número isolado por linha), converter cada registro em um número real, efetuar o somatório total e exibir o resultado. Trate o erro `ValueError` caso alguma linha contenha dados inválidos de digitação.

---

## 🔵 Nível: Médio (Manipulação de Strings e Lógica Intermediária)

### 7. Processador de Notas de Alunos (Gerando Médias)
* **Objetivo:** Desestruturar e tratar linhas de dados textuais usando o método `.split()`.
* **Instruções:** Crie uma função chamada `calcular_medias_alunos()`. Ela deve ler um arquivo chamado `notas.txt`, onde cada linha segue o padrão `Nome,Nota1,Nota2` (Ex: `Ana,8.0,9.0`). A função deve separar as strings, converter as notas, calcular a média de cada estudante e gravar o resultado final em `medias_finais.txt` no formato padrão `Ana: Média 8.5`.

### 8. Localizador de Palavras-Chave (Mecanismo de Busca)
* **Objetivo:** Realizar buscas de substrings em fluxos dinâmicos de leitura.
* **Instruções:** Crie uma função chamada `buscar_palavra_no_texto(palavra_alvo)`. A função deve ler o arquivo `documento.txt` e verificar quais linhas contêm a palavra informada. O terminal deve exibir de forma organizada o número do índice da linha e o seu respectivo conteúdo textual.

### 9. O Limpador de Linhas Vazias
* **Objetivo:** Realizar a higienização de arquivos removendo caracteres invisíveis.
* **Instruções:** Crie a função `limpar_arquivo(origem, destino)`. Ela deve ler o arquivo de origem completo linha por linha, detectar e descartar as linhas que estiverem totalmente vazias ou contendo apenas quebras de linha e espaços, salvando o arquivo resultante totalmente limpo no caminho de destino.

### 10. Simulador de Backup de Segurança
* **Objetivo:** Manipular múltiplos buffers de arquivos simultaneamente sob proteção de escopo.
* **Instruções:** Crie uma função chamada `fazer_backup_dados(nome_arquivo_original)`. O programa deve abrir o arquivo original indicado, carregar seu conteúdo integral e reescrevê-lo dentro de um novo arquivo cujo nome receberá o sufixo `.bak` adicionado ao final (Ex: `dados.csv.bak`). Envolva a lógica em tratamentos de erro contra falhas imprevistas de permissão de gravação do sistema operacional.

---

## 🔴 Nível: Hard (Manipulação de Coordenadas, Matrizes e Plantas ASCII)

### 11. Mapeador de Coordenadas da Planta
* **Objetivo:** Processar o fluxo do arquivo simulando um sistema tridimensional ou bidimensional de eixos (X, Y).
* **Instruções:** Crie uma função chamada `mapear_paredes_planta(nome_arquivo)`. Ela deve ler um arquivo contendo um desenho de matriz ou planta residencial em ASCII (onde paredes são representadas pelo caractere `=` e áreas livres são espaços em branco). A função deve varrer as linhas e colunas do arquivo para identificar cada parede e retornar uma lista de tuplas contendo as coordenadas numéricas inteiras no formato `(linha, coluna)`. Trate o erro caso o arquivo não seja encontrado.

### 12. Calculador de Perímetro e Área Útil
* **Objetivo:** Converter dados estruturados de caracteres em métricas matemáticas reais.
* **Instruções:** Crie uma função chamada `analisar_dimensoes_casa(nome_arquivo)`. Ela deve processar a leitura do mapa de caracteres de uma planta residencial baseada em caracteres `=`. Sabendo que cada caractere ocupa a equivalência de 1 metro quadrado (1m²), conte os dados textuais da matriz para exibir na tela: o perímetro das paredes externas (contagem total de `=`) e a área útil construída (contagem de espaços vazios internos). Dispare um `ValueError` manual caso a planta esteja vazia.

### 13. Conversor de Relatório CSV para Layout de Planta
* **Objetivo:** Converter strings de tabelas CSV para criar e projetar layouts geométricos.
* **Instruções:** Crie uma função chamada `gerar_planta_de_csv(nome_arquivo_csv, nome_arquivo_txt)`. A função deve ler um arquivo CSV cujas linhas trazem dados posicionado como `Tipo,Linha,Coluna` (Ex: `Parede,0,5` ou `Mesa,2,3`). O código deve ler os textos, converter os índices de linhas e colunas para inteiros (`int`), construir uma matriz bidimensional simulada 10x10 com espaços em branco e preencher as posições correspondentes com `=` para as Paredes e `M` para as Mesas. Ao final, grave o desenho gerado no arquivo de texto final.

### 14. Localizador de Móveis na Planta com Dicionários
* **Objetivo:** Associar mapeamento de dados textuais complexos a coleções de dicionários em Python.
* **Instruções:** Crie a função `inventariar_moveis(nome_arquivo)`. Ao varrer o arquivo de texto de uma planta de imóvel, o código deve analisar os caracteres usando manipulação de strings para identificar letras maiúsculas avulsas que representem mobílias (ex: `S` para Sofá, `C` para Cama, `T` para TV). Converta esses dados em um dicionário estruturado onde a chave é a letra do móvel localizado e o valor associado consiste em uma lista contendo as tuplas das coordenadas correspondentes descobertas no arquivo.

### 15. Validador de Portas e Erros de Planta Aberta
* **Objetivo:** Criar validações estruturais em arquivos acionando Exceções Customizadas.
* **Instruções:** Crie uma classe de erro própria chamada `PlantaInvalidaError` que herda de `Exception`. A seguir, construa a função `validar_fechamento_planta(nome_arquivo)`. A lógica deve ler o mapa de caracteres do arquivo. Pela regra de arquitetura, a primeira e a última linha do arquivo, bem como a primeira e a última coluna de todas as linhas do meio, devem conter obrigatoriamente caracteres de parede (`=`) ou de porta (`P`). Caso seja detectado um caractere de espaço em branco (` `) nessas extremidades externas (indicando vazamento estrutural da casa), interrompa a leitura disparando a exceção `PlantaInvalidaError` apontando textualmente qual linha falhou.
