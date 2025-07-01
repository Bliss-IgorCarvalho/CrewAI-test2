# Publicidade

---

1. ### **Requisitos Gerais**

   1. **Mapeamento dos anúncios na app**  
      1. Link para documentação:  [SAPO | Advertisements Mapping \[v1.0\]](https://docs.google.com/spreadsheets/d/1UbU6MW9MVdBU2VqNALwIfavbdFYXa1aprGP5TS5l6aQ/edit?gid=0#gid=0)

   2. **Controlo de Exibição**  
      1. Cada formato de anúncio deverá contar com feature flag via Firebase Remote Config, permitindo que seja possível controlar de forma dinâmica se o formato deve ou não ser exibido na aplicação. 

   3. **Frequência de Impressão**  
      1. Tal como o controlo de exibição, deve ser possível alterar de forma dinâmica as configurações de **frequência de impressão** dos anúncios, também utilizando feature flag via Firebase Remote Config.

   4. **Posicionamento e design**  
      1. O posicionamento e design dos anúncios devem ser implementados conforme especificados no mapeamento em anexo no requisito 1\. Mapeamento e nos designs em Figma. 

   5. **Fallback**   
      O componente de anúncio não deve ser exibido caso ocorram erros, ausência de respostas ou falha no fornecimento de anúncios pelos servidores de anúncios. O layout da app deve se ajustar automaticamente para evitar espaços vazios.  
        
   6. **Out of scope**  
      1. Formatos de publicidade em vídeo e áudio (in-stream) devem ser implementados pelo player a ser utilizado na aplicação [brightcove](https://www.brightcove.com/). Não deve haver integração específica para implementação de publicidade em vídeo ou áudio.

## ---

2. ### **Regras para os Ads Mobile-Native**

   1. **Implementação**  
      Os anúncios nativos devem ser implementados em formatos nativos para mobile através da integração dos SDKs das plataformas especificadas no requisito *2.c-Providers*.

   2. **Formatos**  
      Formatos de anúncio que devem ser suportados na aplicação com implementação **nativa mobile**:  
      

| Formato | Descrição Funcional |
| :---: | ----- |
| Banner In-page | Anúncio estático ou animado inserido dentro do fluxo de conteúdo (scroll), respeitando tamanho padrão. |
| Banner Sticky | Anúncio fixo em rodapé ou topo da tela, persistente durante a navegação na seção definida. |
| Native Ad | Anúncio adaptado ao estilo visual da aplicação, composto por imagem, título e call-to-action. |
| Interstitial Ad | Anúncio de tela cheia exibido em pontos de transição (p.ex.: troca de seção), com opção de fechar. |

3. **Providers**  
   Plataformas (Ad Servers) que devem ser integradas para suportar os anúncios **nativos mobile**:   
   

| Plataforma | Integração | Doc SDK |
| :---: | ----- | ----- |
| Google Ads | Suporte aos formatos por meio do Google Mobile Ads SDK. | [Android](https://developers.google.com/admob/android/sdk) [iOS](https://developers.google.com/admob/ios/download) |
| Outbrain | Integração via SDK da Outbrain para recomendações nativas. | Android iOS |

---

3. ### **Regras para os Ads Web**

   1. **Implementação**  
      1. Os anúncios devem ser implementados em formatos web para as plataformas especificadas no requisito *3.c-Providers*;  
      2. Os anúncios em formato web devem ser exibidos dentro do componente webview, na Página de Artigo.

   2. **Formatos**  
      Formatos de anúncio que devem ser suportados na aplicação com implementação **web**:  
      

| Formato | Descrição Funcional |
| :---: | ----- |
| Banner In-page | Anúncio estático ou animado inserido dentro do fluxo de conteúdo (scroll), respeitando tamanho padrão. |

3. **Providers**  
   Plataformas (Ad Servers) que devem ser integradas para suportar os anúncios **web**:   
   

| Plataforma | Integração | Doc SDK |
| :---: | ----- | ----- |
| Google Ads | Suporte aos formatos por meio do Google Mobile Ads SDK. |  |
| Teads | Player de outstream Teads configurado conforme guideline. |  |

---

