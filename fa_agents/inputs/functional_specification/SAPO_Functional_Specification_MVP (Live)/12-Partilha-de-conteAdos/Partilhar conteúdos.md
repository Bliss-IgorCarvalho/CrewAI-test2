# Partilha de conteúdos

---

Design

1. [Ver design em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB-Handoff--Design-Visual?node-id=5171-15481&t=7o6g8kz0gO3RXhxY-4)

Funcional

1. **Requisitos Gerais**  
   1. A aplicação deve permitir ao utilizador partilhar conteúdos diretamente da app, incluindo artigos, capas, resumos de artigos e digests, com outras aplicações e utilizadores nas suas redes sociais.

2. **Fases de implementação do compartilhamento de conteúdo**  
    A funcionalidade de partilha será entregue em três etapas, garantindo consistência e previsibilidade no deep link gerado:

   1. **\[Entrega 1 \- MVP\]** Compartilhamento de um único artigo \- **Abertura no Site**  
      Independentemente de o utilizador estar a ver a versão áudio, o resumo ou o digest, ao partilhar será sempre enviado um link para a página principal do artigo completo **no site SAPO**.

   2. \[Entrega 2 \- Pós MVP\] Compartilhamento de um único artigo \- **Abertura na App**  
      Independentemente de o utilizador estar a ver a versão áudio, o resumo ou o digest, ao partilhar será sempre enviado um deep link para a página principal do artigo completo **na app SAPO**.

   3. \[Entrega 3 \- Pós MVP\] Compartilhamento de conteúdo específico  
      Mantém-se o limite de um artigo por compartilhamento, mas o deep link passa a apontar diretamente para o recurso que está a ser partilhado (por exemplo, a versão áudio ou o storie do artigo), em vez de direcionar sempre ao artigo principal.

   4. \[Entrega 4 \- Pós MVP\] Compartilhamento de Digest completo  
      Permite enviar múltiplos conteúdos de uma só vez no contexto de um digest, de modo que o utilizador possa partilhar o conjunto completo de Stories ou de episódios em áudio num único link.

3. **Fluxo para utilizadores com app SAPO instalada**  
   1. Caso o utilizador destinatário tenha a app instalada no seu dispositivo, os conteúdos partilhados devem ser abertos diretamente na app SAPO. 

4. **Fluxo para utilizadores sem app SAPO instalada**  
   1. Caso o destinatário não tenha a app instalada, o conteúdo partilhado deve conter um link que redirecione para o site SAPO. O fluxo de redirecionamento e gestão do processo após o clique devem ser tratados no lado do site, seja através da implementação de Universal Links ou de plataformas de gestão de links como a Branch.io.

5. **Preview do Conteúdo**  
   1. Ao acionar “Partilhar” em um conteúdo, a app móvel abre o share sheet nativo do dispositivo e envia apenas o URL do artigo. A montagem do cartão de preview com Imagem Principal, Título, Lead e Logo da Fonte fica a cargo da app receptora (WhatsApp, Telegram, etc.), que faz uma requisição ao site e extrai esses dados das meta-tags HTML. Portanto, é responsabilidade da camada web do SAPO garantir que todas as páginas de artigo possuam corretamente configuradas as tags e demais propriedades necessárias, assegurando que qualquer plataforma de destino gere o preview conforme o design esperado.

6. **Conteúdos Partilháveis**  
   A ação de partilhar deve estar disponível para os seguintes tipos de conteúdo:  
   1. Artigos;  
   2. Capas;  
   3. Resumo de artigo em formato Stories;  
   4. Resumo de artigo em formato Áudio,  
   5. Versão em Áudio de Artigo Completo (TTS).

---

