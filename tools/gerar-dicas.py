# Gera as paginas de /dicas a partir de tools/dicas_paginas.py (pagina nova = novo pg(...) no fim de dicas_paginas.py).
# Atualiza o indice e o sitemap. Uso: python tools/gerar-dicas.py
import json, re, html, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from dicas_paginas import P

R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'public')
B = 'https://aplicativo.marmoristapro.online'
DATA0 = '2026-11-23'

ANT = {
 'calculadora-orcamento-bancada-granito': ('Calculadora de orçamento de bancada de granito', 'Pedra em m², saia, rodabanca, recortes e perda de chapa, direto no celular.'),
 'como-fazer-orcamento-de-bancada-de-granito': ('Como fazer orçamento de bancada de granito', 'O passo a passo das 6 partes que não podem faltar, com exemplo de conta.'),
 'como-calcular-metro-quadrado-de-granito': ('Como calcular o metro quadrado de granito', 'Bancada reta, em L e em U, sem contar o canto duas vezes.'),
 'plano-de-corte-de-chapa-de-granito': ('Plano de corte de chapa de granito', 'Como encaixar as peças na chapa, cuidar do veio e guardar os retalhos.'),
}
NOME = dict((k, v[0]) for k, v in ANT.items())
for p in P:
    NOME[p['slug']] = p['h1'].split(':')[0]

e = lambda s: html.escape(s, quote=True)

for p in P:
    DATA = p['data']; DBR = '/'.join(reversed(DATA.split('-')))
    s = p['slug']; url = f'{B}/dicas/{s}'
    utm = f'/sistema?utm_source=google&amp;utm_medium=organico&amp;utm_campaign=dicas-{s}'
    titulo = p['titulo'] + ' | Marmorista Pro'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Marmorista Pro", "item": f"{B}/sistema"},
            {"@type": "ListItem", "position": 2, "name": "Dicas para marmoraria", "item": f"{B}/dicas/"},
            {"@type": "ListItem", "position": 3, "name": p['h1'], "item": url}]},
        {"@type": "Article", "headline": p['h1'], "description": p['desc'], "inLanguage": "pt-BR",
         "datePublished": DATA, "dateModified": DATA, "mainEntityOfPage": url,
         "image": f"{B}/img/compartilhar.jpg",
         "author": {"@type": "Organization", "name": "Marmorista Pro", "url": f"{B}/sistema"},
         "publisher": {"@type": "Organization", "name": "Marmorista Pro", "logo": {"@type": "ImageObject", "url": f"{B}/img/apple-touch-icon.png"}}}]}
    rel = ''.join(f'<a href="/dicas/{r}"><b>{e(NOME[r])}</b></a>' for r in p['rel'])
    out = f'''<!doctype html>
<html lang="pt-BR">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(titulo)}</title>
<meta name="description" content="{e(p['desc'])}">
<link rel="canonical" href="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0B0D0F">
<meta property="og:type" content="article">
<meta property="og:title" content="{e(titulo)}">
<meta property="og:description" content="{e(p['desc'])}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="Marmorista Pro">
<meta property="og:locale" content="pt_BR">
<meta property="og:image" content="{B}/img/compartilhar.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" sizes="48x48" href="/img/favicon-48.png">
<link rel="preload" as="font" type="font/woff2" href="/fonts/pjs-latin-v12.woff2" crossorigin>
<link rel="stylesheet" href="/dicas/estilo.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False, separators=(',', ':'))}</script>
</head>
<body>
<header class="top"><div class="w">
<a class="logo" href="/sistema"><img src="/img/apple-touch-icon.png" alt="" width="32" height="32">Marmorista <b>Pro</b></a>
<a class="btn sm" href="{utm}">Conhecer o app</a>
</div></header>
<main class="w">
<p class="migalha"><a href="/sistema">Marmorista Pro</a> › <a href="/dicas/">Dicas</a></p>
<h1>{e(p['h1'])}</h1>
<p class="data">Atualizado em {DBR} · {p['min']} min de leitura</p>
<p class="lead">{e(p['lead'])}</p>
{p['corpo'].strip()}
<h2>Leia também</h2>
<div class="lista">{rel}</div>
<div class="cta"><p>No Marmorista Pro você desenha a bancada em 3D, e o app calcula pedra, saia, recortes e meia-esquadria e já monta o orçamento com a sua logo, o plano de corte e a ordem de produção.</p><a class="btn" href="{utm}">Ver o Marmorista Pro funcionando</a></div>
</main>
<footer><div class="w">
<p><a href="/dicas/">Todas as dicas</a><a href="/sistema">O app Marmorista Pro</a><a href="https://marmoristapro.online">Entrar</a></p>
<p>© 2026 Marmorista Pro. Os valores desta página são exemplos; use sempre os preços da sua região e da sua marmoraria.</p>
</div></footer>

</body>
</html>
'''
    open(os.path.join(R, 'dicas', s + '.html'), 'w', encoding='utf-8', newline='\n').write(out)

# índice
itens = [(k, *v) for k, v in ANT.items()] + [(p['slug'], p['h1'].split(':')[0] if False else p['h1'], p['curto']) for p in P]
ix_path = os.path.join(R, 'dicas', 'index.html')
ix = open(ix_path, encoding='utf-8').read()
lista = '<div class="lista">\n' + '\n'.join(f'<a href="/dicas/{k}"><b>{e(t)}</b>{e(d)}</a>' for k, t, d in itens) + '\n</div>'
ix = re.sub(r'<div class="lista">.*?</div>', lambda m: lista, ix, count=1, flags=re.S)
ix = ix.replace('Guias e calculadora grátis para marmoraria: como fazer orçamento de bancada de granito, calcular o m² da pedra e fazer o plano de corte da chapa.',
  'Guias e calculadora grátis para marmoraria: orçamento de bancada, m² da pedra, plano de corte, meia-esquadria, cuba esculpida, saia, rodabanca, medição e instalação.')
ix = ix.replace('Dicas para Marmoraria: Orçamento, m² e Plano de Corte | Marmorista Pro', 'Dicas para Marmoraria: Orçamento, Medidas e Acabamentos | Marmorista Pro')
ix = ix.replace('Guias práticos e ferramentas grátis para o dia a dia da marmoraria: orçamento, medida, chapa e plano de corte.',
  'Guias práticos e ferramentas grátis para o dia a dia da marmoraria: orçamento, medida, chapa, plano de corte, acabamentos e instalação.')
open(ix_path, 'w', encoding='utf-8', newline='\n').write(ix)

# sitemap
sm_path = os.path.join(R, 'sitemap.xml')
sm = open(sm_path, encoding='utf-8').read()
novos = ''.join(f'  <url><loc>{B}/dicas/{p["slug"]}</loc><lastmod>{DATA}</lastmod></url>\n' for p in P if f'/dicas/{p["slug"]}<' not in sm)
sm = sm.replace('</urlset>', novos + '</urlset>')
open(sm_path, 'w', encoding='utf-8', newline='\n').write(sm)
print(len(P), 'paginas')
