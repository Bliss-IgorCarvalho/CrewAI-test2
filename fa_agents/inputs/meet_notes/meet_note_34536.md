# Notas de Reunião — Referente ao CHANGE REQUEST 34536

**Data**: 21/03/2025  
**Participantes**: PO, Tech Lead, UX, Dev Mobile  

## Resumo da reunião
- Foi identificado que a experiência do utilizador está a ser prejudicada quando o mesmo navega entre diferentes áreas da aplicação (Jornais, Feed e Destaques).  
- O comportamento actual faz com que o conteúdo dessas áreas seja sempre recarregado ao retornar, causando perda de contexto, como a posição de scroll.
- A equipa técnica sugeriu que o conteúdo renderizado anteriormente seja mantido em cache.
- UX concorda que a posição de scroll também deve ser restaurada ao retornar para a aba anterior.
- O PO destacou a necessidade de manter a experiência fluida mesmo sem internet — ou seja, se estiver offline, o conteúdo em cache deve continuar visível.
- Ficou decidido que o refresh automático só deve acontecer se a cache tiver expirado **e** houver conexão com a internet.

## Decisões
- Implementar cache para as 3 áreas principais da app.
- Manter posição de scroll ao retornar a uma área.
- Fazer refresh apenas quando houver internet e a cache tiver expirado.
- Em modo offline, manter o conteúdo existente.
