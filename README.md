# Sistema de Controle de Qualidade de Peças

**Universidade:** UniFECAF  
**Curso:** Graduação Tecnológica em Inteligência Artificial e Automação Digital  
**Disciplina:** Algoritmos e Lógica de Programação  
**Aluno:** Waldir Adilson Évora dos Santos  
**RA:** 263388  
**GitHub:** https://github.com/waldirevora/controle-qualidade-pecas  
**Vídeo no YouTube:** https://youtu.be/m2e4H0mH9pg 

## Sobre o projeto

Este projeto foi desenvolvido para simular um sistema simples de controle de qualidade de peças em uma linha de produção.

O programa recebe os dados de cada peça e verifica se ela atende aos padrões definidos para peso, cor e comprimento.

Quando a peça atende a todos os critérios, ela é aprovada. Quando não atende, ela é reprovada e o programa informa o motivo.

As peças aprovadas também são armazenadas em caixas com capacidade para 10 peças. Quando uma caixa chega a 10 peças, ela é fechada e uma nova caixa começa a ser preenchida.

## Critérios de aprovação

Para uma peça ser aprovada, ela precisa atender aos três critérios abaixo:

1. Peso entre 95 g e 105 g.
2. Cor azul ou verde.
3. Comprimento entre 10 cm e 20 cm.

Se uma ou mais condições não forem atendidas, a peça é reprovada.

## Funcionalidades

O programa possui o seguinte menu:

```text
1 - Cadastrar nova peça
2 - Listar peças aprovadas/reprovadas
3 - Remover peça cadastrada
4 - Listar caixas fechadas
5 - Gerar relatório final
```

### 1. Cadastrar nova peça

O programa solicita:

```text
ID
Peso
Cor
Comprimento
```

Depois verifica os critérios de qualidade e informa se a peça foi aprovada ou reprovada.

### 2. Listar peças aprovadas e reprovadas

Mostra separadamente as peças aprovadas e as peças reprovadas.

Nas peças reprovadas, também são mostrados os motivos da reprovação.

### 3. Remover peça cadastrada

O usuário informa o ID da peça que deseja remover.

O programa procura o ID entre as peças cadastradas e remove a peça quando ela é encontrada.

### 4. Listar caixas fechadas

Mostra as caixas que já chegaram ao limite de 10 peças aprovadas.

Também mostra os IDs das peças que estão em cada caixa fechada.

### 5. Gerar relatório final

Mostra:

```text
Total de peças aprovadas
Total de peças reprovadas
Quantidade de caixas utilizadas
Peças reprovadas e seus motivos
```

Depois do relatório final, o programa é encerrado.

## Conceitos utilizados

Durante o desenvolvimento foram utilizados conteúdos estudados na disciplina, como:

1. Variáveis
2. `print()`
3. `input()`
4. `float()`
5. `if`, `elif` e `else`
6. Operadores `and` e `or`
7. Operadores de comparação
8. `while`
9. `for`
10. Listas
11. Dicionários
12. `.append()`
13. `.remove()`
14. `len()`
15. `break`

## Como executar o programa

É necessário ter o Python 3 instalado no computador.

### Passo 1

Baixe os arquivos do projeto.

### Passo 2

Abra o terminal na pasta onde está o arquivo:

```text
main.py
```

### Passo 3

Execute o comando:

```bash
python main.py
```

Dependendo da instalação do Python, também pode ser necessário usar:

```bash
python3 main.py
```

### Passo 4

Escolha uma opção do menu digitando um número de 1 a 5.

## Exemplo de peça aprovada

Entrada:

```text
Escolha uma opção: 1
Digite o ID da peça: P001
Digite o peso da peça em gramas: 100
Digite a cor da peça: azul
Digite o comprimento da peça em cm: 15
```

Saída:

```text
ID informado: P001
Peso informado: 100.0
Cor informada: azul
Comprimento informado: 15.0

Peso 100.0 gramas aprovado.
Cor azul aprovada.
Comprimento 15.0 cm aprovado.
Peça APROVADA.
```

## Exemplo de peça reprovada

Entrada:

```text
Escolha uma opção: 1
Digite o ID da peça: P002
Digite o peso da peça em gramas: 110
Digite a cor da peça: vermelho
Digite o comprimento da peça em cm: 25
```

Saída:

```text
ID informado: P002
Peso informado: 110.0
Cor informada: vermelho
Comprimento informado: 25.0

Peça REPROVADA.
Motivos:
Peso 110.0 gramas fora do padrão.
Cor vermelho fora do padrão.
Comprimento 25.0 cm fora do padrão.
```

## Exemplo de relatório final

```text
RELATÓRIO FINAL

Total de peças aprovadas: 1
Total de peças reprovadas: 1
Quantidade de caixas utilizadas: 1

PEÇAS REPROVADAS E MOTIVOS:

ID: P002
Peso 110.0 gramas fora do padrão.
Cor vermelho fora do padrão.
Comprimento 25.0 cm fora do padrão.

Programa encerrado.
```

## Observação

Os dados ficam armazenados somente enquanto o programa está em execução.

Ao encerrar o programa e executar novamente, as listas começam vazias.
