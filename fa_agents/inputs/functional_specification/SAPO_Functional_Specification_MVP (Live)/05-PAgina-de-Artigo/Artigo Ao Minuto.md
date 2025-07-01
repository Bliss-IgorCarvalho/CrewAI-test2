# Artigo Ao Minuto

# ---

### Descrição

Layout específico para acompanhamento de um tema. Agrega vários artigos em uma única página para acompanhamento em modo timeline.

Requisitos de Design

1. [Ver design em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7794-64038&t=0TRQX4vhQVqMAZ9v-4)

Requisitos Funcionais

1. **Estrutura da Timeline:**   
   1. Entrada \=  Item de conteúdo que compõe a timeline de um *Artigo ao minuto.* As entradas na timeline podem ser:  
      1. Entrada Local: Um *conteúdo* que só existe na timeline do *Artigo ao minuto* e pode ter um link para conteúdo externo.  
      2. Entrada de Artigo: Um *artigo* que existe na app e é incluído na timeline do *Artigo ao minuto.*  
         1. No payload do Artigo Ao Minuto (Liveblog) devem ser identificados pelos posts com objeto relatedArticle.

2. **Comportamento e regras gerais do Artigo Ao Minuto:**  
   1. Pode ser composto por múltiplas entradas (artigos);  
   2. As entradas (artigos) podem estar associadas a diferentes fontes (partners);  
   3. Pode ser atualizado várias vezes ao dia;  
   4. A cada atualização novas entradas podem ser adicionadas;  
   5. As novas entradas são adicionadas em dinâmica de pilha. Os novos artigos são inseridos no topo da lista e os artigos já existentes são mantidos;  
   6. A ordenação da timeline de artigos dentro de um artigo ao minuto é exclusivamente baseada na dinâmica de pilha, independentemente da data de publicação (createdAt) dos artigos adicionados.

3. **Regras para Entrada de Artigo:**  
   1. Podem pertencer à diferentes Fontes/Parceiros (partners);  
   2. Devem ter indicação visual de qual Fonte/Parceiro pertence;  
   3. Pode estar simultaneamente em mais de um artigo ao minuto;  
   4. De ser clicável e possuir link que redireciona o utilizador para página de artigo, onde o utilizador deve poder visualizar o artigo completo.

4. **Regras para Entradas Locais:**  
   1. Todos as entradas locais devem ser considerados produção SAPO;  
   2. Podem ter um link para conteúdo externo;  
   3. Os artigos locais não precisam ter indicação de Fonte/Parceiro (partners).

5. **Publicidade:**  
   1. Devem ser aplicadas as mesmas definições de publicidade do template Padrão.   
      1. Ver especificações em [Advertisements Mapping](https://docs.google.com/spreadsheets/d/1UbU6MW9MVdBU2VqNALwIfavbdFYXa1aprGP5TS5l6aQ/edit?gid=0#gid=0). 

Requisitos Técnicos

1. Deve haver um payload com estrutura específica para o artigo ao minuto;

---

