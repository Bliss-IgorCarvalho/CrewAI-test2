# Feed de Artigos

---

 

Design

* [Link Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5641-8292&t=T3XVzCGXq4oaQvI5-4)

Funcional

1. **Tipos de conteúdo a serem exibidos no Feed:**

   1. **Resumos (digest \- preview)**: Componente de acesso a geração/reprodução do Digest Summary (Resumo de múltiplos artigos).  
      1. As regras de exibição e interação com este componente serão especificadas no escopo da funcionalidade Digest Summary. 

   2. **Card de Artigos**: A app deve ser capaz de apresentar o preview de artigos nos seguintes formatos:   
      1. Top Story ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5641-8306&t=1VQ8Fm6gfBikSio9-4)):   
         1. Formato específico que destaca um preview de um artigo;   
         2. Aplicado **apenas** (e sempre) ao primeiro artigo do Feed (posição \= 1);  
         3. Componentes:  
            1. **Imagem**:Imagem principal do artigo (atributo mainImage)  
            2. **Fonte**:Nome da Fonte associada ao artigo (partner.title).  
            3. **Tempo/Data de publicação**:Informação de quando o artigo foi publicado (ver especificação da regra em [*Página de Artigo*](?tab=t.g0diref5r0rg)).  
            4. **Título**:  Exibe do título do artigo (title).  
            5. **Lead**: Lead: Exibe o lead do artigo (lead).   
            6. **Tempo estimado de leitura**: Exibe o tempo médio estimado para conclusão da leitura do artigo (ver especificação da regra em [*Página de Artigo*](?tab=t.g0diref5r0rg))

      2. Opinião ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-65852&t=dm4TUoskIomG9rAf-4)):   
         1. Formato específico para artigos de opinião;   
         2. Aplicado apenas à artigos da subtemática *Opinião*;  
         3. Componentes:  
            1. **Imagem**: Imagem associada ao autor associado ao artigo. Se houver mais de um autor, deve ser considerado apenas o primeiro autor da lista.  
            2. **Fonte**: Nome da Fonte associada ao artigo (partner.title).  
            3. **Subtemática: A subtemática** Opinião deve ser visualmente identificada por uma tag.  
            4. **Tempo/Data de publicação**: Informação de quando o artigo foi publicado (ver especificação da regra em [*Página de Artigo*](?tab=t.g0diref5r0rg)).  
            5. **Título**:  Exibe do título do artigo (title).  
            6. **Lead**: Exibe o lead do artigo (lead).   
            7. **Tempo estimado de leitura**: Exibe o tempo médio estimado para conclusão da leitura do artigo (ver especificação da regra em [*Página de Artigo*](?tab=t.g0diref5r0rg))

      3. Padrão ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5641-8308&t=1VQ8Fm6gfBikSio9-4)):   
         1. Formato padrão de exibição do preview de artigos;   
         2. Aplicado ao demais artigos do Feed;  
         3. Componentes:  
            1. **Imagem**: Imagem principal do artigo (atributo mainImage)  
            2. **Fonte**: Nome da Fonte associada ao artigo (partner.title).  
            3. **Tempo/Data de publicação**: Informação de quando o artigo foi publicado (ver especificação da regra em [*Página de Artigo*](?tab=t.g0diref5r0rg)).  
            4. **Título**:  Exibe do título do artigo (title).  
            5. **Tempo estimado de leitura**: Exibe o tempo médio estimado para conclusão da leitura do artigo (ver especificação da regra em [*Página de Artigo*](?tab=t.g0diref5r0rg))

      4. Componentes comuns a todos os formatos:  
         1. Tempo/Data de publicação: Exibe a informação de quando o artigo foi publicado

   3. **Publicidade**: A app deve ser capaz de apresentar os seguintes formatos de publicidade entre artigos:  
      1. Banner in page:  
         1. Frequência de impressão: A seguir ao 3º conteúdo, e depois a cada 5 conteúdos;  
         2. [Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5641-8309&t=1VQ8Fm6gfBikSio9-4).  
      2. Banner Sticky:  
         1. Frequência de impressão: Fixo over page  
         2. [Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=6365-10074&t=DsmAedJ2ZzE7nvr4-4).

