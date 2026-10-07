# Atividade em dupla: cubo com satélite texturizado
Tempo: 20 minutos. Use `atividade_cubo.py` como ponto de partida e altere os trechos marcados com `TODO`.

## Requisitos
1. **Textura**: o cubo principal usa `mosaico.png`, incluída em `images`.
2. **Satélite**: crie um segundo cubo com `grade_uv.png` repetida 2x2 em cada face (`{'repeatUV':[2,2]}`).
3. **Hierarquia**: o satélite é filho do cubo principal. Fica a 1.3 unidades do centro, com escala 0.4, e acompanha a rotação do cubo principal (órbita).
4. **Teclado**: as setas para cima e para baixo aumentam e diminuem a velocidade de rotação do cubo principal.
5. **Rotação própria**: o satélite também gira em torno do próprio eixo X, a 2 rad/s.

Dicas:
- `self.isKeyPressed('up')` devolve True enquanto a seta estiver pressionada.
- Métodos de `Object3D`: `add`, `setPosition`, `scale`, `rotateX`, `rotateY`. As transformações são locais por padrão.
- Se o satélite aparecer colado no cubo, a escala foi aplicada antes da translação.

## Entrega
- O arquivo `atividade_cubo.py` alterado.
- Uma captura do resultado: pressione **S** durante a execução para salvar `capturas/resultado.png`.
- Os nomes dos dois integrantes.
- Um parágrafo explicando o papel das coordenadas UV e o efeito de `repeatUV = [2,2]`.

## Critérios (e pontos)
| Critério | Pontos |
|---|---:|
| Textura `mosaico.png` no cubo principal, sem inversão 
| Satélite com `grade_uv.png` repetida 2x2 
| Satélite filho do cubo, na distância correta e acompanhando a rotação 
| Velocidade controlada pelo teclado, com `deltaTime` 
| Rotação própria do satélite 
| Explicação de UV e `repeatUV` 
| Código executável e entrega completa 
