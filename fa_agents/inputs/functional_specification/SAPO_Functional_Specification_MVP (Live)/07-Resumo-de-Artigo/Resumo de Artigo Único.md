# Resumo de Artigo Único

---

Design

1. [Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7794-63518&t=QIuuKTOhs2MdzqAr-4)

Requisitos Funcionais

1. **Requisitos Gerais**  
   1. Todos os *Resumos de Artigo Único* devem ser exibidos em formato *Stories*;  
   2. Cada resumo deve ser composto múltiplos *Stories*;  
   3. O conteúdo do *Resumo de Artigo Único* deve ser totalmente baseado nos resumos em texto associados ao artigo;   
   4. Outros tipos de media ou embeds disponíveis no artigo (fotogaleria, vídeos, etc) não devem ser utilizados nem exibido nos resumos. 

2. **Acesso e Reprodução**  
   1. Acesso ao resumo de artigo: O utilizador deve poder aceder ao resumo de artigo único através das áreas:  
      1. Feed → Através das ações disponíveis no card/preview do artigo ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-65876&t=dm4TUoskIomG9rAf-4))  
      2. Página de Artigo → Através das ações disponíveis no detalhe do artigo ([ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-100425&t=l0h17j8L2oZnbJVj-4))

   2. Aviso de conteúdo criado por IA: Ao aceder o resumo, a aplicação deve exibir o aviso de conteúdo criado por IA, conforme regras especificadas na [funcionalidade](?tab=t.xzrfike6umrp).

3. **Artigos Elegíveis:**  
   Critérios de seleção que definem quais artigos disponíveis são elegíveis para geração e reprodução de resumo em formato Stories:    
   1. Artigos incluídos:  
      1. Artigos (em geral) que possuam resumo em texto.

   2. Artigos não incluídos:  
      1. Artigos (em geral) que não possuam resumo em texto;  
         1. Exemplos: Artigos cujo parceiro não autorize processamento por AI.   
      2. **Artigos de opinião**: Artigos de opinião não possuem resumo;  
      3. **Artigos ao minuto**: O conteúdo pode ser demasiado grande e perde-se o conceito de timeline.

