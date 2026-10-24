// Testa o orçamento de demonstração dentro da página de vendas, num celular simulado com toque de verdade (CDP).
const { chromium, devices } = require('C:/Users/pietr/Downloads/pedrapro/node_modules/playwright');
const URL = process.argv[2] || 'http://localhost:8770/sistema.html';
const OUT = require('os').tmpdir() + '/';
(async () => {
  const b = await chromium.launch({ args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader'] });
  const r = {};
  for (const modo of ['celular', 'computador']) {
    const ctx = await b.newContext(modo === 'celular' ? { ...devices['Pixel 5'] } : { viewport: { width: 1280, height: 900 } });
    const p = await ctx.newPage(); let navs = 0; p.on('framenavigated', fx => { if (fx.url().includes('/demo/')) navs++; });
    await p.goto(URL, { waitUntil: 'load' });
    const fr = async () => { for (let i = 0; i < 60; i++) { const f = p.frames().find(x => /\/demo\//.test(x.url())); if (f && await f.$('#dm-st').catch(() => null)) return f; await p.waitForTimeout(500); } throw new Error('demo não abriu'); };
    const f = await fr(); await p.waitForTimeout(2500); r.navs = r.navs || {}; r.navs[modo] = navs;
    await p.evaluate(() => { document.querySelectorAll('.rv').forEach(e => { e.style.transition = 'none'; e.classList.add('on'); });  });
    const ph = await p.$('#demo .ph');
    await p.evaluate(() => scrollTo(0, document.querySelector('#demo .ph').getBoundingClientRect().top + scrollY - 40));
    await p.waitForTimeout(400);
    const R = { };
    R.altura = await p.evaluate(() => document.querySelector('#demo .ph').style.height);
    R.rolagemInterna = await f.evaluate(() => { const el = document.getElementById('cv-scroll'); return el.scrollHeight - el.clientHeight; });
    R.escondidos = await f.evaluate(() => ({ marmoraria: !!document.querySelector('.cv-brand') && getComputedStyle(document.querySelector('.cv-brand')).display !== 'none', total: !!document.querySelector('.cv-total') && getComputedStyle(document.querySelector('.cv-total')).display !== 'none', aprovar: !!document.querySelector('#cv-approve') && getComputedStyle(document.querySelector('#cv-approve')).display !== 'none' }));
    await p.screenshot({ path: OUT + 'demo-' + modo + '.png' });
    const box3d = async () => { const ifr = await (await f.frameElement()).boundingBox(); const bb = await f.evaluate(() => { const r = document.getElementById('cv-3d').getBoundingClientRect(); return { x: r.x, y: r.y, w: r.width, h: r.height }; }); return { x: ifr.x + bb.x + bb.w / 2, y: ifr.y + bb.y + bb.h / 2 }; };
    if (modo === 'celular') {
      const cdp = await ctx.newCDPSession(p);
      const arrasta = async (x, y, dy) => { await cdp.send('Input.dispatchTouchEvent', { type: 'touchStart', touchPoints: [{ x, y }] }); for (let i = 1; i <= 10; i++) { await cdp.send('Input.dispatchTouchEvent', { type: 'touchMove', touchPoints: [{ x, y: y - dy * i / 10 }] }); await p.waitForTimeout(16); } await cdp.send('Input.dispatchTouchEvent', { type: 'touchEnd', touchPoints: [] }); await p.waitForTimeout(900); };
      let c = await box3d(); let y0 = await p.evaluate(() => scrollY);
      await arrasta(c.x, c.y, 150); R.arrastarNo3dDesligado = (await p.evaluate(() => scrollY)) - y0 + ' px de página';
      await p.evaluate(() => scrollTo(0, document.querySelector('#demo .ph').getBoundingClientRect().top + scrollY - 40)); await p.waitForTimeout(400);
      c = await box3d(); await p.touchscreen.tap(c.x, c.y); await p.waitForTimeout(500);
      R.depoisDeTocar = await f.evaluate(() => ({ ligado: document.getElementById('cv-3d').classList.contains('dm-on'), pronto: !document.querySelector('.dm-ok').hidden }));
      y0 = await p.evaluate(() => scrollY); c = await box3d();
      await arrasta(c.x - 60, c.y, 0); await arrasta(c.x, c.y, 120); R.arrastarNo3dLigado = (await p.evaluate(() => scrollY)) - y0 + ' px de página (tem que ser 0)';
      await p.screenshot({ path: OUT + 'demo-celular-ligado.png' });
      const ok = await f.evaluate(() => { const r = document.querySelector('.dm-ok').getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + r.height / 2 }; }); const ifr = await (await f.frameElement()).boundingBox();
      await p.touchscreen.tap(ifr.x + ok.x, ifr.y + ok.y); await p.waitForTimeout(400); R.depoisDePronto = await f.evaluate(() => document.getElementById('cv-3d').classList.contains('dm-on') ? 'ainda ligado' : 'desligado');
      const pd = await f.evaluate(() => { const r = document.querySelector('[data-dmst="quartzo"]').getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + r.height / 2 }; });
      await p.touchscreen.tap(ifr.x + pd.x, ifr.y + pd.y); await p.waitForTimeout(500); R.tocarPedra = await f.evaluate(() => document.querySelector('[data-dmst="quartzo"]').getAttribute('aria-pressed'));
      y0 = await p.evaluate(() => scrollY); await arrasta(ifr.x + pd.x, ifr.y + pd.y, 140); R.arrastarNasPedras = (await p.evaluate(() => scrollY)) - y0 + ' px de página';
      R.pedraNaoMudouAoArrastar = await f.evaluate(() => document.querySelector('[data-dmst="quartzo"]').getAttribute('aria-pressed'));
      const tb = await f.evaluate(() => { const r = document.querySelector('[data-cvi="2"]').getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + r.height / 2 }; });
      await p.evaluate(() => scrollTo(0, document.querySelector('#demo .ph').getBoundingClientRect().top + scrollY - 40)); await p.waitForTimeout(300);
      const ifr2 = await (await f.frameElement()).boundingBox(); await p.touchscreen.tap(ifr2.x + tb.x, ifr2.y + tb.y); await p.waitForTimeout(1500);
      R.trocarProjeto = await f.evaluate(() => document.querySelector('[data-cvi="2"]').getAttribute('aria-selected'));
      await p.waitForTimeout(600); R.alturaDepoisDeTrocar = await p.evaluate(() => document.querySelector('#demo .ph').style.height);
    } else {
      const c = await box3d(); const y0 = await p.evaluate(() => scrollY);
      await p.mouse.move(c.x, c.y); await p.mouse.wheel(0, 300); await p.waitForTimeout(500); R.rodaNo3d = (await p.evaluate(() => scrollY)) - y0 + ' px de página';
    }
    R.erros = []; r[modo] = R; await ctx.close();
  }
  console.log(JSON.stringify(r, null, 1)); await b.close();
})().catch(e => { console.error('FALHOU', e); process.exit(1); });
