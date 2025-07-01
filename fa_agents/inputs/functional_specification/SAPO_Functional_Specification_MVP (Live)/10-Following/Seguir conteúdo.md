# Following \- Seguir conteúdo

---

Requisitos de Design

1. [Ver design em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=6081-41075&t=d393wPn6Kz5XhKSI-4)

Funcionais

1. **Requisitos Gerais**  
   1. Following:  
      1. O utilizador deve poder seguir um “tipo” de conteúdo, para indicar preferências de forma explícita;  
      2. O conteúdo seguido deve ser adicionado às preferências do utilizador e associado a sua conta SAPO ID;  
      3. As novas preferências devem ser utilizadas pelas funcionalidades e regras de recomendação e filtragem de artigos entregues ao utilizador nas áreas de conteúdo personalizado.

   2. Unfollowing:  
      1. O utilizador deve poder deixar seguir um “tipo” de conteúdo, para indicar preferências de forma explícita;  
      2. O conteúdo deve ser removido das preferências do utilizador e desassociado a sua conta SAPO ID;  
      3. As antigas preferências devem deixar de ser utilizadas pelas funcionalidades e regras de recomendação e filtragem de artigos entregues ao utilizador nas áreas de conteúdo personalizado.

2. **O que pode ser seguido**  
   Elementos/atributos dos conteúdos que podem ser seguidos pelo utilizador:

   1. **Temática** (category ou parentCategory):  
      1. Corresponde à temática a qual o conteúdo pertence;

      2. Following: Ao seguir uma temática, o utilizador deve passar automaticamente a seguir todas as subtemáticas que pertençam a temática seguida;

      3. Unfollowing: Ao deixar de seguir uma temática, o utilizador deve:  
         1. Deixa de seguir a temática;  
         2. Deixa de seguir as sub-temáticas que foram seguidas em consequência ao seguimento da temática pai;  
         3. Continuar se seguir as sub-temáticas que foram seguidas manualmente (antes do seguimento da temática pai)

      4. Nota: Sobrepõe-se ao following de sub-temáticas. 

   2. **Sub-temática** (category):  
      1. Corresponde à sub-temática a qual o conteúdo pertence;

      2. Following: Ao seguir uma sub-temática, o utilizador deve passar a seguir apenas a sub-temática escolhida;

      3. Unfollowing:  Ao deixar de seguir uma temática, o utilizador deve deixar seguir apenas a sub-temática escolhida.  
           
   3. **Fonte/Parceiro** (partner):  
      1. Corresponde à fonte/parceiro fornecedor do conteúdo;

   4. **Tag**:  
      1. Corresponde a uma tag associada ao conteúdo;  
      2. Os conteúdos podem ter mais de uma tag associada. Todos os conteúdo associados a tag seguida devem ser considerados como preferência, independente das outras tags associadas ao mesmo conteúdo.  

   5. **Autor** (authors):   
      1. Corresponde a um autor associado ao conteúdo;  
      2. Os conteúdos podem ter mais de um autor associado. Todos os conteúdos associados ao autor seguido devem ser considerados como preferência, independente dos outros autores associados ao mesmo conteúdo. 

3. **Sincronização de Preferências**  
   1. As alterações aos conteúdos seguidos devem reflectir nos dados de preferências do utilizador;  
   2. Para utilizadores autenticados, as alterações devem ser sincronizadas com a conta SAPO ID;  
   3. Todas as sincronizações devem ser realizadas conforme fluxo de [Sincronização de preferências](?tab=t.uybrqu3pzgl9); 

4. **Funcionalidades Impactadas**  
   1. Feed de Artigos   
      1. O feed passa a ser filtrado por conteúdos seguidos.  
         1. Nota: aplicável somente na ausência do recommender. 

   2. Digest  
      1. A seleção de artigos do Digest passa a ser filtrada por conteúdos seguidos (conforme o Feed).

   3. Recomendação de Conteúdo (AI-Recommender)  
      1. O serviço de recomendação de conteúdo deve considerar os conteúdos seguidos como dados de preferência explícita do utilizador. 

---

