**CHANGE REQUEST 34991**  
Bloco Exclusivos do Parceiro | Fallback para artigos sem imagem.

**Contexto**  
O bloco exclusivo do parceiro consome diretamente do endpoint do SAPO o conteúdo (artigos) e os elementos (imagem e título) necessários para montar o card de pré-visualização do artigo. No entanto, alguns artigos estão a ser recebidos sem imagem.

**Comportamento Atual**  
O cartão de pré-visualização do artigo exibe a imagem e o título diretamente dos dados recebidos do endpoint, sem fallback em caso de falha no recebimento.

**Novo Comportamento**  
O card do preview do artigo (e a correta exibição dos componentes previstos em design), deve ser composto pelos recebidos na resposta do endpoint:

1. **Título**  
   1. **Descrição**: Título do artigo exibido no card.  
   2. **Atributo**: Corresponde ao atributo title da resposta do endpoint.  
   3. **Campo obrigatório**: Caso não seja recebido, o artigo não deve ser exibido no bloco.

2. **Imagem**  
   1. **Descrição**: Imagem do artigo exibido no card.  
   2. **Atributo**: Corresponde ao atributo image da resposta do endpoint.  
   3. **Campo opcional \[fallback 1\]**: Caso não seja recebido, a imagem de logo do parceiro (fonte do artigo \- partner) deve ser utilizada como imagem do card.   
   4. **\[Fallback 2\]**: Se não for possível obter a imagem de logo do parceiro, então deve ser utilizada uma imagem placeholder (a definir em Design) como imagem do card.

3. **Link**   
   1. **Descrição**: Link para o artigo no site do parceiro   
   2. **Atributo**: Corresponde ao atributo url da resposta do endpoint  
   3. **Campo obrigatório**:Caso não seja recebido, o artigo não deve ser exibido no bloco.

