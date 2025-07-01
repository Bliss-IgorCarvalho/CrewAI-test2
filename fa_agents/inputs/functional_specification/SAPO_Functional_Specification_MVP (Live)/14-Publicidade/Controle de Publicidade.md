# Controle de Publicidade

---

## **1\. Requisitos Gerais – Setup Default**

1.1. **Ad Servers e Fornecimento de Publicidade**

* A app SAPO deve integrar com as plataformas Google Ads Manager, Outbrain e Teads. O fornecimento dos anúncios será feito e controlado exclusivamente pelos Ad Servers  
* A app não deverá integrar publicidade fornecida diretamente pelos parceiros, o controlo e fornecimento da publicidade ficam a cargo do Ad Server.

1.2. **Ficheiro de Configuração (**partnership.json**)**

* Deve haver um ficheiro único que agrupa as regras e comportamentos de publicidade para cada parceria.  
* Cada parceiro definido no ficheiro (por exemplo, “Sic”) possui configurações específicas em níveis de providers e blocos (ex.: advertisement.providers.google.show, highlights.partner.displayAds).

---

## **2\. Níveis de Controlo e Ordem de Precedência**

A exibição de publicidade na Página de Artigo é controlada de forma hierárquica, conforme os seguintes níveis e ordem de precedência:

2.1. **Nível do Artigo**

* **hideAds (payload do artigo):**  
  * Se o atributo hideAds estiver definido como **true**, nenhum anúncio deverá ser exibido, ignorando as demais regras.  
  * Caso hideAds seja **false** ou não esteja definido, a app deverá descer ao próximo nível de hierarquia (nível do parceiro).

2.2. **Nível do Parceiro**  
 Aplicável aos artigos cujo parceiro está configurado no ficheiro de parcerias (partnership.json). Nesta camada, as regras são avaliadas da seguinte forma:

* **a) Regras da Parceria – Providers:**  
  * Para cada provider (ex.: google, outbrain, teads), verificar o atributo show (ex.: advertisement.providers.google.show):  
    * Se o valor for **false**, os anúncios deste provider não serão exibidos;  
    * se **true**, a avaliação segue para as próximas regras.

* **b) Página de Artigo:**  
  * O atributo advertisement.show presente na configuração do parceiro determina se a publicidade no layout principal do artigo (banners in page, banners sticky, interstitials) deverá ser exibida.  
  * Se definido como **false**, nenhum anúncio será exibido na página principal para aquele parceiro (podendo, entretanto, haver exibição em blocos específicos, se estes permitirem).

* **c) Blocos (dentro do artigo):**  
  * Cada bloco configurado (por exemplo, blockName.displayAds para blocos de highlights, partnerExternal.show, sugestionBlock.show) deverá ser avaliado individualmente.  
    * Se o atributo show do bloco estiver definido como **false**, não serão exibidos anúncios neste bloco;  
    * se **true** e o atributo displayAds também estiver **true**, os anúncios poderão ser exibidos dentro daquele componente.

* **Fluxo de exceção:** Se o atributo advertisement.show for **true**, mas não existirem dados de configuração de publicidade presentes no ficheiro de configuração (partnership.json), então deverão ser aplicadas as regras default.

2.3. **Setup Default (Nível Padrão)**

* Para artigos que não se enquadrem em regras específicas de parceiro ou quando estes atributos não estiverem definidos, aplica-se um conjunto padrão de regras de exibição de anúncios definido internamente pela app.  
  * [Link para mapeamento de publicidade](https://docs.google.com/spreadsheets/d/1UbU6MW9MVdBU2VqNALwIfavbdFYXa1aprGP5TS5l6aQ/edit?gid=0#gid=0)

**Ordem de Precedência Resumida**

* **Artigo:** Primeiro verificar hideAds – se **true**, desativa a publicidade (prevalência exclusiva); caso contrário, desce para o próximo nível.

* **Parceiro:**  
  * Provider: Avaliar configuração de exibição de publicidade para cada provedor (google.show, outbrain.show, teads.show);

  * Página do artigo: Avaliar configuração de exibição de publicidade para a página do artigo (advertisement.show);

  * Blocos: Avaliar configuração de exibição de publicidade para cada bloco (blockName.displayAds).

* **Default:** Se não houver definições específicas, aplicar o comportamento padrão.

---

