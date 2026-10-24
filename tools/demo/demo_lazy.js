/* ORÇAMENTO DE DEMONSTRAÇÃO (24/10/2026, pedido do Pietro): a página de vendas (aplicativo.marmoristapro.online/sistema.html) mostra,
   num iframe, a página que o cliente recebe pelo link: marmoristapro.online/?orc=demo... (DEMO). São 3 projetos (os orçamentos #112,
   #113 e #106 da conta do Pietro) e o visitante troca a pedra de cada projeto entre 3 pedras (São Gabriel, Café Imperial e Quartzo Branco; poucas para a página ficar leve). Nada vai ao banco: propFn
   responde daqui (abrir e aprovar). Os preços (V, um por projeto e pedra) saíram da tabela de preços da conta do Pietro em 24/10/2026,
   com orcTotals (sem o desconto manual do #106); a cópia não leva custo, margem nem tabela. Mudar projetos ou preços: gere V de novo. */
LZK.demo=()=>({$,esc,brl,STONES,get cv(){return cv},get PUB(){return PUB},pedra:id=>{curStone=id;if(S.ready){applyStone();wake3D();}},renderClient:()=>renderClient(),clientBuild:f=>clientBuild(f)});
/*LAZY:demo*/
(window.__LZ=window.__LZ||{}).demo=function(K){const{$,esc,brl,STONES}=K;
const V=__V__,IT=__IT__,off={on:0},tot=o=>o.itens.reduce((t,it,i)=>t+(V[i][it.st]||0),0),avisa=m=>{try{if(parent!==window)parent.postMessage({mpDemo:m},'*');}catch(e){}};
function fn(b){if(b.action==='aprovar'){avisa('aprovou');return{ok:true,j:{ok:true,situacao:{status:'aprovado',aprovOp:0,aprovEm:Date.now()}}};}
 const o={id:'demo',num:214,cliente:{nome:'Maria Oliveira',end:'Cozinha, área gourmet e lavabo'},opcoes:[null],itens:JSON.parse(JSON.stringify(IT)),extras:{andar:off,frete:off,molde:off,visita:off,retirada:off},cuba:{inc:0},instalacao:null,instV:0,mats:[],
  prazo:{tipo:'combinar',ini:'',fim:''},validade:10,cond:'',status:'visto',aprovOp:null,aprovEm:null,criado:Date.now(),showPlan:0,cgOff:['sap','n2','esp','prat','alt','itens','rod']};
 avisa('abriu');return{ok:true,j:{proposta:{o,vit:{nome:'Sua Marmoraria',tel:'(00) 00000-0000',cidade:''},T:[{venda:tot(o)}],st:IT.map(x=>x.st),nm:{},plan:null}}};}
/* 25/10/2026 (pedido do Pietro): o orçamento fica parado, sem rolagem própria. Só aparecem as abas dos projetos, o 3D, Medidas /
   Separar peças / Fundo e as 3 pedras (sem marmoraria, cliente, total nem aprovar). A altura vai para a página (mpDemo 'h'), que
   ajusta a moldura. No celular o 3D só gira depois de tocar em "Toque aqui para girar o projeto" (botão "Pronto" volta a rolar);
   fora disso, arrastar em qualquer lugar rola a página (o próprio código empurra a página, com embalo). A roda do mouse rola a página. */
const DENTRO=parent!==window,TOQUE=matchMedia('(pointer:coarse)').matches||'ontouchstart' in window;let ativo=false,P=null;
try{if(DENTRO&&parent.document)P=parent;}catch(e){}
(function css(){const st=document.createElement('style');st.textContent=
 '#cv-body>*:not(.cv-tabs):not(.cv-3d):not(.cv-tools):not(.cg-menu):not(.dm-keep){display:none!important}#cv-scroll{overflow:hidden!important}'
 +'.cv-tabs{display:grid!important;grid-template-columns:repeat(3,1fr);overflow:visible!important}.cv-tabs button{height:auto!important;min-height:40px;padding:6px 6px!important;white-space:normal;line-height:1.2;font-size:13px!important;border-radius:12px!important}'
 +'#dm-st{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;overflow:visible}#dm-st .cv-stone{width:auto;font-size:13px}'
 +'.dm-go{position:absolute;inset:0;z-index:3;display:flex;align-items:flex-end;justify-content:center;padding:0 12px 16px;border:0;background:linear-gradient(transparent 45%,rgba(0,0,0,.55));color:inherit;font:inherit;cursor:pointer}'
 +'.dm-go span{display:inline-flex;align-items:center;gap:8px;padding:12px 18px;border-radius:999px;background:#F5B800;color:#1A1400;font-weight:800;font-size:16px;box-shadow:0 8px 24px rgba(0,0,0,.45)}'
 +'.dm-ok{position:absolute;top:10px;right:10px;z-index:3;padding:10px 16px;border-radius:999px;border:0;background:#F5B800;color:#1A1400;font:inherit;font-weight:800;font-size:15px;box-shadow:0 6px 18px rgba(0,0,0,.45);cursor:pointer}'
 +'.dm-dica{position:absolute;left:10px;right:10px;bottom:10px;z-index:3;text-align:center;font-size:13px;font-weight:600;color:#fff;background:rgba(0,0,0,.6);padding:7px 10px;border-radius:10px;pointer-events:none}'
 +'.cv-3d .cv-hint{display:none!important}.dm-tag{position:absolute;top:10px;left:10px;z-index:2;background:rgba(22,27,30,.72);color:#fff;font-size:12px;padding:5px 10px;border-radius:14px;pointer-events:none}'
 +(DENTRO&&TOQUE?'html,body{touch-action:none!important}':'');document.head.appendChild(st);})();
function altura(){if(!DENTRO)return;const el=document.getElementById('cv-scroll');if(!el)return;avisa2(Math.ceil(el.getBoundingClientRect().top+el.scrollHeight));}
const avisa2=h=>{try{parent.postMessage({mpDemo:'h',h},'*');}catch(e){}};
let RO=null;
function modo(on){ativo=on;const c=$('#cv-3d');if(!c)return;c.classList.toggle('dm-on',on);const g=c.querySelector('.dm-go'),k=c.querySelector('.dm-ok'),d=c.querySelector('.dm-dica');
 if(g)g.hidden=on;if(k)k.hidden=!on;if(d)d.hidden=!on;}
function ui(){const c=K.cv,o=c&&c.o,it=o&&o.itens[c.it],b=$('#cv-body');if(!it||!b)return;const at=b.querySelector('.cg-menu')||b.querySelector('.cv-tools');
 if(at)at.insertAdjacentHTML('afterend',`<h4 class="cv-h dm-keep">Escolha a pedra${o.itens.length>1?' deste projeto':''}</h4><div class="cv-stones dm-keep" id="dm-st">${STONES.filter(s=>V[c.it][s.id]!=null).map(s=>`<button class="cv-stone" data-dmst="${s.id}" aria-pressed="${s.id===it.st}"><span class="sw" style="background-image:url(${s.sw})"></span><span>${esc(s.nome)}</span></button>`).join('')}</div>`);
 const v3=$('#cv-3d');if(v3){if(!TOQUE)v3.insertAdjacentHTML('beforeend','<span class="dm-tag">Clique e arraste para girar</span>');
  if(TOQUE)v3.insertAdjacentHTML('beforeend','<button class="dm-go" type="button"><span>👆 Toque aqui para girar o projeto</span></button><button class="dm-ok" type="button" hidden>✓ Pronto</button><span class="dm-dica" hidden>Arraste com um dedo para girar. Dois dedos para aproximar.</span>');}
 modo(false);
 b.onclick=e=>{if(e.target.closest('.dm-go')){modo(true);return;}if(e.target.closest('.dm-ok')){modo(false);return;}
  const x=e.target.closest('[data-dmst]');if(x){it.st=x.dataset.dmst;K.PUB.T[0].venda=tot(o);b.querySelectorAll('[data-dmst]').forEach(y=>y.setAttribute('aria-pressed',y===x));K.pedra(it.st);avisa('pedra');}};
 if(!RO&&window.ResizeObserver){RO=new ResizeObserver(altura);RO.observe(b);}altura();setTimeout(altura,400);}
addEventListener('resize',altura);
/* roda do mouse: sempre rola a página (não dá zoom no 3D sem querer) */
if(P)addEventListener('wheel',e=>{e.preventDefault();e.stopPropagation();P.scrollBy({top:e.deltaY*(e.deltaMode===1?16:1),behavior:'instant'});},{passive:false,capture:true});
/* dedo: fora do 3D ligado, arrastar rola a página; um toque sem arrastar continua sendo clique. Mede pela tela (screenY):
   a página sobe e leva o iframe junto, então clientY perderia metade do movimento */
if(P&&TOQUE){let y0=0,x0=0,yl=0,tl=0,v=0,mv=false,no3d=false,meu=false;
 const em3d=t=>ativo&&t&&t.closest&&t.closest('#cv-3d')&&!t.closest('.dm-ok');
 addEventListener('touchstart',e=>{meu=false;if(e.touches.length!==1)return;const T=e.touches[0];no3d=!!em3d(e.target);y0=yl=T.screenY;x0=T.screenX;tl=Date.now();v=0;mv=false;meu=true;},{passive:true,capture:true});
 addEventListener('touchmove',e=>{if(!meu||no3d||e.touches.length!==1)return;const T=e.touches[0],now=Date.now();if(!mv&&Math.hypot(T.screenX-x0,T.screenY-y0)>8)mv=true;
  if(mv){const d=yl-T.screenY;if(d){meu2=true;P.scrollBy({top:d,behavior:'instant'});v=d/Math.max(1,now-tl);}}yl=T.screenY;tl=now;},{passive:true,capture:true});
 addEventListener('touchend',()=>{if(meu&&mv&&!no3d&&Math.abs(v)>.2)P.scrollBy({top:v*300,behavior:'smooth'});meu=false;},{passive:true,capture:true});
 addEventListener('click',e=>{if(mv&&!no3d){e.preventDefault();e.stopPropagation();}mv=false;},true);
 let meu2=false;P.addEventListener('scroll',()=>{if(ativo&&!meu2)modo(false);meu2=false;},{passive:true});}
return{fn,ui};};
/*/LAZY:demo*/
