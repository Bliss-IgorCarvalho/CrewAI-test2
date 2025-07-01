# Artigo Patrocinado

Regras aplicáveis aos artigos patrocinados  
---

Requisitos de Design

1. [Ver design em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7794-64043&t=uYin3GgsPdJ580oA-4)

Requisitos Funcionais

1. **Descrição**  
   1. *Artigos Patrocinados* são artigos cujo conteúdo trata-se de *content marketing*, patrocinado por uma entidade externa ao ecossistema de Fontes/Parceiros do SAPO. Esses artigos devem apresentar uma indicação visual específica, que informa quem é o patrocinador do conteúdo e oferece acesso ao seu website. 

2. **Aplicação do template**  
   1. Este template deve ser aplicado ao artigo somente se:  
      1. O artigo possuir dados de **patrocinador** (sponsor)  
         **E**  
      2. O atributo hideSponsor \= false 

   2. Dados esperados no payload;  
      1. Patrocinador (sponsor.title) \[atributo obrigatório\];  
      2. Link do site do patrocinador (sponsor.url) \[atributo opcional\];  
      3. Logo do patrocinador (sponsor.logo.url) \[atributo opcional\].

3. **Layout & Componentes**  
   1. Deve conter indicação do patrocinador ([Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=9252-33280&t=EjRhM9K1tCgRu04j-4))  
      1. Formato: *Patrocinado por* \+ Logo \+ Patrocinador (Ex: Patrocinado por 🩺 Farmácias Portuguesas)  
         1. Se não houver logo, o componente não deve ser exibido.  
      2. Se houver Link do site do patrocinador  
         1. Deve ser clicável;  
         2. Deve direcionar o utilizador para o site do patrocinador (conforme o link recebido)  
      3. Se não houver Link do site do patrocinador  
         1. Não deve ser clicável.

4. **Publicidade**  
   1. A exibição de publicidade para o template de artigo patrocinado deve seguir as mesmas regras especificadas em [Controle de Publicidade](?tab=t.q2wu7vijixnr).   
   2. **Nota**: Na maioria dos casos, a exibição de publicidade será definida pelo atributo hideAds no payload do artigo.  
      

---

