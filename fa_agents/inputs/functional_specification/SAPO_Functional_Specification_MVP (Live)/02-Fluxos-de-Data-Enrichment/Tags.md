# Data Enrichment \- Tags

---

 

### Classificação 

O fluxo consiste em um pipeline de enriquecimento de dados baseado em IA que analisa o conteúdo dos artigos, identifica termos relevantes e os classifica automaticamente em categorias predefinidas. O processo inclui:

* **Extração**: O sistema de IA processa o texto e identifica entidades, palavras-chave e conceitos utilizando Large Language Models (LLMs)  
* **Classificação**: As tags são atribuídas a categorias específicas (como "Assunto", "Localização geográfica", "Nomes de pessoas", etc.) com base na relevância e no contexto identificado pela IA.  
* **Validação e persistência**: As tags geradas são validadas contra regras predefinidas, e as informações enriquecidas são armazenadas em um banco de dados estruturado, para uso editorial ou automação

1. Fluxo:

### **1\) Extração de Texto**

O primeiro passo consiste na **extração do texto** a ser analisado. Dependendo do tipo de documento processado, essa extração pode ocorrer de duas formas:

* **Para enriquecimento de capas de jornais:** O texto extraído será o conjunto de **manchetes** das publicações. (Capas sem manchete não têm data enrichment).  
* **Para enriquecimento de artigos:** O texto extraído será o **corpo do artigo**.

### **2\) Criação Inicial de Tags**

A partir do texto extraído, um modelo de linguagem gera um conjunto inicial de **tags categorizadas**, identificando entidades presentes no texto que pertençam a um conjunto de categorias relevantes. As categorias incluem:

* **Localizações**  
* **Nomes de Pessoas**  
* **Organizações**  
* **Eventos**  
* **Público-Alvo**

### **3\) Validação das Tags**

Após a criação inicial, as tags passam por um **processo de validação** para reforçar que cumprem as regras definidas para a sua categoria.

### **4\) Geração de Descrições para as Tags**

Cada tag validada recebe uma **descrição curta**, que fornece contexto adicional sobre a entidade. Esse passo tem como principal objetivo **melhorar os resultados da pesquisa semântica** que será realizada na etapa seguinte.

Se a tag for um acrônimo ou sigla, a descrição pode conter seu nome por extenso, caso seja conhecido. Caso a tag não tenha uma definição clara, ela é eliminada do conjunto final.

### **5\) Correspondência com Banco de Dados Vetorial**

Para evitar a criação de múltiplas variações da mesma entidade e garantir consistência ao longo do tempo, as tags geradas são comparadas com um banco de dados vetorial.

1. **Pesquisa Semântica:** A descrição das tags é utilizada para realizar uma busca por similaridade no banco vetorial (**top-3 resultados mais semelhantes**).  
2. **Verificação de Correspondência Direta:** Se uma das correspondências for idêntica à tag gerada, a versão já existente é utilizada.  
3. **Decisão via LLM:** Caso não haja correspondência exata, o modelo de linguagem decide se uma das correspondências pode substituir a tag original. As opções são:  
   * **0:** Nenhuma correspondência adequada → A tag original é mantida e adicionada ao banco de dados.  
   * **1, 2 ou 3:** Substituição pela 1ª, 2ª ou 3ª correspondência mais próxima encontrada no banco.  
4. **Remoção de Duplicados:** Se duas ou mais tags geradas forem “muito” semelhantes, é possível que a pesquisa semântica resulte na mesma tag. Quando isso ocorre, são removidas as duplicadas.   
5. **Atualização da Base de Dados:** Se uma tag for considerada "nova" (sem correspondências adequadas), é armazenada no banco vetorial para futuras buscas.

### **6\) Armazenamento e Envio dos Resultados**

Após o processamento, os dados são armazenados e enviados para garantir a sua integração com o **Sapo**.

#### **a) Envio ao SAPO via Message Broker**

A pedido do Sapo, e para fins de visibilidade, os dados processados são estruturados num **payload JSON** (anexo 1), que é enviado ao **Sapo** através do message broker.

#### **b) Armazenamento na Tabela de Tags**

Cada tag gerada (nova ou já existente) é armazenada em uma **tabela de tags**, estruturada para ter um relacionamento **many-to-one** com a tabela de artigos. Ou seja, a tabela de tags terá as seguintes informações:

* **ID da Tag**  
* **Nome da Tag**  
* **ID do Artigo ao qual foi associada**

Dessa forma, uma mesma tag pode estar associada a múltiplos artigos.

2. Persistência Tags

**1\) Critérios para Expiração de Tags**

Uma tag pode ser considerada irrelevante e candidata à remoção se:

