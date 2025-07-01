# Pesquisa

---

### **Pesquisa de Capa**

O utilizador deve poder pesquisar por Capas-Fonte com base no nome da fonte.

Design

1. [Link Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-15494&t=wAieDihblOGN662Q-0)  
   

Funcional

1. **Mecanismo de pesquisa**  
   1. A pesquisa deve ser realizada em formato de busca por texto, e utilizar um input do tipo “search”;  
   2. Placeholder: Deve haver um placeholder que deixe explícito ao utilizador que a pesquisa é baseada em **Capas-fonte**. O texto deve ser definido em Figma por design. 

2. **Exibição dos resultados**  
   1. Devem ser exibidas apenas as **Capas-fonte** cujo nome corresponda ao termo pesquisado;  
      1. **Nota técnica**: O nome da *Capa-Fonte* deve ser obtido através do atributo producer.name do objeto capa, retornado pelo RabbitMQ-SAPO.   
   2. A correspondência deve ser feita por meio de *regex*, permitindo a identificação em qualquer posição do nome da Capa-fonte.  
      1. Exemplo:  Termo pesquisado “xpre” ; Corresponde com “Expresso”, “Expresso Revista”, etc.  
   3. A correspondência *regex* não deve ser sensível a maiúsculas, minúsculas nem caracteres especiais.  
      1. Exemplo:  Termo pesquisado “diario” ; Corresponde com “Diário de Notícias”

3. **Histórico de pesquisa**  
   1. No layout de pesquisa, a aplicação deve exibir o histórico mais recente de pesquisa realizada pelo utilizador;  
   2. O histórico deve ser limitado aos últimos 5 termos pesquisados;   
   3. Os itens exibidos no histórico devem ser clicáveis;  
   4. Ao selecionar um termo do histórico, a pesquisa deve ser executada imediatamente com o termo selecionado.

### ---

