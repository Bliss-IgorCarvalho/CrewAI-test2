# Notas de Reunião — Referente ao CHANGE REQUEST 34614

**Data**: 04/04/2025  
**Participantes**: PO, Equipa de Recomendação, UX  

## Resumo da reunião
- Foi identificado um problema nos cards do Digest: nem sempre há conteúdo suficiente para todos os formatos (texto ou áudio).
- O recommender retorna até 12 artigos recomendados, mas nem todos têm resumo em texto e/ou áudio.
- UX indicou que isso causa inconsistências na interface: às vezes o toggle de "Texto/Áudio" aparece mesmo quando não existem artigos disponíveis em ambos os formatos.
- PO solicitou que a exibição do card e do toggle seja condicionada à existência efetiva de resumos.

## Decisões
- Criar duas listas distintas: uma com artigos que têm resumo em texto e outra com artigos com resumo em áudio.
- O frontend deve verificar essas listas para decidir:
  - Se exibe ou não o card do Digest.
  - Se exibe ou não o seletor de formato (Texto/Áudio).
