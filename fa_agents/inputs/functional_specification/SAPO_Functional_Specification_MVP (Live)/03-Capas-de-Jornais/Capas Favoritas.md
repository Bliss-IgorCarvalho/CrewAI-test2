# Capas Favoritas

---

### **Adicionar Capa aos Favoritos**

O utilizador deve poder **adicionar** uma **Capa-Fonte** aos favoritos

Functional

1. A capa-fonte adicionada aos favoritos deve passar a ser exibida no *Carrossel de Capas Favoritas*;  
2. A capa-fonte adicionada aos favoritos deve continuar a ser exibida no carrossel correspondente a temática da capa;  
3. Sincronização:  
   1. Para utilizadores **autenticados** as Capas Favoritas devem ser sincronizadas com a conta SAPO ID, conforme as os fluxos e regras de sincronização descritos em [Sincronização de preferências](?tab=t.uybrqu3pzgl9);  
   2. Para utilizadores **não autenticados** as Capas Favoritas não devem ser sincronizadas com o SAPO ID. A informação é registada localmente e é perdida em casos de desinstalação da app (também conforme as regras de [sincronização de preferências](?tab=t.uybrqu3pzgl9)).

---

### **Remover Capa dos Favoritos**

O utilizador deve poder **remover** uma **Capa-Fonte** dos favoritos

Functional

1. A capa-fonte removida dos favoritos deve deixar de ser exibida no *Carrossel de Capas Favoritas*;  
2. A capa-fonte removida dos favoritos deve continuar a ser exibida no carrossel correspondente a temática da capa;  
3. Sincronização:  
   1. Para utilizadores **autenticados** as Capas Favoritas devem ser sincronizadas com a conta SAPO ID, conforme as os fluxos e regras de sincronização descritos em [Sincronização de preferências](?tab=t.uybrqu3pzgl9);  
   2. Para utilizadores **não autenticados** as Capas Favoritas não devem ser sincronizadas com o SAPO ID. A informação é registada localmente e é perdida em casos de desinstalação da app (também conforme as regras de [sincronização de preferências](?tab=t.uybrqu3pzgl9)).

---

### **Visualizar Capas Favoritas (Carrossel)**

O utilizador deve poder **visualizar** suas **Capas-Fonte** favoritas

Functional

1. **Regras de exibição do componente**  
   1. Se houver uma ou mais capas-fonte definidas como “favorita”:  
      1. Então o componente *Carrossel* é exibido, conforme o [UI-Layout](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-15506&t=wAieDihblOGN662Q-0).  
   2. Se não houverem capas-fonte definidas como “favorita”:  
      1. Então deve ser exigido o componente placeholder, conforme o [UI-Layout](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-15541&t=wAieDihblOGN662Q-0);  
      2.  O componente placeholder deve ser dismissible;  
      3. Após ser “dismissed”, o placeholder não deve ser exibido novamente.

2. **Regras de exibição das capas**  
   1. Para cada capa-fonte, deve ser exibida apenas 1 capa-publicação;   
   2. Para cada capa-fonte, deve ser exibida a capa-publicação com data de publicação mais recente (independente do valor da data ou da periodicidade de publicação);  
   3. Devem ser exibidas **apenas** as capas definidas como *favoritas*;  
   4. Devem ser exibidas **todas** as capas definidas como *favoritas*;  
   5. A filtragem por capas favoritas **independe** da *temática* ou *sub-temática* a qual as capas pertençam.

3. **Aceder à lista completa de capas favoritas**   
   1. Ao interagir com o carrossel, a aplicação deve ser capaz de redirecionar o utilizador para o layout [*Lista de Capas*](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-15499&t=wAieDihblOGN662Q-0);  
   2. Após o redirecionamento, a Lista *de Capas* deve ser automaticamente filtrada por capas favoritas;  
   3. As regras de **exibição** devem ser as mesmas descritas no tópico acima (e também descritas em [*Lista de Capas*](https://dev.azure.com/blissapps/SAPO%20App/_workitems/edit/29387));  
   4. As regras de **ordenação** devem ser as mesmas descritas no tópico abaixo.

---

### **Ordenar Capas Favoritas**

O utilizador deve poder **ordenar** suas **Capas-Fonte** favoritas no *Carrossel de Capas Favoritas*

Design

1. [Link Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-15655&t=wAieDihblOGN662Q-0)

Functional

1. **Ordenação Default**: Por default, a ordenação de capas favoritas deve seguir a lógica de “fila”. Cada nova capa-fonte adicionada aos favoritos deve ser posicionada ao final de lista;

2. **Ordenação Manual**: O utilizador deve poder alterar manualmente a ordenação das capas favoritas ([Ver fluxo em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-15655&t=wAieDihblOGN662Q-0));

3. **Regras de exibição do botão *Ordenar*:**  
   1. Exibição do Feed de Capas:  
      1. Deve ser exibido no *Carrossel de Capas favoritas*;  
      2. Deve ser exibido somente se houver mais de 1 capa adicionada aos favoritos.

   2. Exibição na Lista de Capas:  
      1. Deve ser exibido somente quando filtrado por *Favoritos*;   
      2. Deve ser exibido somente se houver mais de 1 capa adicionada aos favoritos.  
            
4. **Comportamento local**: A ordenação manual deve ser um comportamento local, que **não deve ser sincronizado com o Portal Web** e deve estar associada ao dispositivo. Se o utilizador desinstalar a aplicação, a ordenação manual não é mantida. Ao instalar a aplicação novamente deve ser aplicada a ordenação default. Este comportamento deve ser aplicado tanto para utilizadores anónimos quanto para utilizadores autenticados.

### ---

