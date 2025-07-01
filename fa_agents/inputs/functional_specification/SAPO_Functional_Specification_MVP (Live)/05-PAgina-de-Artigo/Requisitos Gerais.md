# Requisitos Gerais & Template Padrão

Regras aplicáveis a todos os templates  
---

Requisitos de Design

1. [Ver design em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=6081-41075&t=d393wPn6Kz5XhKSI-4)

Requisitos Funcionais

1. #### **Layout & Componentes**

   1. Logo da fonte:  
      1. Default: Exibe a **imagem logo** da Fonte associada ao artigo.  
      2. Fallback: Para artigos de fontes que não possuam ou por algum motivo não seja possível obter a imagem do logo, este componente não deve ser exibido. 

   2. Fonte: Exibe **nome** da Fonte associada ao artigo.  
      1. atributo partner.title

      2. Fontes clicáveis:  
         1. As fontes devem ser clicáveis;  
         2. Ao clicar em uma fonte, o utilizador deve ser redirecionado para um ecrã do tipo [lista de artigos](?tab=t.7ia3otqqi5x);  
         3. Após o redirecionamento, a lista de artigos deve ser automaticamente filtrada, exibindo apenas artigos que estejam associados à mesma fonte escolhida pelo utilizador, ordenados por ordem descendente pela data de publicação \[publishedAt\] (o mais recente no topo). 

   3. Tempo/Data de publicação: Exibe a informação de quando o artigo foi publicado:    
      1. **Referência**  
         1. O cálculo de tempo/data de publicação do artigo deve utilizar o valor do atributo publishedAt;  
         2. Timezone: Deve ser assumido que os valores retornados por publishedAt estarão sempre no fuso horário de Lisboa.

      2. **Formato**: A informação deve ser apresentada em diferentes formatos, consoante a data e hora da publicação  
         1. Formato em ‘**min**’:  
            1. Exibido se o artigo foi publicado a menos de 1 hora  
            2. Deve exibir o formato há X **min** (exemplo: há 5 min)  
            3. Onde X é a diferença em **minutos** entre data e hora atual e data e hora da publicação do artigo.  
         2. Formato em ‘**horas**’:  
            1. Exibido se o artigo foi publicado a mais de 1 hora e menos de 24 horas  
            2. Deve exibir o formato há X **horas** (exemplo: há 2 horas)  
            3. Onde X é a diferença em **horas** entre data e hora atual e a data e hora da publicação do artigo.  
         3. Formato em ‘**dias**’:  
            1. Exibido se o artigo foi publicado a mais de 24 horas e menos de 168 horas (7 dias)  
            2. Deve exibir o formato há X **dias**  (exemplo: há 3 dias)  
            3. Onde X é a diferença em **dias** entre data atual e a data da publicação do artigo  
         4. Formato em ‘**data**’:  
            1. Exibido se o artigo foi publicado a mais de 168 horas (7 dias)  
            2. Deve exibir o formato **dia mês ano** (exemplo: 20 nov 2024)  
            3. Onde dia mês ano corresponde **exatamente** a data da publicação do artigo (publishedAt)

   4. Título: Exibe do título do artigo.   
      1. Atributo title

   5. Autores: Exibe o nome dos autores do artigo  
      1. Atributo authors.name;  
      2. Pode conter múltiplos valores/autores:  
         1. Quando houver mais de um autor, os nomes devem ser separados por separador a ser definido em Design.  
      3. Pode não conter nenhum valor/autor:  
         1. Quando não houver nenhum valor/autor, o componente não deve ser exibido.

   6. Tempo estimado de leitura: Exibe o tempo médio estimado para conclusão da leitura do artigo:  
      1. O cálculo deve ser realizado pelo serviço de AI, durante processo de data enrichment;  
      2. O cálculo deve ser baseado no conteúdo de texto do artigo;  
      3. O tempo estimado deve ser sempre apresentado em minutos.

   7. Temática / Sub-temática: Exibe o nome da temática ou sub-temática associada ao artigo (category.name).   
      1. Se o artigo **estiver** associado a uma Sub-temática   
         1. Então deve ser exibido o nome da sub-temática associada ao artigo.  
            1. Nota técnica: Se **Regra de Exibição**:  \!= null .

      2. Se o artigo **não estiver** associado a uma Sub-temática **e estiver** associado apenas a uma Temática:  
         1. Então deve ser exibido o nome da temática associada ao artigo.  
            1. Nota técnica: Se parentCategory \= null (ou não existir).

      3. Temáticas / Sub-temáticas clicáveis:  
         1. O componente deve ser clicável;  
         2. Ao clicar no componente, o utilizador deve ser redirecionado para um ecrã do tipo [lista de artigos](?tab=t.7ia3otqqi5x);  
         3. Após o redirecionamento, a lista de artigos deve ser automaticamente filtrada, exibindo apenas artigos que estejam associados à mesma temática ou sub-temática escolhida pelo utilizador, ordenados por ordem descendente pela data de publicação \[publishedAt\] (o mais recente no topo).  

   8. Media principal:  
      1. Default: Exibe a imagem principal do artigo (atributo mainImage)  
      2. Exceção: Para artigos que não possuam ou por algum motivo não seja possível obter a imagem principal, este componente não deve ser exibido. 

   9. Lead: Exibe o lead do artigo.   
      1. Atributo lead

   10. Texto: Texto completo do artigo.  
       1. Atributo content

   11. Seção Tags: Exibe as tags associadas ao artigo  
       1. Regras de exibição:  
          1. O componente/secção deve ser exibido somente se houver ao menos 1 tag associada ao artigo;  
          2. Devem ser exibidas no máximo 5 tags. Mesmo que o artigo possua mais de 5 tags associadas;  
          3. Se o artigo possuir mais de 5 tags associadas, devem ser exibidas as 5 primeiras tags conforme ranking de relevância retornado pelo serviço de AI.   
                
       2. Tags clicáveis:  
          1. As tags devem ser clicáveis;  
          2. Ao clicar em uma tag, o utilizador deve ser redirecionado para um ecrã do tipo [lista de artigos](?tab=t.7ia3otqqi5x);  
          3. Após o redirecionamento, a lista de artigos deve ser automaticamente filtrada, exibindo apenas artigos que estejam associados à mesma tag escolhida pelo utilizador. 

   12. Secção Feedback: Elemento interativo que permite ao utilizador indicar se gostou ou não do artigo (botões “Sim” e “Não”).  
       1. As ações realizadas neste componente são execuções da funcionalidade Feedback da relevância (Like/Dislike);    
       2. Os requisitos funcionais e regras de comportamento estarão especificados no escopo da funcionalidade;  
       3. **Disclaimer**: Para MPV, os dados de interação do utilizador (like/dislike) serão coletados e armazenados para fins de analytics e histórico de interações, mas não terão efeito na apresentação de conteúdo na app, seja em Feed ou Explore.

