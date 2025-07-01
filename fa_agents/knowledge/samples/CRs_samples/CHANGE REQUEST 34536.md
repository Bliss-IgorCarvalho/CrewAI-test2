**CHANGE REQUEST 34536**  
Controlar carregamento do conteúdo das áreas após navegação entre tabs.

**Contexto**  
Ao navegar entre as diferentes áreas da aplicação, em particular ao sair de uma área (Jornais, Feed ou Destaques) e regressar, o conteúdo da área não deve ser automaticamente recarregado. A aplicação deverá manter em cache o conteúdo já renderizado, carregando novos conteúdos apenas após a sua expiração.

**Comportamento Actual**  
Actualmente, quando o utilizador sai de uma área e navega para outra área (tabs), ao retornar, a aplicação actualiza o ecrã automaticamente, carregando novos conteúdos.

**Novo Comportamento Proposto**  
Ao sair de uma área e navegar para outra área, a aplicação deverá manter em cache o conteúdo já renderizado bem como a posição de scroll actual. Ao retornar, se a cache for ainda válida, o utilizador deverá voltar ao ponto exacto onde saiu. Caso a cache já tenha expirado, então o ecrã deverá ser actualizado (refresh). O refresh deve ser realizado somente se a aplicação tiver conexão com internet. Em modo offline, tanto os dados em cache quanto os conteúdos já renderizados devem ser mantidos. 

**Escopo**  
Este comportamento deve ser aplicado para as 3 áreas (tabs) de conteúdo da app: **Jornais**, **Feed** e **Destaques**. Deve ser respeitado o tempo de expiração de cache definido para cada área.   
