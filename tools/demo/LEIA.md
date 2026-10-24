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