2. #### **Navegação entre Artigos**

   1. Descrição Geral  
      1. A aplicação deve permitir a leitura contínua de artigos encadeados.

   2.  Regras de Encadeamento  
      1. A função de encadeamento deve estar disponível apenas quando o acesso ao artigo é feito a partir do Feed;  
      2. A navegação entre artigos faz‑se por navegação scroll horizontal (swipe →left para próximo e swipe →right para anterior).  
      3. Ao renderizar um artigo, a aplicação deve carregar automaticamente o artigo seguinte;  
      4. A sequência de artigos segue rigorosamente a ordenação do Feed (posição atual \+ 1);

      5. Exemplo:   
         1. Quando um utilizador acede a um artigo na posição 5 do Feed a aplicação prepara o artigo da posição 6 para exibição. Esta sequência mantém-se consistente para todas as posições no Feed.

      

   3. Comportamento de Navegação  
      1. Próximo artigo (swipe → left)   
         1. O próximo artigo é exibido quando o utilizador faz swipe‑left até ao limite direito da página do artigo atual.  
         2. O encadeamento deve ser interrompido quando o utilizador atinge a **última posição** do Feed.

      2. Artigo Anterior (swipe ← right)  
         1. O artigo anterior é exibido quando o utilizador faz swipe‑right até ao limite esquerdo da página do artigo atual.  
         2. O encadeamento deve ser interrompido quando o utilizador atinge a posição original de acesso no Feed. Ou seja, quando atinge a posição do artigo que foi clicado quando ainda estava no Feed..

         

      3. Retorno ao Feed  
         1. Quando o utilizador fecha o componente de página de artigo, é redirecionado para o ecrã antecessor (Feed);  
         2. A posição original de acesso no Feed é preservada ao retornar.

            Exemplo:  
            1.  Utilizador inicia na posição 5 do Feed,  
            2.  Navega progressivamente através dos artigos até à posição 8,  
            3.  Ao retornar ao Feed, a aplicação mantém o scroll do Feed na posição 5\.

      4. Secção Artigos Relacionados  
         1. A navegação entre artigos não deve estar disponível na secção de *Artigos Relacionados*;   
         2. Para os artigos que possuam a secção *Artigos Relacionados* (exibidos no final do ecrã) a aplicação deve:  
            1. **Desativar** a navegação por swipe horizontal nesta secção;  
            2. O swipe‑left ou swipe‑right nessa área não deve avançar nem retroceder artigos no Feed, devendo apenas permitir a interação normal de scroll ou clique nos itens do componente.

            

3. #### **Ações**

   1. Reproduzir media:   
      1. A aplicação deve permitir ao utilizador reproduzir conteúdos multimédia (áudio, imagem e vídeo) diretamente na página de artigo;  
      2. As **regras de exibição** e **funções de reprodução** estão diretamente dependentes do atual media player (Brightcove) e das funções originais dos embeds associados ao artigo. 

      

   2. Reproduzir versão resumida:   
      1. Ver secção [*Escopo Futuro*](https://docs.google.com/document/d/1a3t5THaJcIA4sg-vOfnkq44QXRPjn7N72hBHLhH5yEY/edit?tab=t.53ajcrus5et7#heading=h.nopdv7nh1rf5)

   3. Reproduzir versão áudio:   
      1. Ver secção [*Escopo Futuro*](https://docs.google.com/document/d/1a3t5THaJcIA4sg-vOfnkq44QXRPjn7N72hBHLhH5yEY/edit?tab=t.53ajcrus5et7#heading=h.nopdv7nh1rf5)

   4. Guardar artigo:   
      1. Ver secção [*Escopo Futuro*](https://docs.google.com/document/d/1a3t5THaJcIA4sg-vOfnkq44QXRPjn7N72hBHLhH5yEY/edit?tab=t.53ajcrus5et7#heading=h.nopdv7nh1rf5)

   5. Partilhar artigo:   
      1. Ver secção [*Escopo Futuro*](https://docs.google.com/document/d/1a3t5THaJcIA4sg-vOfnkq44QXRPjn7N72hBHLhH5yEY/edit?tab=t.53ajcrus5et7#heading=h.nopdv7nh1rf5)

### ---

