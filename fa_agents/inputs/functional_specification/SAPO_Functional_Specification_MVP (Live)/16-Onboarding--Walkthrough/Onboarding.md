# Onboarding

---

Design

* [Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=11596-186791&p=f&t=j7hIOXokL1RVxjMQ-0)

Requisitos Funcionais  
A aplicação deve conduzir o utilizador por um fluxo inicial de boas‑vindas e recolher as permissões obrigatórias (notificações, App Tracking Transparente e consentimento GDPR) de acordo com as guidelines de iOS e Android, garantindo conformidade legal e uma experiência intuitiva.

---

### **Fluxo Geral** Ao instalar (ou abrir pela primeira vez) a app, o utilizador percorre sequencialmente:

1. **Ecrã de Boas‑Vindas**  
   1. Apresenta uma ecrã inicial com mensagem de boas vindas e apresentação da app e da marca;  
   2. Disponibiliza apenas a ação \[**Continuar**\]: Avança para a solicitação de permissões de notificações.

2. **Permissão de Notificações**  
   1. A app exibe um ecrã que explica brevemente a utilidade das notificações e oferece duas opções:   
      **Ativar notificações** ou **Agora não**.  
   2. Se o utilizador escolher **Ativar notificações**:  
      1. Dispara o prompt nativo de permissões de notificações do SO (iOS/Android).  
      2. Se o utilizador permitir, guarda o consentimento como **true** e assume subscrição global, conforme definição em [Envio de Notificações](?tab=t.v96w55mlrhu5).  
      3. Se o utilizador recusar, guarda o consentimento como **false** e assume não‑subscrição global, conforme especificado em [Envio de Notificações](?tab=t.v96w55mlrhu5).  
   3. Após qualquer escolha, segue para o passo seguinte.

3. **Permissão de App Tracking (iOS apenas)**  
   1. Informa o utilizador sobre a recolha de dados de tracking para personalização de conteúdo e publicidade relevante.  
   2. Só é exibido em dispositivos iOS que ainda não tenham definido o estado ATT;  
   3. Invoca o prompt de App Tracking Transparency nativo do iOS;  
   4. Independentemente da resposta, grava o estado e avança para o CMP/GDPR.

4. **Consent Management Platform (CMP) / GDPR**  
   1. A aplicação móvel deve apresentar um componente CMP de terceiros. Este componente permitirá o consentimento detalhado para cookies e para o tratamento de dados pessoais;  
   2. O comportamento do componente e os objetos de consentimento são controlados diretamente pela CMP implementada, conforme requisitos especificados em [Consent Management Platform (CMP)](?tab=t.7xp2wtyja25t);  
   3. Este ecrã deve ser exibido apenas uma vez por instalação, salvo se o utilizador definir manualmente nas definições da app.

---

