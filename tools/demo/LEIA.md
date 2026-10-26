# Orçamento de demonstração (public/demo/)

`public/demo/` + `public/assets/` + `public/icons/` são uma **cópia** do app (build de 24/10/2026), usada só no
iframe da `sistema.html`. O app de verdade (marmoristapro.online) não foi alterado.

A cópia tem duas mudanças: abre o orçamento de demonstração (`?orc=demo...`, sem banco: abrir e aprovar
respondem daqui) e não registra service worker.

Refazer (quando o app mudar muito):
1. `git archive HEAD` do repositório `pedrapro` numa pasta temporária `app-demo` (junction para o `node_modules`).
2. `python -I demo_edit.py <pasta>/app-demo/index.html` (só aceita caminho com `app-demo`; nunca rode no pedrapro).
   (o script também tira o service worker e faz a cópia baixar só as fotos das 3 pedras)
3. `node tools/build.mjs` na cópia; copie `dist/index.html` para `public/demo/` e `dist/assets` e `dist/icons` para `public/`.

`V.json`: preço de cada projeto em cada pedra (tabela de preços da conta do Pietro, 24/10/2026, sem o desconto
manual do #106). `itens.json`: os projetos dos orçamentos #106, #113 e #112.

Teste de toque (celular simulado com toque de verdade e computador): `node tools/demo/teste-demo.cjs [endereço]`
(padrão: http://localhost:8770/sistema.html; para o site no ar use https://aplicativo.marmoristapro.online/sistema).
4. Depois de copiar: `python tools/demo/preload.py` (pré-cargas no <head> da demonstração) e, se o visual do orçamento mudou, refazer a foto `public/img/demo-poster.webp` (aparece no lugar do 3D até a pessoa mexer na página).

26/10/2026 (pedido do Pietro): a demonstração abre no **Lavatório com cuba esculpida** (Quartzo Branco), com o **fundo escuro**
e as **Medidas ligadas**; no lavatório aparecem também frontão, saia e bracinho (nos outros projetos, só comprimento e largura).
A tela do cliente virou parte sob demanda no app (`LAZY:cv`), então o `demo_edit.py` liga a demonstração pelo K (`demoUi`).
Foto do lugar do 3D refeita com `poster2.cjs` (print da moldura no computador, 560 e 400 px).
26/10/2026: o fundo segue a pedra (clara = fundo escuro, escura = fundo claro, pela cor `base` da pedra), ao abrir e ao trocar
de projeto ou de pedra; o botão Fundo continua trocando na mão. A foto do lugar do 3D tem também versão AVIF (`poster2.cjs`).
