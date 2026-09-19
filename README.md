# 🎲 Par ou Ímpar

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-concluído-brightgreen)
![License](https://img.shields.io/badge/license-MIT-blue)

## 📋 Sobre o projeto

Jogo em Python do clássico "Par ou Ímpar", jogado contra o computador. O jogador escolhe "par" ou "ímpar", digita um número e o computador sorteia outro número aleatório entre 1 e 11. A soma dos dois números define o resultado da rodada. O jogo continua enquanto o jogador for vencendo e contabiliza as vitórias consecutivas.

## ⚙️ Como funciona

1. O jogador escolhe **par** ou **ímpar**.
2. O jogador digita um número.
3. O computador sorteia aleatoriamente um número entre 1 e 11.
4. Os dois números são somados e o resultado é mostrado.
5. Se o resultado bater com a escolha do jogador (par/ímpar), ele vence a rodada e o jogo continua; caso contrário, o jogador perde e o jogo termina.
6. Ao final, é exibido o total de vitórias consecutivas.

## ▶️ Como executar

Pré-requisito: ter o [Python 3](https://www.python.org/downloads/) instalado.

```bash
python app.py
```

### Exemplo de execução

```
Vamos jogar Par ou Impar
Par ou Impar? par
Digite um número: 4
Resultado: 9 - Impar!
Você perdeu!
Vitórias consecutivas: 0
```

## 🛠️ Tecnologias utilizadas

- Python 3
- Módulo `random` (função `randint`)

## 📌 Observações

- A validação de entrada usa `escolha not in 'par'` e `escolha not in 'impar'`, o que funciona para os valores exatos "par" e "impar", mas tecnicamente aceitaria substrings (ex.: "a" está contido em "par"). Uma melhoria futura seria validar com `escolha not in ('par', 'impar')`.
- O contador de vitórias é reiniciado a cada execução do programa (não é salvo entre partidas).