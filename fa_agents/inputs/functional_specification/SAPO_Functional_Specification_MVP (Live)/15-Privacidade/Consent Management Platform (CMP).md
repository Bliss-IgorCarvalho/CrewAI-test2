# Consent Management Platform (CMP)

---

## **Visão Geral**

A aplicação móvel deve integrar-se com a CMP [Inmobi](https://advertising.inmobi.com/cmp) para gerir os consentimentos dos utilizadores relativos à recolha, processamento e partilha de dados pessoais (publicidade e analytics), garantindo conformidade com o GDPR e boas práticas de privacidade.

1. #### **Primeira Abertura (Onboarding)**

   1. O painel de consentimento da CMP Inmobi deve ser exibido na primeira utilização da aplicação, durante o processo de onboarding. O painel deve ser exibido conforme os componentes e design nativos da plataforma Inmobi. O utilizador deve poder aceitar ou gerir as suas preferências de consentimento.

2. #### **Acesso Permanente**

   1. Disponibilizar, na área de Perfil, a opção “Definições de Privacidade” que abre o ecrã de consentimento da CMP, sempre no idioma do sistema.

3. #### **Verificação dos Consentimentos**

   1. As funcionalidades de publicidade e analytics devem sempre verificar as configurações de consentimento definidas no CMP antes de rastrear os utilizadores.

4. #### **Fluxo de Re-consentimento Automático**

   1. Sempre que a política de privacidade ou as categorias de consentimento forem atualizadas para uma nova versão, o utilizador deve ser forçado a rever e reconfirmar o consentimento no próximo arranque da app, o ecrã de consentimento é novamente apresentado, bloqueando o acesso até a ação do utilizador.

5. #### **Suporte a Múltiplos Idiomas**

   1. O ecrã de consentimento (CMP Inmobi) deve ser apresentado automaticamente no idioma definido no dispositivo (pt-PT, en-US, es-ES, etc.).   
   2. Se o idioma do dispositivo não for suportado, recorrer ao inglês por defeito.

6. #### **Link para Política de Privacidade**

   1. Dentro do ecrã “Definições de Privacidade” (Perfil), disponibilizar um link ou visualização embutida que abra a Política de Privacidade completa e os Termos de Serviço, sem sair da app.

---

