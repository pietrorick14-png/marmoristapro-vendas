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
function ui(){const c=K.cv,o=c&&c.o,it=o&&o.itens[c.it],b=$('#cv-body');if(!it||!b)return;const ap=['aprovado','producao','concluido'].includes(o.status),
  at=b.querySelector('.cg-menu')||b.querySelector('.cv-tools');
 if(ap){const n=b.querySelector('.banner.ok');if(n)n.insertAdjacentHTML('afterend','<span class="hint center">Demonstração: na vida real, a marmoraria recebe o aviso na hora.</span><button class="btn-ghost" data-dmre="1">Ver de novo</button>');}
 else if(at)at.insertAdjacentHTML('afterend',`<h4 class="cv-h">Escolha a pedra${o.itens.length>1?' deste projeto':''}</h4><div class="cv-stones" id="dm-st">${STONES.filter(s=>V[c.it][s.id]!=null).map(s=>`<button class="cv-stone" data-dmst="${s.id}" aria-pressed="${s.id===it.st}"><span class="sw" style="background-image:url(${s.sw})"></span><span>${esc(s.nome)}<small>${brl(V[c.it][s.id])}</small></span></button>`).join('')}</div><span class="hint">Toque numa pedra: o 3D e o total mudam na hora.</span>`);
 const sel=b.querySelector('#dm-st [aria-pressed="true"]');if(sel){const r=sel.parentNode;r.scrollLeft=sel.offsetLeft-r.clientWidth/2+sel.clientWidth/2;}
 b.onclick=e=>{const x=e.target.closest('[data-dmst]');if(x){it.st=x.dataset.dmst;K.PUB.T[0].venda=tot(o);b.querySelectorAll('[data-dmst]').forEach(y=>y.setAttribute('aria-pressed',y===x));
   const t=b.querySelector('.cv-total b');if(t)t.textContent=brl(tot(o));K.pedra(it.st);avisa('pedra');return;}
  if(e.target.closest('[data-dmre]')){Object.assign(o,{status:'visto',aprovOp:null,aprovEm:null});K.renderClient();K.clientBuild(true);}};}
/* dentro da página de vendas: quando a lista do orçamento chega ao fim (ou ao topo), a rolagem passa para a página
   (roda do mouse e dedo, com embalo no fim do toque); no 3D o dedo e a roda continuam girando e dando zoom */
(function(){if(parent===window)return;let P;try{P=parent.document&&parent;}catch(e){return;}if(!P)return;
 const sc=()=>document.getElementById('cv-scroll'),fim=(el,d)=>d>0?el.scrollTop+el.clientHeight>=el.scrollHeight-2:el.scrollTop<=0,
  fora=t=>!!(t&&t.closest&&t.closest('#cv-3d'));
 addEventListener('wheel',e=>{const el=sc();if(!el||!el.contains(e.target)||fora(e.target))return;if(fim(el,e.deltaY))P.scrollBy(0,e.deltaY*(e.deltaMode===1?16:1));},{passive:true});
 let y=null,x=0,v=0,t0=0;
 addEventListener('touchstart',e=>{if(e.touches.length!==1){y=null;return;}y=e.touches[0].clientY;x=e.touches[0].clientX;v=0;t0=Date.now();},{passive:true});
 addEventListener('touchmove',e=>{const el=sc(),T=e.touches[0];if(y==null||!el||!el.contains(e.target)||fora(e.target))return;const d=y-T.clientY,dx=x-T.clientX,now=Date.now();
  y=T.clientY;x=T.clientX;if(d&&Math.abs(d)>=Math.abs(dx)&&fim(el,d)){P.scrollBy(0,d);v=d/Math.max(1,now-t0);}else v=0;t0=now;},{passive:true});
 addEventListener('touchend',()=>{if(y!=null&&Math.abs(v)>.25)P.scrollBy({top:v*280,behavior:'smooth'});y=null;v=0;},{passive:true});})();
return{fn,ui};};
/*/LAZY:demo*/
