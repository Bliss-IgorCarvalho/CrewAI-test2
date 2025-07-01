# Versão Áudio de Artigos Completos

---

Design

1. [Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=8032-38386&t=0TRQX4vhQVqMAZ9v-4)

Requisitos Funcionais

1. **Requisitos Gerais**  
   1. O utilizador deve poder reproduzir/ouvir a **versão em áudio de um artigo inteiro**;  
   2. A versão em áudio deve ser baseada no conteúdo em texto completo do corpo do artigo;  
   3. Deve estar disponível em Português (Portugal);  
   4. Deve ser utilizada a opção de voz Raquel (feminino, adulto), disponível no serviço [Azure-AI-Speech](https://ai.azure.com/explore/models/aiservices/Azure-AI-Speech/version/1/registry/azureml-cogsvc/tryout/texttospeech#voicegallery).

2. **Artigos Elegíveis**  
   Critérios de seleção que definem quais artigos disponíveis são elegíveis para reprodução de versão em áudio:    
   1. Artigos incluídos:  
      1. Artigos (em geral) que possuam ficheiro **de áudio em versão integral**.

   2. Artigos não incluídos:  
      1. **Artigos sem versão em áudio**  
         1. Artigos (em geral) que não possuam **versão em áudio integral**;  
         2. **Nota**: São excluídos artigos que durante o processo de data enrichment não tiveram os ficheiros de áudio em versão integral gerados, seja por problemas técnicos ou por ausência de autorização do parceiro produtor do artigo. 

      2. **Artigos ao minuto**:  
         1. O conteúdo pode ser demasiado grande e perde-se o conceito de timeline.

      3. **Video, Podcast, Photo-Gallery:**  
         1. Artigos identificados como artigos de vídeo, podcast ou galeria de fotos, e que contenham menos de 100 palavras;  
         2. Um artigo pode ter até três tipos diferentes associados. A verificação desta regra é cumulativa: se o artigo corresponder a pelo menos um dos tipos definidos, a regra aplica-se.  
         3. **Nota Técnica**: A identificação do tipo é obtida no payload do artigo, através do atributos hasVideo, hasPodcast e hasGallery.   

3. **Acesso e Reprodução à Versão Áudio**  
   1. Página de Artigo:  
      1. O utilizador deve poder iniciar a reprodução da versão em áudio diretamente da Página de Artigo, em todos os artigos que sejam elegíveis para esta funcionalidade.

   2. Conteúdo Partilhado  
      1. O utilizador deve poder reproduzir a versão áudio do conteúdo partilhado quando recebe o link de áudio de outro utilizador.

4. **Formatos de Reprodução**  
   1. Fullscreen ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=8032-40866&t=0TRQX4vhQVqMAZ9v-4).):  
      1. O player de áudio deve ser exibido em tela cheia, conforme especificações de Design.

   2. Minimizado ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=8032-40974&t=0TRQX4vhQVqMAZ9v-4)):  
      1. O player de áudio deve ser exibido em formato minimizado, conforme especificações de Design;  
      2. O player minimizado deve persistir enquanto o usuário navega na aplicação, exceto se for manualmente fechado;  
      3. Quando a reprodução de um áudio individual ou de uma playlist for concluída, o player minimizado deve continuar visível na interface. O áudio deve voltar ao início automaticamente , mas permanecer pausado no tempo 00:00, pronto para ser reproduzido novamente caso o utilizador inicie esta ação.

   3. Background:  
      1. A reprodução em background da versão áudio dos artigos deverá seguir os comportamentos padrão de cada sistema operativo (Android e iOS), permitindo que o utilizador continue a ouvir o conteúdo enquanto utiliza outras aplicações ou com o ecrã bloqueado.

