# Geração de Resumo de Artigo em **Texto**

---

 

1. **Requisitos Gerais**  
   1. O resumo em texto deve ser gerado com base em todo o conteúdo de texto do corpo do artigo (atributo content);  
   2. Não devem ser considerados quaisquer outros elementos de conteúdo do artigo (título, lead, media, embeds, etc).

2. **Especificações e Estrutura do Resumo**  
   1. Idioma: Português (Portugal)  
   2. Número de palavras: Até 100 palavras.  
   3. Estrutura: Organizado em 3 a 5 bullet points, cada um cobrindo uma ideia-chave.  
   4. Tom: Informativo e neutro, evitando opiniões ou análises pessoais  
   5. Estilo:  
      1. Frases curtas e diretas.  
      2. Evitar termos técnicos complexos, exceto quando essenciais.  
      3. Linguagem simples e acessível. 

3. **Artigos Elegíveis:**  
   Critérios de seleção que definem quais artigos são elegíveis para geração de ficheiro de **resumo em texto**:   
   1. Artigos incluídos:  
      1. Por default, todos os artigos recebidos pela app são elegíveis para geração de resumo em texto, exceto as condições especificadas abaixo.

   2. Exceções \- Artigos não incluídos:  
      1. **Artigos de Opinião**: Os artigos que estejam associados a sub-temática *Opinião* não devem ser resumidos;  
      2. **Permissões do Parceiro**: Artigos que pertençam a parceiros (fontes) que estejam presentes no ficheiro de configuração de parcerias (partnership), em que seja negada permissão de uso e processamento do conteúdo do artigo para geração de resumo (partners.ai.automaticSummaryGeneration \= false).  
         1. **Nota**: Na ausência de declaração de permissão (se o parceiro não está presente no ficheiro de configuração ou partners.ai.automaticSummaryGeneration \= null), por default, será assumido partners.ai.automaticSummaryGeneration \= true.

4. **Fluxo de Geração**  
   1. **Automático**: A aplicação deve gerar automaticamente **resumo em texto** para **todos os artigos** recebidos pela app que sejam enquadrados na regra de inclusão (de resumo em texto). Os resumos devem ser gerados conforme especificações e estrutura descritos acima.

---

