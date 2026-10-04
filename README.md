# Página de vendas · Marmorista Pro

Página única (`index.html`), sem build, sem fontes nem bibliotecas de fora. Nota 100 no Lighthouse (celular) em desempenho, acessibilidade, boas práticas e SEO.

## Publicar na Cloudflare (Workers & Pages → Criar → Pages → Conectar ao Git)
- Repositório: `marmoristapro-vendas`
- Framework: nenhum
- Comando de build: (vazio)
- Pasta de saída: `/`

## Colocar a VSL (VTurb)
1. No `index.html`, apague o bloco `<div class="vsl-ph">…</div>` (dentro de `<div class="vsl" id="vsl">`) e cole no lugar o código do player do VTurb.
2. No `<head>`, tire o comentário dos 3 `preconnect` do VTurb (carrega o vídeo mais rápido).
3. No fim do arquivo, troque `var PITCH = 0;` pelo segundo do pitch (ex.: 8 min 30 s = `510`).

Tudo dentro de `<div class="esconder" id="oferta">` (e o botão fixo de baixo) só aparece nesse segundo.
Quem já viu a oferta e volta à página vê o botão direto. Para conferir sem esperar o vídeo: abra a página com `?ver=1` no fim do endereço.

Os botões levam para `https://marmoristapro.online/` (tela de criar conta) e repassam as UTMs do anúncio.