4. **Layout e Componentes**  
   1. Resumo um artigo:  
      1. Conjunto de múltiplos stories que compõem um resumo de um único artigo.

   2. Story de um resumo:  
      1. **Texto**: Cada *Story* deve exibir o conteúdo de um bullet point do *resumo em texto* associado ao artigo, conforme requisitos especificados em [Fluxo de Geração \- Resumos, 1\. Estrutura do Resumo](?tab=t.n3takcnnq7o1);  
      2. **Imagem**: Todo os *Stories* do resumo (de um mesmo artigo) devem utilizar a imagem principal do artigo como plano de fundo (quando houver);  
         1. Quando não houver a imagem principal do artigo, os resumos devem apresentar apenas o texto e componentes visuais a serem definidos em UI.

   3. Fonte:  
      1. Exibe **nome** da Fonte associada ao artigo.  
      2. atributo partner.title

   4. Tempo/Data de publicação:  
      1. Exibe a informação de quando o artigo foi publicado:  
      2. Aplicam-se as mesmas regras de referência e formato da [Página de Artigos](https://docs.google.com/document/d/1a3t5THaJcIA4sg-vOfnkq44QXRPjn7N72hBHLhH5yEY/edit?tab=t.skvfiivnrta2).

   5. Barra de progresso do story:  
      1. Barra de progresso dinâmica, que indica a quantidade de stories disponíveis no resumo atual e em qual story o utilizador se encontra. A barra deve avançar à medida que o utilizador percorre cada story (tal como no Instagram).

   6. Temática/Subtemática:  
      1. Exibe o nome da temática ou sub-temática associada ao artigo    
      2. Atributo (category.name)  
      3. Aplicam-se as mesmas regras da [Página de Artigos](https://docs.google.com/document/d/1a3t5THaJcIA4sg-vOfnkq44QXRPjn7N72hBHLhH5yEY/edit?tab=t.skvfiivnrta2).

   7. Aviso de conteúdo criado por IA:  
      1. Ver requisitos no escopo da [funcionalidade](https://docs.google.com/document/d/1uUaEqci9KOMwbfr-ZIowWBjzusV7uY_avEmvADxGgw4/edit?tab=t.8ufhlzav52jg).

   8. CTA \[Ver artigo completo\]:  
      1. Para os artigos com vídeo, fotogalerias ou podcast o ícone do CTA \[Ver artigo completo\] é alterado consoante ao tipo de media do artigo, adotando o respetivo ícone. Segue a mesma regra do thumbnail de artigo no Feed

5. **Ações**  
   1. **Ver artigo completo**: O utilizador deve ser redirecionado para a página de artigo para visualização do artigo completo;   
      1. Ao retornar, o utilizador deve poder voltar para o resumo no story de origem de onde entrou.

   2. **Reportar problema:** O utilizador deve poder reportar problemas no conteúdo.  
      1. Ver requisitos no escopo da [funcionalidade](?tab=t.bmoeqea3zr7s).  
      2. **Disclaimer**: Esta ação deve estar disponível apenas após a implementação da funcionalidade [Reportar Problema](https://docs.google.com/document/d/1uUaEqci9KOMwbfr-ZIowWBjzusV7uY_avEmvADxGgw4/edit?tab=t.x1qn29dlpsyr).

   3. **Partilhar digest**: O utilizador deve poder partilhar o resumo com outras plataformas e utilizadores.   
      1. Ver requisitos no escopo da [funcionalidade](?tab=t.7t57iyz5hp70).  
      2. **Disclaimer**: Esta ação deve estar disponível apenas após a implementação da funcionalidade *Partilha de Conteúdo*.

   4. **Reiniciar exibição do resumo**: Ao chegar ao final da exibição do resumo, após o último step do último story, o utilizador deve poder reiniciar a exibição do resumo. 

6. **Navegação**  
   1. Avançar para o próximo story do resumo actual  
      1. Interação: Tap-right  
      2. ~~No último story navega para o wrap-up~~

   2. Voltar ao story anterior do resumo actual  
      1. Interação: Tap-left  
      2. No primeiro story reinicia o story 

   3. Pausar story do resumo actual  
      1. Interação: Long press

   4. Fechar resumo de artigo único:  
      1. Interação: Clique no CTA \[X\]  
         1. Encerra a reprodução do resumo, fechando o componente story, independentemente do story (primeiro, segundo ou terceiro).

      2. Interação: Swipe-left  
         1. Encerrar a reprodução do resumo, fechando o componente story, independentemente do story (primeiro, segundo ou terceiro).

      3. Redirecionamento  
         1. Ao fechar o componente, o utilizador deve ser direcionado de volta para o Feed de artigos ou para a Página de Artigo, consoante onde se acedeu ao resumo.

7. **Wrap-up**  
   1. Ao final da exibição do resumo a app deve exibir:   
      1. Para artigos em template Padrão (SAPO): A lista de Artigos Relacionados.  
         1. **Disclaimer**: Este comportamento deve estar disponível apenas após a implementação da funcionalidade *Artigos Relacionados*.  
      2. Para artigos em template de Parceiros: A lista de Artigos relacionada ao bloco Destaques do Parceiro (Ver requisitos da [Página de Artigos](?tab=t.93skitw4a6qf)).

8. **Limite para utilizadores anónimos**  
   1. Para MVP não deve haver limite de uso desta funcionalidade. O controle e limite de utilização deve ser implementado em pós MVP, após a implementação do Login.   
      1. Nota: Criado o [Ticket 33393](https://dev.azure.com/blissapps/SAPO%20App/_workitems/edit/33393) em DevOps para inclusão deste desenvolvimento em pós MVP.

---

