# Reportar Problema

---

 

Design

1. [Ver em Figma](https://www.figma.com/design/jWFlJEYGhbSeCSDxLjKHTp/Sapo%E3%83%BB%5BHandoff%5D-Design-Visual?node-id=7794-63648&t=nJiIcfmqpGlmk5Dp-4)

Requisitos Funcionais

**Reportar problema em conteúdo criado por IA**:   
A aplicação deve permitir que os utilizadores reportem problemas identificados em conteúdos tratados ou gerados automaticamente por inteligência artificial.

1. **Funcionalidades aplicáveis**  
   1. O recurso de reportar problemas deve estar disponível em todas as funcionalidades que utilizam IA para geração ou tratamento de conteúdo, especificamente nas seguintes áreas:  
      1. Resumo em Stories (‘summary\_stories’)  
      2. Resumo em Áudio  (‘summary\_audio’)  
      3. Página de Artigo Versão Áudio (‘article\_audio’)  
      4. Página de Artigo (‘article\_page’)

2. **Formulário de Report**  
   1. Não deve ser permitido submeter o report sem escolher uma opção;  
   2. Não deve ser permitido escolher mais de uma opção;  
   3. Não deve ser permitido o envio de múltiplos reports para o mesmo artigo na mesma funcionalidade.  
      1. Exemplo: O artigo X pode ser consumido em um resumo e em um áudio. Cada um dos formatos pode ter um report separado. 

3. **Informação contextual por funcionalidade**  
   As opções devem ser contextuais e adaptadas à funcionalidade. Para cada funcionalidade devem ser exibidas opções e personalizadas:   
   1. **Geral (exibido em todas as features)**  
      1. Erro no conteúdo  
      2. Problemas na tradução (apenas para conteúdos traduzidos)  
      3. Idioma incorreto (apenas para conteúdos traduzidos)  
      4. Outros  
      5. Descreva seu problema  
         1. Formato: caixa de texto com o máximo de 350 caracteres;  
         2. Preenchimento opcional

      6. **Nota**: A aplicação SAPO Mobile identifica conteúdo traduzido se um artigo possuir tradução para francês (FR) e a aplicação estiver em francês, ou se possuir tradução para inglês (EN) e a aplicação estiver em inglês. Caso a aplicação esteja em português ou o artigo não tenha tradução, o conteúdo é tratado como normal.

   2. **Resumos em Stories (1)**  
      1. Resumo pouco claro  
      2. Conteúdo incompleto

   3. **Resumos em Áudio (2)**  
      1. Problemas com o som  
      2. Conteúdo incompleto

   4. **Verão Áudio de Artigos Completos (3)**  
      1. Problemas com o som  
      2. Conteúdo incompleto

4. **Feedback ao utilizador**  
   1. Após o envio do formulário, a aplicação deverá apresentar uma mensagem de confirmação de gravação bem-sucedida do report.  
   2. O CTA de ação principal  deverá adotar uma aparência visual de desativado, mas manter a sua funcionalidade de clique.  
   3. Caso o utilizador clique no CTA (no estado "desativado") após já ter submetido um report, a aplicação deverá exibir uma mensagem a informar que o utilizador já efetuou um envio e não é permitida uma nova submissão.

5. **Persistência  e envio dos dados para infraestrutura SAPO**  
   1. Os dados do report devem ser armazenados e enviado por email para as equipas de suporte SAPO;  
   2. Email de destino: mobile@suporte.sapo.pt  
   3. A cada resposta deve incluir:  
      1. **Dados do Report**  
         1. Data do Report (report\_date);  
         2. Opção selecionada; (article\_report\_option\_id)  
         3. Descrição do problema (campo texto) (description)  
      2. **Dados do Conteúdo**  
         1. ID do artigo; (article\_id)  
         2. Posição do step do story (article\_summary\_part)  
         3. Funcionalidade; (article\_report\_type\_id)  
            1. Values: ‘summary\_stories’, ‘summary\_audio’, ‘article\_audio’, ‘article\_page’  
      3. **Dados do Utilizador**  
         1. Conta SAPO (sapo\_id)  
         2. Nome (user\_name)  
            1. Utilizadores não autorizados devem ser identificados com o texto fixo *“anónimo”*.  
         3. Email (user\_email)  
      4. **Dados do Dispositivo**  
         1. Versão do OS (os\_version)  
         2. Versão da App (app\_version)  
         3. Dispositivo (device)  
         4. Idioma do dispositivo (device\_language)  
         5. Idioma da app (app\_language)

   4. Formato de envio do email:

```
Dados do Report  
report_date: 2025-05-14  
article_report_option_id: Resumo pouco claro  
description: O resumo apresenta frases desconexas e não reflete o conteúdo do artigo original.  

Dados do Conteúdo  
article_id: 982374  
article_summary_part: 2  
article_report_type_id: summary_stories  

Dados do Utilizador  
sapo_id: 837463  
user_name: João Martins  
user_email: joao.martins@example.com  

Dados do Dispositivo  
os_version: iOS 17.4  
app_version: 4.8.2  
device: iPhone 13  
device_language: pt-PT  
app_language: pt-PT
```

---

