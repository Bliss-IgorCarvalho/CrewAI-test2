# Geração de Áudio de Artigo **Completo**

---

 

1. **Requisitos Gerais**  
   1. A **versão em áudio integral** deve ser gerado com base em **todo o conteúdo** de texto do corpo do artigo (atributo content);  
   2. Não devem ser considerados quaisquer outros elementos de conteúdo do artigo (título, lead, media, embeds, etc).

2. **Especificações do Áudio**  
   1. Idioma: Português (Portugal);  
   2. Deve ser utilizada a opção de voz Raquel (feminino, adulto), disponível no serviço [Azure-AI-Speech](https://ai.azure.com/explore/models/aiservices/Azure-AI-Speech/version/1/registry/azureml-cogsvc/tryout/texttospeech#voicegallery);  
   3. O áudio deve ser gerado em apenas 1 voz.

3. **Artigos Elegíveis:**  
   Critérios de seleção que definem quais artigos são elegíveis para geração de ficheiro de **resumo em áudio**:  
   1. Artigos incluídos:  
      1. **Artigos Destacados**: Artigos recebidos pela app através da estrutura highlights-group.

   2. Exceções \- Artigos não incluídos:  
      1. **Permissões do Parceiro**: Artigos que pertençam a parceiros (fontes) que estejam presentes no ficheiro de configuração de parcerias (partnership), em que seja negada permissão de uso e processamento do conteúdo do artigo para geração de áudio (partners.ai.audioCreation \= false).  
         1. **Nota**: Na ausência de declaração de permissão (se o parceiro não está presente no ficheiro de configuração ou partners.ai.audioCreation \= null), por default, será assumido partners.ai.audioCreation \= true.

      2. **Artigos ao minuto**:  
         1. O conteúdo pode ser demasiado grande e perde-se o conceito de timeline.

      3. **Video, Podcast, Photo-Gallery:**  
         1. Artigos identificados como artigos de vídeo, podcast ou galeria de fotos, e que contenham menos de 100 palavras;  
         2. Um artigo pode ter até três tipos diferentes associados. A verificação desta regra é cumulativa: se o artigo corresponder a pelo menos um dos tipos definidos, a regra aplica-se.  
         3. **Nota Técnica**: A identificação do tipo é obtida no payload do artigo, através do atributos hasVideo, hasPodcast e hasGallery.   

4. **Fluxo de Geração**  
   1. **Automático**:  
      1. A aplicação deve gerar automaticamente **versão em áudio completo** para todos os artigos recebidos pela app que sejam enquadrados na regra de inclusão.

   2. **On demand**:  
      1. Para MVP, não deve haver geração de áudio on demand.

---

