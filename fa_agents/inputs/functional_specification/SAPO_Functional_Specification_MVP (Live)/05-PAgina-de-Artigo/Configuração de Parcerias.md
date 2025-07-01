# Configuração de Parcerias

# ---

**Descrição**

O ficheiro de configuração de parcerias (partnership.json) define as regras e configurações para exibição de artigos e destaques de parceiros na app SAPO. Este ficheiro gere as parcerias (partnershipID) e os parceiros (partners) de cada parceria. A configuração permite definir permissões de IA, restrições de conteúdo e configurações de blocos e publicidade. A estrutura de dados é enviada via RabbitMQ para atualizar as regras de exibição na aplicação. 

1. **Requisito Gerais**  
   1. Parceria: É uma entidade abstrata que agrupa diferentes parceiros que partilham os mesmos acordos comerciais ou conjunto de regras.

   2. Parceiro: São as *Fontes* ou *OCS (órgãos de comunicação social)*, como *A Bola, SIC*, *Expresso, etc*.

   3. Deve haver apenas um único ficheiro de configuração. Neste ficheiro devem estar listadas todas as parcerias (partnershipID) vigentes, cada uma com os respectivos parceiros (partners) que fazem parte desta parceria;

      1. Fluxo de exceção 1 \- Duplicidade Parceiros na mesma Parceria:   
         1. Se o ficheiro partnership contiver uma lista de parcerias e um mesmo parceiro aparecer mais de uma vez na mesma lista, a aplicação deve considerar apenas os dados da última ocorrência desse parceiro. Por exemplo, se um parceiro estiver presente na posição 2 e na posição 5 da lista, serão considerados apenas os dados da posição 5\.

            Exemplo: \[parceiroA, parceiroB, parceiroA, parceiroC\] Neste caso, a aplicação deve considerar os dados associados ao **parceiroA** na **posição 2** (última aparição) e ignorar os dados da posição 0\.

      2. Fluxo de exceção 2 \- Duplicidade Parceiros em Parcerias diferentes:  
         1. Se o ficheiro partnership contiver uma lista de parcerias e um mesmo parceiro aparecer mais de uma vez em parcerias diferentes, a aplicação deve considerar apenas os dados da última ocorrência desse parceiro. Por exemplo, se um parceiro estiver presente na lista da parceira 1 e presente na lista da parceira 2, serão considerados apenas os dados presentes na lista 2\.

            Exemplo:  
             Lista 1: \[**parceiroA**, parceiroB,parceiroC\],  
             Lista 2: \[parceiroD, parceiroE,**parceiroA**\]   
            Neste caso, a aplicação deve considerar os dados associados ao **parceiroA** na **lista 2** (última aparição) e ignorar os dados da posição 0\.

   4. Os dados do ficheiro devem ser recebidos pela app via RabbitMQ; 

   5. Os dados do ficheiro podem ser actualizados periodicamente via RabbitMQ. A cada nova mensagem recebida, os dados do ficheiro corrente devem ser integralmente substituídos pelos dados do novo ficheiro. Cada nova configuração recebida sobrescreve a configuração anterior. 

2. **Configurações a nível de Parceria**  
   1. Parceiros  
      1. Especifica os parceiros que fazem parte da parceria.

3. **Configurações a nível de Parceiro**  
   1. Permissão para transformação e tratamento por IA  
      1. Determina se o conteúdo dos artigos produzidos ou publicados pelos parceiros que pertencem à parceria podem ser partilhados e processados por ferramentas/serviços de inteligência artificial para criação e/ou transformação de conteúdo. 

   2. Restrição de conteúdo  
      1. Determina se os blocos de conteúdos exibidos nos artigos produzidos ou publicados pelos parceiros que pertencem à parceria podem exibir artigos de outros parceiros que não pertencem à mesma parceria.

   3. Blocos  
      1. Quais blocos devem fazer parte do layout do template e configuração de conteúdo de cada um dos blocos

   4. Publicidade  
      1. Determina a exibição e comportamento de publicidade nos artigos para cada um dos parceiros.

4. **Permissão para transformação e tratamento por IA**:  
   1. Requisitos Gerais;  
      1. Apenas os atributos com valor

   2. Geração automática de resumos dos artigos:  
      1. Determina se o conteúdo do artigo pode ser utilizado para geração de resumos automáticos feitos;  
      2. Atributo automaticSummaryGeneration;

   3. Tradução automática para outros idiomas:  
      1. Determina se o conteúdo do artigo pode ser traduzido para outro idiomas (diferentes o original);  
      2. Atributo automaticTranslation;

   4. Criação de versões em áudio dos artigos:  
      1. Determina se o conteúdo do artigo pode ser utilizado para geração automática de áudio (Text-to-Speech);  
      2. Atributo audioCreation;

   5. Geração de vídeos com avatares baseados nos artigos:  
      1. Determina se o conteúdo do artigo pode ser utilizado para geração automática de vídeos;  
      2. Atributo videoCreationWithAvatar;

   6. Enriquecimento automático dos dados com tags e metadados:  
      1. Determina se o conteúdo do artigo pode ser utilizado para processos de classificação e enriquecimento de dados;   
      2. Atributo tagEnrichment;

5. **Blocos**:  
   1. Estrutura Base  
      1. show: Determina se o bloco deve ser exibido nos artigos do parceiro;  
      2. viewItems: Determina quantos itens (artigos) devem ser exibidos no bloco;  
      3. dataGroupId: Quando informado, determina os artigos que devem ser exibidos no bloco;  
      4. title:  Determina o título a ser exibido no o bloco nos artigos do parceiro;  
      5. displayAds: Determina se o bloco deve apresentar publicidade. 

   2. Últimas do Parceiro (highlights):  
      1. Define as configurações de comportamento e conteúdo para o bloco *Últimas do Parceiro*, exibido no final dos artigos do parceiro questão.  
      2. [Ver bloco em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7773-34395&t=0TRQX4vhQVqMAZ9v-4)

   3. Exclusivos do Parceiro (partnerExternal):  
      1. Define as configurações de comportamento e conteúdo para o bloco *Exclusivos do Parceiro*, exibido no final dos artigos do parceiro questão.  
      2. [Ver bloco em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7773-34401&t=0TRQX4vhQVqMAZ9v-4)

   4. Últimas da Parceria (sugestionBlock):  
      1. Define as configurações de comportamento e conteúdo para o bloco *Últimas da Parceria*, exibido no final dos artigos do parceiro questão.  
      2. [Ver bloco em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7773-34407&t=0TRQX4vhQVqMAZ9v-4)  

6. **Publicidade**:  
   1. Ver [Regras de Publicidade](?tab=t.q2wu7vijixnr).

---

