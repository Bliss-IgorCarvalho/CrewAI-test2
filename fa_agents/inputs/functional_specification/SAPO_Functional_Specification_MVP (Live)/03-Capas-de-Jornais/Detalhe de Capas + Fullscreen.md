# Detalhe de Capas \+ Fullscreen

---

### **Detalhe de Capa**

O utilizador deve poder visualizar os detalhes de uma capa-publicação específica.

Design

1. [Link Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=6517-29514&t=Bg8k5r4xSiit6KsJ-4)  
   

Funcional

1. **Componentes e Comportamentos:**  
   1. Temática e sub-temática:  
      1. A temática e/ou sub-temática exibida deve ser baseada no filtro aplicado no layout antecessor (seja *Feed* ou *Lista de Capas)*.   
         1. **Nota**: A temática e/ou sub-temática exibida não devem ser baseadas nas sub-temáticas associadas à capa em visualização.

   2. Indicador de Progresso:  
      1. Formato: **n de m** (onde **n** é a capa atual e **m** é o total de capas filtradas).

   3. Imagem da Capa-Publicação;  
      1. Regras de redimensionamento  
         1. **Disclaimer:** Para atender aos layouts previstos em design, a app deve ser capaz de fazer o redimensionamento de imagens. Este redimensionamento pode causar perda de qualidade visual em dispositivos com resoluções maiores ou diferentes proporções. Recomendamos a utilização de imagens com alta resolução para minimizar este impacto.

   4. **Imagem logo** da Capa-Fonte  
      1. Default: Exibe a **imagem logo** da Fonte associada ao artigo.  
      2. Fallback: Para artigos de fontes que não possuam ou por algum motivo não seja possível obter a imagem do logo, este componente não deve ser exibido. 

   5. Nome da Capa-Fonte;  
      1. O nome da capa deve ser clicável;  
      2. Ao clicar, a aplicação deverá levar o utilizador para o website da fonte, utilizando o URL associado à mesma;  
      3. Quando não existir URL associado, o elemento deve manter o mesmo visual;  
      4. **Notas técnicas**:   
         1. Nome da Capa-Fonte: atributo producer.name  
         2. URL para redirecionamento: atributo producer.url

   6. Data de publicação da Capa-Publicação;  
      1. **Nota técnica**: atributo DateTime do objeto capa, retornado pelo RabbitMQ-SAPO.

   7. Floating action button:  
      1. Descrição:   
         1. Interface que dá ao utilizador acesso às principais ações que podem ser realizadas no contexto do detalhe da capa.

      2. Ações:  
         1. Adicionar/Remover capa aos/dos favoritos:;  
         2. Partilhar capa:;  
         3. Ver arquivo de capas: 

      3. Comportamentos:  
         1. Para *Capas* que **não possuam** *Artigos Relacionados*:  
            1. O componente deve ser exibido por default na renderização do ecrã;  
            2. A exibição do componente deve ser contínua.

         2. Para *Capas* que **possuam** *Artigos Relacionados*:  
            1. O componente deve ser exibido por default na renderização do ecrã;  
            2. Ao ser feito scroll down, o componente deve ser escondido/removido;  
            3. Ao ser feito scroll up, o componente deve ser novamente exibido.  
               1. O componente deve permanecer visível até a próxima ação de scroll down.

2. **Regras de exibição e navegação:**  
   1. Navegação entre capas:  
      1. Deve ser possível navegar entre capas diretamente no layout de Detalhe de Capas;  
      2. O carrossel do layout *Detalhe de Capas* deve herdar o mesmo filtro aplicado no layout antecessor (seja *Feed* ou *Lista de Capas);*   
      3. A navegação deve ser limitada às capas da mesma temática e/ou sub-temática filtrada.

