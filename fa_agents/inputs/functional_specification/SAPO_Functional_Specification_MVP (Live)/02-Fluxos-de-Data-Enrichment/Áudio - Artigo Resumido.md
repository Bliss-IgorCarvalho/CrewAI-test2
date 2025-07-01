# Geração de Áudio de Artigo **Resumido**

---

 

1. **Requisitos Gerais**  
   1. O áudio deve ser gerado com base no conteúdo do **resumo em texto** do artigo.

2. **Especificações do Áudio**  
   1. Idioma: Português (Portugal);  
   2. Deve ser utilizada a opção de voz Raquel (feminino, adulto), disponível no serviço [Azure-AI-Speech](https://ai.azure.com/explore/models/aiservices/Azure-AI-Speech/version/1/registry/azureml-cogsvc/tryout/texttospeech#voicegallery);

   3. O áudio deve ser gerado em apenas 1 voz.

3. **Artigos Elegíveis**  
   Critérios de seleção que definem quais artigos são elegíveis para geração de ficheiro de **resumo em áudio**:   
   1. Artigos incluídos:  
      1. Por default, todos os artigos recebidos pela app **que possuam resumo em texto** são elegíveis para geração de **resumo em áudio**, exceto as condições especificadas abaixo.

   2. Exceções \- Artigos não incluídos:  
      1. **Artigos sem resumo:** Os artigos que não possuam resumo em texto;  
      2. **Permissões do Parceiro**: Artigos que pertençam a parceiros (fontes) que estejam presentes no ficheiro de configuração de parcerias (partnership), em que seja negada permissão de uso e processamento do conteúdo do artigo para geração de áudio (partners.ai.audioCreation \= false).  
         1. **Nota**: Na ausência de declaração de permissão (se o parceiro não está presente no ficheiro de configuração ou partners.ai.audioCreation \= null), por default, será assumido partners.ai.audioCreation \= true.

4. **Fluxo de Geração**  
   1. **Automático**: A aplicação deve gerar automaticamente **resumo em áudio** para **todos os artigos** recebidos pela app que sejam enquadrados na regra de inclusão (de resumo em áudio).

---

