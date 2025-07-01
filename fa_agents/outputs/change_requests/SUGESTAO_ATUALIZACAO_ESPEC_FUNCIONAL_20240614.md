# Sugestão de Alterações na Especificação Funcional (base CR34536, CR34614)

## 1. Navegação, Cache e Estado nas Áreas Principais (Jornais, Feed, Destaques)

### Itens a atualizar
- **04-Feed/Feed de Artigos.md**
  - Expandir seção de cache (substituir: "O tempo de expiração de cache previsto para o ecrã Feed deve ser de 10 min. ...") para explicar a nova regra: cache em memória mantendo o conteúdo e a posição de scroll ao alternar entre abas, refresh só se cache expirou E houver conexão, manter conteúdo offline mesmo expirado, sem erro.
  - Detalhar, no início do arquivo e/ou em seção 'Navegação entre Áreas Principais', que ao alternar entre as áreas (Jornais, Feed, Destaques) devem ser preservados conteúdo renderizado e scroll.
- **03-Capas-de-Jornais/Feed de Capas.md**
  - Atualizar regra de cache para incluir: manter conteúdo e posição de scroll das abas "Jornais" (e carrosséis) quando alternando ou retornando entre áreas principais, seguindo a mesma mecânica: refresh só sob as novas condições, manter visualização offline.
- **Incluir seção específica (pode ser nota técnica compartilhada ao final dos arquivos ou nova seção geral)**
  - Explicitar o funcionamento de cache/navegação/scroll das três áreas principais: memoria por aba, refresh condicional, manutenção do último estado visual.

## 2. Digest – Regras para Exibição dos Cards e Toggle Texto/Áudio

### Itens a atualizar
- **07-Resumo-de-Artigo/Digest.md**
  - Adicionar seção "Regras de Exibição Condicional":
    - Explicitar que:
      1. O componente Digest só deve ser exibido se houver pelo menos um artigo elegível em texto OU áudio.
      2. A interface deve montar listas separadas para artigos elegíveis com resumo em texto e em áudio.
      3. O toggle de texto/áudio **só aparece se** ambas as listas tiverem pelo menos um elemento.
      4. Ao usuário alternar, mostrar apenas o conteúdo do formato disponível. Esconder toggle se só existir um formato.
      5. Não existindo conteúdo em ambos formatos, Digest não é apresentado.
- **04-Feed/Feed de Artigos.md**
  - Ao descrever o card/componente Digest no Feed, incluir cláusula de visibilidade baseada nas novas regras (ou referenciar o tópico específico do Digest.md).

## 3. Seções/Trechos sugeridos
### Trecho exemplo para cache/scroll/refresh (incluir onde mencionado cache ou navegação entre áreas):

> "Para as áreas principais da aplicação (Jornais, Feed de Artigos, Destaques), o conteúdo renderizado e a posição de scroll devem ser preservados ao alternar ou retornar entre estas áreas. O refresh de conteúdo ocorre somente quando a cache expirar **e** houver conectividade ativa. Caso a cache esteja expirada e não haja conexão, o conteúdo anterior deve ser exibido normalmente, sem mensagens de erro. Esta lógica aplica-se exclusivamente a essas três áreas."

### Trecho exemplo para regras de Digest/toggle:

> "Antes de apresentar o card Digest, a aplicação deverá verificar a disponibilidade de artigos elegíveis em texto e em áudio, mantendo listas separadas. O card Digest só aparecerá se ao menos uma destas listas não estiver vazia. O toggle para alterar entre 'Texto' e 'Áudio' só estará presente se ambos os formatos tiverem pelo menos um artigo disponível. Não existindo conteúdo em ambos formatos, o Digest não será exibido no Feed."
