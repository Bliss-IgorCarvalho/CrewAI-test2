# Sincronização de preferências

---

A aplicação permite que os utilizadores naveguem anonimamente ou se autentiquem através de uma conta SAPO ID. Para garantir a continuidade da experiência entre dispositivos, a sincronização de dados (como favoritos, guardados, preferências ou outras personalizações) é implementada com base no estado de autenticação do utilizador e no dispositivo utilizado. 

Fluxos de sincronização:

1. **Primeira autenticação (merge inicial):**  
   Quando um utilizador anônimo autentica-se na app pela primeira vez (independentemente de ser um registro ou acesso a uma conta já existente), os dados armazenados localmente no dispositivo são mesclados com os dados sincronizados na conta autenticada (SAPO ID). Após essa sincronização inicial, a aplicação passa a exibir sempre os dados sincronizados à conta SAPO ID.

2. **Demais autenticações**  
   Quando um utilizador anônimo autentica-se na app pela segunda vez (ou posterior) com a mesma conta SAPO ID (independente do dispositivo), os dados locais do dispositivo não serão mesclados com os dados da conta autenticada. A aplicação exibirá apenas os dados sincronizados à conta SAPO ID. 

3. **Sessões autenticadas:**  
   Enquanto o utilizador estiver autenticado, qualquer alteração nos dados de preferências (apenas os sujeitos a sincronização)  serão sincronizados com a conta SAPO ID autenticada. Assim, ao acessar a conta em outro dispositivo autenticado, os dados refletem sempre o estado mais recente armazenado na conta SAPO ID.

4. **Sessões anónimas:**  
   No caso de uma mudança de Device ID enquanto o utilizador estiver navegando anonimamente (por exemplo, após uma reinicialização de fábrica ou troca de dispositivo), a app criará um novo perfil anónimo, desvinculado dos dados anteriormente armazenados. Isso ocorre porque a app identifica usuários anônimos exclusivamente pelo Device ID.

5. **Dados de preferências sujeitos a sincronização:**  
   1. Capas Favoritas;  
   2. Artigos Guardados;  
   3. Following:  
      1. Fontes;  
      2. Temáticas;  
      3. Sub-temáticas;  
      4. Tags;  
      5. Autores.  
   4. Interações de Feedback:  
      1. Ver mais;  
      2. Ver menos.  
   5. Subscrição de Notificações

---

