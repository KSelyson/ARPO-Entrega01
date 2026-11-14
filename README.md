# 🤖 Robô de Navegação em Matriz (DFS vs. Algoritmo Guloso)

Este projeto consiste em um algoritmo de movimentação e busca de caminhos em uma matriz bidimensional (grade/mapa). O objetivo principal é guiar um robô da posição inicial `(0, 0)` no canto superior esquerdo até a posição final `(N-1, M-1)` no canto inferior direito, respeitando bloqueios e minimizando o custo total do trajeto.

O repositório traz a implementação de duas abordagens distintas para a resolução do problema: uma busca em profundidade baseada em **Backtracking (DFS)** e uma estratégia heurística baseada em **Algoritmo Guloso (Greedy)**.

---

## 🎯 Funcionalidades e Validações

- **Validação de Entrada (`validar_entrada`)**: Garante que o mapa seja uma matriz retangular/quadrada válida, composta por inteiros não negativos ou valores nulos (`None`).
- **Verificação de Viabilidade**: Confirma se a célula inicial `(0, 0)` ou o destino final `(N-1, M-1)` não estão bloqueados (valores `0` ou `None`).
- **Movimentos Permitidos**: O robô pode se mover estritamente para a **direita** e para **baixo**, evitando saídas fora dos limites do mapa.

---

## 🛠️ Algoritmos Implementados

### 1. Backtracking com Busca em Profundidade (`caminhada`)
- **Estratégia**: Explora exaustivamente todas as rotas possíveis da origem ao destino usando recursão (DFS).
- **Vantagem**: Garante encontrar todas as rotas válidas e, consequentemente, o **caminho mínimo absoluto** (ótimo global) ao avaliar a lista de custos acumulados.
- **Complexidade**: Alta complexidade de tempo em matrizes grandes devido à exploração combinatória de caminhos.

### 2. Algoritmo Guloso (`guloso`)
- **Estratégia**: Em cada passo, avalia as posições adjacentes disponíveis (Direita e Baixo) e escolhe imediatamente a opção de **menor custo local**.
- **Vantagem**: Execução rápida e baixo consumo de memória, tomando decisões em tempo real com laço iterativo.
- **Limitação**: Por focar na melhor escolha local imediata, pode ficar preso em mínimos locais ou falhar em encontrar o caminho ótimo global.

---

## 📂 Estrutura do Código

```text
├── main.py              # Script principal contendo mapas, validação e algoritmos
└── README.md            # Documentação do projeto