1. For utilizada em menos de X artigos nos últimos Y meses (por exemplo, menos de 5 artigos num período de 12 meses).  
2. Não tiver sido associada a nenhum artigo novo durante um determinado período de tempo.  
3. Nunca tiver atingido um número mínimo de utilizações desde a sua criação.

Estes critérios permitem garantir que apenas tags que continuam a ser relevantes e recorrentes permaneçam no sistema.

**2\) Processo de Expiração**

A expiração de tags pouco utilizadas será um processo automatizado e periódico, garantindo que a remoção ocorra de forma eficiente e sem impacto na performance da base de dados. O processo é dividido nos seguintes passos:

**2.1) Monitorização da Utilização das Tags**

Para determinar a frequência de utilização das tags, é mantida uma tabela auxiliar que armazena estatísticas de utilização. Esta tabela regista o número total de artigos em que cada tag foi utilizada e a data da sua última associação a um artigo.

Esta tabela é atualizada periodicamente para refletir o número de artigos que utilizaram cada tag nos últimos Y meses. Dessa forma, é possível identificar rapidamente tags que deixaram de ser relevantes.

**2.2) Identificação de Tags Pouco Utilizadas**

Com base nas estatísticas de utilização, um processo automático analisa as tags e verifica se estas cumprem os critérios de expiração definidos. Tags que não atingiram o limiar mínimo de utilização são marcadas para remoção.

**3\) Agendamento do Processo**

Para garantir que o sistema se mantém atualizado sem necessidade de intervenção manual, o processo de expiração de tags é executado de forma programada em intervalos regulares. A frequência da execução pode ser ajustada consoante as necessidades da aplicação.

A monitorização da utilização das tags pode ser feita diariamente, enquanto a remoção de tags pouco utilizadas pode ser efetuada de forma mais espaçada, como mensalmente. Desta forma, evita-se um impacto desnecessário na performance da base de dados.

3. Categorias de Tags:

   * **Localização geográfica**  
     * País ou região: Referência ao local onde os acontecimentos descritos no artigo ocorreram ou a que se referem (e.g., Portugal, Europa, Nova Iorque).  
       * Granularidade máxima: País  
     * Cidades ou locais específicos: Quando relevante, menção de cidades, vilas ou localidades envolvidas.  
       * Granularidade mínima: Concelho

   * **Nomes de pessoas**  
     * Personagens importantes: Políticos, celebridades, especialistas, empresários, desportistas, artistas, outras personalidades com destaque na sociedade ou qualquer pessoa citada ou relevante para o conteúdo do artigo.  
     * Autores ou jornalistas: Identificação dos jornalistas ou autores mencionados no artigo.  
       * A tag deve ser equivalente aos autor do artigo, identificado através do atributo authors.name do objeto article, retornado pelo RabbitMQ-SAPO (payload antigo).

   * **Entidades ou organizações**  
     * Empresas: Marcas, empresas, corporações, institutos, associações, etc, mencionadas no artigo.  
     * Instituições governamentais ou não-governamentais: Ministérios, ONGs, organizações internacionais (e.g., ONU, União Europeia).  
       * Apresentação: Entidades/Organizações tendem a seguir o formato apresentado no texto. Foi criado um passo que procura enviesar o modelo para escolher acrónimos/siglas de organizações com \>= 3 palavras.  
   * **Eventos**  
     * Acontecimentos específicos: Eleições, conferências, lançamentos de produtos, eventos desportivos, eventos artísticos, crises económicas ou desastres naturais.  
       * Eventos que se repetem devem conter o ano (ex: legislativas 2024). O Ano é extraído do payload e passado no prompt.

---

### Classificação (Público Alvo)

1. Descrição  
   1. Este tópico busca identificar se o artigo aborda temas relevantes para grupos específicos de interesse, como jovens, estudantes, profissionais de saúde, consumidores de tecnologia, entre outros. A classificação automática nesta categoria visa ajudar na segmentação do conteúdo e audiência.

2. Problemática  
   1. A categorização automática com base no público-alvo pode ser desafiadora e suscetível a erros, gerando associações inadequadas entre público e conteúdo. Isso pode reforçar estereótipos e preconceitos, especialmente em tópicos sensíveis relacionados a minorias ou grupos historicamente marginalizados. Por exemplo, classificar automaticamente um conteúdo como direcionado a uma determinada etnia, gênero ou classe social pode resultar em discriminação, viés algorítmico e danos à reputação da app e da marca. Além disso, a subjetividade na definição de público-alvo torna difícil criar regras claras e seguras para classificação, comprometendo a precisão e a neutralidade do sistema.  
        
