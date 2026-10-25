# Depois de copiar a demonstração nova para public/demo e public/assets: põe no <head> de public/demo/index.html as
# pré-cargas das partes do app e das fotos das 3 pedras (baixam juntas, o 3D abre mais rápido). Rodar na pasta do repositório.
import os,re
d='public/demo/index.html';h=open(d,encoding='utf-8',newline='').read()
h=re.sub(r'<!--dm-pre-->.*?<!--/dm-pre-->','',h,flags=re.S)
A=sorted(os.listdir('public/assets'));I=sorted(os.listdir('public/assets/img'))
js=[f for n in ['supa','app','demo','three','b3d','cantos','tex'] for f in A if re.fullmatch(n+r'-[0-9a-f]{10}\.js',f)]
img=[f for n in ['pedra-saogabriel','pedra-cafe','pedra-quartzo'] for f in I if re.fullmatch(n+r'-[0-9a-f]{10}\.webp',f)]
tags=''.join('<link rel="preload" as="script" href="/assets/%s">'%f for f in js)+''.join('<link rel="preload" as="image" href="/assets/img/%s">'%f for f in img)
h=h.replace('<head>','<head><!--dm-pre-->'+tags+'<!--/dm-pre-->',1)
open(d,'w',encoding='utf-8',newline='').write(h);print('pré-cargas:',len(js),'partes,',len(img),'fotos')
