# Ecrã de Destaques (Blocos)

---

Requisitos de Design

1. [Ver design em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-140796&t=l0h17j8L2oZnbJVj-4)

Requisitos Funcionais

**Requisitos Gerais**

1. #### **Ações**

   1. As ações disponíveis a partir da página principal do *Explore* devem ser as mesmas disponíveis a partir do [Feed de Artigos](?tab=t.5k6yo6t7k8dc), conforme a disponibilidade de funcionalidades para cada artigo.

2. #### **Regras de Exibição dos Blocos**

   1. **Ordenação fixa para MVP**: Para o MVP, a ordem de exibição dos blocos é pré-definida. A sequência de blocos deve refletir exatamente a ordem definida pela equipa de produto, sem alterações dinâmicas durante a execução.

   2. **É mantido até o recebimento de um novo payload**: Cada bloco permanece visível até que a aplicação receba um payload atualizado. Assim que um novo payload chega, qualquer bloco não incluído nessa nova listagem deve deixar de ser exibido automaticamente.  
      1. **Exceções**: Blocos *Hot Topics* e *Últimas*.

   3. **Exibição condicionada a regras de conteúdo mínimo para cada bloco**: Alguns blocos exigem um número mínimo de itens (artigos) para serem exibidos. Caso a lista de artigos associada ou obtida para o bloco não atenda esse requisito mínimo, o bloco não deve ser exibido no ecrã Explore.

3. #### **Blocos com UI-Layout Específico**

   1. Layouts específicos que devem ser aplicados apenas a um tipo específico de bloco;  
   2. A quantidade mínima e máxima de itens permitidos pode variar dependendo do bloco.

4. #### **Blocos com UI-Layout Genérico** {#blocos-com-ui-layout-genérico}

   1. O layout genérico pode ser aplicado a diferentes tipos de blocos;  
   2. Quantidade mínima de itens a serem exibidos: **3**  
   3. Quantidade máxima de itens a serem exibidos: **10**  
   4. Se houver menos de 3 itens, o bloco não deve ser exibido.  
   5. Se houver mais de 10 itens, apenas os 10 primeiros serão exibidos.

5. #### **Blocos de Conteúdo de Estático** 

   1. Os artigos exibidos no bloco devem ser explicitamente fornecidos através das listas de destaques (highlights-group);  
   2. Os blocos devem estar devidamente configurados no payload de ecrã de destaques, conforme regras especificadas em [Requisitos Técnicos](#payload).

6. #### **Blocos de Conteúdo de Dinâmico**

   1. A lista de artigos a ser exibida deve ser obtida de forma dinâmica, consoante a regras especificadas para cada bloco.

7. **Navegação em profundidade para Lista de Artigos**  
   1. Para alguns blocos, o utilizador deve poder navegar em profundidade e aceder à página *Lista de Artigos* para visualizar a lista completa de artigos;  
   2. Após o redirecionamento, aplicam-se as regras de exibição e paginação especificadas em [*Lista de Artigos*](?tab=t.7ia3otqqi5x). 

---

**Blocos**  
---

1. #### **Destaque Principal** ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11296-37776&t=phUWx5HFpeXrby6R-4))    Destaque principal da curadoria manual SAPO. Pode ou não ser apresentado junto com artigos relacionados.   

   1. **UI-Layout**: Específico

   2. **Conteúdo**: Estático

   3. **Regras de Exibição**  
      1. Bloco principal \- Artigo Principal  
         1. Deve ser sempre exibido  
         2. Quantidade de itens: Sempre único

      2. Sub-bloco: Artigos Relacionados ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11296-37797&t=phUWx5HFpeXrby6R-4))  
         1. Exibe os artigos presentes no atributo relatedPosts do artigo principal  
         2. Quantidade mínima de itens: 1  
         3. Quantidade máxima de itens: 3  
         4. Se houver mais de 3 artigos relacionados, devem ser exibidos os 3 primeiros artigos da lista.  
         5. Este sub bloco é opcional. Se o artigo não tiver artigos relacionados, o bloco principal continua a ser apresentado, mas este sub bloco não será visível.

   4. **Navegação em profundidade para *Lista de Artigos***  
      1. Não disponível

   

---

