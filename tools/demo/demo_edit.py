import json
import sys
P=sys.argv[1]
assert 'app-demo' in P
import os
D=os.path.dirname(os.path.abspath(__file__))+'/'
s=open(P,'rb').read().decode('utf-8')
V=json.load(open(D+'V.json',encoding='utf-8'))
IT=json.load(open(D+'itens.json',encoding='utf-8'))
IT[1]['nome']='Cozinha em L'
# ordem: cozinha em L, pia com vão, lavatório
IT=[IT[1],IT[2],IT[0]];V=[V[1],V[2],V[0]]
# só 3 pedras (pedido do Pietro, 24/10/2026: "bem levinho"); o lavatório começa no Quartzo Branco
PEDRAS=['saogabriel','cafe','quartzo']
V=[{k:v[k] for k in PEDRAS} for v in V];IT[2]['st']='quartzo'
assert all(it['st'] in PEDRAS for it in IT)
js=lambda x:json.dumps(x,ensure_ascii=False,separators=(',',':'))
def rep(a,b):
    global s
    assert s.count(a)==1,(s.count(a),a[:80])
    s=s.replace(a,b)
# 1) link da demonstração
a="const PUB_T=(function(){"
i=s.index(a);j=s.index('\n',i)
line=s[i:j]
assert line.count('let PUB=null;')==1
rep(line,line.replace('let PUB=null;',"let PUB=null;const DEMO=/^demo/.test(PUB_T||'');/* orçamento de demonstração da página de vendas (LAZY:demo) */"))
# 2) função proposta: na demonstração responde a parte sob demanda (nada vai ao banco)
rep("async function propFn(b){const d=","async function propFn(b){if(DEMO)return lazy('demo').then(()=>lzSync('demo').fn(b));const d=")
# 3) tela do cliente: escolha de pedra por projeto
rep('<footer class="cv-foot">Proposta feita com Marmorista Pro</footer>`;}','<footer class="cv-foot">Proposta feita com Marmorista Pro</footer>`;if(DEMO&&LZM.demo)LZM.demo.ui();}')
# 4) só as fotos das 3 pedras são baixadas antes (o app baixa as 44, ~8 MB)
rep("STONE_ORDER.forEach((id,i)=>setTimeout(()=>{const im=photoImg(id);","PEDRAS_DEMO.forEach((id,i)=>setTimeout(()=>{const im=photoImg(id);")
rep("function photoImg(id){const u=STONE_PHOTO[id];if(!u)return null;","function photoImg(id){const u=STONE_PHOTO[id];if(!u||!"+js(PEDRAS)+".includes(id))return null;")
rep("function warmPhotos(){","const PEDRAS_DEMO="+js(PEDRAS)+";function warmPhotos(){")
# 5) sem service worker na cópia
rep("navigator.serviceWorker.register('/sw.js',{updateViaCache:'none'})","Promise.reject(0)/* cópia da demonstração: sem service worker */")
# 6) parte sob demanda
lz=open(D+'demo_lazy.js',encoding='utf-8').read()
lz=lz.replace('__V__',js(V)).replace('__IT__',js(IT)).replace('\r\n','\n').replace('\n','\r\n')
rep("/* ---- enviar ---- */",lz+"/* ---- enviar ---- */")
open(P,'wb').write(s.encode('utf-8'))
print('ok',len(lz))
