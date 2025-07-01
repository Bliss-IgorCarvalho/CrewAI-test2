# Template Artigos de Parceiros

Regras aplicáveis ao template de parceiros (fontes do conteúdo)  
---

Requisitos de Design

1. [Ver design em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=6091-47711&t=6WCdTqZAtCsXu3ll-4)

Requisitos Funcionais

1. **Contexto**  
   1. Parceria vs Parceiro: A "**parceria**" (partnershipID) é uma entidade abstrata que agrupa diferentes parceiros com o mesmo conjunto de regras, enquanto o "**parceiro**" (partnerID) refere-se às fontes, como *A Bola* ou *Expresso*;

   2. A configuração dos comportamentos aplicados ao template de *Artigos de Parceiros* deve ser gerida a nível de parceiro. As regras definidas para um parceiro devem ser aplicadas a todos os artigos que pertençam a este parceiro. 

2. **Aplicação do template**  
   1. Este template deve ser aplicado ao artigo somente se a **fonte/parceiro** (partnerID) associada ao artigo **estiver** presente no **ficheiro de configuração de parcerias**.

      1. Nota técnica:   
         1. A fonte associada ao artigo deve estar presente no atributo partners do ficheiro, partnership.json.

3. **Layout & Componentes (blocos)**  
   1. **Últimas do Parceiro**:  ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7773-34311&t=aCBbAyIg8vbX2kJP-4)) \[highlights\]  
      1. Descrição:  
         1. Bloco que exibe uma listagem limitada dos últimos artigos publicados pelo parceiro em questão.

      2. Configuração / Personalização:   
         1. Deve ser possível definir / personalizar:  
            1. Se o bloco deve ser exibido nos artigos do parceiro configurado (show);  
            2. O título do componente consoante ao parceiro (title);  
            3. A quantidade de itens/artigos a serem exibidos no bloco (viewItems);  
            4. Os artigos a serem exibidos no bloco (dataGroupId). 

      3. Regras de Exibição do componente:  
         1. O bloco deve ser exibido somente se:  
            1. O parâmetro de exibição do bloco estiver definido a “true” no ficheiro de configuração (highlights.show \= True).

      4. Conteúdo:   
         1. Se **houver** lista de conteúdos definida para o bloco (highlights.dataGroupId \!= null):  
            1. Então, o conteúdo a ser exibido neste bloco deve ser obtido através de mensagens recebidas via RabbitMQ, nas mensagens do tipo highlights-group.json correspondentes ao bloco em questão.

         2. Se **não houver** lista de conteúdos definida para o bloco (highlights.dataGroupId \= null):  
            1. Então, o conteúdo a ser exibido neste bloco deve ser os últimos artigos publicados pelo parceiro em questão;  
            2. Devem ser considerados todos os artigos disponíveis na app (não apenas destaques);  
            3. Ordenados em decrescente por data de publicação (createdAt);  
            4. A quantidade máxima de itens/artigos exibidos deve ser limitada conforme valor definido no atributo partner.viewItems.  
               1. Fallback: se o atributo partner.viewItems não estiver definido, deve ser assumido o valor default \= 5\.

      5. Regras de Publicidade:   
         1. Este bloco não deve exibir publicidade.

   2. **Exclusivos do Parceiro** ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7773-34317&t=aCBbAyIg8vbX2kJP-4)) \[partnerExternal\]  
      1. Descrição:  
         1. Bloco que exibe uma listagem de artigos selecionados pelo parceiro, de artigos que **não** **existem na app** e são abertos via webview. 

      2. Configuração / Personalização:   
         1. Deve ser possível definir / personalizar:  
            1. Se o bloco deve ser exibido nos artigos do parceiro configurado (show);  
            2. O título do componente consoante ao parceiro (title);  
            3. A quantidade de itens/artigos a serem exibidos no bloco (viewItems);  
            4. Os artigos a serem exibidos no bloco (dataGroupId). 

      3. Regras de Exibição do componente:  
         1. Deve ser exibido apenas em artigos das fontes **expresso**, **sicnoticias**, **sic** e **dn-madeira** (são as fontes para as quais há endpoint configurado).  
         2. O bloco deve ser exibido somente se:  
            1.   
            2. O parâmetro de exibição do bloco estiver definido a “true” no ficheiro de configuração (highlights.show \= True)  
               **E**  
            3. Se **houver** lista de conteúdos definida para o bloco (highlights.dataGroupId \!= null)

      4. Conteúdo:   
         1. O conteúdo a ser exibido neste bloco deve ser obtido através de um endpoint específico para cada parceiro;  
            1. **expresso**: [https://flex.sapo.pt/api/partners/expresso](https://flex.sapo.pt/api/partners/expresso)  
            2. **sicnoticias**: [https://flex.sapo.pt/api/partners/sic-noticias](https://flex.sapo.pt/api/partners/sic-noticias)  
            3. **sic**: [https://flex.sapo.pt/api/partners/sic](https://flex.sapo.pt/api/partners/sic)  
            4. **dn-madeira**: [https://flex.sapo.pt/api/partners/dn-madeira](https://flex.sapo.pt/api/partners/dn-madeira)

         2. Os artigos a serem exibidos neste bloco devem ser abertos em webview;

         3. Os artigos devem ser exibidos na ordem retornada pela API;

         4. Nota técnica: Para correta exibição dos componentes previstos em design, devem ser recebidos na resposta do endpoint todos os elementos necessário para criação do componente de artigo:  
            1. Título;  
            2. Imagem;  
            3. Link para o artigo no site do parceiro.

      5. Regras de Publicidade:   
         1. Este bloco não deve exibir publicidade.

   3. **Últimas da Parceria** ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7773-34323&t=aCBbAyIg8vbX2kJP-4)) \[sugestionBlock\]  
      1. Descrição:   
         1. Bloco que exibe uma listagem limitada dos últimos artigos publicados pelos parceiros que pertencem à parceria em questão mais os artigos SAPO, ou os últimos artigos publicados por qualquer fonte presente na app.

      2. Configuração / Personalização:  
         1. Deve ser possível definir / personalizar:  
            1. Se o bloco deve ser exibido nos artigos do parceiro configurado (show);  
            2. O título do componente consoante ao parceiro (title);  
            3. A quantidade de itens/artigos a serem exibidos no bloco (viewItems);  
            4. Os parceiros/fonte de artigos que podem ser exibidos no bloco (restrictHighlights);   
            5. O comportamento de exibição de publicidade no bloco (displayAds) .

      3. Regras de Exibição do componente:  
         1. O bloco deve ser exibido somente se:  
            1. O parâmetro de exibição do bloco estiver definido a “true” no ficheiro de configuração (highlights.show \= True).

      4. Conteúdo:   
         O conteúdo a ser exibido neste bloco deve ser selecionado conforme as seguintes regras:

         1. Seleção do conteúdo:  
            1. Se **houver** lista de conteúdos definida para o bloco (highlights.dataGroupId \!= null):  
               1. Então, o conteúdo a ser exibido neste bloco deve ser obtido através de mensagens recebidas via RabbitMQ, nas mensagens do tipo highlights-group.json correspondentes ao bloco em questão.

            2. Se **não houver** lista de conteúdos definida para o bloco (highlights.dataGroupId \= null), então aplicam-se as seguintes regras:

               1. Se restrictHighlights \= True:  
                  1. Exibe os últimos artigos publicados pelos parceiros (partner) que pertencem à mesma parceria (partnershipID) mais os artigos SAPO;  
                  2. Devem ser considerados todos os artigos disponíveis na app (não apenas destaques);

               2. Se restrictHighlights \= False:  
                  1. Exibe os últimos artigos publicados por qualquer fonte/parceiro existente na app;  
                  2. Devem ser considerados todos os artigos disponíveis na app (não apenas destaques);

         2. Ordenação e Limite:  
            1. Os artigos devem ser ordenados em decrescente por data de publicação (createdAt);  
            2. A quantidade máxima de itens/artigos exibidos deve ser limitada conforme valor definido no atributo sugestionBlock.viewItems.  
               1. Fallback: se o atributo sugestionBlock.viewItems não estiver definido, deve ser assumido o valor default \= 5\.

      5. Regras de Publicidade:   
         1. O bloco deve poder apresentar 2 tipos de comportamento:  
            1. Se displayAds \= True:  
               1. Comportamento Padrão: Aplicam-se as mesmas regras do componente Artigos Relacionados;  
               2. A publicidade deve ser fornecida por Outbrain, com integração para o mesmo ambiente já configurado para esta plataforma.

            2. Se displayAds \= False:  
               1. Sem Publicidade: Não devem ser exibidos anúncios no bloco.

4. **Ações**  
   1. Ver artigo no site da fonte:   
      1. A aplicação deve permitir ao utilizador visualizar o artigo atual diretamente no site da fonte do artigo. 

      2. Regras de redirecionamento  
         1. Quando realizada esta ação, a aplicação deve redirecionar o utilizador para a url informada no atributo PartnerArticleUrl.

      3. Regras de exibição do componente  
         1. Se o atributo PartnerArticleUrl estiver vazio, o CTA não deve ser exibido.

---

