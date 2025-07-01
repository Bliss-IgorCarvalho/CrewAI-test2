# Digest

---

 

### **Requisitos Gerais**

1. **Fluxo de Geração do Digest:**  
   1. O resumo deve ser gerado automaticamente 3 vezes ao dia, em períodos específicos \[Manhã, Meio dia, Noite\] e reproduzido on-demand.  
   2. **Nota**: Este processo está sujeito a ajustes, dependendo do tempo real necessário para completar a geração das recomendações para todos os utilizadores.  
      1. **Manhã**:  O digest da manhã deve estar disponível às **08:30 AM**. O processo de geração das recomendações tem início às **07:30 AM** e decorre até às **08:29 AM**, com cada recomendação a ser produzida com base nas notícias disponíveis no momento exato da sua geração.  
      2. **Tarde**: O digest do meio-dia deve estar disponível às **13:30 PM**. A geração tem início às **12:30 PM** e prolonga-se até às **13:29 PM**, considerando as notícias disponíveis no momento exato da sua geração.  
      3. **Noite**: O digest da noite deve estar disponível às **20:30 PM**. A geração começa às **19:30 PM** e termina às **20:29 PM**, sendo cada digest personalizado de acordo com as notícias disponíveis no momento da sua criação.

2. **Seleção dos artigos:**  
   1. **Fonte:** O digest deve utilizar como base a lista de conteúdos recomendados pelo serviço Recommender:

   2. **Filtro e ordenação:** O conteúdo apresentado deve corresponder exatamente a lista fornecida pelo Recommender, respeitando filtros e ordenação;

   3. **Quantidade:** Os primeiros \[4, 8 ou 12\] artigos do *Feed de Artigos*, consoante a escolha do utilizador nas opções de configuração do Digest (ver requisito 4\. Setup do Digest).

      

3. **Acesso e Reprodução do Digest**  
   1. Acesso:  
      1. O utilizador deve poder aceder ao *Digest* através do *Feed de Artigos*;  
      2. O acesso ao Digest deve ser garantido a todo momento em que o utilizador estiver no Feed, seja através da secção Digest (quando o utilizador estiver no topo do Feed), seja na top bar (quando o utilizador não estiver no topo do Feed).

   2. Aviso de conteúdo criado por IA: Ao aceder o resumo, a aplicação deve exibir o aviso de conteúdo criado por IA, conforme regras especificadas na [funcionalidade](?tab=t.xzrfike6umrp).

   3. Reprodução:  
      1. **Novo digest**: Quando o utilizador reproduz um novo Digest (com nova lista de recomendação gerada pelo serviço de AI), a aplicação deve exibir os resumos com a lista de artigos atualizada, conforme o comportamento vigente de seleção dos artigos (ver requisito *2\. Seleção de Artigos*).    
      2. **Digest Visto**: Quando o utilizador reproduz um Digest já reproduzido anteriormente, a aplicação deve exibir o mesmo digest (mesma lista de resumos de artigos) exibido na reprodução anterior. A reprodução do Digest entre os períodos de geração/atualização deve apresentar sempre o último Digest gerado.   
         1. **Exemplo 1**: Um novo resumo é gerado de manhã cedo, e outro será gerado no início da tarde. Sempre que um utilizador aceder à app e reproduzir um resumo entre esses dois horários, será reproduzido o mesmo resumo gerado pela manhã;  
         2. **Exemplo 2**: Um utilizador visualiza inicialmente um resumo contendo 8 artigos. Ao aceder novamente à aplicação antes da próxima atualização, o mesmo utilizador reproduz o digest já visualizado. Desta vez, são apresentados 12 artigos. Os primeiros 8 artigos correspondem aos previamente vistos, enquanto os 4 últimos são novos para o utilizador, embora integrem a mesma lista de 12 gerada na atualização anterior.

