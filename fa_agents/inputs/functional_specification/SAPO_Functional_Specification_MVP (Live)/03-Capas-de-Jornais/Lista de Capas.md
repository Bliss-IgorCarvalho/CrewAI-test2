# Lista de Capas

---

### **Lista de Capas**

O utilizador deve poder visualizar uma listagem completa de capas filtradas por temática ou sub-temática.

Design

1. [Link Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-15501&t=wAieDihblOGN662Q-0)  
   

Funcional

1. **Regras de exibição**  
   1. Global:  
      1. Para cada capa-fonte, deve ser exibida apenas 1 capa-publicação;  
      2. Para cada capa-fonte, deve ser exibida a capa-publicação com data de publicação mais recente (independente do valor da data ou da periodicidade de publicação);

   2. Quando filtrado por *favoritas*:  
      1. Devem ser exibidas **apenas** as capas definidas como *favoritas*;  
      2. Devem ser exibidas **todas** as capas definidas como *favoritas*;  
      3. A filtragem por capas favoritas **independe** da *temática* ou *sub-temática* a qual as capas pertençam.

   3. Quando filtrado apenas por *temática*:  
      1. Devem ser exibidas **apenas** as capas-fonte pertencentes à **temática**;  
      2. Por default, devem ser exibidas **todas** as capas-fonte pertencentes à **temática** escolhida e associadas à **sub-temática** *todos*.

   4. Quando filtrado por *sub-temática*:  
      1. Devem ser exibidas **apenas** as capas pertencentes à **sub-temática** escolhida.  
      2. Devem ser exibidas **todas** as capas pertencentes à **sub-temática** escolhida. 

2. **Regras de Ordenação:**   
   1. Para Capas Favoritas  
      1. Ver em [Ordenar Capas Favoritas](?tab=t.t5wzxs7yo65t#heading=h.ticsymrt3ylh)

   2. Para Capas Não Favoritas  
      1. A aplicação deve ordenar as capas com base na seguinte hierarquia:  
         1.  1º: Ordenar **ascendente** por ***posição***;  
         2. 2º: Ordenar **descendente** por ***data de publicação***;  
         3. 2º: Ordenar **ascendente** por ***nome da capa-fonte***;  
      2. Para este ecrã (*Lista de Capas*) deve ser aplicado o valor de posição associada à sub-temática escolhida no filtro;  
      3. Se o filtro de sub-temática não for aplicado, por default deve ser utilizado o valor de posição associada à sub-temática “*todos”.*

      4. **Nota técnicas**:   
         1. Todos os atributos fazem parte do objeto capa, retornado pelo RabbitMQ-SAPO:  
            1. *posição \=* position;  
            2. *data de publicação \=* DateTime;  
            3. *nome da capa-fonte \=* Producer.Name.  
         2. As capas possuem um valor de posição para cada sub-temática a qual fazem parte, podendo ter diferentes valores de posição entre as sub-temáticas. 

3. **Ações**  
   1. Aceder ao detalhe de um capa em específico:  
      1. Ao interagir com uma capa específica, a aplicação deve ser capaz de redirecionar o utilizador para o layout *[Detalhe de Capa](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5084-13011&t=ENxt9u8Wb4Uvyghy-4)*;  
      2. Deve ser exibido o detalhe da capa selecionada.

---

### **Filtrar capas por Subtemática** 

O utilizador deve poder filtrar capas por sub-temática

Design

1. [Link Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5270-11508&t=vJJ2S42ilo0Nn0uz-4)  
   

Funcional

1. **Comportamento do botão:**  
   1. Para cada temática, devem ser apresentadas como opções de filtro todas as **sub-temáticas** associadas à **temática** escolhida;   
   2. O botão deve ser exibido somente se a temática filtrada possuir capas-fonte associadas a no mínimo uma sub-temática diferente de “*Todos*”;  
   3. Deve poder ser escolhida apenas uma sub-temática por vez.

2. **Comportamento da bottom sheet:**  
   1. Ordenação das opções de filtro (sub-temáticas): As opções de sub-temática disponíveis no filtro devem ser ordenadas em **ascendente** por nome da sub-temática.

   

3. **Comportamento do filtro:**  
   1. Ao escolher uma subtemática, devem ser exibidas apenas as capas associadas a **sub-temáticas** escolhida;  
   2. Deve ser aplicada ordenação utilizando o valor de posição associado a sub-temática escolhida.

---

