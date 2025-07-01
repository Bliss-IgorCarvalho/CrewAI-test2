# Pesquisa de Artigos

---

### **Pesquisa de Artigos no Explore**

O utilizador deve poder pesquisar artigos através de um campo de busca por texto. 

Requisitos de Design

1. [Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=10691-32739&t=7o6g8kz0gO3RXhxY-4)

Requisitos Funcionais

1. #### **Requisitos Gerais**

   1. **Tipo de Conteúdo**: Apenas artigos devem ser considerados para a pesquisa (capas não estão incluídas);  
   2. **Limite temporal**: As pesquisa deve ser baseada  em artigos publicados nos últimos 6 meses

---

2. #### **Pesquisa por texto**    O utilizador pode pesquisar artigos através de qualquer termo textual introduzido no campo de pesquisa.  {#pesquisa-por-texto-o-utilizador-pode-pesquisar-artigos-através-de-qualquer-termo-textual-introduzido-no-campo-de-pesquisa.}

   1. **Mecanismo de pesquisa**  
      1. A pesquisa é do tipo simples, realizada em base de dados e exibe resultados que correspondem exatamente aos termos introduzidos.

   2. **Referência de pesquisa**  
      A funcionalidade de pesquisa por texto nos artigos considera os seguintes campos de conteúdo para encontrar correspondências com os termos introduzidos pelo utilizador:  
      1. **Título** do artigo (title);  
      2. **Lead** do artigo (lead);  
      3. **Texto** do artigo (content).

   3. **Resultados**  
      1. A pesquisa deve gerar como resultado uma lista de artigos correspondente ao termos pesquisados;  
      2. Máximo de itens: ilimitado com paginação de 10  
      3. A página de resultados deve exibir um disclaimer que informe ao utilizador que a pesquisa foi realizada com base em artigos publicados nos últimos 6 meses. 

---

3. #### **Pesquisa por termo sugerido**    O utilizador pode pesquisar artigos através de termos sugeridos pela aplicação. Conforme requisitos da função [*Autocomplete*](#autocomplete-\(ver-em-figma\)-a-aplicação-deve-exibir-sugestões-de-termos-de-pesquisa-com-base-nos-caracteres-já-digitados-pelo-utilizador-no-campo-de-pesquisa;).  {#pesquisa-por-termo-sugerido-o-utilizador-pode-pesquisar-artigos-através-de-termos-sugeridos-pela-aplicação.-conforme-requisitos-da-função-autocomplete.}

   1. **Mecanismo de pesquisa**  
      1. Ao pesquisar por um termo sugerido, o utilizador deve ser redirecionado para o ecrã [*Lista de Artigos*](?tab=t.7ia3otqqi5x). A lista de artigos deve ser automaticamente filtrada pelo atributo correspondente ao termo sugerido selecionado.  
         1. **Exemplo**: Ao digitar no campo de pesquisa o termo “Eco”, a aplicação sugere a categoria *Economia*. O utilizador clica na sugestão e é redirecionado para o ecrã *Lista de Artigos*, que automaticamente é filtrado pela categoria *Economia*.

   2. **Referência de pesquisa**  
      A pesquisa por termo sugerido considera os seguintes metadados do artigo:  
      1. **Temática** associada ao artigo (parentCategory ou category);  
      2. **Sub-temática** associada ao artigo (category);  
      3. **Fonte/parceiro** associado ao artigo (partners);  
      4. **Autores** associados ao artigo (authors);   
      5. **Tags** associadas ao artigo;  
         1. Aplicável apenas para artigos que possuam tags (processados em data enrichment).

#### ---

4. #### **Histórico de Pesquisa** ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-141153&t=UEF0pbrbAh9N2ydQ-4))    Deve ser exibido um histórico dos últimos termos pesquisados pelo utilizador 

   1. **Regras de Exibição**  
      1. O histórico deve ser exibido quando o utilizador tem o cursor no campo de pesquisa e digitou menos de 3 caracteres;  
      2.  Devem ser exibidos os últimos **5** termos pesquisados.

   2. **Pesquisa**  
      1. Ao escolher um termo sugerido, a aplicação de realizar uma [pesquisa por texto](#pesquisa-por-texto-o-utilizador-pode-pesquisar-artigos-através-de-qualquer-termo-textual-introduzido-no-campo-de-pesquisa.).

---

5. #### **Autocomplete** ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-141195&t=UEF0pbrbAh9N2ydQ-4))    A aplicação deve exibir sugestões de termos de pesquisa com base nos caracteres já digitados pelo utilizador no campo de pesquisa;  {#autocomplete-(ver-em-figma)-a-aplicação-deve-exibir-sugestões-de-termos-de-pesquisa-com-base-nos-caracteres-já-digitados-pelo-utilizador-no-campo-de-pesquisa;}

   1. **Regras de Exibição**  
      1. A sugestão de termos de pesquisa deve ser exibida quando o utilizador tem o cursor no campo de pesquisa e já digitou 3 ou mais caracteres.

   2. **Sugestões**  
      Os termos sugeridos pela aplicação devem ser atributos do artigo e agrupados visualmente por:  
      1. Palavra chave  
         1. Exibe o texto exato digitado pelo utilizador  
         2. Sempre deve ser exibido na primeira posição da lista  
         3. Ao ser clicado aciona uma **pesquisa por texto**

      2. Fonte  
         1. Exibe nome de fontes/parceiros (partner.title) que correspondam com o texto digitado  
         2. Ao ser clicado aciona uma pesquisa por termo sugerido

      3. Temática e/ou sub-temática  
         1. Exibe nome de temáticas ou sub-temáticas (category.name) que correspondam com o texto digitado  
         2. Ao ser clicado aciona uma pesquisa por termo sugerido

      4. Autor  
         1. Exibe nome de autores (authors.name) que correspondam com o texto digitado  
         2. Ao ser clicado aciona uma pesquisa por termo sugerido

      5. Tag (Sugestões)  
         1. Exibe nome de tags que correspondam com o texto digitado  
         2. Ao ser clicado aciona uma pesquisa por termo sugerido

   3. **Pré seleção de sugestões**  
      1. A app deve pré-selecionar, para exibição nas sugestões de Autocomplete, apenas os atributos de artigo (Temática/Sub-temática, Fonte/Parceiro, Autor e Tag) que possuam pelo menos um artigo publicado nos últimos 6 meses;  
      2. A pré-seleção deve ocorrer como uma rotina, executada a cada 2 horas;  
      3. Cada vez que a rotina é executada, cria-se uma lista de atributos. Esta lista serve de base para as sugestões apresentadas até à próxima execução da rotina, que gerará uma nova lista;  
      4. Artigos novos com atributos não incluídos na seleção prévia só aparecerão na lista gerada na próxima execução da rotina. Novas Temáticas, Sub-temas, Fontes, Autores ou Tags podem levar até 2 horas para serem exibidos nas sugestões.

   4. **Pesquisa**  
      1. Ao escolher um termo sugerido, a aplicação deve realizar uma [pesquisa por termo sugerido](#pesquisa-por-termo-sugerido-o-utilizador-pode-pesquisar-artigos-através-de-termos-sugeridos-pela-aplicação.-conforme-requisitos-da-função-autocomplete.).

---