3. Recomendação Bliss  
   1. Dada a alta probabilidade de erros e os riscos éticos associados, recomenda-se **não implementar esta categoria** de classificação automática no sistema. O valor agregado é nulo em comparação aos riscos significativos de danos à imagem da app e do SAPO. Existem alternativas mais eficientes e seguras para a segmentação de público, como o uso de análises de comportamento, interações com o conteúdo e preferências explicitamente fornecidas pelos utilizadores, que permitem uma abordagem personalizada sem comprometer a imparcialidade ou a ética.

---

Anexo 1: Exemplo Proposta Payload Artigo

```json

{
  "header": {
    "enrichment_services": ["summary", "tags", "short_audio"]
  },
  "doc": {
    "id": "5c77ceaecafe1805930fd9bf",
    "partner_id": "partner_12345",
    "title": "Banks to Cap Public Guarantee on Youth Housing Credit",
    "clean_body": "Banks that adhere to the public guarantee on housing credit for young people will have a limit on the guaranteed amount they can lend...",
    "reading_time": 3,
    "word_count": 550,
    "partner_config": {
      "ai_automatic_summary_generation_enabled": true,
      "ai_audio_creation_enabled": true,
      "ai_automatic_translation_enabled": true,
      "ai_metadata_enrichment_enabled": false,
      "ai_tag_enrichment_enabled": true,
      "ai_video_creation_with_avatar_enabled": false
    }
  },
  "enrichments": {
    "tags": {
      "pt_PT": [
        { "tag_id": "t_pt_001", "name": "ONU" },
        { "tag_id": "t_pt_002", "name": "Bruno Vitor" }
      ],
      "en_US": [
        { "tag_id": "t_en_001", "name": "UN" },
        { "tag_id": "t_en_002", "name": "Bruno Vitor" }
      ],
      "fr_FR": [
        { "tag_id": "t_fr_001", "name": "ONU" },
        { "tag_id": "t_fr_002", "name": "Bruno Vitor" }
      ]
    },
    "original_content": {
      "pt_PT": "<div>Conteúdo original</div>",
      "en_US": "<div>Original content</div>",
      "fr_FR": "<div>Contenu original</div>"
    },
    "summary": {
      "pt_PT": {
        "audio": "https://azure_BLOB_STORAGE.blob.core.windows.net/audio/5c77ceaecafe1805930fd9bf/summary/pt.mp3",
        "parts": [
          {
            "text": "Os bancos que aderirem à garantia pública no crédito à habitação a jovens terão um limite ao montante garantido que poderão emprestar...",
            "audioOffset": 0,
            "duration": 10700
          },
          {
            "text": "Caberá ao Ministro das Finanças definir o montante máximo da garantia pública ao crédito à habitação.",
            "audioOffset": 10800,
            "duration": 5262
          },
          {
            "text": "O montante máximo da garantia pública ao crédito à habitação será definido por despacho do Ministro das Finanças.",
            "audioOffset": 16062,
            "duration": 5262
          }
        ]
      },
      "en_US": {
        "audio": "https://azure_BLOB_STORAGE.blob.core.windows.net/audio/5c77ceaecafe1805930fd9bf/summary/en.mp3",
        "parts": [
          {
            "text": "Banks that adhere to the public guarantee on housing credit for young people will have a limit on the guaranteed amount they can lend...",
            "audioOffset": 0,
            "duration": 10700
          },
          {
            "text": "It will be up to the Minister of Finance to define the maximum amount of the public guarantee on housing credit.",
            "audioOffset": 10800,
            "duration": 5262
          },
          {
            "text": "The maximum amount of the public guarantee on housing credit will be defined by an order from the Minister of Finance.",
            "audioOffset": 16062,
            "duration": 5262
          }
        ]
      },
      "fr_FR": {
        "audio": "https://azure_BLOB_STORAGE.blob.core.windows.net/audio/5c77ceaecafe1805930fd9bf/summary/fr.mp3",
        "parts": [
          {
            "text": "Les banques qui adhèrent à la garantie publique sur le crédit immobilier pour les jeunes auront une limite sur le montant garanti qu'elles peuvent prêter...",
            "audioOffset": 0,
            "duration": 10700
          },
          {
            "text": "Il appartiendra au ministre des Finances de définir le montant maximum de la garantie publique sur le crédit immobilier.",
            "audioOffset": 10800,
            "duration": 5262
          },
          {
            "text": "Le montant maximum de la garantie publique sur le crédit immobilier sera défini par un arrêté du ministre des Finances.",
            "audioOffset": 16062,
            "duration": 5262
          }
        ]
      }
    }
  }
}
```

---