4. **Setup do Digest**  
   1. Formato:  
      1. O utilizador deve poder escolher em que formato deseja consumir o Digest:  
         1. **Stories**: Exibição dos resumos de artigos em formato stories, semelhante às redes sociais (ver [Digest em Stories](#digest-em-stories)).

         2. **Áudio**: Exibição dos resumos de artigos em formato podcast. Aplicam-se os mesmo comportamentos e requisitos previstos para a funcionalidade Text-to-Speech (ver [Digest em Áudio](#digest-em-áudio))

   2. Quantidade de Artigos ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=8758-73392&t=Uu6wScxUmPGcwkY1-4)):  
      1. Por default a quantidade de artigos deve ser definida para 12\.  
      2. O utilizador deve poder personalizar o número de artigos incluídos no seu Resumo, selecionando entre opções pré-definidas (4, 8 ou 12 artigos). A aplicação deve fornecer uma estimativa da duração do resumo em minutos para cada uma destas opções.

   3. Guardar Preferências:   
      1. Após a escolha da quantidade de artigos, o utilizador deve poder gravar as definições de setup (formato e quantidade de artigos);   
      2. Nas próximas reproduções do Digest a app deve aplicar automaticamente as definições salvas;  
      3. As definições salvas não devem ser sincronizadas com a conta SAPO ID do utilizador.

5. **Limite para utilizadores anónimos**  
   1. Para MVP não deve haver limite de uso desta funcionalidade. O controle e limite de utilização deve ser implementado em pós MVP, após a implementação do Login.   
      1. Nota: Criado o [Ticket 33393](https://dev.azure.com/blissapps/SAPO%20App/_workitems/edit/33393) em DevOps para inclusão deste desenvolvimento em pós MVP.

### ---

 **Digest em Stories** {#digest-em-stories}

Design

1. [Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7794-63518&t=QIuuKTOhs2MdzqAr-4)

Requisitos Funcionais

1. **Formato do Resumo**  
   1. O Digest deve ser um compilado de *Resumos de Artigos Único*;  
   2. Ao gerar e reproduzir um Digest, a aplicação deve exibir uma sequência de *Resumos de Artigos,* consoante as regras vigentes de *Seleção dos artigos*.

2. **Artigos Elegíveis**  
   1. Aplicam-se as mesmas regras de artigos elegíveis para o *Resumo de Artigo Único*.

3. **Layout e Componentes**  
   1. Aplicam-se as mesmas regras de Layout e Componentes do *Resumo de Artigo Único*;

   2. Componentes exclusivos do Digest:  
      1. Barra de progresso do Resumo: Barra de progresso dinâmica, que indica a quantidade de resumos/artigos disponíveis no Digest atual e em qual resumo/artigo o utilizador se encontra. A barra deve avançar à medida que o utilizador percorre cada resumo (tal como no Instagram).

4. **Ações**  
   1. Aplicam-se as mesmas regras de Ações do *Resumo de Artigo Único*;

5. **Navegação**  
   1. Aplicam-se as mesmas regras de Navegação do *Resumo de Artigo Único*;

   2. Navegações exclusivas do Digest:  
      1. Avançar para o próximo story do resumo actual  
         1. Interação: Tap-right  
         2. No último story avança para o próximo resumo

      2. Voltar ao story anterior do resumo actual  
         1. Interação: Tap-left  
         2. No primeiro story do primeiro resumo reinicia o story  
         3. No primeiro story do segundo resumo (ou posterior) retorna para resumo anterior 

      3. Avançar para para o resumo do próximo artigo  
         1. Interação: Swipe-right  
         2. No último story navega para o wrap-up

      4. Voltar ao resumo do artigo anterior  
         1. Interação: Swipe-left  
         2. Não disponível no primeiro resumo

      5. Fechar resumo digest:  
         1. Interação: Clique no CTA \[X\]  
            1. Encerra a reprodução do resumo, fechando o componente story, independentemente do story (primeiro, segundo ou terceiro).

         2. Interação: Swipe-left  
            1. Fechar a reprodução do resumo e o componente de story apenas se o resumo apresentado for o primeiro, independentemente da ordem do story (primeiro, segundo ou terceiro).

         3. Redirecionamento  
            1. Ao fechar o componente, o utilizador deve ser direcionado de volta para o Feed de artigos.

6. **Wrap-up**  
   1. Ao final da exibição do resumo a app deve exibir a lista dos artigos incluídos no digest  
   2. Os itens na lista devem ser clicáveis, ao clicar, a aplicação deve redirecionar o utilizador para a página de artigo, para visualização do artigo escolhido.  
   3. O utilizador deve poder reiniciar a reprodução do digest completo. 

---

### **Digest em Áudio** {#digest-em-áudio}

Design

1. [Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=8032-40866&t=QIuuKTOhs2MdzqAr-4)

Requisitos Funcionais

1. **Formato do Resumo**  
   1. Reprodução do Digest em formato de áudio. O resumo deve ser um compilado de ***Resumos em áudio (TTS)*** dos artigos selecionados;  
   2. Ao gerar e reproduzir um Digest em Áudio, a aplicação deve exibir uma “playlist” de ***Resumos em áudio**,* consoante as regras vigentes de *Seleção dos artigos*.

2. **Artigos Elegíveis**  
   Critérios de seleção que definem quais artigos disponíveis são elegíveis para geração e reprodução de resumo em formato Áudio:  
   1. Artigos incluídos no Digest:  
      1. Artigos (em geral) que possuam versão em áudio **resumido**.

   2. Artigos não incluídos no Digest:  
      1. Artigos que não possuam versão em áudio **resumido**;  
      2. **Artigos de opinião**: Artigos de opinião não possuem versão em audio;  
      3. **Artigos ao minuto**: Artigos ao minuto não possuem versão em audio.

3. **Layout e Componentes**  
   1. Aplicam-se as mesmas regras de layout e componentes da funcionalidade [Versão Áudio de Artigos (TTS)](?tab=t.trh1oscjllgi).

4. **Ações**  
   1. Aplicam-se as mesmas regras de ações da funcionalidade [Versão Áudio de Artigos (TTS)](?tab=t.trh1oscjllgi).

5. **Navegação**  
   1. Aplicam-se as mesmas regras de navegação da funcionalidade [Versão Áudio de Artigos (TTS)](?tab=t.trh1oscjllgi).

---

