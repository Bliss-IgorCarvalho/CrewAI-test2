**CHANGE REQUEST 34614**  
Adicionar validação para controlar exibição do toggle (Texto vs Áudio)

**Contexto**  
Os artigos exibidos em Digest são resultado da seleção dos 12 primeiros artigos da lista de recomendações gerada pelo recommender. O utilizador pode escolher a quantidade de resumos a ser vista (4, 8 ou 12\) e o formato de exibição (stories ou áudio). No entanto, é possível que não haja 12 artigos com disponibilidade de áudio e ou resumos em texto.

**Solicitação**  
A aplicação deve validar se os artigos selecionados para exibição em Digest possuem ficheiro de resumo em texto e resumo em áudio, e consoante ao resultado desta validação controlar se o card do Digest e o toggle de seleção de formato devem ser exibidos.  

**Novos comportamentos**

* A aplicação deverá gerar duas listas de resumos para o digest:  
  * **Lista para stories**: Os 12 primeiros artigos recomendados com resumo em texto.  
  * **Lista para áudio**: Os 12 primeiros artigos recomendados com resumo em áudio.

* As aplicações devem verificar as listas recebidas e, com base nisso, controlar a apresentação do bloco de digest e da opção de escolha do formato:  
  * **Existindo** listas de resumos para stories **e** para áudio, mostrar o card de acesso ao digest e o seletor de formato.  
  * **Existindo** lista de resumos para stories **e não existindo** para áudio, mostrar o card de acesso ao digest, mas não o seletor de formato.  
  * **Não existindo** lista de resumos para stories, não mostrar o card de acesso ao digest.

