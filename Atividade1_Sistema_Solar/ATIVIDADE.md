# Atividade em dupla: mini sistema solar
Tempo: 25 minutos. Use `atividade_sistema_solar.py` como ponto de partida e altere apenas os trechos marcados com `TODO`.

![Estado inicial](capturas_exemplos/atividade_inicial.png)

## Requisitos
1. **Sol**: gira em torno do próprio centro (`self.anguloSol`).
2. **Órbita**: o planeta orbita o sol a uma distância de `RAIO_ORBITA_PLANETA` (`self.anguloOrbita`).
3. **Rotação própria**: o planeta também gira em torno do próprio eixo, com velocidade diferente da órbita (`self.anguloRotacaoPlaneta`).
4. **Lua**: orbita o **planeta** a uma distância de `RAIO_ORBITA_LUA` e o acompanha na órbita (`self.anguloOrbitaLua`). Reaproveite a matriz da órbita do planeta.
5. **Teclado**: as setas para cima e para baixo (`"up"` e `"down"`) aumentam e diminuem a velocidade da órbita do planeta, que nunca fica negativa.

Dicas:
- Use apenas `Matrix.make_translation`, `Matrix.make_rotation_z` e `Matrix.make_scale`, combinadas com `@`.
- Leia a composição da direita para a esquerda: escala → rotação própria → translação → rotação da órbita.
- A escala deve ficar **à direita** de tudo. Assim ela não altera o raio da órbita.

## Entrega
- O arquivo `atividade_sistema_solar.py` alterado.
- Uma captura do resultado: pressione **P** durante a execução para salvar `capturas/resultado.png`.
- Os nomes dos dois integrantes.
- Um parágrafo explicando por que a órbita usa `R @ T` e a rotação própria fica à direita da translação.

## Critérios ( 1 ponto)
| Critério | Pontos |
|---|---:|
| Sol girando no próprio centro 
| Planeta orbitando o sol 
| Rotação própria do planeta, independente da órbita 
| Lua orbitando o planeta (hierarquia) 
| Controle de velocidade pelo teclado, sem valor negativo 
| Explicação da ordem das matrizes 
| Código executável e entrega completa 
