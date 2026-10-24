/* ORÇAMENTO DE DEMONSTRAÇÃO (24/10/2026, pedido do Pietro): a página de vendas (aplicativo.marmoristapro.online/sistema.html) mostra,
   num iframe, a página que o cliente recebe pelo link: marmoristapro.online/?orc=demo... (DEMO). São 3 projetos (os orçamentos #112,
   #113 e #106 da conta do Pietro) e o visitante troca a pedra de cada projeto entre 3 pedras (São Gabriel, Café Imperial e Quartzo Branco; poucas para a página ficar leve). Nada vai ao banco: propFn
   responde daqui (abrir e aprovar). Os preços (V, um por projeto e pedra) saíram da tabela de preços da conta do Pietro em 24/10/2026,
   com orcTotals (sem o desconto manual do #106); a cópia não leva custo, margem nem tabela. Mudar projetos ou preços: gere V de novo. */
LZK.demo=()=>({$,esc,brl,STONES,get cv(){return cv},get PUB(){return PUB},pedra:id=>{curStone=id;if(S.ready){applyStone();wake3D();}},renderClient:()=>renderClient(),clientBuild:f=>clientBuild(f),cotas:()=>{CL.cotas=!CL.cotas;document.querySelectorAll('[data-clt="cotas"]').forEach(x=>x.setAttribute('aria-pressed',CL.cotas));if(S.ready){S.cotas.visible=CL.cotas;S._dcKey='';wake3D();}}});
/*LAZY:demo*/
(window.__LZ=window.__LZ||{}).demo=function(K){const{$,esc,brl,STONES}=K;
const V=__V__,IT=__IT__,off={on:0},tot=o=>o.itens.reduce((t,it,i)=>t+(V[i][it.st]||0),0),avisa=m=>{try{if(parent!==window)parent.postMessage({mpDemo:m},'*');}catch(e){}};
function fn(b){if(b.action==='aprovar'){avisa('aprovou');return{ok:true,j:{ok:true,situacao:{status:'aprovado',aprovOp:0,aprovEm:Date.now()}}};}
 const o={id:'demo',num:214,cliente:{nome:'Maria Oliveira',end:'Cozinha, área gourmet e lavabo'},opcoes:[null],itens:JSON.parse(JSON.stringify(IT)),extras:{andar:off,frete:off,molde:off,visita:off,retirada:off},cuba:{inc:0},instalacao:null,instV:0,mats:[],
  prazo:{tipo:'combinar',ini:'',fim:''},validade:10,cond:'',status:'visto',aprovOp:null,aprovEm:null,criado:Date.now(),showPlan:0,cgOff:['rod','saia','alt','esp','itens','n2','prat','mont','sap','base','prato']};
 avisa('abriu');return{ok:true,j:{proposta:{o,vit:{nome:'Sua Marmoraria',tel:'(00) 00000-0000',cidade:''},T:[{venda:tot(o)}],st:IT.map(x=>x.st),nm:{},plan:null}}};}
/* 25/10/2026 (pedido do Pietro): o orçamento fica parado, sem rolagem própria. Só aparecem as abas dos projetos, o 3D, Medidas /
   Separar peças / Fundo e as 3 pedras (sem marmoraria, cliente, total nem aprovar). A altura (até o fim das pedras) vai para a
   página (mpDemo 'h'), que ajusta a moldura. "Medidas" liga/desliga só comprimento e largura, sem abrir a lista.
   No celular o 3D só gira depois de tocar em "Toque aqui para girar o projeto" ("Pronto" trava de novo; rolar a página também).
   Rolagem no celular: a página põe uma película dela por cima do iframe (o navegador não passa a rolagem de dentro do iframe
   para a página); a película rola como qualquer página e repassa os toques. Com o 3D ligado ('3d-on') a película sai.
   Antes o código empurrava a página a cada movimento e, no celular de verdade, tremia. A roda do mouse rola a página. */
const DENTRO=parent!==window,TOQUE=matchMedia('(pointer:coarse)').matches||'ontouchstart' in window;let ativo=false,P=null;
try{if(DENTRO&&parent.document)P=parent;}catch(e){}
(function css(){const st=document.createElement('style');st.textContent=
 '#cv-body>*:not(.cv-tabs):not(.cv-3d):not(.cv-tools):not(.dm-keep){display:none!important}#cv-scroll{overflow:hidden!important}.cg-menu{display:none!important}'
 +'.cv-tabs{display:grid!important;grid-template-columns:repeat(3,1fr);overflow:visible!important;touch-action:pan-y}.cv-tabs button{height:auto!important;min-height:40px;padding:6px 6px!important;white-space:normal;line-height:1.2;font-size:13px!important;border-radius:12px!important}'
 +'#dm-st{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;overflow:visible;touch-action:pan-y}#dm-st .cv-stone{width:auto;font-size:13px}.cv-tools{touch-action:pan-y}'
 +'.cv-3d:not(.dm-on){touch-action:pan-y!important}'
 +'.dm-go{position:absolute;inset:0;z-index:3;display:flex;align-items:flex-end;justify-content:center;padding:0 12px 16px;border:0;background:linear-gradient(transparent 45%,rgba(0,0,0,.55));color:inherit;font:inherit;cursor:pointer;touch-action:pan-y}'
 +'.dm-go span{display:inline-flex;align-items:center;gap:8px;padding:12px 18px;border-radius:999px;background:#F5B800;color:#1A1400;font-weight:800;font-size:16px;box-shadow:0 8px 24px rgba(0,0,0,.45)}'
 +'.dm-ok{position:absolute;top:10px;right:10px;z-index:3;padding:10px 16px;border-radius:999px;border:0;background:#F5B800;color:#1A1400;font:inherit;font-weight:800;font-size:15px;box-shadow:0 6px 18px rgba(0,0,0,.45);cursor:pointer}'
 +'.dm-dica{position:absolute;left:10px;right:10px;bottom:10px;z-index:3;text-align:center;font-size:13px;font-weight:600;color:#fff;background:rgba(0,0,0,.6);padding:7px 10px;border-radius:10px;pointer-events:none}'
 +'.cv-3d .cv-hint{display:none!important}.dm-tag{position:absolute;top:10px;left:10px;z-index:2;background:rgba(22,27,30,.72);color:#fff;font-size:12px;padding:5px 10px;border-radius:14px;pointer-events:none}'
 +'html,body{overscroll-behavior:auto!important}';document.head.appendChild(st);})();
let hU=0;function altura(){if(!DENTRO)return;const el=document.getElementById('dm-st');if(!el)return;const h=Math.ceil(el.getBoundingClientRect().bottom+16);if(Math.abs(h-hU)<2)return;hU=h;try{parent.postMessage({mpDemo:'h',h},'*');}catch(e){}}
let RO=null;
let yAtivo=0;function modo(on){const mud=ativo!==on;ativo=on;if(on&&P)yAtivo=P.scrollY;if(mud||!on)avisa(on?'3d-on':'3d-off');const c=$('#cv-3d');if(!c)return;c.classList.toggle('dm-on',on);const g=c.querySelector('.dm-go'),k=c.querySelector('.dm-ok'),d=c.querySelector('.dm-dica');
 if(g)g.hidden=on;if(k)k.hidden=!on;if(d)d.hidden=!on;}
function ui(){const c=K.cv,o=c&&c.o,it=o&&o.itens[c.it],b=$('#cv-body');if(!it||!b)return;const at=b.querySelector('.cv-tools');
 if(at)at.insertAdjacentHTML('afterend',`<h4 class="cv-h dm-keep">Escolha a pedra${o.itens.length>1?' deste projeto':''}</h4><div class="cv-stones dm-keep" id="dm-st">${STONES.filter(s=>V[c.it][s.id]!=null).map(s=>`<button class="cv-stone" data-dmst="${s.id}" aria-pressed="${s.id===it.st}"><span class="sw" style="background-image:url(${s.sw})"></span><span>${esc(s.nome)}</span></button>`).join('')}</div>`);
 const md=b.querySelector('[data-clt="cotas"]');if(md){md.textContent='Medidas';md.removeAttribute('aria-expanded');}
 const v3=$('#cv-3d');if(v3){if(!TOQUE)v3.insertAdjacentHTML('beforeend','<span class="dm-tag">Clique e arraste para girar</span>');
  if(TOQUE)v3.insertAdjacentHTML('beforeend','<button class="dm-go" type="button"><span>👆 Toque aqui para girar o projeto</span></button><button class="dm-ok" type="button" hidden>✓ Pronto</button><span class="dm-dica" hidden>Arraste com um dedo para girar. Dois dedos para aproximar.</span>');}
 modo(false);
 b.onclick=e=>{if(e.target.closest('.dm-go')){modo(true);return;}if(e.target.closest('.dm-ok')){modo(false);return;}
  const x=e.target.closest('[data-dmst]');if(x){it.st=x.dataset.dmst;K.PUB.T[0].venda=tot(o);b.querySelectorAll('[data-dmst]').forEach(y=>y.setAttribute('aria-pressed',y===x));K.pedra(it.st);avisa('pedra');}};
 if(!RO&&window.ResizeObserver){RO=new ResizeObserver(altura);RO.observe(b);}altura();setTimeout(altura,400);}
/* "Medidas": liga/desliga, sem abrir a lista (pega o clique antes do app) */
addEventListener('click',e=>{const m=e.target.closest&&e.target.closest('[data-clt="cotas"]');if(!m)return;e.preventDefault();e.stopImmediatePropagation();K.cotas();},true);
/* roda do mouse: sempre rola a página (não dá zoom no 3D sem querer) */
if(P)addEventListener('wheel',e=>{e.preventDefault();e.stopPropagation();P.scrollBy({top:e.deltaY*(e.deltaMode===1?16:1),behavior:'instant'});},{passive:false,capture:true});
/* 3D ligado e a pessoa rolou a página, ou tocou fora do 3D: trava de novo (a página volta a pôr a película por cima) */
if(P)P.addEventListener('scroll',()=>{if(ativo&&Math.abs(P.scrollY-yAtivo)>60)modo(false);},{passive:true});
addEventListener('touchstart',e=>{if(ativo&&!(e.target.closest&&e.target.closest('#cv-3d')))modo(false);},{passive:true,capture:true});
return{fn,ui};};
/*/LAZY:demo*/
