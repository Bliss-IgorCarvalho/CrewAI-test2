# Envio de Notificações

---

1. **Requisitos Gerais**  
   1. A aplicação SAPO deve ser capaz de enviar push notifications;  
         
   2. O envio de notificações deve ser feito através da plataforma OneSignal, ficando a cargo do backoffice SAPO a definição e disparo das mensagens.

2. **Subscrição de Notificações**  
   1. A aplicação deve solicitar ao utilizador permissão para o envio de push notifications. Os utilizadores devem poder permitir ou bloquear notificações a nível do sistema operativo (conforme comportamento nativo das plataformas Android e iOS);

   2. A subscrição de notificações deve ser global. Se um utilizador recusar notificações no sistema operativo, não receberá nenhuma, se aceitar, receberá todas as notificações enviadas.

   3. A gestão de subscrições segmentadas (por categorias, temas, etc.) **não está disponível no MVP**. Todos os utilizadores recebem as mesmas notificações globais.

   4. Tanto utilizadores autenticados como anónimos podem receber notificações push, pois não há restrições de subscrição no MVP.

3. **Envio das Push-notifications**  
   1. O envio das notificações push deve ser realizado manualmente através do backoffice SAPO, utilizando a plataforma OneSignal;

   2. O conteúdo das notificações (título, subtítulo, texto, imagem e idioma) deve ser definido no backoffice SAPO, conforme as opções suportadas pelo OneSignal.

4. **Ação ao Clicar (Deep Link)**  
   1. As notificações devem ser clicáveis. O comportamento de direcionamento ao clicar nas notificações será implementado em fases, conforme as seguintes entregas: 

      1. **\[Entrega 1 \- MVP\]** Redirecionamento para o artigo \- **Abertura na App**  
         O utilizador é redirecionado para um **artigo específico** (conforme configurado no Deep Link) **na app SAPO** ([Página de Artigo](?tab=t.g0diref5r0rg)).

      2. \[Entrega 2 \- Pós MVP\] Redirecionamento para o conteúdo específico \- **Abertura na App**  
         O utilizador é redirecionado para um **conteúdo específico** (conforme configurado no Deep Link) **na app SAPO**, podendo ter diferentes formatos (Resumos, Áudio, etc).

   2. Os Deep Links devem ser definidos e configurados no backoffice SAPO, através do OneSignal;

   3. Fallback: Se não existir um deep link válido configurado na notificação, ao clicar deve abrir-se a aplicação na secção principal da app.

---

