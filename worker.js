/* Bloqueio na VSL (6/10/2026, pedido do Pietro): quem está na lista de bloqueio do app não vê a página de vendas.
   A VSL é um Worker (Workers Builds) com os arquivos estáticos; este script só roda na página (run_worker_first).
   Mesma regra do site do app (pedrapro/worker.js): bloqueia pela marca no navegador (cookie mpb=1, gravada pelo app
   no domínio marmoristapro.online quando a conta é bloqueada) e pelo IP (ip_livre no banco do app).
   Se o banco não responder em 0,8 s, deixa passar: a VSL nunca cai por causa disso. */
const SUPA = 'https://srtwlmrhtivijkwjxqvn.supabase.co';
const KEY = 'sb_publishable_o4VnbRkSpR6tPydMncy4mQ_J84Qlmcy'; // chave pública do app
const cache = new Map();

async function ipLivre(ip) {
  const c = cache.get(ip);
  if (c && c.t > Date.now()) return c.v;
  let v = true;
  try {
    const r = await fetch(SUPA + '/rest/v1/rpc/ip_livre', {
      method: 'POST',
      headers: { apikey: KEY, 'Content-Type': 'application/json' },
      body: JSON.stringify({ p_ip: ip }),
      signal: AbortSignal.timeout(800),
    });
    if (r.ok) v = (await r.json()) !== false;
  } catch (_) { /* banco fora do ar: deixa passar */ }
  if (cache.size > 5000) cache.clear();
  cache.set(ip, { v, t: Date.now() + 5 * 60 * 1000 });
  return v;
}

const PAGINA = '<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Acesso indisponível</title>'
  + '<body style="margin:0;min-height:100vh;display:grid;place-items:center;padding:24px;box-sizing:border-box;background:#0E1113;color:#ddd;text-align:center;font:16px system-ui,sans-serif">'
  + '<div><h1 style="font-size:20px;margin:0 0 8px">Acesso indisponível</h1><p style="margin:0;opacity:.7">Não foi possível abrir esta página.</p></div></body></html>';

export default {
  async fetch(req, env) {
    try {
      if (req.method === 'GET' && (req.headers.get('accept') || '').includes('text/html')) {
        const ip = req.headers.get('cf-connecting-ip') || '';
        if (/(?:^|;\s*)mpb=1(?:;|$)/.test(req.headers.get('cookie') || '') || (ip && !(await ipLivre(ip)))) {
          return new Response(PAGINA, { status: 403, headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'no-store' } });
        }
      }
    } catch (_) { /* qualquer erro: deixa passar */ }
    return env.ASSETS.fetch(req);
  },
};