5. **Layout e Componentes**  
   1. Player em Fullscreen  
      1. Título do ecrã:  
         1. Quanto no contexto do **Digest** (vários áudios), exibe o texto fixo “**Resumo de Artigos**”;  
         2. Quando no contexto da **Versão Áudio de Artigo** (um único artigo), exibe o título do artigo.  
            1. atributo title

      2. Contagem de artigos:  
         1. Exibido somente no contexto do Digest, onde são reproduzidos vários áudios (em playlist);  
         2. Formato: “**n de m Artigos”** (onde **n** é o artigo atual e **m** é o total de de artigos).

      3. Logo:  
         1. Exibe o **logo** da Fonte associada ao artigo. 

      4. Fonte:  
         1. Exibe **nome** da Fonte associada ao artigo.  
         2. atributo partner.title

      5. Tempo/Data de publicação:  
         1. Exibe a informação de quando o artigo foi publicado:  
         2. Aplicam-se as mesmas regras de referência e formato da [Página de Artigos](?tab=t.g0diref5r0rg).

      6. Título do Artigo:  
         1. Exibe sempre o título do artigo em reprodução;  
         2. atributo title

      7. Barra de progresso:  
         1. Indicação visual do tempo reproduzido de áudio  
         2. Pode ser utilizado para as ações de Avançar / Retroceder (na mesma faixa de áudio). 

      8. Aviso de conteúdo criado por IA:  
         1. Ver requisitos no escopo da [funcionalidade](?tab=t.xzrfike6umrp).

   2. Player Minimizado ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=8032-40974&t=watMY2yOvb1q0sYW-4))  
      1. Barra de progresso:  
         1. Indicação visual do tempo reproduzido de áudio

      2. Tempo de Reprodução:  
         1. Exibe o tempo restante de reprodução do áudio;

      3. Título:  
         1. Exibe do título do artigo em reprodução;  
         2. atributo title

6. **Ações e Navegação**  
   1. **Ler artigo completo**: O utilizador deve ser redirecionado para a página de artigo para visualização do artigo completo;   
      1. Ao redirecionar para a Página de Artigo, o player deve ser minimizado e continuar visível.

   2. **Partilhar conteúdo**: O utilizador deve poder partilhar a versão em áudio do artigo com outras plataformas e utilizadores.   
      1. Ver requisitos no escopo da [funcionalidade](?tab=t.7t57iyz5hp70).  
      2. **Disclaimer**: Esta ação deve estar disponível apenas após a implementação da funcionalidade *Partilha de Conteúdo*.

   3. **Reportar problema:** O utilizador deve poder reportar problemas no conteúdo.  
      1. Ver requisitos no escopo da [funcionalidade](?tab=t.bmoeqea3zr7s).  
      2. **Disclaimer**: Esta ação deve estar disponível apenas após a implementação da funcionalidade [Reportar Problema](?tab=t.bmoeqea3zr7s).

7.   
   1. Player em Fullscreen  
      As ações de reprodução do áudio estão diretamente associadas e dependentes dos recursos disponíveis no audio player escolhido para a app ([Brightcove](https://www.brightcove.com/)). As ações esperadas são:  
      1. Play / Pause;  
      2. Avançar / Retroceder (na mesma faixa de áudio);  
      3. Avançar / Retroceder (entre faixas de áudio diferentes);  
         1. **Nota**: Aplicável somente ao contexto do Digest  
      4. Controle de velocidade de reprodução (Playback Speed);  
      5. Minimizar player  
      6. Fechar player

   2. Player Minimizado  
      As ações e recursos de reprodução devem ser reduzidas no player minimizado. Ações disponíveis:  
      1. Play / Pause;

      2. Maximizar player:   
         1. O player deve ser clicável, e quando clicado deve reabrir o player em formato fullscreen.

      3. Fechar audio player:  
         1. Ao fechar o player, a aplicação deve redirecionar o utilizador para o Feed. 

8. **Limite para utilizadores anónimos**  
   1. Para MVP não deve haver limite de uso desta funcionalidade. O controle e limite de utilização deve ser implementado em pós MVP, após a implementação do Login.   
      1. Nota: Criado o [Ticket 33393](https://dev.azure.com/blissapps/SAPO%20App/_workitems/edit/33393) em DevOps para inclusão deste desenvolvimento em pós MVP.

---

