# Atividade em dupla: braço robótico
Tempo: 25 minutos. Use `atividade_braco.py` como ponto de partida e complete os trechos marcados com `TODO`.

| Início | Esperado |
|---|---|
| ![](capturas_exemplos/atividade_inicial.png) | braço com base, braço, antebraço e garra, articulado pelo teclado |

## Requisitos
1. **Ombro e braço**: um `Object3D` (pivô) no topo da base e o braço laranja preso a ele pela ponta de baixo.
2. **Cotovelo e antebraço**: um pivô na ponta de cima do braço e o antebraço azul preso a ele.
3. **Garra**: uma caixa cinza na ponta do antebraço.
4. **Base**: A e D giram a base (e todo o braço) em torno do eixo Y.
5. **Articulações**: W e S giram o ombro; I e K giram o cotovelo, em torno do eixo Z.

Dicas:
- `caixa(...)` cria uma caixa **centrada** na origem local. Para que a ponta de baixo fique no pivô, desloque-a para cima metade da altura.
- Um `Object3D` vazio não aparece na tela, mas tem posição e rotação: é a articulação.
- Pense em quem é pai de quem: ao girar o ombro, o cotovelo, o antebraço e a garra devem ir junto.

## Entrega
- O arquivo `atividade_braco.py` alterado.
- Uma captura com o braço dobrado: pressione **P** para salvar `capturas/resultado.png`.
- Os nomes dos dois integrantes.
- Um parágrafo explicando por que foi preciso usar pivôs (`Object3D`) em vez de girar as caixas diretamente.

## Critérios (1 ponto)
| Critério | Pontos |
|---|---:|
| Ombro como pivô e braço preso pela ponta
| Cotovelo como pivô e antebraço preso pela ponta 
| Garra na ponta do antebraço 
| Base gira com A/D, levando o braço junto 
| Ombro e cotovelo giram com W/S e I/K 
| Explicação dos pivôs 
| Código executável e entrega completa 