2. #### **Destaques Secundário** ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-140804&t=vCIDrrbnNCSgd5ya-4))    Seleção de outros artigos destacados da curadoria manual SAPO. 

   1. **UI-Layout**: Genérico

   2. **Conteúdo**: Estático

   3. **Regras de Exibição**  
      1. Aplicam-se as regras de exibição do [Blocos com UI-Layout Genérico](#blocos-com-ui-layout-genérico).

   4. **Navegação em profundidade para Lista de Artigos**  
      1. Não disponível

---

3. #### **Destaque 100%** ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=12241-13050&t=1Q7Q88cW2QsEdz7h-4))    Bloco de destaque de item único. Apresenta destaque de curadoria manual SAPO.  

   1. **UI-Layout**: Estático

   2. **Conteúdo**: Estático

   3. **Regras de exibição**  
      1. Quantidade de itens: Sempre exibe apenas 1 artigo por vez

   4. **Navegação em profundidade para Lista de Artigos**  
      1. Não disponível

---

4. #### **Hot Topics** ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=12241-12904&t=1Q7Q88cW2QsEdz7h-4))    Bloco que exibe os *Hot Topics* e os respectivos artigos relacionados a eles.  {#hot-topics-(ver-em-figma)-bloco-que-exibe-os-hot-topics-e-os-respectivos-artigos-relacionados-a-eles.}

   1. **UI-Layout**: Específico

   2. **Definições**  
      1. Payload de Hot Topics: Ficheiro json recebido via RabbitMQ que contém uma lista de *Hot Topics*;  
      2. Hot Topic: É um agrupamento de *Tópicos*. Cada Hot Topic contém uma lista de tópicos e uma lista de categorias.    
      3. Tópico: É conceito do agrupamento de múltiplos artigos que fazem parte de um mesmo assunto. Cada Tópico contém uma lista de tags e uma lista de categorias.  

   3. **Conteúdo** \- Dinâmico  
      1. Para cada Tópico, a aplicação deve buscar os artigos satisfaçam:   
         (tag1 OR tag2 OR ... OR tagN) AND (categ1 OR categ2 OR ... OR categM)  
           
      2. Se um Tópico tiver categorias associadas, então devem ser utilizadas as categorias e tags associadas a este tópico;

      3. Se um Tópico não tiver categorias associadas (isto é, só tiver tags), as categorias a serem usadas na query devem ser as categorias associadas ao Hot Topic pai (caso existam).  
           
      4. Se não houverem categorias associadas nem tópico nem no hot topic (pai), então a consulta deve ser realizada apenas pela tags associadas ao tópico.  
           
            
   4. **Regras de exibição**  
      1. Lista de Artigos  
         1. Quantidade de itens: Fixo em 3  
         2. Não deve ser exibido para Hot Topics com menos de 3 artigos  
         3. Ordenação: Os artigos devem ordenados por data de publicação (desc)    
      2. Carrossel de Tags (Hot Topics)  
         1. Quantidade mínima de itens: 1  
         2. Quantidade máxima de itens: Ilimitado  
         3. Não deve ser exibido se não houver pelo menos 1 Hor Topic em exibição

   5. **Navegação em profundidade para Lista de Artigos**  
      1. Disponível

---

8. #### **As Mais populares** ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-140849&t=1Q7Q88cW2QsEdz7h-4))    Exibe os artigos mais visualizados no portal SAPO. 

   1. **UI-Layout**: Genérico

   2. **Conteúdo**: Estático

   3. **Regras de exibição**  
      1. Aplicam-se as regras de exibição do [Blocos com UI-Layout Genérico](#blocos-com-ui-layout-genérico).  
           
   4. **Fluxos de Exceção**  
      1. Se o payload incluir IDs de artigos que não existam ou não estejam disponíveis na app, estes devem ser ignorados. Apenas os artigos efetivamente disponíveis devem ser exibidos no bloco.

   5. **Navegação em profundidade para Lista de Artigos**  
      1. Não disponível

   6. **Notas**  
      1. No MVP, as métricas de visualização são calculadas exclusivamente com base nas visualizações de artigos no portal web do SAPO e recebidas via RebbitMQ (conforme o mesmo processo utilizando os ficheiros de destaque). A consolidação dessas visualizações com as obtidas na app é um requisito pós-MVP, a ser tratado futuramente.

---

9. #### **Opinião** ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-140859&t=1Q7Q88cW2QsEdz7h-4))    Destaque de artigos de opinião, selecionados pela curadoria SAPO. 

   1. **UI-Layout**: Genérico

   2. **Conteúdo**: Estático

   3. **Regras de Exibição**  
      1. Aplicam-se as regras de exibição do [Blocos com UI-Layout Genérico](#blocos-com-ui-layout-genérico).

   4. **Navegação em profundidade para Lista de Artigos**  
      1. Disponível

   5. **Fluxos de Exceção:**  
      1. Se houver mais de um autor associado ao mesmo artigo, deve ser considerado como opinador apenas o primeiro autor da lista. Os outros autores devem ser ignorados;

      2. Se não houver nenhum autor (author.name) associado ao artigo, então deve ser assumido o campo Parceiro (partner.title) como o autor do artigo.

         

      3. Se não houver nenhuma imagem associada ao autor do artigo, então a aplicação deve exibir uma imagem de placeholder como fallback. 

      4. **Nota**: A imagem/logo do parceiro nunca deve ser utilizada em substituição a imagem do autor. Caso o parceiro seja assumido como autor, então deve ser utilizada a imagem placeholder. 

---

10. #### **Sugestões do Dia** ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-140885&t=1Q7Q88cW2QsEdz7h-4))     Conjuntos de artigos destacados sugeridos diariamente pela curadoria manual SAPO. 

    1. **UI-Layout**: Genérico

    2. **Conteúdo**: Estático

    3. **Regras de Exibição**  
       1. Aplicam-se as regras de exibição do [Blocos com UI-Layout Genérico](#blocos-com-ui-layout-genérico).

    4. **Navegação em profundidade para Lista de Artigos**  
       1. Não disponível

    5. **Notas**  
       1. Para MVP não está contemplado no escopo os widgets patrocinados (no portal eles exibidos em conjunto ao artigo patrocinado, que é sempre o último item do bloco). 

---

11. #### **Temáticos**     Blocos de destaque segmentados por temática.  

    1. **Blocos**: Ao todo devem existir 3 blocos temáticos:  
       1. Notícias ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-140895&t=1Q7Q88cW2QsEdz7h-4))  
       2. Desporto ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-140915&t=1Q7Q88cW2QsEdz7h-4))  
       3. Cultura e Lifestyle. ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-140925&t=1Q7Q88cW2QsEdz7h-4))

    2. **UI-Layout**: Genérico

    3. **Conteúdo**: Estático

    4. **Regras de Exibição**  
       1. Aplicam-se as regras de exibição do [Blocos com UI-Layout Genérico](#blocos-com-ui-layout-genérico).

    5. **Navegação em profundidade para Lista de Artigos**  
       1. Disponível

---

12. #### **Últimas** ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-140925&t=1Q7Q88cW2QsEdz7h-4))     Grupo destacado de últimas notícias publicadas. 

    1. **UI-Layout**: Genérico

    2. **Conteúdo**: Dinâmico  
       1. Exibe os últimos 10 artigos publicados na app.

    3. **Regras de Exibição**  
       1. Deve ser sempre o último bloco, independente de quantos blocos existam;  
       2. Aplicam-se as regras de exibição do [Blocos com UI-Layout Genérico](#blocos-com-ui-layout-genérico).

    4. **Navegação em profundidade para Lista de Artigos**  
       1. Disponível

    5. **Notas**  
       1. Este bloco não está presente no payload do ecrã de destaques, pois não utiliza nenhum dos atributos de configuração presentes no payload. 

---

Requisitos Técnicos

1. ### Payload {#payload}

   1. **Requisitos Gerais**  
      1. A app deve receber um ficheiro único contendo a estrutura completa de payload para a página Explore.  
      2. Este ficheiro deve conter uma array de blocos, representando os blocos que devem ser renderizados na página.  
      3. Sempre que um novo ficheiro for recebido, ele substitui completamente o anterior.

   2. **Estrutura do payload**  
      1. type:  (obrigatório):  
         1. Define o tipo de bloco (por exemplo: "hot-topics", "opinião", "últimas").  
         2. Deve ser utilizado pela app para determinar o comportamento, layout e lógica de exibição aplicáveis ao bloco;  
         3. Os valores a serem recebidos neste campo devem estar dentro do subset especificado na tabela abaixo. Cada bloco tem seu valor próprio de type esperado.   
         4. Caso este atributo não seja informado, ou possua valores diferentes do esperado, o bloco não deve ser exibido no Explore.  
         5. **Exceções**: Os blocos Blocos *Hot Topics* e *Últimas* não estão presentes no ficheiro, e são incluídos pela aplicação de forma fixa em MVP. 

| Bloco | Valor |
| ----- | ----- |
| Destaque Principal | main\_highlights |
| Destaques Secundários | secondaries\_highlights |
| Hot Topics | hot\_topics |
| Destaque 100% | highlight\_100 |
| As Mais Populares | most\_popular |
| Opinião | opinion |
| Sugestões do Dia | suggestionsDay |
| Temático Notícias | category\_news |
| Temático Desporto | category\_sports |
| Temático Lifestyle | cateory\_lifestyle |

      2. name (opcional):  
         1. Define o título do bloco a ser apresentado no layout;  
         2. **Nota**: Para o **MVP**, este campo **não será utilizado**. Os títulos devem ser definidos diretamente no backend, de forma estática.

      3. highlightsGroupId (obrigatório para blocos de conteúdo estático):  
         1. Refere-se ao ID do ficheiro de destaques (highlights-group) que contém os artigos a serem exibidos no bloco;  
         2. Deve ser um atributo obrigatório para todos dos blocos de conteúdo estático;  
         3. Quando não for informado para um bloco de conteúdo estático, o bloco não deve ser exibido na página *Explore*.

      4. hotTopicId (obrigatório para o bloco Hot Topics):  
         1. Refere-se ao ID do ficheiro de hot topic (hotTopic) que contém as tópicos, categorias e tags que devem ser utilizadas para filtrar os artigos para cada tópico (ver regras de negócio nos [requisitos do bloco Hot Topic](#hot-topics-\(ver-em-figma\)-bloco-que-exibe-os-hot-topics-e-os-respectivos-artigos-relacionados-a-eles.)).

      5. interval (opcional):  
         1. Define o intervalo de artigos a ser considerado dentro de um highlightsGroupId;  
         2. Permite que múltiplos blocos ou áreas da app reutilizem o mesmo ficheiro de destaques, exibindo subconjuntos distintos.

      6. interval.start (opcional):  
         1. Índice do primeiro artigo a ser exibido;  
         2. Caso não seja definido, é assumido valor default \= 0\.  
               
      7. interval.length (opcional):  
         1. Define o número de artigos a serem exibidos a partir de interval.start;  
         2. Caso não seja definido, a aplicação deve considerar todos os artigos do grupo de destaques a partir do interval.start.  
         3. Em blocos de conteúdo com um único artigo, o atributo deve ser ignorado, assumindo o valor padrão de 1\. Apenas o artigo correspondente ao índice em interval.start será exibido.

      8. categoryIds (obrigatório para blocos temáticos com navegação em profundidade disponível):  
         1. Utilizado por blocos com navegação em profundidade disponível;  
         2. Define as categorias que devem ser passadas como parâmetro de filtro para a consulta dos artigos que serão exibidos na página [*Lista de Artigos*](?tab=t.7ia3otqqi5x).

         3. **⚠️ ️ DISCLAIMER**: Este atributo é do tipo lista e permite múltiplos valores de categoria. No entanto, as primeiras versões da app (MVP, V1 e V2) não suportam mais de um valor. Caso este atributo seja preenchido mais de uma categoria, a aplicação irá considerar apenas o primeiro valor da lista. 

            1. ℹ️ Por que este atributo recebe uma lista? \-\> Decisão da equipa técnica SAPO para antecipar no modelo dados futuras necessidades de ter mais flexibilidade para criar filtros mais específicos e granulares na página *Lista de Artigos*.

            2. ℹ️ Por que a app não suporta múltiplos valores? \-\>A atual apresentação da *Lista de Artigos* foi concebida para mostrar conteúdo de uma única temática, possibilitando a exploração de subtemáticas dentro da temática selecionada. A seleção de diversas temáticas simultaneamente compromete a estrutura visual e a organização hierárquica estabelecida.

      9. tagIds (opcional):  
         1. Utilizado por blocos com navegação em profundidade disponível;  
         2. Define as tags que devem ser passadas como parâmetro de filtro para a consulta dos artigos que serão exibidos na página [*Lista de Artigos*](?tab=t.7ia3otqqi5x).

---

Anexo \- Payload da Página de Destaques do *Explore*

```
[
    {
        "type": "main_highlights",
        "name": null, 
        "highlightsGroupId": "67a61faaf70f44caf596b5a9",
        "hotTopicId": null,
        "interval": {
            "start": 5,
            "length": 1 
        },
        "categoryIds": null,
        "tagIds": null
    },
    {
        "type": "secondaries_highlights",
        "name": null, 
        "highlightsGroupId": "67a61faaf70f44caf596b5a9",
        "hotTopicId": null,
        "interval": {
            "start": 5,
            "length": 10 
        },
        "categoryIds": null,
        "tagIds": null
    },
    {
        "type": "hot_topics",
        "name": null,
        "highlightsGroupId": null,
        "hotTopicId": "56hrhfaaf70af596tht5",
        "interval": {
            "start": 1,
            "length": 1 
        },
        "categoryIds": null,
        "tagIds": null
    },
    {
        "type": "highlight_100", 
        "name": null,
        "highlightsGroupId": "67a61faaf70f44caf596b5a9",
        "hotTopicId": null,
        "interval": {
            "start": 1,
            "length": 1 
        },
        "categoryIds": null,
        "tagIds": null
    },
    {
        "type": "most_popular",
        "name": "As Mais Populares",
        "highlightsGroupId": "67a61faaf70f44caf596b5a9",
        "hotTopicId": null,
        "interval": {
            "start": 5,
            "length": 10 
        },
        "categoryIds": null,
        "tagIds": null 
    },
    {
        "type": "opinion",
        "name": "Opinião",
        "highlightsGroupId": "67a61faaf70f44caf596b5a9",
        "hotTopicId": null,
        "interval": {
            "start": 5,
            "length": 10 
        },
        "categoryIds": [
            "676d3fe6ebd8a83755d40838",
            "676d3fe6ebd8a83755d40895"
        ],
        "tagIds": null 
    },
    {
        "type": "suggestionsDay",
        "name": "Sugestão do Dia",
        "highlightsGroupId": "67a61faaf70f44caf596b5a9",
        "hotTopicId": null,
        "interval": {
            "start": 5,
            "length": 10 
        },
        "categoryIds": null,
        "tagIds": null 
    },
    {
        "type": "category_news",
        "name": "Notícias",
        "highlightsGroupId": "67a61faaf70f44caf596b5a9",
        "hotTopicId": null,
        "interval": {
            "start": 5,
            "length": 10 
        },
        "categoryIds": [
            "676d3fe6ebd8a83755d40838",
            "676d3fe6ebd8a83755d40895"
        ],
        "tagIds": [
            "676d3fe6ebd8a83755d40838",
            "676d3fe6ebd8a83755d40899"
        ]
    },
    {
        "type": "category_sports",
        "name": "Desporto",
        "highlightsGroupId": "67a61faaf70f44caf596b5a9",
        "hotTopicId": null,
        "interval": {
            "start": 5,
            "length": 10 
        },
        "categoryIds": [
            "676d3fe6ebd8a83755d40838",
            "676d3fe6ebd8a83755d40895"
        ],
        "tagIds": [
            "676d3fe6ebd8a83755d40838",
            "676d3fe6ebd8a83755d40899"
        ]
    },
    {
        "type": "category_lifestyle",
        "name": "Cultura e Lifestyle",
        "highlightsGroupId": "67a61faaf70f44caf596b5a9",
        "hotTopicId": null,
        "interval": {
            "start": 5,
            "length": 10 
        },
        "categoryIds": [
            "676d3fe6ebd8a83755d40838",
            "676d3fe6ebd8a83755d40895"
        ],
        "tagIds": [
            "676d3fe6ebd8a83755d40838",
            "676d3fe6ebd8a83755d40899"
        ]
    }
]
```