3. **Ações**:  
   1. Zoom In:  
      1. O utilizador deve poder aplicar zoom in ao interagir com capa a partir do ecrã de detalhe;  
      2. As interações/gestos específicos que aplicam o zoom, tal como o fluxo dessas interações devem ser implementadas conforme os padrões de interação e guidelines de cada uma das plataformas (Android e iOS);  
         1. Ver detalhes em [Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-15478&t=ypKxIt6CegLiMwGK-0).  
      3. O foco do zoom in deve ser aplicado centralizando a área da capa/imagem onde a interação/gesto foi feita.

   2. Visualizar capa em fullscreen:  
      1.  O utilizador deve aceder ao modo de visualização da capa em fullscreen ao interagir com a capa a partir do ecrã de detalhe;  
      2. As interações/gestos específicos que aplicam o zoom, tal como o fluxo dessas interações devem ser implementadas conforme os padrões de interação e guidelines de cada uma das plataformas (Android e iOS);  
         1. Ver detalhes em [Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-15478&t=ypKxIt6CegLiMwGK-0).

         

   3. Adicionar / Remover dos Favoritos  
      1. Requisitos especificados em [Capas Favoritas](https://dev.azure.com/blissapps/SAPO%20App/_workitems/edit/29390)

   4. Partilhar Capa  
      1. Requisitos especificados em Partilhar conteúdos

   5. Aceder ao Arquivo de Capas  
      1. Redireciona o utilizador para o ecrã [Arquivo de Capas](https://dev.azure.com/blissapps/SAPO%20App/_workitems/edit/29391).

4. **Artigos Relacionados:**  
   1. Requisitos especificados em Artigos Relacionados (Capas)

---

### **Detalhe de Capa \- Fullscreen view**

O utilizador deve poder visualizar uma capa-publicação específica em modo fullscreen.

Design

1. [Link Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-16024&t=wAieDihblOGN662Q-0)  
   

Funcional

1. **Componentes e Comportamentos::**  
   1. Imagem da capa-publicação:  
      1. A aplicação deve exibir a imagem da  capa-publicação selecionada em modo fullscreen;

   2. Floating action button:  
      1. Por default o componente **não deve** ser exibido na renderização do ecrã;  
      2. Ao interagir com a imagem da capa-publicação, o componente deve ser exibido.  
         1. As interação/gesto específicos deve ser implementada conforme os padrões de interação e guidelines de cada uma das plataformas (Android e iOS). Ver detalhes em [Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-15478&t=ypKxIt6CegLiMwGK-0).

2. **Regras de navegação:**  
   1. Navegação entre capas:  
      1. Deve ser possível navegar entre capas diretamente modo de visualização de Capas em fullscreen;  
      2. O carrossel do modo de visualização de Capas em fullscreen deve manter o mesmo filtro aplicado no layout antecessor (*Feed* ou *Lista de Capas);*   
      3. A navegação deve ser limitada às capas da mesma temática ou sub-temática.

3. **Ações:**  
   1. Zoom-in e Zoom-out:  
      1. Ao interagir com a imagem da  capa-publicação em modo fullscreen, o utilizador deve poder aplicar Zoom-in e Zoom-out;  
      2. As interações/gestos específicos que aplicam o zoom, tal como o fluxo dessas interações devem ser implementadas conforme os padrões de interação e guidelines de cada uma das plataformas (Android e iOS);  
         1. Ver detalhes em [Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=5171-15478&t=ypKxIt6CegLiMwGK-0).  
      3. O foco do zoom in deve ser aplicado centralizando a área da capa/imagem onde a interação/gesto foi feita.

   2. Voltar para o Detalhe  
      1. O utilizador deve poder voltar ao ecrã de detalhe a partir do ecrã fullscreen.  

---

### **Bottom Bar**

Comportamento da Bottom App Bar nos ecrãs Detalhe de Capas e Fullscreen

Funcional

1. **Regras de exibição:**  
   1. Default: Por default, a Bottom App Bar **nunca é exibida**.

### ---

### **Escopo Futuro**

Este bloco descreve funcionalidades planejadas para a versão final das Capas de Jornais, mas que não serão incluídas na entrega atual do PBI. Essas funcionalidades serão gradualmente implementadas em futuras versões da app, conforme o roadmap do produto.

1. **Artigos Relacionados:** Bloco de conteúdo que exibe artigos relacionados à capa em visualização:  
   1. Este componente será implementado em um PBI separado, com requisitos a serem especificados em [Artigos Relacionados (Capas)](https://dev.azure.com/blissapps/SAPO%20App/_workitems/edit/29392), após a implementação e entrega de [Data Enrichment: Tags](https://dev.azure.com/blissapps/SAPO%20App/_workitems/edit/29591).

---

