# Plano de 7 dias para aparecer no Google (24 a 30/11/2026)

Meta: usar toda a cota diária de "Solicitar indexação" do Search Console (cerca de 10 por dia), publicar páginas novas
úteis todo dia e aparecer também no Bing (que alimenta o ChatGPT, o Copilot e o DuckDuckGo).

Regras de cada página: modelo de `public/dicas/como-calcular-metro-quadrado-de-granito.html` (gerador em
`tools/gerar-dicas.py`), passo a passo de verdade, exemplos de marmoraria, preço só como exemplo com aviso,
nenhum número de mercado inventado como fato, "Leia também" ligando às outras, índice `public/dicas/index.html` e
`public/sitemap.xml` atualizados, 390 px sem nada sobrando para os lados. Nada de página rala ou repetida.

Marque `[x]` no que ficar feito e anote no "Diário" no fim.

## Dia 1 — 24/11 (ter)
- [ ] (24/11: cota já esgotada no 1º pedido; passa para 25/11) Pedir indexação das 9 que ficaram de 23/11: recorte-de-cooktop-no-granito, como-medir-bancada-de-granito,
      tamanho-de-chapa-de-granito, como-instalar-bancada-de-granito, nicho-de-granito-para-banheiro,
      soleira-e-peitoril-de-granito, como-colar-granito, granito-ou-quartzo, como-abrir-uma-marmoraria; e `/dicas/`
- [x] Ligar o **IndexNow** (Bing, Yandex e outros): arquivo da chave em `public/<chave>.txt` e envio de todos os
      endereços do sitemap para `https://api.indexnow.org/indexnow`. A partir daqui, toda página nova também vai pelo IndexNow.
      Chave: `a6c8a437bade984fe167d4d1172b890d` (arquivo `public/a6c8a437bade984fe167d4d1172b890d.txt`).
- [x] Páginas novas (indexar no Dia 2): `escada-de-granito-medidas` (piso, espelho, bocel, conta de degraus),
      `tipos-de-acabamento-de-borda-de-granito` (reto, boleado, meia-cana, chanfrado, bisotê, como cobrar)

## Dia 2 — 25/11 (qua)
- [ ] Indexar as páginas do Dia 1
- [ ] Páginas: `como-polir-granito`, `bancada-de-churrasqueira-em-granito`, `cuba-de-embutir-sobrepor-ou-apoio`
- [ ] Completar a cota com páginas antigas que ainda aparecem "O URL não está no Google"

## Dia 3 — 26/11 (qui)
- [ ] Indexar as do Dia 2 (+ completar a cota)
- [ ] Páginas: `como-cortar-granito-sem-lascar`, `como-furar-granito`, `ilha-de-cozinha-em-granito-medidas`

## Dia 4 — 27/11 (sex)
- [ ] Indexar as do Dia 3 (+ completar a cota)
- [ ] Páginas: `como-tirar-mancha-de-granito` (para o marmorista orientar o cliente), `impermeabilizante-para-granito`,
      `bancada-de-banheiro-medidas`

## Dia 5 — 28/11 (sáb)
- [ ] Indexar as do Dia 4 (+ completar a cota)
- [ ] Páginas: `quanto-cobrar-instalacao-de-bancada-de-granito`, `mao-francesa-para-bancada-de-granito`,
      `como-transportar-chapa-de-granito`

## Dia 6 — 29/11 (dom)
- [ ] Indexar as do Dia 5 (+ completar a cota)
- [ ] Páginas: `retalho-de-granito-o-que-fazer`, `como-conseguir-clientes-para-marmoraria`, `modelo-de-orcamento-marmoraria`

## Dia 7 — 30/11 (seg)
- [ ] Indexar as do Dia 6 (+ completar a cota)
- [ ] Relatório: no Search Console, quantas páginas de `/dicas/` já estão no Google, impressões e cliques da semana e
      quais buscas apareceram (Desempenho > Consultas). Nova rodada rápida de pesquisa (autocompletar + "As pessoas também
      perguntam") para o plano da semana seguinte, anotada em `docs/pesquisa-buscas.md`.

## Fora do Google (o Pietro precisa fazer ou autorizar)
- Perfil da empresa no Google (Google Meu Negócio) do Marmorista Pro, se ainda não existe
- Bing Webmaster Tools: entrar com a conta Google e importar a propriedade do Search Console (1 clique)
- YouTube/Instagram: cada página de dica pode virar um vídeo curto com o mesmo título

## Diário
- 23/11: 14 páginas publicadas (f4a8d25), sitemap reenviado (21 páginas), indexação pedida de 5 (cuba esculpida,
  meia-esquadria, espessura, rodabanca, saia). Cota acabou na 6ª.
- 24/11: 2 páginas publicadas (7649bc3): escada-de-granito-medidas e tipos-de-acabamento-de-borda-de-granito (pesquisa: autocompletar + "As pessoas também perguntam"; 375 px sem sobrar). IndexNow ligado: 23 endereços enviados, resposta 202. Sitemap reenviado (23 páginas). Indexação: 0 — "A cota foi excedida" já no 1º pedido (recorte-de-cooktop), às ~9h20. Ficam para 25/11: as 9 de 23/11 + /dicas/ + as 2 de hoje (12 no total, mais que a cota; prioridade nesta ordem). Relatório de Páginas ainda "em processamento".