2. **Regras de exibição dos conteúdos**

   1. **Seleção dos Artigos:**  
      1. Os artigos exibidos no Feed devem ser selecionados conforme as regras especificadas na funcionalidade [Recomendação de Artigos](?tab=t.ew9jfe4u1623).

   2. **Formato *infinite scroll****:*  
      1. O Feed deve apresentar um formato de leitura infinita de artigos (semelhante ao utilizado em redes sociais).  
      2. Se após múltiplos scrolls o utilizador chegar ao fim do Feed (não houver mais novos conteúdos a serem carregados), então a aplicação deve disponibilizar ao utilizador um CTA de redirecionamento para o ecrã Explore ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5641-8428&t=ORzNNOxcmbXud7VV-4)). 

   3. **Paginação**  
      1. Renderização inicial da página;  
         1. A aplicação deve carregar 10 novos conteúdos que formarão o Feed inicial. 

      2. Scroll:  
         1. Quando o utilizador rolar até X% do conteúdo exibido (valor de X a ser definido pelas equipas técnicas), a aplicação deve carregar e adicionar 10 novos conteúdos ao final do Feed, mantendo os conteúdos já exibidos.

      3. Refresh Feed:   
         1. Ação do utilizador para atualizar manualmente o conteúdo apresentado no Feed. A aplicação deve remover os conteúdos em exibição no Feed e carregar 10 novos conteúdos que formarão um novo Feed.  (descrito em 3\. i)

   4. **Tempo de cache**:  
      1. O tempo de expiração de cache previsto para o ecrã Feed deve ser de 10 min. Enquanto a cache estiver válida, a app não deve fazer novos pedidos para carregamento de novos conteúdos.  

3. **Ações disponíveis a partir do Feed:**  
   1. **Aceder ao digest**  
      1. As regras de interação com este componente serão especificadas no escopo da funcionalidade Digest Summary. 

   2. **Aceder página de artigo**  
      1. Ao interagir com um conteúdo do feed (preview de um artigo), o utilizador deve ser redirecionado para o detalhe do artigo (Página de Artigo) escolhido. 

   3. **Guardar conteúdo** (pós MVP)  
      1. O utilizador deve poder guardar um artigo a partir do Feed;  
      2. As regras e o fluxo desta ação serão especificadas no escopo da funcionalidade *Guardar conteúdo*.

   4. **~~Ouvir versão em áudio (TTS)~~**~~;~~  
      1. ~~O utilizador deve poder reproduzir a versão em áudio um artigo a partir do Feed;~~  
      2. ~~As regras e o fluxo desta ação serão especificadas no escopo da funcionalidade *Versão áudio de artigo*;~~  
      3. ~~Esta ação deve estar disponível apenas para artigos em formato Top Story ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5641-8306&t=HyoYvveG7oME5tT5-4)).~~

   5. **Ver Resumo**;  
      1. O utilizador deve poder gerar/visualizar a versão em resumo de um artigo a partir do Feed;  
      2. As regras e o fluxo desta ação serão especificadas no escopo da funcionalidade *Summary (artigo único)*;

   6. **Partilhar conteúdo**  
      1. O utilizador deve poder partilhar um artigo a partir do Feed;  
      2. As regras e o fluxo desta ação serão especificadas no escopo da funcionalidade *Partilhar conteúdo*.

   7. **Ver Mais (Like)**  
      1. O utilizador deve poder indicar gosto/interesse em um artigo a partir do Feed;  
      2. Requisitos especificados no escopo da funcionalidade *Feedback da relevância (Ver mais);*  
      3. **Disclaimer**: Para versão MVP da app, esta ação não terá efeito sobre os conteúdos exibidos na app. Os dados gerados pela interação Ver Mais serão posteriormente utilizados no escopo de implementação do Recommender. 

   8. **Ver Menos (Dislike)**  
      1. O utilizador deve poder indicar desinteresse em um artigo a partir do Feed;  
      2. Requisitos especificados no escopo da funcionalidade *Feedback da relevância (Ver menos);*  
      3. **Disclaimer**: Para versão MVP da app, esta ação não terá efeito sobre os conteúdos exibidos na app. Os dados gerados pela interação Ver Menos serão posteriormente utilizados no escopo de implementação do Recommender. 

   9. **Refresh Feed** **(carregar novos conteúdos)**  
      1. O utilizador deve poder atualizar o conteúdo do Feed “manualmente”. O refresh do feed pode ser acionado através de dois tipos de interação:

         1. **Pull to refresh**:   
            1. Ação de swipe down realizada no topo do feed;  
            2. Executada somente se scroll do Feed \= 0%;  
            3. Aplicam-se as regras de paginação descritas no tópico 2.d.iii.

         2. **Tab on home**:   
            1. Ação de clique no item Feed da Bottom Bar.  
            2. Executada somente se scroll do Feed **\=** 0%;  
            3. Executada somente se screen **\=** Feed;  
            4. Aplicam-se as regras de paginação descritas no tópico 2.d.iii.

   10. **Back to top**:  
       1. O utilizador deve poder retornar ao topo do Feed, sem precisar fazer scroll up:  
          1. Ação de clique no item Feed da Bottom Bar.  
          2. Executada somente se scroll do Feed **diferente de** 0%;  
          3. Executada somente se screen **igual a** Feed;  
          4. Direciona o utilizador para o topo do Feed (Feed **igual a** 0%);  
          5. Não carrega novos conteúdos.

### ---

