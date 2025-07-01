# Aviso de conteúdo criado por IA

---

 

Design

1. [Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7794-59130&t=nJiIcfmqpGlmk5Dp-4)

Requisitos Funcionais

**Aviso de conteúdo criado por IA**:   
A aplicação deve exibir um disclaimer informando o utilizador de que foi utilizada uma ferramenta automática de inteligência artificial para geração do conteúdo.

1. **Funcionalidades aplicáveis**  
   1. O disclaimer deve ser exibido em todas as funcionalidades que façam uso de inteligência artificial para geração ou tratamento do conteúdo. O alerta deve ser exibido nas seguintes funcionalidades:  
      1. Resumo de Artigo Único  
      2. Digest em Stories  
      3. Digest em Áudio  
      4. Versão Áudio de Artigos  
      5. Tradução de Conteúdo

2. **Disclaimer em tela cheia**  
   1. A aplicação deve exibir um disclaimer completo e detalhado em fullscreen;  
   2. O ecrã deve ser exibido antes da reprodução da funcionalidade em questão;  
   3. O utilizador deve poder indicar que está ciente do aviso e solicitar que a mensagem não seja exibida novamente;  
      1. Se o utilizador **indicar** que não deseja visualizar a mensagem novamente, então o disclaimer em fullscreen **não deve** ser exibido novamente para este utilizador.   
      2. Enquanto o utilizador **não indicar** que não deseja visualizar a mensagem novamente, o disclaimer em fullscreen **deve** ser exibido novamente todas as vezes em que o digest for reproduzido.  
      3. Por default, o valor do indicador deve ser definido a *false*;  
      4. O controle e validação da indicação de “não visualizar a mensagem novamente” deve ser aplicado separadamente por funcionalidade. Isto é, marcar o indicador em um disclaimer exibido no contexto de um Resumo de Artigos (por exemplo) não afeta a exibição do disclaimer no contexto da reprodução de Verão Áudio de Artigos.

3. **Disclaimer fixo**  
   1. A aplicação deve exibir um disclaimer resumido, que deve ser exibido de forma fixa durante a reprodução do digest  (story ou áudio).

4. **Informação contextual por funcionalidade**  
   1. A mensagem do disclaimer deve ser contextual e adaptada à funcionalidade, de forma que esteja claro na mensagem o tipo de tratamento ou criação realizada e os possíveis erros a serem considerados. 

---

