# Conteúdo das páginas novas de /dicas
P = []

def pg(slug, titulo, h1, desc, lead, minutos, corpo, rel, curto, data='2026-11-23'):
    # data = dia da publicação (AAAA-MM-DD); página nova usa a data do dia
    P.append(dict(slug=slug, titulo=titulo, h1=h1, desc=desc, lead=lead, min=minutos, corpo=corpo, rel=rel, curto=curto, data=data))

pg('meia-esquadria-em-granito',
 'Meia-Esquadria em Granito: o que é, como fazer e como cobrar',
 'Meia-esquadria em granito: o que é, como fazer e como cobrar',
 'O que é meia-esquadria na pedra, onde usar (saia, quina, pé de bancada), como cortar a 45° sem lascar, colar e cobrar por metro linear.',
 'Meia-esquadria é o encontro de duas peças de pedra cortadas a 45°, formando uma quina sem a emenda aparecendo. É o acabamento que faz a bancada parecer um bloco maciço.',
 5,
 '''
<h2>O que é meia-esquadria</h2>
<p>Em vez de colar uma peça "por cima" da outra (e a borda de uma delas ficar à vista), as duas peças são cortadas em ângulo de 45°. Quando se encontram, formam 90° e a quina fica fechada, com o desenho da pedra contínuo. Na obra também se fala "45", "esquadria" ou "meio esquadro".</p>
<div class="box au"><b>Reta (topo) × meia-esquadria</b><br>Na colagem reta, a saia encosta embaixo do tampo e a espessura das duas peças aparece na frente. Na meia-esquadria, só a quina aparece, como se a pedra fosse grossa.</div>

<h2>Onde se usa</h2>
<ul>
<li><b>Saia da bancada</b>: tampo e saia se encontram a 45° na frente. É o uso mais comum.</li>
<li><b>Quina da saia</b>: onde a saia da frente vira para a lateral.</li>
<li><b>Pé de bancada (pé de piano)</b>: o tampo desce até o chão e o encontro tampo-pé é em 45°.</li>
<li><b>Cuba esculpida</b>: laterais e fundo da cuba montados em 45° ficam sem linha de cola.</li>
<li><b>Nichos, ilhas, revestimento de pilar, degraus de escada</b>.</li>
</ul>

<h2>Como fazer, passo a passo</h2>
<ol>
<li><b>Confira a medida final</b>. Na meia-esquadria, a medida é da face de fora. Ex.: saia de 4 cm com tampo de 2 cm. A peça da saia sai com 4 cm de altura total, contando a ponta do 45°.</li>
<li><b>Corte a 45° na serra-ponte ou na máquina de meia-esquadria</b>, com disco bom e água. Corte com a face boa para cima e deixe uns milímetros sem chegar ao fio, para não lascar a ponta.</li>
<li><b>Deixe uma pontinha</b> (cerca de 1 a 2 mm de "dente" reto no fim do 45°). Ponta muito fina quebra na colagem e no transporte.</li>
<li><b>Teste a seco</b>: encoste as duas peças e veja se o encontro fecha por inteiro.</li>
<li><b>Cole</b> com massa ou adesivo de pedra tingido na cor da pedra (veja <a href="/dicas/como-colar-granito">como colar granito</a>), segure com grampo ou sargento e tire o excesso antes de endurecer.</li>
<li><b>Acabe a quina</b>: lixe e dê polimento leve, ou um pequeno chanfro/boleado para não ficar cortante.</li>
</ol>

<h2>Cuidados</h2>
<ul>
<li>Pedra muito clara mostra mais a linha de cola: capriche no tom da massa.</li>
<li>Pedra com veio forte: corte as duas peças na sequência da chapa, para o desenho "virar" a quina.</li>
<li>Meia-esquadria aumenta o tempo de máquina e o risco de perda. Isso tem que estar no preço.</li>
</ul>

<h2>Como cobrar</h2>
<p>A forma mais usada é <b>por metro linear</b> de meia-esquadria, somado ao preço da pedra. Exemplo (valores só para ilustrar, use os seus):</p>
<div class="tab"><table>
<tr><th>Item</th><th>Conta</th><th>Valor</th></tr>
<tr><td>Saia em meia-esquadria na frente</td><td>2,40 m × R$ 60,00</td><td>R$ 144,00</td></tr>
<tr><td>Quina da saia (lateral)</td><td>0,60 m × R$ 60,00</td><td>R$ 36,00</td></tr>
<tr><td><b>Total do serviço de 45°</b></td><td></td><td><b>R$ 180,00</b></td></tr>
</table></div>
<p>A pedra da saia continua entrando no m² ou no metro linear da saia (veja <a href="/dicas/saia-de-granito">saia de granito</a>). O 45° é a mão de obra a mais.</p>
''',
 ['saia-de-granito','cuba-esculpida-em-granito','como-colar-granito','espessura-de-granito-para-bancada'],
 'O que é, onde usar, como cortar a 45° e como cobrar por metro linear.')

pg('cuba-esculpida-em-granito',
 'Cuba Esculpida em Granito: medidas, profundidade e como fazer',
 'Cuba esculpida em granito: medidas, profundidade e como fazer',
 'Medidas comuns da cuba esculpida, profundidade, caimento para o ralo, rampa ou canaleta escondida, como montar as peças na marmoraria e como cobrar.',
 'Cuba esculpida é a cuba feita da própria pedra da bancada. Fica bonita porque parece uma peça só, mas é a que mais dá problema quando a medida, o caimento ou a colagem saem errados.',
 6,
 '''
<h2>Os tipos mais pedidos</h2>
<ul>
<li><b>Cuba com rampa</b>: fundo inclinado que leva a água para uma canaleta escondida no fundo (o ralo fica "sumido"). É a mais pedida em banheiro e lavabo.</li>
<li><b>Cuba reta (caixa)</b>: fundo plano com leve caimento para a válvula. Mais simples de fazer.</li>
<li><b>Cuba com tampa no ralo</b>: o ralo fica embaixo de uma tampinha da mesma pedra, solta ou apoiada.</li>
</ul>

<h2>Medidas comuns (para começar o desenho)</h2>
<p>Não existe medida obrigatória: ela depende do tamanho da bancada e do gosto do cliente. Estas faixas são as mais vistas em banheiro e servem de ponto de partida:</p>
<div class="tab"><table>
<tr><th>Medida</th><th>Faixa comum</th><th>Observação</th></tr>
<tr><td>Comprimento</td><td>40 a 60 cm</td><td>Lavabo costuma usar a menor</td></tr>
<tr><td>Largura (frente-fundo)</td><td>30 a 40 cm</td><td>Deixe pelo menos uns 5 cm de pedra na frente</td></tr>
<tr><td>Profundidade</td><td>8 a 15 cm</td><td>Rasa demais respinga; funda demais pesa e custa mais</td></tr>
<tr><td>Canaleta da rampa</td><td>3 a 5 cm</td><td>Larga o bastante para limpar</td></tr>
</table></div>
<p>Antes de cortar, confira a <b>torneira</b>: o jato tem que cair dentro da cuba, mais para o meio. Torneira de parede ou de mesa muda a conta.</p>

<h2>Caimento: o ponto que mais dá retorno</h2>
<p>A água tem que correr sozinha para o ralo. Na rampa, o fundo desce da frente para a canaleta. Na cuba reta, o fundo desce de leve para a válvula. Teste com água na marmoraria, antes de levar para a obra. Água parada na cuba é o motivo número um de cliente reclamar.</p>

<h2>Como montar, passo a passo</h2>
<ol>
<li><b>Faça o desenho com as peças</b>: tampo com o furo, duas laterais, frente, fundo e rampa (ou fundo reto). Anote a medida de cada uma.</li>
<li><b>Corte o furo no tampo</b> e as peças da cuba, de preferência da mesma chapa, para a cor bater.</li>
<li><b>Monte as laterais em <a href="/dicas/meia-esquadria-em-granito">meia-esquadria</a></b> ou coladas no topo, conforme o acabamento combinado.</li>
<li><b>Cole com adesivo próprio para pedra</b> e reforce por baixo (cantoneira ou tiras de pedra) para a cuba não "descolar" com o peso da água.</li>
<li><b>Vede as emendas por dentro</b> com a massa na cor da pedra e dê o polimento.</li>
<li><b>Teste com água</b> e só então embale.</li>
</ol>

<h2>Como cobrar</h2>
<p>Muita marmoraria cobra a cuba esculpida como um <b>valor fixo por cuba</b> (que cobre a mão de obra e as peças a mais) somado ao m² da bancada. Outras somam o m² das peças da cuba + um valor de mão de obra. Exemplo (só para ilustrar):</p>
<ul>
<li>Bancada 1,20 × 0,50 m = 0,60 m² × R$ 600,00 = R$ 360,00</li>
<li>Cuba esculpida com rampa: R$ 450,00 (valor fixo do exemplo)</li>
<li><b>Total: R$ 810,00</b> + saia, frontão e instalação, se tiver</li>
</ul>
<p>Para fechar o orçamento completo, veja <a href="/dicas/como-fazer-orcamento-de-bancada-de-granito">como fazer orçamento de bancada de granito</a>.</p>
''',
 ['meia-esquadria-em-granito','como-colar-granito','nicho-de-granito-para-banheiro','como-medir-bancada-de-granito'],
 'Medidas, profundidade, caimento, montagem das peças e cobrança.')

pg('espessura-de-granito-para-bancada',
 'Espessura de Granito para Bancada: 2 cm ou 3 cm?',
 'Espessura de granito para bancada: 2 cm ou 3 cm?',
 'Qual espessura de granito usar em bancada de cozinha, banheiro, escada, soleira e piso; quando engrossar com saia e o que muda no preço e no peso.',
 'No Brasil, as chapas de granito mais comuns são de 2 cm e de 3 cm. A escolha muda o preço, o peso, o apoio e o acabamento da borda. Veja quando usar cada uma.',
 4,
 '''
<h2>Resposta rápida</h2>
<div class="box au"><b>Bancada de cozinha e banheiro:</b> 2 cm é o mais usado, com saia para dar aparência de pedra grossa.<br><b>3 cm:</b> quando o cliente quer a borda grossa sem saia, vão grande sem apoio ou balcão em balanço.</div>

<h2>Onde vai cada espessura</h2>
<div class="tab"><table>
<tr><th>Peça</th><th>Uso mais comum</th><th>Por quê</th></tr>
<tr><td>Bancada de cozinha</td><td>2 cm + saia</td><td>Mais leve e mais barata; a saia dá a "grossura"</td></tr>
<tr><td>Bancada de banheiro</td><td>2 cm</td><td>Peça menor, pouco esforço</td></tr>
<tr><td>Balcão em balanço / ilha com vão</td><td>3 cm ou 2 cm com reforço</td><td>Pedra fina em balanço trinca</td></tr>
<tr><td>Degrau de escada</td><td>2 ou 3 cm</td><td>Depende do apoio e do tráfego</td></tr>
<tr><td>Soleira e peitoril</td><td>2 cm</td><td>Veja <a href="/dicas/soleira-e-peitoril-de-granito">soleira e peitoril</a></td></tr>
<tr><td>Piso</td><td>2 cm</td><td>Assentado direto no contrapiso</td></tr>
<tr><td>Revestimento de parede, nicho</td><td>1 a 2 cm</td><td>Não leva carga</td></tr>
</table></div>
<p>Use a tabela como referência do dia a dia. Em caso de vão grande ou carga pesada, siga o que o fornecedor da chapa e o responsável pela obra indicarem.</p>

<h2>Engrossar com saia</h2>
<p>Com chapa de 2 cm você chega à aparência de 4 cm, 6 cm ou mais colando uma <a href="/dicas/saia-de-granito">saia</a> na frente. Com <a href="/dicas/meia-esquadria-em-granito">meia-esquadria</a> a emenda nem aparece. Por isso a chapa de 3 cm é menos comum em bancada simples.</p>

<h2>Peso: conta rápida</h2>
<p>Granito pesa em torno de 2.600 a 2.800 kg por m³ (varia com a pedra). Uma conta prática: <b>cada m² de chapa de 2 cm pesa algo perto de 55 kg</b>; de 3 cm, perto de 80 kg. Uma bancada de 2,00 × 0,60 m em 2 cm (1,20 m²) passa de 60 kg, sem contar a saia. Isso decide quantas pessoas vão na instalação e o tipo de apoio (veja <a href="/dicas/como-instalar-bancada-de-granito">como instalar bancada de granito</a>).</p>

<h2>E no preço?</h2>
<p>A chapa de 3 cm costuma custar mais por m² que a de 2 cm da mesma pedra, e pesa mais no transporte. No orçamento, deixe claro qual espessura foi cotada e se a borda grossa é de chapa grossa ou de saia colada.</p>
''',
 ['saia-de-granito','tamanho-de-chapa-de-granito','como-instalar-bancada-de-granito','meia-esquadria-em-granito'],
 '2 cm ou 3 cm em cada peça, engrossar com saia, peso e preço.')

pg('rodabanca-e-frontao',
 'Rodabanca e Frontão: diferença, altura e como cobrar',
 'Rodabanca e frontão: qual a diferença, que altura usar e como cobrar',
 'Diferença entre rodabanca, frontão e testeira na bancada de granito, alturas mais usadas, como medir, colar e cobrar por metro linear.',
 'Rodabanca e frontão são a pedra que sobe na parede atrás da bancada. A diferença é a altura: a rodabanca é baixa, o frontão é alto. Cada região chama de um jeito, por isso vale combinar com o cliente com a medida escrita.',
 4,
 '''
<h2>Qual a diferença</h2>
<div class="tab"><table>
<tr><th>Nome</th><th>O que é</th><th>Altura comum</th></tr>
<tr><td>Rodabanca</td><td>Faixa baixa na parede, colada atrás da bancada</td><td>7 a 15 cm (10 cm é a mais vista)</td></tr>
<tr><td>Frontão</td><td>Faixa alta, que protege a parede da pia ou do fogão</td><td>40 a 60 cm, ou até o armário de cima</td></tr>
<tr><td>Testeira</td><td>Em muitas regiões, a pedra na lateral da bancada (encostada na parede do lado)</td><td>Igual à rodabanca</td></tr>
</table></div>
<p>As alturas são as mais vistas no mercado, não uma regra. O que manda é a parede: tomada, janela e armário aéreo.</p>

<h2>Como medir</h2>
<ol>
<li>Meça o comprimento <b>de cada parede</b> que encosta na bancada (em L e U, cada lado é uma peça).</li>
<li>Veja onde estão as <b>tomadas</b> e o registro: rodabanca alta ou frontão vai precisar de recorte.</li>
<li>Confira se a parede está no prumo. Parede torta pede rodabanca um pouco mais alta para esconder a fresta.</li>
<li>No canto do L, decida quem passa por cima de quem (uma peça encosta na outra).</li>
</ol>

<h2>Como instalar</h2>
<p>Cole a rodabanca em cima da bancada, encostada na parede, com adesivo ou massa e acabe com silicone neutro na emenda com a bancada. O silicone ali impede a água de escorrer para trás do armário. O frontão vai colado na parede com argamassa ou adesivo próprio para pedra.</p>

<h2>Como cobrar</h2>
<p>A rodabanca normalmente entra por <b>metro linear</b>; o frontão, por <b>m²</b> (porque é alto). Exemplo (valores só para ilustrar):</p>
<ul>
<li>Rodabanca de 10 cm: 2,40 m + 0,60 m (testeira) = 3,00 m × R$ 45,00 = R$ 135,00</li>
<li>Frontão de 50 cm atrás do fogão: 0,90 × 0,50 = 0,45 m² × R$ 600,00 = R$ 270,00</li>
<li>Recorte de tomada no frontão: 2 × R$ 25,00 = R$ 50,00</li>
</ul>
<p>Para somar com a bancada, a saia e os recortes, use a <a href="/dicas/calculadora-orcamento-bancada-granito">calculadora de orçamento de bancada</a>.</p>
''',
 ['saia-de-granito','como-medir-bancada-de-granito','como-instalar-bancada-de-granito','calculadora-orcamento-bancada-granito'],
 'Diferença entre rodabanca, frontão e testeira, alturas e cobrança.')

pg('saia-de-granito',
 'Saia de Granito: alturas, tipos de colagem e como cobrar',
 'Saia de granito: alturas, tipos de colagem e como cobrar',
 'O que é a saia da bancada de granito, alturas mais usadas (4, 7, 10 cm e até o chão), colagem reta ou em meia-esquadria, como medir e cobrar por metro linear.',
 'A saia é a faixa de pedra colada na frente (e às vezes na lateral) da bancada. Ela esconde o armário, dá aparência de pedra grossa e protege a borda. É também onde muito orçamento perde dinheiro, por esquecer metro.',
 5,
 '''
<h2>Alturas mais usadas</h2>
<div class="tab"><table>
<tr><th>Altura</th><th>Onde aparece</th></tr>
<tr><td>4 cm</td><td>Bancada de cozinha "padrão": parece pedra de 4 cm</td></tr>
<tr><td>7 a 10 cm</td><td>Bancada de banheiro, balcão, visual mais pesado</td></tr>
<tr><td>15 a 20 cm</td><td>Bancada de banheiro suspensa, esconde a cuba de embutir</td></tr>
<tr><td>Até o chão</td><td>Pé da bancada (pé de piano), ilha</td></tr>
</table></div>

<h2>Colagem reta ou meia-esquadria</h2>
<ul>
<li><b>Reta (de topo)</b>: a saia encosta por baixo do tampo. Mais rápida e barata; a emenda aparece na frente.</li>
<li><b><a href="/dicas/meia-esquadria-em-granito">Meia-esquadria</a></b>: tampo e saia cortados a 45°. A emenda some, mas leva mais máquina e mais cuidado.</li>
</ul>
<p>Combine no orçamento qual das duas foi cotada. Cliente que viu foto de meia-esquadria e recebeu colagem reta volta reclamando.</p>

<h2>Como medir a saia</h2>
<ol>
<li>Some <b>toda a frente livre</b> da bancada (em L e U, cada lado).</li>
<li>Some as <b>laterais livres</b> (pontas que não encostam na parede).</li>
<li>Na quina da saia, conte só uma vez: as duas peças se encontram ali.</li>
<li>Desconte o trecho onde a saia é cortada (fogão de piso entre bancadas, por exemplo).</li>
</ol>
<p>Exemplo: bancada em L com frente de 2,50 m e 1,80 m, lateral livre de 0,60 m. Saia = 2,50 + (1,80 − 0,60) + 0,60 = <b>4,30 m</b>. O lado de 1,80 m perde 0,60 m porque o canto já está na frente do outro lado.</p>

<h2>Como colar</h2>
<p>Lixe as faces que vão se encontrar, cole com massa ou adesivo na cor da pedra, prenda com grampo e tire o excesso. Detalhes em <a href="/dicas/como-colar-granito">como colar granito</a>.</p>

<h2>Como cobrar</h2>
<p>O jeito mais comum é <b>por metro linear</b>, com o preço mudando conforme a altura (saia de 4 cm custa menos que a de 10 cm). Outra opção é somar a pedra da saia no m² e cobrar a colagem à parte. Exemplo (só para ilustrar):</p>
<ul>
<li>Saia de 4 cm, colagem reta: 4,30 m × R$ 40,00 = R$ 172,00</li>
<li>A mesma saia em meia-esquadria: 4,30 m × R$ 40,00 + 4,30 m × R$ 60,00 = R$ 430,00</li>
</ul>
<p>Escolha um jeito e use sempre o mesmo, para os orçamentos baterem entre si.</p>
''',
 ['meia-esquadria-em-granito','rodabanca-e-frontao','espessura-de-granito-para-bancada','como-calcular-metro-quadrado-de-granito'],
 'Alturas, colagem reta ou em 45°, como medir em L e como cobrar.')

pg('recorte-de-cooktop-no-granito',
 'Recorte de Cooktop no Granito: medidas e como cortar',
 'Recorte de cooktop no granito: medidas e como cortar sem trincar',
 'Como achar a medida do recorte do cooktop de 4 e 5 bocas, quanto deixar de pedra na frente e atrás, cantos arredondados, cuidados para não trincar e como cobrar.',
 'O recorte do cooktop é dos que mais dá dor de cabeça: um centímetro a menos e o cooktop não entra, a mais e sobra fresta. A regra de ouro é simples: a medida vem do manual do aparelho, nunca de tabela da internet.',
 5,
 '''
<h2>De onde vem a medida</h2>
<div class="box au"><b>Peça ao cliente o modelo exato do cooktop (marca e código)</b> e pegue a medida de recorte no manual de instalação ou no site do fabricante. Cooktops com o mesmo número de bocas têm recortes diferentes de uma marca para outra.</div>
<p>Se o aparelho já estiver na obra, meça a parte de baixo (a "caixa" que entra na pedra) e confira com o manual. A medida que importa é a do corpo de baixo, não a do vidro.</p>

<h2>Quanto de pedra deixar em volta</h2>
<ul>
<li><b>Na frente</b>: deixe uma faixa de pedra firme entre o recorte e a borda (o manual costuma dar a distância mínima). Faixa muito fina quebra no transporte.</li>
<li><b>Atrás</b>: respeite a distância da parede ou do frontão pedida pelo fabricante, por causa do calor e das panelas.</li>
<li><b>Dos lados</b>: confira a distância da parede lateral, de armário alto e de geladeira.</li>
<li><b>Por baixo</b>: veja se a gaveta ou o forno de baixo não bate na caixa do cooktop.</li>
</ul>

<h2>Como cortar sem trincar</h2>
<ol>
<li>Marque o recorte com o esquadro, já com a folga que o manual pede.</li>
<li><b>Arredonde os cantos internos</b> (furo com serra-copo ou broca diamantada em cada canto). Canto vivo concentra força e é por onde a pedra trinca.</li>
<li>Corte as retas com disco diamantado e água, sem forçar.</li>
<li>Se der, faça o recorte na marmoraria e leve a peça reforçada (uma ripa ou tira de pedra embaixo da faixa fina) até instalar.</li>
<li>Teste o encaixe com o aparelho ou com um gabarito do tamanho dele.</li>
</ol>

<h2>Quando a bancada é em L</h2>
<p>Cooktop perto do canto do L aperta: confira se sobra pedra entre o recorte e a emenda do canto e se a panela grande não bate na parede. Se não couber com folga, avise o cliente antes de cortar.</p>

<h2>Como cobrar</h2>
<p>O recorte de cooktop costuma ser <b>um valor por recorte</b>, igual ao recorte de cuba, somado ao m² da bancada. Exemplo (só para ilustrar): recorte de cooktop R$ 80,00 + furo de torneira R$ 25,00. Veja como somar tudo em <a href="/dicas/como-fazer-orcamento-de-bancada-de-granito">como fazer orçamento de bancada de granito</a>.</p>
''',
 ['como-medir-bancada-de-granito','como-fazer-orcamento-de-bancada-de-granito','como-instalar-bancada-de-granito','plano-de-corte-de-chapa-de-granito'],
 'Medida pelo manual, pedra em volta, cantos arredondados e cobrança.')

pg('como-medir-bancada-de-granito',
 'Como Medir Bancada de Granito na Obra (reta, L e U)',
 'Como medir bancada de granito na obra: reta, em L e em U',
 'Passo a passo para medir bancada de granito na obra sem erro: esquadro, prumo, medidas de cada lado do L e do U, cuba, cooktop, torneira, altura e quando fazer gabarito.',
 'Medida errada vira pedra perdida e viagem a mais. A medição na obra é rápida quando você segue sempre a mesma ordem e anota tudo num desenho, não num papel solto.',
 6,
 '''
<h2>O que levar</h2>
<ul>
<li>Trena (de preferência a laser + trena de fita), nível e esquadro grande</li>
<li>Prancheta ou celular para desenhar a bancada vista de cima</li>
<li>Modelo da cuba, do cooktop e da torneira (peça ao cliente antes)</li>
</ul>

<h2>Passo a passo</h2>
<ol>
<li><b>Desenhe a bancada vista de cima</b> e dê um nome para cada parede (A, B, C).</li>
<li><b>Meça cada parede em três alturas</b>: rente ao armário, no meio e mais acima. Parede raramente está reta; use a menor medida onde a pedra vai encaixar entre paredes.</li>
<li><b>Meça a profundidade</b> em cada ponta e no meio. A profundidade mais comum de cozinha fica perto de 60 cm, mas meça sempre.</li>
<li><b>Confira o esquadro dos cantos</b>. Canto fora de 90° muda o corte do L: anote quantos milímetros abre ou fecha.</li>
<li><b>Marque as peças</b>: centro da cuba, posição do cooktop, furo da torneira, ralo, tomadas na parede (para a <a href="/dicas/rodabanca-e-frontao">rodabanca e o frontão</a>).</li>
<li><b>Meça a altura</b> do chão até o topo do armário ou da alvenaria e confira o nível.</li>
<li><b>Anote a saia e o que encosta</b>: lados livres, geladeira, fogão de piso, janela.</li>
<li><b>Tire fotos</b> de cada parede com a trena aparecendo.</li>
</ol>

<h2>Bancada em L e em U</h2>
<p>Meça cada lado <b>de parede até a ponta</b>, sempre pela parede do fundo. Depois decida no desenho onde fica a emenda e quem é o lado "inteiro". Lembre que o canto só entra uma vez no m²: a conta está em <a href="/dicas/como-calcular-metro-quadrado-de-granito">como calcular o metro quadrado de granito</a>.</p>

<h2>Alturas de referência</h2>
<p>A altura da bancada de cozinha costuma ficar perto de 90 cm do chão (entre 85 e 92 cm é o mais visto); a de banheiro, entre 80 e 90 cm, dependendo da cuba. Para pessoa muito alta ou baixa, ajuste junto com o cliente. São referências de mercado, não regra.</p>

<h2>Quando fazer gabarito</h2>
<p>Faça gabarito (molde em MDF fino, papelão ou ripas) quando a parede é muito torta, tem curva, pilar no meio ou canto muito fora de esquadro. Ele custa uma hora a mais e evita perder uma chapa.</p>

<h2>Depois da medição</h2>
<p>Passe as medidas para o orçamento no mesmo dia. Se o cliente fechar, confirme a cuba e o cooktop que chegaram na obra antes de cortar (veja <a href="/dicas/recorte-de-cooktop-no-granito">recorte de cooktop</a>).</p>
''',
 ['como-calcular-metro-quadrado-de-granito','recorte-de-cooktop-no-granito','como-instalar-bancada-de-granito','rodabanca-e-frontao'],
 'Passo a passo da medição, L e U, alturas de referência e gabarito.')

pg('tamanho-de-chapa-de-granito',
 'Tamanho de Chapa de Granito: medidas e aproveitamento',
 'Tamanho de chapa de granito: medidas e como aproveitar',
 'Por que não existe tamanho padrão de chapa de granito, faixas de medida mais vistas, chapa de quartzo, como medir a chapa útil e como calcular quantas peças saem dela.',
 'Chapa de granito não tem tamanho fixo: cada bloco da pedreira rende chapas de medidas diferentes. Por isso o certo é medir a chapa que você comprou e fazer as contas em cima dela.',
 4,
 '''
<h2>Medidas mais vistas</h2>
<p>As chapas de granito costumam ter algo entre <b>2,60 e 3,20 m de comprimento</b> e entre <b>1,60 e 2,00 m de altura</b>, em 2 ou 3 cm de espessura. Pedras exóticas podem vir maiores ou menores. As chapas de quartzo industrializado têm medida fixa por fabricante (pergunte ao distribuidor). Use isso só como referência: <b>a medida que vale é a da etiqueta ou da sua trena</b>.</p>

<h2>Chapa bruta × chapa útil</h2>
<p>A borda da chapa quase sempre vem irregular, lascada ou com trinca. Antes de planejar, meça a <b>área útil</b>: desconte de 2 a 5 cm de cada borda e marque defeitos, manchas e furos.</p>
<div class="box au">Exemplo: chapa de 3,00 × 1,90 m. Descontando 3 cm em volta, sobra 2,94 × 1,84 m = <b>5,41 m² úteis</b> (de 5,70 m² brutos).</div>

<h2>Quantas peças cabem</h2>
<p>Para bancadas de 60 cm de profundidade, uma chapa de 1,84 m úteis de altura rende 3 faixas de 60 cm (1,80 m) com 4 cm de sobra para o corte. Já para 65 cm, cabem só 2 faixas e sobra uma tira de uns 50 cm, boa para saia, rodabanca e soleira. É assim que se decide a melhor chapa para cada obra.</p>
<p>O passo a passo do encaixe está em <a href="/dicas/plano-de-corte-de-chapa-de-granito">plano de corte de chapa de granito</a>.</p>

<h2>Quanto custa uma chapa</h2>
<p>O preço da chapa é dado por m² e varia muito com a pedra, a espessura, o lote e a região. Para saber o custo da chapa inteira: <b>m² da chapa × preço do m²</b>. Ex.: 5,70 m² × R$ 280,00 = R$ 1.596,00 (valor só de exemplo). No orçamento, lembre que você paga a chapa inteira, não só o pedaço que vai na obra.</p>
''',
 ['plano-de-corte-de-chapa-de-granito','espessura-de-granito-para-bancada','como-calcular-metro-quadrado-de-granito','calculadora-orcamento-bancada-granito'],
 'Faixas de medida, chapa útil, quantas peças saem e custo da chapa.')

pg('como-instalar-bancada-de-granito',
 'Como Instalar Bancada de Granito: apoio, cola e vedação',
 'Como instalar bancada de granito: apoio, nível, cola e vedação',
 'Passo a passo para instalar bancada de granito: conferir a medida, apoio em alvenaria, armário ou mão francesa, chumbador em parede de drywall, nível, colagem e silicone.',
 'Uma bancada bem feita pode ser estragada na instalação. Nível, apoio firme e vedação certa evitam trinca, bancada balançando e água escorrendo para dentro do armário.',
 6,
 '''
<h2>Antes de sair da marmoraria</h2>
<ul>
<li>Confira as peças pelo desenho e pelo <a href="/dicas/como-medir-bancada-de-granito">levantamento de medidas</a>.</li>
<li>Transporte a pedra <b>em pé</b> (de lado), nunca deitada: deitada ela trinca com o balanço.</li>
<li>Peças com recorte de cuba ou cooktop vão com reforço na faixa fina.</li>
<li>Leve nível, cunhas, silicone neutro, adesivo/massa para pedra, furadeira e buchas.</li>
</ul>

<h2>Tipos de apoio</h2>
<div class="tab"><table>
<tr><th>Apoio</th><th>Quando usar</th><th>Cuidado</th></tr>
<tr><td>Alvenaria</td><td>Cozinha e área de serviço</td><td>Topo nivelado e com apoio a cada trecho</td></tr>
<tr><td>Armário</td><td>Cozinha planejada</td><td>Armário nivelado e firme; o armário não foi feito para segurar balanço</td></tr>
<tr><td>Mão francesa / suporte de aço</td><td>Bancada suspensa de banheiro, balcão</td><td>Suporte próprio para o peso e bem chumbado</td></tr>
<tr><td>Chumbada na parede</td><td>Bancada de banheiro sem móvel</td><td>Rasgo na parede e argamassa; em drywall, só com reforço interno</td></tr>
</table></div>

<h2>Passo a passo</h2>
<ol>
<li><b>Confira o nível</b> do apoio e corrija com cunha ou argamassa antes de colocar a pedra.</li>
<li><b>Apresente a pedra</b> sem cola, veja encaixe nas paredes e posição da cuba e do cooktop.</li>
<li><b>Fixe</b>: em alvenaria e armário, cordões de adesivo/silicone ou argamassa; em mão francesa, apoio em toda a peça.</li>
<li><b>Monte as emendas do L e do U</b> com adesivo na cor da pedra, nivelando as duas faces (veja <a href="/dicas/como-colar-granito">como colar granito</a>).</li>
<li><b>Instale a cuba</b> (embutir: colada por baixo e reforçada; sobrepor: silicone em volta).</li>
<li><b>Coloque a <a href="/dicas/rodabanca-e-frontao">rodabanca</a></b> e vede com silicone neutro a emenda com a bancada e com a parede.</li>
<li><b>Limpe</b> o excesso de cola e silicone antes de secar.</li>
</ol>

<h2>Parede de drywall</h2>
<p>Drywall sozinho não segura bancada suspensa. É preciso reforço dentro da parede (madeira ou perfil metálico) colocado antes do fechamento, ou um suporte que descarregue no chão. Combine isso com quem fez a parede antes de marcar a instalação.</p>

<h2>Não esqueça de cobrar</h2>
<p>Instalação tem custo de equipe, transporte, material e risco. Deixe no orçamento se está inclusa ou à parte, e o que fica por conta do cliente (hidráulica, elétrica, armário). Veja <a href="/dicas/como-fazer-orcamento-de-bancada-de-granito">como fazer orçamento de bancada</a>.</p>
''',
 ['como-medir-bancada-de-granito','como-colar-granito','espessura-de-granito-para-bancada','rodabanca-e-frontao'],
 'Transporte, tipos de apoio, nível, emendas, cuba e drywall.')

pg('nicho-de-granito-para-banheiro',
 'Nicho de Granito para Banheiro: medidas, altura e peças',
 'Nicho de granito para banheiro: medidas, altura e como montar',
 'Medidas comuns de nicho de banheiro em granito ou porcelanato, altura na parede, profundidade possível, peças que levam, prateleira, caimento e como cobrar.',
 'O nicho é uma caixa na parede do box para xampu e sabonete. Em pedra, ele é montado com várias peças pequenas, e por isso tem mais mão de obra do que a área sugere.',
 4,
 '''
<h2>Medidas comuns</h2>
<div class="tab"><table>
<tr><th>Medida</th><th>Faixa comum</th></tr>
<tr><td>Largura</td><td>30 a 60 cm (ou o vão todo entre paredes, no nicho corrido)</td></tr>
<tr><td>Altura</td><td>30 a 60 cm; com prateleira no meio, de 50 cm para cima</td></tr>
<tr><td>Profundidade</td><td>Depende da parede: em alvenaria comum, algo entre 7 e 10 cm</td></tr>
<tr><td>Altura do chão até a base</td><td>Perto de 1,00 a 1,20 m (o mais visto)</td></tr>
</table></div>
<p>São medidas de mercado, não obrigatórias. A profundidade é a parede que manda: sempre confirme com o pedreiro antes de cortar.</p>

<h2>Peças de um nicho</h2>
<ul>
<li><b>Base</b> (com leve caimento para fora, para a água não empoçar)</li>
<li><b>Teto</b></li>
<li><b>Duas laterais</b></li>
<li><b>Fundo</b> (às vezes fica no revestimento da parede)</li>
<li><b>Prateleira</b>, se tiver</li>
<li><b>Moldura / faixa da frente</b>, se o cliente quiser a borda em pedra</li>
</ul>
<p>Laterais e base em <a href="/dicas/meia-esquadria-em-granito">meia-esquadria</a> deixam o nicho com cara de peça única.</p>

<h2>Como montar</h2>
<ol>
<li>Receba a medida do vão já aberto e com reboco (ou com o revestimento definido).</li>
<li>Corte as peças descontando a espessura de cola.</li>
<li>Assente a base primeiro, com caimento, depois laterais, teto e fundo.</li>
<li>Vede as emendas com silicone ou massa na cor da pedra.</li>
</ol>

<h2>Como cobrar</h2>
<p>Muita marmoraria cobra o nicho por <b>unidade</b> (conforme o tamanho), porque o m² é pequeno e o trabalho é grande. Exemplo (só para ilustrar): nicho 60 × 30 × 10 cm com prateleira, R$ 280,00 a unidade. Se o nicho tem meia-esquadria, cobre a mais.</p>
''',
 ['meia-esquadria-em-granito','cuba-esculpida-em-granito','soleira-e-peitoril-de-granito','como-colar-granito'],
 'Medidas comuns, altura, peças, montagem e cobrança por unidade.')

pg('soleira-e-peitoril-de-granito',
 'Soleira e Peitoril de Granito: medidas, pingadeira e preço',
 'Soleira e peitoril de granito: medidas, pingadeira e como cobrar',
 'Como medir soleira de porta e peitoril de janela em granito, larguras comuns, pingadeira, caimento, acabamento das pontas e como cobrar por peça ou metro linear.',
 'Soleira e peitoril são peças simples, mas aparecem em quase toda obra e em quantidade. Medida certa, pingadeira no peitoril e preço por peça bem feito fazem diferença no fim do mês.',
 4,
 '''
<h2>Diferença</h2>
<ul>
<li><b>Soleira</b>: pedra no chão, na passagem da porta. Separa pisos e segura a água do banheiro ou da área externa.</li>
<li><b>Peitoril</b>: pedra embaixo da janela, por fora (e às vezes por dentro). Joga a água da chuva para longe da parede.</li>
</ul>

<h2>Como medir</h2>
<ol>
<li><b>Comprimento</b>: o vão da porta ou da janela. No peitoril, some o que entra na parede de cada lado (as "orelhas", muitas vezes 2 a 3 cm por lado).</li>
<li><b>Largura</b>: a espessura da parede pronta (com reboco). No peitoril, some a sobra para fora da parede (aba).</li>
<li>Anote se a soleira tem desnível (degrauzinho) ou rebaixo para o box.</li>
</ol>
<p>Larguras comuns de soleira ficam perto de 14 a 20 cm, conforme a parede; porta interna mais vista tem vão de 60 a 90 cm. Sempre confira na obra.</p>

<h2>Pingadeira e caimento do peitoril</h2>
<p>A <b>pingadeira</b> é um sulco (friso) feito por baixo da aba do peitoril, perto da borda. A gota de água que escorre por baixo cai ali e não volta para a parede, o que evita a mancha escura embaixo da janela. Além dela, o peitoril vai assentado com <b>leve caimento para fora</b>.</p>

<h2>Acabamento</h2>
<ul>
<li>Borda da frente polida e boleada ou reta, conforme o pedido.</li>
<li>Pontas: polidas quando aparecem; brutas quando entram na parede.</li>
<li>Soleira no mesmo nível do piso, ou com pequeno degrau quando separa área molhada.</li>
</ul>

<h2>Como cobrar</h2>
<p>Soleira e peitoril costumam ser cobrados <b>por peça</b> (para tamanhos comuns) ou <b>por metro linear</b>, com a pingadeira e o polimento de ponta somados. Exemplo (só para ilustrar):</p>
<ul>
<li>Soleira 80 × 15 cm: R$ 70,00 a peça</li>
<li>Peitoril 1,20 m × 18 cm com pingadeira: 1,20 × R$ 90,00 = R$ 108,00</li>
</ul>
<p>Com muitas soleiras numa obra, dá para tirar todas dos <a href="/dicas/plano-de-corte-de-chapa-de-granito">retalhos e sobras da chapa</a>.</p>
''',
 ['plano-de-corte-de-chapa-de-granito','espessura-de-granito-para-bancada','nicho-de-granito-para-banheiro','como-calcular-metro-quadrado-de-granito'],
 'Medidas, pingadeira, caimento, acabamento e cobrança por peça.')

pg('como-colar-granito',
 'Como Colar Granito: qual cola usar em cada emenda',
 'Como colar granito: qual cola usar em cada emenda',
 'Qual cola usar no granito: massa plástica, adesivo epóxi, PU e silicone. Como colar saia, emendar bancada em L, colar pedra quebrada e dar o tom da cor da pedra.',
 'Na marmoraria, cada emenda pede um produto. Saia, emenda de L, cuba, pedra quebrada e rodabanca não se colam do mesmo jeito. Veja qual usar e o passo a passo.',
 5,
 '''
<h2>Qual produto para cada caso</h2>
<div class="tab"><table>
<tr><th>Produto</th><th>Melhor uso</th><th>Observação</th></tr>
<tr><td>Massa plástica / cola para mármore e granito (poliéster)</td><td>Saia, meia-esquadria, emendas, pequenos reparos</td><td>Seca rápido; aceita pigmento para pegar a cor da pedra</td></tr>
<tr><td>Adesivo epóxi para pedra</td><td>Emendas que pedem mais força, cuba, área externa, pedra quebrada</td><td>Mais resistente; tempo de cura maior</td></tr>
<tr><td>Adesivo PU / selante</td><td>Fixar pedra em parede, base ou metal</td><td>Fica flexível; não é para emenda à vista</td></tr>
<tr><td>Silicone neutro</td><td>Vedar rodabanca, cuba de sobrepor, junta com parede</td><td>Veda, não cola peça estrutural</td></tr>
<tr><td>Argamassa</td><td>Assentar soleira, piso, frontão, peitoril</td><td>Siga a indicação do fabricante para pedra</td></tr>
</table></div>
<p>Use sempre o que o fabricante do produto indica para pedra natural, e prefira silicone <b>neutro</b>: o acético pode manchar algumas pedras.</p>

<h2>Passo a passo de uma emenda</h2>
<ol>
<li><b>Limpe e seque</b> as duas faces. Pó e água atrapalham a cola.</li>
<li><b>Lixe</b> de leve as faces que vão se encontrar, para a cola agarrar.</li>
<li><b>Tinja a massa</b> com pigmento até chegar perto da cor da pedra. Teste num cantinho.</li>
<li><b>Misture com o catalisador</b> na quantidade da embalagem. Catalisador demais dá trinca e escurece.</li>
<li><b>Aplique, una e prenda</b> com grampo, sargento ou ventosa de nivelar.</li>
<li><b>Nivele as faces</b> antes de endurecer e tire o excesso.</li>
<li>Depois de seco, <b>lixe e dê polimento</b> na emenda.</li>
</ol>

<h2>Emenda de bancada em L e U</h2>
<p>Use ventosas de nivelamento (emendador) para as duas peças ficarem no mesmo plano, deixe a junta bem fina e reforce por baixo quando a emenda passa sobre vão sem apoio.</p>

<h2>Pedra quebrada</h2>
<p>Dá para colar uma pedra que trincou ou quebrou, com adesivo epóxi e reforço por baixo, mas a emenda vai aparecer. Em peça grande e à vista, avise o cliente ou troque a peça.</p>
''',
 ['meia-esquadria-em-granito','saia-de-granito','como-instalar-bancada-de-granito','cuba-esculpida-em-granito'],
 'Massa, epóxi, PU ou silicone; passo a passo de emenda e pedra quebrada.')

pg('granito-ou-quartzo',
 'Granito ou Quartzo: diferenças para explicar ao cliente',
 'Granito ou quartzo: as diferenças para explicar ao cliente',
 'Diferenças entre granito, quartzo e mármore para o marmorista explicar ao cliente: origem, mancha, calor, cor uniforme, emenda, tamanho de chapa e o que muda no orçamento.',
 'Granito ou quartzo é uma das dúvidas que o cliente mais traz para a marmoraria. Quem explica bem, com calma e sem empurrar, fecha mais. Aqui estão as diferenças práticas, sem marca.',
 5,
 '''
<h2>O que é cada um</h2>
<ul>
<li><b>Granito</b>: pedra natural, cortada direto do bloco da pedreira. Cada chapa é diferente.</li>
<li><b>Quartzo (industrializado)</b>: pedra feita em fábrica, com grãos de quartzo unidos por resina. A cor é uniforme e se repete.</li>
<li><b>Mármore</b>: pedra natural mais macia e mais sensível a ácido (limão, vinagre).</li>
</ul>

<h2>Comparação prática</h2>
<div class="tab"><table>
<tr><th>Ponto</th><th>Granito</th><th>Quartzo</th></tr>
<tr><td>Aparência</td><td>Desenho natural, cada chapa única</td><td>Cor uniforme, bom para branco liso</td></tr>
<tr><td>Mancha</td><td>Depende da pedra; as claras e porosas mancham mais e podem pedir impermeabilizante</td><td>Pouco poroso, mancha menos no uso do dia a dia</td></tr>
<tr><td>Calor</td><td>Aguenta bem panela quente</td><td>A resina não gosta de calor direto: use descanso de panela</td></tr>
<tr><td>Sol (área externa)</td><td>Vai bem</td><td>Muitos fabricantes não indicam para sol direto</td></tr>
<tr><td>Emenda</td><td>Some menos em pedra com muito desenho</td><td>Fica fácil de disfarçar pela cor lisa</td></tr>
<tr><td>Chapa</td><td>Tamanho varia por bloco</td><td>Tamanho fixo de fábrica</td></tr>
<tr><td>Preço</td><td>Varia muito: há opções bem em conta e pedras caras</td><td>Costuma ficar na faixa média-alta</td></tr>
</table></div>
<p>Confirme sempre as recomendações do fabricante do quartzo e do fornecedor da pedra que você vai usar.</p>

<h2>Como explicar sem perder a venda</h2>
<ol>
<li>Pergunte o uso: cozinha muito usada, churrasqueira, área externa ou banheiro?</li>
<li>Mostre duas ou três opções lado a lado no mesmo projeto, com o preço de cada uma.</li>
<li>Deixe por escrito os cuidados (descanso de panela no quartzo, impermeabilizante no granito claro).</li>
</ol>

<h2>O que muda no orçamento</h2>
<p>Além do m², muda o <b>aproveitamento da chapa</b> (o quartzo tem tamanho fixo e pode exigir emenda diferente) e o tempo de corte. Monte o orçamento das duas pedras para o cliente comparar; a conta está em <a href="/dicas/como-fazer-orcamento-de-bancada-de-granito">como fazer orçamento de bancada</a> e o encaixe em <a href="/dicas/tamanho-de-chapa-de-granito">tamanho de chapa</a>.</p>
''',
 ['tamanho-de-chapa-de-granito','espessura-de-granito-para-bancada','como-fazer-orcamento-de-bancada-de-granito','calculadora-orcamento-bancada-granito'],
 'Granito, quartzo e mármore: mancha, calor, chapa e orçamento.')

pg('como-abrir-uma-marmoraria',
 'Como Abrir uma Marmoraria: passo a passo para começar',
 'Como abrir uma marmoraria: passo a passo para começar',
 'O que precisa para abrir uma marmoraria: modelo de negócio, local, máquinas, documentos, fornecedores de chapa, formação de preço, captação de clientes e controle.',
 'Abrir marmoraria pede mais do que saber cortar pedra: precisa de lugar certo, máquinas, fornecedor, preço bem feito e cliente chegando. Este é o roteiro para planejar, sem números inventados.',
 6,
 '''
<h2>1. Escolha o modelo</h2>
<ul>
<li><b>Marmorista autônomo</b>: começa com ferramentas manuais, terceiriza cortes grandes e atende obras pequenas.</li>
<li><b>Marmoraria de bairro</b>: galpão próprio, máquinas básicas, bancadas, soleiras e lavatórios.</li>
<li><b>Marmoraria com máquina automática</b> (CNC, serra-ponte de controle): mais produção, mais investimento.</li>
</ul>
<p>O investimento muda muito de um modelo para outro e de uma cidade para outra. Faça a conta com orçamentos reais de máquinas e aluguel da sua região.</p>

<h2>2. Local e estrutura</h2>
<ul>
<li>Galpão com pé-direito e piso para chapa e cavalete, entrada para caminhão</li>
<li>Água para os cortes e sistema para a lama (decantação) — confira as regras ambientais da prefeitura</li>
<li>Energia adequada às máquinas</li>
<li>Área de estoque para chapas (em pé, em cavalete) e para retalhos</li>
</ul>

<h2>3. Máquinas e ferramentas de começo</h2>
<p>Serra (manual ou ponte), lixadeiras e politrizes, esmerilhadeiras com discos diamantados, furadeira com serra-copo, máquina de meia-esquadria, ventosas, grampos, nível, trena a laser e EPI (máscara para poeira de sílica, protetor auricular, óculos e luvas). A poeira da pedra faz mal: corte sempre com água e use máscara própria.</p>

<h2>4. Documentos</h2>
<p>Abra a empresa (veja com um contador se cabe como MEI ou se precisa de outro enquadramento, conforme a atividade e o faturamento), alvará da prefeitura, licença ambiental quando exigida e as regras de segurança do trabalho para funcionários.</p>

<h2>5. Fornecedores</h2>
<p>Tenha pelo menos dois fornecedores de chapa, um de cubas e insumos (cola, discos, silicone) e combine prazo de entrega e frete. Aprenda a <a href="/dicas/tamanho-de-chapa-de-granito">medir a chapa útil</a> na compra.</p>

<h2>6. Preço que dá lucro</h2>
<p>Some custo da chapa (inteira, não só o que vai na obra), perda, mão de obra, insumos, frete, instalação, impostos e sua margem. Veja <a href="/dicas/como-fazer-orcamento-de-bancada-de-granito">como fazer orçamento de bancada</a> e use a <a href="/dicas/calculadora-orcamento-bancada-granito">calculadora</a> para treinar.</p>

<h2>7. Cliente chegando</h2>
<ul>
<li>Perfil no Google (Google Meu Negócio) com fotos de obras prontas: é ali que o cliente procura "marmoraria perto de mim"</li>
<li>Instagram e WhatsApp com antes e depois</li>
<li>Parceria com arquitetos, construtoras, marceneiros e lojas de cuba</li>
<li>Orçamento rápido e bonito: quem responde primeiro, com desenho, fecha mais</li>
</ul>

<h2>8. Controle desde o primeiro dia</h2>
<p>Anote cada orçamento, obra, chapa e retalho. Sem isso, não dá para saber qual serviço dá lucro e quanto de pedra fica parada no pátio.</p>
''',
 ['como-fazer-orcamento-de-bancada-de-granito','plano-de-corte-de-chapa-de-granito','tamanho-de-chapa-de-granito','calculadora-orcamento-bancada-granito'],
 'Modelo, local, máquinas, documentos, fornecedor, preço e clientes.')

pg('escada-de-granito-medidas',
 'Escada de Granito: medidas do degrau, espelho, bocel e conta',
 'Escada de granito: medidas do degrau, espelho, bocel e como fazer a conta',
 'Medida de piso e espelho de escada de granito, fórmula de Blondel, quantos degraus vai numa escada, bocel, antiderrapante, qual granito usar e como calcular o m² da pedra.',
 'Escada boa de subir tem degrau na medida certa. Aqui está a conta que o marmorista faz na obra: quantos degraus, altura do espelho, profundidade do piso, bocel e quanto de pedra comprar.',
 6,
 '''
<h2>As partes da escada em pedra</h2>
<ul>
<li><b>Piso</b>: a peça onde se pisa (também chamada de degrau ou pisada).</li>
<li><b>Espelho</b>: a peça em pé, entre um piso e outro. Escada "sem espelho" (vazada) só tem o piso.</li>
<li><b>Bocel</b>: a frente do piso que avança um pouco sobre o espelho, normalmente com a quina boleada.</li>
<li><b>Patamar</b>: o piso maior onde a escada faz a curva ou o descanso.</li>
<li><b>Rodapé da escada</b>: a faixa de pedra na parede, acompanhando os degraus.</li>
</ul>

<h2>Medida do degrau: piso e espelho</h2>
<p>A referência mais usada no Brasil é a da norma de acessibilidade (NBR 9050) para escadas de uso comum: <b>espelho de 16 a 18 cm</b> e <b>piso de 28 a 32 cm</b>. Para conferir se o degrau fica confortável, use a <b>fórmula de Blondel</b>:</p>
<div class="box au"><b>2 × espelho + piso = 63 a 65 cm</b><br>Ex.: espelho de 17,5 cm e piso de 28 cm → 2 × 17,5 + 28 = 63 cm. Está dentro.</div>
<p>Em casa, a escada às vezes sai fora disso por falta de espaço. Avise o cliente por escrito quando o degrau ficar alto ou curto demais. Confira também o código de obras da sua cidade e o projeto do arquiteto.</p>

<h2>Quantos degraus vai numa escada</h2>
<ol>
<li><b>Meça a altura total</b>, do piso de baixo pronto até o piso de cima pronto (não do contrapiso). Ex.: 2,80 m.</li>
<li><b>Divida pela altura de espelho que você quer</b>: 280 ÷ 17,5 = 16. São <b>16 espelhos</b>.</li>
<li>Se der número quebrado, arredonde e divida de novo: 280 ÷ 16 = 17,5 cm cada espelho, todos iguais.</li>
<li><b>Pisos = espelhos − 1</b> (o último "degrau" é o próprio piso de cima). Aqui: <b>15 pisos</b>.</li>
<li><b>Comprimento da escada</b> = pisos × profundidade do piso: 15 × 28 = 4,20 m de projeção no chão.</li>
</ol>
<div class="tab"><table>
<tr><th>Altura total</th><th>Espelhos</th><th>Espelho (cm)</th><th>Pisos</th></tr>
<tr><td>1,00 m</td><td>6</td><td>16,7</td><td>5</td></tr>
<tr><td>2,60 m</td><td>15</td><td>17,3</td><td>14</td></tr>
<tr><td>2,80 m</td><td>16</td><td>17,5</td><td>15</td></tr>
<tr><td>3,00 m</td><td>17</td><td>17,6</td><td>16</td></tr>
</table></div>
<p>Degrau com altura diferente dos outros é o que mais faz gente tropeçar. Se o contrapiso estiver torto, corrija na massa, não no tamanho do espelho.</p>

<h2>Bocel e espessura da pedra</h2>
<ul>
<li>O bocel costuma avançar <b>de 1,5 a 3 cm</b> sobre o espelho. Some esse avanço na profundidade da peça do piso: piso de 28 cm + 2 cm de bocel = peça de 30 cm.</li>
<li>Para o piso, a espessura mais vista é 2 cm. Em escada de uso pesado ou com bocel engrossado, cola-se uma tira embaixo da frente (fica com cara de 4 cm). Veja <a href="/dicas/espessura-de-granito-para-bancada">espessura do granito</a>.</li>
<li>O espelho entra <b>entre</b> os pisos: a altura da peça do espelho é a altura do degrau menos a espessura do piso. Ex.: 17,5 − 2 = 15,5 cm.</li>
</ul>

<h2>Escada de granito escorrega?</h2>
<p>Granito <b>polido</b> molhado escorrega, principalmente em área externa e escada de piscina. Opções que o marmorista oferece:</p>
<ul>
<li><b>Flameado ou apicoado</b>: superfície áspera, boa para área externa.</li>
<li><b>Levigado</b>: fosco, menos liso que o polido.</li>
<li><b>Frisos antiderrapantes</b> fresados no bocel, ou fita antiderrapante.</li>
</ul>

<h2>Qual granito usar na escada</h2>
<p>As buscas mais comuns são por preto São Gabriel, branco Siena, verde Ubatuba e bege Bahia. Na escolha, pense em três coisas: <b>sujeira</b> (pedra clara mostra mais o pé sujo), <b>sol e água</b> (área externa pede acabamento áspero) e <b>emenda</b> (pedra com muito desenho esconde melhor as diferenças entre degraus). Mármore é mais macio e risca mais com a areia do sapato; em escada de muito uso, o granito costuma ser a escolha.</p>

<h2>Como fazer a conta da pedra</h2>
<p>Exemplo da escada de 2,80 m com 1,00 m de largura (medidas só para ilustrar):</p>
<div class="tab"><table>
<tr><th>Peça</th><th>Conta</th><th>m²</th></tr>
<tr><td>15 pisos de 1,00 × 0,30 m</td><td>15 × 1,00 × 0,30</td><td>4,50</td></tr>
<tr><td>16 espelhos de 1,00 × 0,155 m</td><td>16 × 1,00 × 0,155</td><td>2,48</td></tr>
<tr><td><b>Total de pedra</b></td><td></td><td><b>6,98</b></td></tr>
</table></div>
<p>Depois some a <b>perda</b> de corte e o encaixe na chapa (veja <a href="/dicas/plano-de-corte-de-chapa-de-granito">plano de corte</a>), o bocel por metro linear (15 × 1,00 = 15 m) e a instalação. A conta do m² está em <a href="/dicas/como-calcular-metro-quadrado-de-granito">como calcular o metro quadrado de granito</a>.</p>

<h2>Quanto custa uma escada de granito</h2>
<p>Não existe preço único: muda com a pedra, o número de degraus, o bocel, o antiderrapante, o patamar e a cidade. Monte o preço assim: <b>m² de pedra (com perda) × preço da pedra + metro linear de bocel + rodapé + instalação</b>. Para o cliente comparar, mostre duas pedras no mesmo projeto.</p>
''',
 ['tipos-de-acabamento-de-borda-de-granito','soleira-e-peitoril-de-granito','como-calcular-metro-quadrado-de-granito','plano-de-corte-de-chapa-de-granito'],
 'Piso, espelho, Blondel, quantos degraus, bocel e conta da pedra.',
 data='2026-11-24')

pg('tipos-de-acabamento-de-borda-de-granito',
 'Tipos de Acabamento de Borda de Granito: reto, boleado, meia-cana, chanfrado',
 'Tipos de acabamento de borda de granito: reto, boleado, meia-cana, chanfrado e bisotê',
 'Os acabamentos de borda (filete) do granito: reto simples, reto engrossado, meio-boleado, boleado, meia-cana, chanfrado, bisotê, francesa e slim. Onde usar cada um e como cobrar por metro linear.',
 'A borda é a parte da pedra que o cliente mais vê e mais toca. Saber mostrar as opções, com nome e desenho, evita briga na entrega e ajuda a vender um acabamento melhor.',
 5,
 '''
<h2>Borda não é o mesmo que acabamento da superfície</h2>
<p>Quando o cliente pergunta "qual o acabamento do granito", ele pode estar falando de duas coisas:</p>
<ul>
<li><b>Acabamento da superfície</b> (o tampo todo): polido (brilho), levigado (fosco), flameado ou apicoado (áspero, para área externa), escovado.</li>
<li><b>Acabamento da borda</b> (o filete, a frente da peça): reto, boleado, chanfrado etc. É o assunto desta página.</li>
</ul>

<h2>Os tipos de borda</h2>
<div class="tab"><table>
<tr><th>Borda</th><th>Como é</th><th>Onde vai bem</th></tr>
<tr><td><b>Reto simples</b></td><td>Frente reta e polida, quinas levemente quebradas</td><td>Bancada moderna, a mais pedida</td></tr>
<tr><td><b>Reto engrossado</b> (duplo)</td><td>Cola uma tira embaixo da frente; a borda parece ter 4 cm ou mais</td><td>Cozinha, ilha, quem quer pedra "grossa" sem pagar chapa grossa</td></tr>
<tr><td><b>Meio-boleado</b></td><td>Só a quina de cima arredondada</td><td>Banheiro, bancada com criança, peitoril</td></tr>
<tr><td><b>Boleado</b> (inteiro)</td><td>Frente toda arredondada, em meia-lua</td><td>Soleira, degrau, bocel, mesa</td></tr>
<tr><td><b>Boleado duplo</b></td><td>Boleado na peça engrossada (cima e baixo)</td><td>Mesa, balcão clássico</td></tr>
<tr><td><b>Meia-cana</b></td><td>Perfil curvo feito com fresa de meia-cana</td><td>Peças clássicas, degrau, borda de piscina</td></tr>
<tr><td><b>Chanfrado</b></td><td>Quina cortada em pequeno ângulo (45°)</td><td>Bancada reta que não pode ficar cortante</td></tr>
<tr><td><b>Bisotê</b></td><td>Chanfro largo e inclinado na face de cima</td><td>Mesa, tampo de móvel</td></tr>
<tr><td><b>Francesa</b> (perfil ogee)</td><td>Curva em "S" trabalhada</td><td>Estilo clássico, lavatório e mesa</td></tr>
<tr><td><b>Slim</b></td><td>Borda bem fina, a pedra parece delicada</td><td>Projeto moderno, banheiro</td></tr>
</table></div>
<div class="box au"><b>Atenção aos nomes</b><br>Meia-cana, boleado e bisotê mudam de nome de região para região. Antes de fechar, mostre ao cliente o <b>desenho ou uma amostra</b> e escreva o nome no orçamento.</div>

<h2>E a meia-esquadria?</h2>
<p>Meia-esquadria não é desenho de borda: é o <b>encontro a 45°</b> do tampo com a saia, que dá a impressão de pedra maciça. Ela pode ser combinada com uma quina chanfrada ou levemente boleada. Veja <a href="/dicas/meia-esquadria-em-granito">meia-esquadria em granito</a> e <a href="/dicas/saia-de-granito">saia de granito</a>.</p>

<h2>Qual o nome do acabamento da pia?</h2>
<p>Em pia de cozinha, os mais vistos são o <b>reto simples</b> (com quina quebrada), o <b>reto engrossado</b> e a <b>saia em meia-esquadria</b>. Em pia de banheiro, entram também o meio-boleado e o slim. Pergunte ao cliente se a bancada vai ter saia e de qual altura, porque isso muda o acabamento da frente.</p>

<h2>Como fazer a borda sem estragar a peça</h2>
<ol>
<li>Marque na peça quais lados levam acabamento (frente, laterais à vista). Lado encostado na parede fica reto bruto.</li>
<li>Faça o perfil com a fresa ou o rebolo certo, sempre com água.</li>
<li>Passe as lixas na sequência, da mais grossa para a mais fina, até o polimento igualar com o tampo.</li>
<li>Em pedra escura, confira o brilho contra a luz: borda opaca aparece muito.</li>
</ol>

<h2>Como cobrar o acabamento de borda</h2>
<p>O mais comum é cobrar <b>por metro linear</b> de borda trabalhada, com preço diferente para cada tipo (reto simples mais barato; francesa e boleado duplo mais caros). Exemplo só para ilustrar (use os seus valores):</p>
<div class="tab"><table>
<tr><th>Item</th><th>Conta</th><th>Valor</th></tr>
<tr><td>Borda reta simples na frente</td><td>2,20 m × R$ 25,00</td><td>R$ 55,00</td></tr>
<tr><td>Engrossamento da frente</td><td>2,20 m × R$ 45,00</td><td>R$ 99,00</td></tr>
<tr><td>Lateral à vista</td><td>0,60 m × R$ 25,00</td><td>R$ 15,00</td></tr>
<tr><td><b>Total da borda</b></td><td></td><td><b>R$ 169,00</b></td></tr>
</table></div>
<p>A pedra do engrossamento também entra na conta do m² ou do metro linear. O passo a passo do orçamento está em <a href="/dicas/como-fazer-orcamento-de-bancada-de-granito">como fazer orçamento de bancada de granito</a>.</p>
''',
 ['meia-esquadria-em-granito','saia-de-granito','escada-de-granito-medidas','como-fazer-orcamento-de-bancada-de-granito'],
 'Reto, engrossado, boleado, meia-cana, chanfrado, bisotê e como cobrar.',
 data='2026-11-24')

pg('como-polir-granito',
 'Como Polir Granito: lixas, passo a passo e como devolver o brilho',
 'Como polir granito: sequência de lixas, passo a passo e como devolver o brilho',
 'Como polir granito na marmoraria e na obra: sequência de lixas (grana 50 a 3000), lixadeira ou politriz com água, lustro final, granito preto, manual ou com furadeira, e o que fazer quando o brilho some.',
 'Polir é tirar os riscos da pedra em etapas, de lixa grossa para lixa fina, até a superfície refletir a luz. Quem pula etapa vê o risco aparecer depois, principalmente no granito preto.',
 6,
 '''
<h2>O que é usado para polir granito</h2>
<ul>
<li><b>Politriz ou lixadeira angular de velocidade variável</b> com alimentação de água (ou borrifador). Lixadeira de rotação fixa alta esquenta e mancha a pedra.</li>
<li><b>Lixas diamantadas flexíveis (pads)</b> com velcro, em sequência de grana. Para o polimento a água, as mais usadas vão de 50 a 3000.</li>
<li><b>Suporte (prato) de borracha</b> para o velcro.</li>
<li><b>Pó ou pasta de polimento</b> e boina de feltro para o brilho final (opcional, dá o "lustro").</li>
<li><b>Impermeabilizante</b> para depois, se a pedra for porosa.</li>
<li>Óculos, máscara, protetor auricular e luva. Com água e máquina elétrica, use tomada com DR e extensão sem emenda no chão molhado.</li>
</ul>

<h2>Qual lixa se usa para polir granito (sequência)</h2>
<p>Cada lixa tira o risco da anterior. Comece pela grana que corresponde ao estrago e não pule mais de uma etapa.</p>
<div class="tab"><table>
<tr><th>Grana</th><th>Para quê</th><th>Quando começar por ela</th></tr>
<tr><td>50</td><td>Desbaste: tira dente de serra, degrau, lasca</td><td>Borda recém-cortada, emenda desnivelada</td></tr>
<tr><td>100</td><td>Acerta o desbaste</td><td>Risco fundo, marca de disco</td></tr>
<tr><td>200</td><td>Tira o risco da 100</td><td>Risco médio</td></tr>
<tr><td>400</td><td>Começa a fechar a pedra</td><td>Pedra fosca, risco leve</td></tr>
<tr><td>800</td><td>Superfície lisa, ainda fosca (levigado)</td><td>Só perdeu o brilho</td></tr>
<tr><td>1500</td><td>Começa a refletir</td><td>Brilho fraco</td></tr>
<tr><td>3000</td><td>Brilho final</td><td>Retoque de brilho</td></tr>
</table></div>
<div class="box au"><b>Os números mudam de marca para marca</b><br>Algumas linhas vão até 3000, outras terminam numa lixa "buff" preta. Siga a ordem que o fabricante das suas lixas indica.</div>

<h2>Passo a passo do polimento</h2>
<ol>
<li><b>Limpe e olhe com luz rasante</b> (lanterna de lado). Marque com lápis o que precisa sair: risco, degrau de emenda, mancha de cola.</li>
<li><b>Escolha a lixa de início</b> pela tabela. Borda cortada começa na 50; só perda de brilho começa na 800.</li>
<li><b>Lixe com água sempre</b>, com a máquina em rotação baixa a média (siga a rotação que o fabricante das lixas indica), sem fazer força: o peso da máquina basta.</li>
<li><b>Movimento em cruz</b>: passe num sentido e depois no outro, cobrindo toda a área. Não pare a máquina num ponto só, senão vira "panela" (afundado).</li>
<li><b>Lave e seque entre uma lixa e outra</b>. Olhe na luz: se ainda tem risco da lixa anterior, volte uma etapa.</li>
<li><b>Siga até a última grana</b> e, se quiser mais brilho, passe pó de polimento com boina de feltro.</li>
<li><b>Lave bem</b>, deixe secar e aplique impermeabilizante se a pedra pedir (granito claro e poroso costuma pedir).</li>
</ol>

<h2>Como polir a borda (filete)</h2>
<p>É onde o marmorista mais pole na obra: depois de um corte ou de um ajuste de recorte. Mantenha a máquina reta em relação à borda, quebre a quina com a lixa (sem deixar cortante) e iguale o brilho com o do tampo. Para os tipos de borda, veja <a href="/dicas/tipos-de-acabamento-de-borda-de-granito">acabamento de borda</a>.</p>

<h2>Como polir granito manualmente ou com furadeira</h2>
<ul>
<li><b>À mão</b>: dá para fazer retoque pequeno (uma quina, um risquinho) com lixa d'água ou diamantada num taco de madeira, com água, seguindo a mesma sequência. Numa bancada inteira, à mão não iguala o brilho.</li>
<li><b>Com furadeira</b>: existe adaptador de velcro, mas a furadeira não tem água e cansa o motor. Serve para retoque, não para tampo inteiro.</li>
</ul>

<h2>Granito preto (São Gabriel, Absoluto): cuidados</h2>
<ul>
<li>Preto mostra qualquer risco e qualquer diferença de brilho. Não pule lixa.</li>
<li>Na última etapa, confira o reflexo com uma lâmpada: a imagem tem que sair nítida, sem "nuvem".</li>
<li>Se a pedra foi resinada ou tingida na fábrica, polir fundo pode clarear a região. Teste num canto e confira com o fornecedor.</li>
</ul>

<h2>O que passar no granito para voltar o brilho</h2>
<p>Depende do motivo da perda de brilho:</p>
<div class="tab"><table>
<tr><th>O cliente vê</th><th>Causa mais comum</th><th>O que fazer</th></tr>
<tr><td>Fosco só onde se limpa</td><td>Produto ácido, sapólio, palha de aço</td><td>Polimento a partir da 800 ou 1500</td></tr>
<tr><td>Mancha escura de óleo</td><td>Pedra porosa sem impermeabilizante</td><td>Tirar a mancha e impermeabilizar (polir não resolve)</td></tr>
<tr><td>Risco que pega a unha</td><td>Panela, faca, areia</td><td>Começar na 200 ou 400</td></tr>
<tr><td>Brilho apagado no geral</td><td>Desgaste natural</td><td>Lustro com pó de polimento</td></tr>
</table></div>
<p>"Cera" e lustra-móveis dão brilho por uns dias e depois deixam a pedra engordurada. Oriente o cliente a limpar com detergente neutro e pano macio.</p>

<h2>Quanto cobrar pelo polimento</h2>
<p>Polimento de tampo costuma ser cobrado por m² e o de borda por metro linear, com uma visita mínima. O preço muda com a grana de início (desbaste custa mais), a cor da pedra e o acesso. Monte o seu valor pelo tempo de máquina, o gasto de lixa e a ida até a obra. Para o restante do orçamento, veja <a href="/dicas/como-fazer-orcamento-de-bancada-de-granito">como fazer orçamento de bancada</a>.</p>
''',
 ['tipos-de-acabamento-de-borda-de-granito','como-colar-granito','granito-ou-quartzo','como-instalar-bancada-de-granito'],
 'Sequência de lixas, passo a passo, borda, preto e volta do brilho.',
 data='2026-11-25')

pg('bancada-de-churrasqueira-em-granito',
 'Bancada de Churrasqueira em Granito: medidas, altura e como orçar',
 'Bancada de churrasqueira em granito: medidas, altura, pia e como fazer o orçamento',
 'Medidas da bancada de churrasqueira em granito: altura, profundidade, comprimento, bancada em L, pia, cooktop, revestimento da churrasqueira com granito, qual pedra aguenta calor e como orçar.',
 'A bancada da área de churrasco é um dos pedidos que mais chegam na marmoraria. Tem tampo, pia, às vezes cooktop, revestimento da churrasqueira e muita peça pequena: medida errada aparece no orçamento.',
 6,
 '''
<h2>As peças de uma área de churrasco</h2>
<ul>
<li><b>Tampo da bancada</b> (reta, em L ou em U), muitas vezes com <b>pia</b> e às vezes com <b>cooktop</b>.</li>
<li><b>Rodabanca</b> ou frontão na parede (veja <a href="/dicas/rodabanca-e-frontao">rodabanca e frontão</a>).</li>
<li><b>Saia</b> na frente do tampo (veja <a href="/dicas/saia-de-granito">saia de granito</a>).</li>
<li><b>Revestimento da churrasqueira</b>: a frente, a base de apoio do carvão e, às vezes, a coifa.</li>
<li><b>Balcão de apoio</b> do outro lado, para servir.</li>
</ul>

<h2>Medidas mais vistas</h2>
<p>Não há medida obrigatória. Estas faixas são as mais comuns em projetos de área gourmet e servem de ponto de partida:</p>
<div class="tab"><table>
<tr><th>Medida</th><th>Faixa comum</th><th>Observação</th></tr>
<tr><td>Altura do tampo (pronto)</td><td>90 a 95 cm</td><td>Igual à bancada da cozinha; pessoa alta pede mais</td></tr>
<tr><td>Profundidade do tampo</td><td>55 a 65 cm</td><td>Com pia, 60 cm é o mais visto</td></tr>
<tr><td>Bancada livre ao lado da churrasqueira</td><td>60 a 80 cm ou mais</td><td>Lugar para tábua e travessa</td></tr>
<tr><td>Balcão para sentar</td><td>105 a 110 cm de altura</td><td>Banqueta alta; avanço de 25 a 30 cm</td></tr>
</table></div>
<p>A altura da base do carvão depende do modelo da churrasqueira (pré-moldada ou de alvenaria): confira com o fabricante ou com o pedreiro antes de cortar o revestimento.</p>

<h2>Qual a altura ideal da bancada da churrasqueira</h2>
<p>Uma regra prática usada em cozinha é deixar o tampo uns <b>10 a 15 cm abaixo do cotovelo</b> de quem mais usa. Ex.: pessoa de 1,60 m costuma ficar bem com 85 a 90 cm; pessoa de 1,80 m, com 95 a 100 cm. Se o cliente não souber, use 90 cm e anote no orçamento.</p>

<h2>Bancada em L com churrasqueira</h2>
<ul>
<li>A churrasqueira costuma ficar numa ponta ou no canto; a pia fica na outra perna do L, longe da brasa.</li>
<li>No canto do L, decida a <b>emenda</b>: em 45° (diagonal) ou reta. Em pedra com veio, desenhe a emenda junto com o cliente.</li>
<li>Peça de L inteira raramente cabe na chapa: confira o <a href="/dicas/tamanho-de-chapa-de-granito">tamanho da chapa</a> antes de prometer "sem emenda".</li>
</ul>

<h2>Pia e cooktop na bancada do churrasco</h2>
<ul>
<li><b>Pia</b>: cuba de embutir ou de sobrepor (veja <a href="/dicas/cuba-de-embutir-sobrepor-ou-apoio">qual cuba escolher</a>). Deixe a torneira longe da brasa.</li>
<li><b>Cooktop</b>: o recorte segue o gabarito do fabricante; deixe pedra suficiente na frente e no fundo. Detalhes em <a href="/dicas/recorte-de-cooktop-no-granito">recorte de cooktop</a>.</li>
</ul>

<h2>Revestir a churrasqueira com granito</h2>
<p>É comum revestir a frente e a base da churrasqueira pré-moldada ou de alvenaria com a mesma pedra da bancada.</p>
<ol>
<li><b>Por fora</b> (frente, laterais, testeira): granito colado com argamassa ou adesivo próprio para pedra e para calor. Confira com o fabricante a temperatura que o produto aguenta.</li>
<li><b>Por dentro</b>, onde o fogo encosta: o mais visto é tijolo refratário. Pedra em contato direto com a brasa pode trincar por choque térmico; se o cliente pedir granito por dentro, avise o risco por escrito.</li>
<li>Deixe uma <b>junta</b> entre a pedra e a parte que esquenta mais, para a pedra não forçar quando dilatar.</li>
</ol>

<h2>Qual granito usar na churrasqueira</h2>
<ul>
<li>Granito aguenta calor melhor que quartzo (o quartzo tem resina e pode manchar com calor; veja <a href="/dicas/granito-ou-quartzo">granito ou quartzo</a>).</li>
<li>Pedra <b>escura</b> esconde fuligem e gordura; as buscas mais comuns são preto São Gabriel e verde Ubatuba.</li>
<li>Pedra clara e porosa mancha com gordura: impermeabilize e avise o cliente.</li>
</ul>

<h2>Como fazer o orçamento</h2>
<p>Exemplo de bancada em L de 2,50 m + 1,50 m com 60 cm de profundidade (medidas só para ilustrar):</p>
<div class="tab"><table>
<tr><th>Item</th><th>Conta</th><th>Quantidade</th></tr>
<tr><td>Tampo em L</td><td>(2,50 + 1,50 − 0,60) × 0,60</td><td>2,04 m²</td></tr>
<tr><td>Rodabanca 10 cm</td><td>(2,50 + 1,50) × 0,10</td><td>0,40 m²</td></tr>
<tr><td>Saia na frente do L</td><td>(2,50 − 0,60) + (1,50 − 0,60) + 0,60 + 0,60 (cabeças)</td><td>4,00 m lineares</td></tr>
<tr><td>Recorte de pia</td><td>1 unidade</td><td>1</td></tr>
<tr><td>Revestimento da churrasqueira</td><td>medir peça a peça</td><td>conforme o modelo</td></tr>
</table></div>
<p>Depois some a perda de corte, o acabamento de borda, os recortes e a instalação. A conta passo a passo está em <a href="/dicas/como-calcular-metro-quadrado-de-granito">como calcular o m² de granito</a> e em <a href="/dicas/como-fazer-orcamento-de-bancada-de-granito">orçamento de bancada</a>.</p>
''',
 ['cuba-de-embutir-sobrepor-ou-apoio','recorte-de-cooktop-no-granito','como-medir-bancada-de-granito','rodabanca-e-frontao'],
 'Altura, profundidade, L, pia, revestimento da churrasqueira e orçamento.',
 data='2026-11-25')

pg('cuba-de-embutir-sobrepor-ou-apoio',
 'Cuba de Embutir, Sobrepor ou Apoio: qual a diferença e qual escolher',
 'Cuba de embutir, sobrepor, semi-encaixe ou apoio: qual a diferença e qual escolher',
 'Diferença entre cuba de embutir, de sobrepor, semi-encaixe, de apoio e esculpida: vantagens, desvantagens, qual vai melhor no banheiro e na cozinha, como fica o recorte no granito e como cobrar.',
 'Quando o cliente pergunta "qual cuba?", a resposta muda o recorte, o acabamento da pedra, a altura da bancada e o preço. Esta página ajuda o marmorista a explicar as opções e a fazer o recorte certo.',
 6,
 '''
<h2>Os tipos de cuba, em resumo</h2>
<div class="tab"><table>
<tr><th>Tipo</th><th>Como fica</th><th>Recorte na pedra</th></tr>
<tr><td><b>Embutir</b> (sob o tampo)</td><td>Cuba presa por baixo; a borda da pedra fica à vista</td><td>Recorte com borda polida</td></tr>
<tr><td><b>Sobrepor</b></td><td>A aba da cuba apoia em cima da pedra</td><td>Recorte bruto (a aba cobre)</td></tr>
<tr><td><b>Semi-encaixe</b></td><td>Parte dentro da bancada, a frente para fora</td><td>Recorte aberto na borda da frente</td></tr>
<tr><td><b>Apoio</b></td><td>A cuba fica inteira em cima da pedra</td><td>Só o furo da válvula (e da torneira, se sair da pedra)</td></tr>
<tr><td><b>Esculpida</b></td><td>Feita da própria pedra</td><td>Montada na marmoraria</td></tr>
</table></div>

<h2>Qual a diferença entre cuba de embutir e de sobrepor</h2>
<p>Na <b>de embutir</b>, a cuba fica embaixo da pedra e a água do tampo escorre direto para dentro: limpar é só puxar com o pano. Na <b>de sobrepor</b>, a aba da cuba fica por cima da pedra e forma um degrau onde a sujeira para.</p>
<ul>
<li><b>Embutir</b>: mais bonita e fácil de limpar; dá mais trabalho na marmoraria (recorte polido, fixação por baixo com cola e suporte).</li>
<li><b>Sobrepor</b>: instalação mais rápida e troca fácil; o recorte não precisa de polimento porque a aba esconde.</li>
</ul>

<h2>Qual a desvantagem da cuba de sobrepor</h2>
<ul>
<li>A aba fica alta: água e sujeira acumulam no encontro com a pedra.</li>
<li>O silicone em volta da aba escurece com o tempo e precisa ser trocado.</li>
<li>Visual mais simples; em projeto de arquiteto, quase sempre pedem a de embutir.</li>
</ul>

<h2>Cuba de sobrepor pode ser embutida?</h2>
<p>Em geral, não fica bem: a aba é feita para ficar à vista e, por baixo, atrapalha a fixação e a vedação. Alguns modelos de inox são vendidos como "embutir ou sobrepor": siga o que o fabricante diz para aquele modelo. Na dúvida, peça o gabarito ou a ficha técnica.</p>

<h2>Qual a melhor cuba para cozinha</h2>
<ul>
<li>A mais pedida com granito é a <b>cuba de inox de embutir</b>: fácil de limpar e aguenta panela pesada.</li>
<li>Cuba grande ou dupla pede bancada de uns 60 cm de profundidade e armário com vão compatível.</li>
<li>Cozinha simples ou imóvel de aluguel: sobrepor resolve rápido e custa menos.</li>
<li>Tanque de área de serviço segue a mesma lógica.</li>
</ul>

<h2>Qual o melhor tipo de cuba para o banheiro</h2>
<ul>
<li><b>Embutir</b>: bancada limpa e prática; a mais usada em banheiro social.</li>
<li><b>Apoio</b>: visual de destaque em lavabo; a bancada costuma ficar mais baixa para compensar a altura da cuba.</li>
<li><b>Semi-encaixe</b>: bancada estreita, banheiro pequeno.</li>
<li><b>Esculpida</b>: peça única na pedra; veja <a href="/dicas/cuba-esculpida-em-granito">cuba esculpida em granito</a>.</li>
</ul>

<h2>A altura da bancada muda com a cuba</h2>
<p>O que importa para quem usa é a altura da <b>borda da cuba</b>, não a da pedra. Com cuba de apoio, a borda sobe junto com a altura da cuba; por isso a bancada costuma ser montada mais baixa. Confirme a altura com o projeto e com o cliente antes de chumbar o suporte.</p>

<h2>Como fazer o recorte no granito</h2>
<ol>
<li><b>Peça o gabarito</b> ou a ficha técnica da cuba. Medir a cuba com trena engana, principalmente a de louça.</li>
<li><b>Embutir</b>: o recorte fica alguns milímetros para dentro da borda interna da cuba, a borda da pedra é polida e a cuba é colada por baixo com adesivo e presa com suporte.</li>
<li><b>Sobrepor</b>: o recorte segue a linha indicada no gabarito, com folga para a cuba entrar sem forçar.</li>
<li><b>Apoio</b>: só o furo da válvula (normalmente com serra-copo) e o da torneira, se ela sair da pedra.</li>
<li>Deixe pedra suficiente na frente do recorte para a peça não quebrar no transporte. Veja também <a href="/dicas/como-instalar-bancada-de-granito">como instalar bancada</a>.</li>
</ol>

<h2>Como cobrar</h2>
<p>O mais comum é cobrar o <b>recorte por unidade</b>, com preço diferente para cada tipo: o de embutir (polido) costuma custar mais que o de sobrepor (bruto) e que o furo da cuba de apoio. A cuba pode ser do cliente ou fornecida por você. Escreva no orçamento qual cuba e qual recorte estão inclusos. Para a conta completa, veja <a href="/dicas/como-fazer-orcamento-de-bancada-de-granito">orçamento de bancada</a>.</p>
''',
 ['cuba-esculpida-em-granito','recorte-de-cooktop-no-granito','bancada-de-churrasqueira-em-granito','como-instalar-bancada-de-granito'],
 'Embutir × sobrepor × semi-encaixe × apoio: qual escolher e como recortar.',
 data='2026-11-25')

pg('como-cortar-granito-sem-lascar',
 'Como Cortar Granito Sem Lascar: disco, água, fita e passo a passo',
 'Como cortar granito sem lascar: disco, água, fita e passo a passo',
 'Como cortar granito sem lascar: disco diamantado certo, água na linha, fita crepe, apoio da chapa inteira e passadas. Por que a borda racha e o que fazer se lascar.',
 'A lasca na borda é o erro que mais custa tempo na marmoraria: a peça vai para o lixo e o cliente espera de novo. Quase sempre a causa é apoio, disco ou pressão, não a máquina.',
 5,
 '''
<h2>Por que o granito lasca</h2>
<p>A lasca aparece quando a pedra não tem apoio por baixo, o disco aquece e perde o corte, ou a linha é feita com força demais de uma vez. Quase sempre é um destes problemas:</p>
<table>
<tr><th>O que aconteceu</th><th>Por que lasca</th></tr>
<tr><td>Chapa apoiada só nas pontas</td><td>No meio ela cede e a pedra quebra perto do fim do corte</td></tr>
<tr><td>Corte a seco</td><td>O disco esquenta, perde o corte e arranca pedaço</td></tr>
<tr><td>Disco gasto ou de outro material</td><td>Morde de forma irregular e solta lasca na borda</td></tr>
<tr><td>Passada única e forçada</td><td>A máquina trava e a pedra estala</td></tr>
<tr><td>Linha sem fita</td><td>A borda de saída é a que mais racha</td></tr>
</table>

<h2>O que você precisa</h2>
<ul>
<li><b>Disco diamantado para granito</b> (disco de concreto ou de corte a seco não serve). O segmentado costuma cortar mais rápido; o contínuo deixa a borda mais lisa. Confira o que o fabricante indica.</li>
<li><b>Água na linha de corte</b>, por mangueira ou gotejamento. Sem água o disco aquece e lasca.</li>
<li><b>Fita crepe</b> sobre a linha: protege a superfície e segura a lasca.</li>
<li><b>Apoio inteiro</b>: cavaletes ou espuma por baixo de toda a chapa, deixando livre a parte que vai cair.</li>
<li><b>Grampos ou ventosas</b> para segurar a peça.</li>
</ul>

<h2>Passo a passo</h2>
<ol>
<li><b>Marque a linha</b> com lápis de cera sobre a fita crepe e confira a medida duas vezes.</li>
<li><b>Apoie a chapa inteira</b>. A sobra precisa ficar livre, sem peso em cima.</li>
<li><b>Ligue a água</b> antes de encostar o disco na pedra.</li>
<li><b>Corte em duas ou três passadas</b>, com a máquina em velocidade constante e sem forçar. Deixe o disco trabalhar.</li>
<li><b>Na última passada</b>, segure a sobra ou escore-a para ela não cair de repente e levar a borda junto.</li>
<li><b>Em curva ou recorte interno</b>, faça cortes em tiras, aos poucos, e feche o arco no fim.</li>
</ol>

<h2>Se a borda lascar mesmo assim</h2>
<ul>
<li><b>Lasca pequena</b>: lixe com lixa diamantada grossa, depois a fina, e polia. Em geral some.</li>
<li><b>Lasca grande</b>: a peça geralmente está perdida. Não tente esconder com cola ou massa, o cliente vê. Refaça a peça e avise o cliente antes.</li>
<li><b>Canto do recorte</b>: arredonde os cantos para a trinca não começar ali (veja <a href="/dicas/recorte-de-cooktop-no-granito">recorte de cooktop</a>).</li>
</ul>

<h2>Cuidados na oficina</h2>
<ul>
<li>Corte em cima de espuma ou borracha, nunca direto no piso de cerâmica.</li>
<li>Use óculos, luva e protetor de ouvido. Poeira de pedra faz mal ao pulmão: use máscara boa e aspiração.</li>
<li>Recolha a água de corte em vez de deixar escorrer para o ralo.</li>
</ul>

<h2>Cobrança</h2>
<p>Quem refaz peça por lasca paga duas vezes em material e tempo. Por isso vale cobrar com folga o corte de peça grande ou com curva, e incluir o desgaste do disco. Para a conta da chapa, veja <a href="/dicas/plano-de-corte-de-chapa-de-granito">plano de corte de chapa de granito</a>.</p>
''',
 ['recorte-de-cooktop-no-granito','plano-de-corte-de-chapa-de-granito','como-polir-granito','tamanho-de-chapa-de-granito'],
 'Disco certo, água, fita e apoio inteiro: cortar sem lascar e o que fazer se lascar.',
 data='2026-11-26')

pg('como-furar-granito',
 'Como Furar Granito: broca, serra-copo e passo a passo sem trincar',
 'Como furar granito: broca, serra-copo e passo a passo sem trincar',
 'Como furar granito para torneira, cuba, válvula ou parafuso: qual broca usar, velocidade, água, furo perto da borda e os erros que racham a pedra.',
 'Furo mal feito é uma das coisas que mais racham o granito depois de instalado. O furo certo começa pela broca certa, sem impacto e com água.',
 5,
 '''
<h2>Quando você precisa furar</h2>
<ul>
<li><b>Torneira de bancada</b>: o furo da torneira na pedra.</li>
<li><b>Cuba de apoio</b> ou furo da válvula da cuba.</li>
<li><b>Passagem de fio, tomada ou cano</b> por dentro da pedra.</li>
<li><b>Fixação</b> de suporte, corrimão ou prateleira com parafuso.</li>
</ul>

<h2>Ferramentas</h2>
<table>
<tr><th>Ferramenta</th><th>Para que serve</th></tr>
<tr><td>Serra-copo diamantada</td><td>Furos maiores e redondos: torneira, válvula da cuba, passagem de cano</td></tr>
<tr><td>Broca diamantada</td><td>Furos pequenos, de fixação de parafuso, ou para começar um furo</td></tr>
<tr><td>Furadeira com velocidade variável</td><td>Velocidade baixa e <b>sem modo de impacto</b> (martelo). O impacto quebra a pedra.</td></tr>
<tr><td>Água</td><td>Refrigera a broca e leva o pó embora</td></tr>
</table>

<h2>Passo a passo</h2>
<ol>
<li><b>Marque o centro</b> com caneta. Para torneira, use o gabarito da torneira ou o que vier com a cuba.</li>
<li><b>Cole fita crepe</b> sobre a marca: segura a broca no começo e evita lascar.</li>
<li><b>Comece em velocidade baixa</b>, sem pressão, com água pingando sobre o furo.</li>
<li><b>Mantenha a broca reta</b> e a pressão constante. Quem faz o corte é a broca, não a força.</li>
<li><b>Tire a broca de vez em quando</b> para limpar a lama e deixar a água entrar.</li>
<li><b>Ao atravessar</b>, diminua a pressão: é o momento em que o lado de baixo costuma lascar. Se o furo for passante, termine por baixo ou apoie uma tábua.</li>
<li><b>Limpe e confira</b> se a torneira ou a peça encaixa antes de colar ou fixar.</li>
</ol>

<h2>Erros que lascam ou racham</h2>
<table>
<tr><th>Erro</th><th>O que acontece</th></tr>
<tr><td>Furadeira com impacto</td><td>A pedra trinca em volta do furo</td></tr>
<tr><td>Furar a seco</td><td>Esquenta, a broca perde o corte e a borda do furo queima</td></tr>
<tr><td>Furo perto da borda ou de outro furo</td><td>Racha entre eles, principalmente na pedra fina</td></tr>
<tr><td>Pressão forte no fim</td><td>Lasca do lado de saída</td></tr>
</table>

<h2>Furo perto da borda ou de canto</h2>
<p>Quanto mais perto da borda ou de um canto, mais o furo enfraquece a pedra. Deixe pedra sobrando em volta. Se o projeto pedir furo muito perto, avise o cliente antes e confirme com o fabricante da torneira ou da cuba. Canto vivo com furo ao lado é onde mais trinca.</p>

<h2>Fixar parafuso sem racha</h2>
<p>Para suporte ou corrimão, faça o furo com broca diamantada pequena e use bucha química ou bucha própria para pedra. Não aperte bucha de expansão além do que ela pede: ela racha o granito. O diâmetro da broca é o que a bucha indicar.</p>

<h2>Quando não furar</h2>
<p>Se a pedra tem fissura, veio aberto ou já está lascada no lugar do furo, não fure ali. Avise o cliente e veja outra posição ou outra peça. Furar em cima de defeito é a causa de muita reclamação depois.</p>

<h2>Cobrança</h2>
<p>O furo costuma ser cobrado por unidade, com preço diferente para furo de torneira, de cuba e de parafuso. Escreva no orçamento quantos furos e de que tipo. Para o recorte da cuba, veja <a href="/dicas/cuba-de-embutir-sobrepor-ou-apoio">cuba de embutir, sobrepor ou apoio</a>.</p>
''',
 ['como-cortar-granito-sem-lascar','recorte-de-cooktop-no-granito','cuba-de-embutir-sobrepor-ou-apoio','como-instalar-bancada-de-granito'],
 'Broca certa, sem impacto e com água: furo para torneira, cuba ou parafuso sem trincar.',
 data='2026-11-26')

pg('ilha-de-cozinha-em-granito-medidas',
 'Ilha de Cozinha em Granito: medidas, altura, banqueta e espaço ao redor',
 'Ilha de cozinha em granito: medidas, altura, banqueta e espaço ao redor',
 'Medidas de ilha de cozinha em granito: altura do tampo e da banqueta, profundidade, espaço para circular, balanço para sentar, cuba e cooktop na ilha.',
 'A ilha é o destaque da cozinha e a peça que mais dá erro de medida, porque o cliente pensa no visual e esquece do espaço para andar e sentar. Confira estas medidas antes de cortar a pedra.',
 6,
 '''
<h2>Medidas de referência</h2>
<p>São medidas usadas na prática, não normas obrigatórias. O que vale no fim é o projeto, o armário que já está no lugar e o uso do cliente.</p>
<table>
<tr><th>Item</th><th>Referência</th><th>Observação</th></tr>
<tr><td>Altura do tampo</td><td>Em torno de 90 cm</td><td>Igual à bancada de trabalho. Se a ilha for só para comer, pode ser um pouco mais alta.</td></tr>
<tr><td>Altura da banqueta</td><td>Em torno de 60 a 75 cm</td><td>Depende da altura do tampo: sentar e apoiar o braço tem que ficar confortável.</td></tr>
<tr><td>Balanço para sentar</td><td>Costuma ser pelo menos 30 cm</td><td>É o que cabe a perna de quem senta. Balanço grande pede espessura ou reforço.</td></tr>
<tr><td>Espaço para circular</td><td>Em torno de 90 cm a 1,20 m</td><td>Entre a ilha e a parede ou o armário. Mais espaço quando duas pessoas cozinham e passam ao mesmo tempo.</td></tr>
<tr><td>Comprimento</td><td>Conforme a cozinha</td><td>Como referência, conte cerca de 60 cm de tampo por lugar sentado.</td></tr>
</table>

<h2>Ilha só com tampo, com cuba ou com cooktop</h2>
<ul>
<li><b>Só tampo</b>: mais simples. A pedra pode ter borda reta.</li>
<li><b>Com cuba</b>: a ilha precisa de água e esgoto no lugar certo. Confirme o ponto antes de cortar. Veja <a href="/dicas/cuba-de-embutir-sobrepor-ou-apoio">cuba de embutir, sobrepor ou apoio</a>.</li>
<li><b>Com cooktop</b>: sem parede atrás, a coifa precisa de instalação própria. Confirme com o cliente e com o fabricante.</li>
</ul>

<h2>Balanço: o ponto fraco</h2>
<p>A parte da pedra que passa do armário (o balanço) é onde a ilha mais trinca. Quanto maior o balanço, mais espessura ou reforço embaixo. Confira a tabela em <a href="/dicas/espessura-de-granito-para-bancada">espessura de granito para bancada</a>.</p>

<h2>Como medir, passo a passo</h2>
<ol>
<li>Meça o vão livre entre as paredes e as portas do lado da ilha.</li>
<li>Marque no chão a área da ilha com fita crepe e veja com o cliente se a banqueta cabe. Peça para ele sentar ali de verdade.</li>
<li>Anote a altura do tampo e confirme com o modelo da banqueta escolhida.</li>
<li>Veja onde ficam tomadas, água e gás, se houver cuba ou cooktop.</li>
<li>Passe a medida final ao gabarito e só então corte a pedra. Veja <a href="/dicas/como-medir-bancada-de-granito">como medir bancada de granito</a>.</li>
</ol>

<h2>A ilha na chapa</h2>
<p>Ilha grande costuma consumir chapa inteira. Antes de cortar, veja se a peça cabe com a emenda longe da cuba e do cooktop. Veja <a href="/dicas/tamanho-de-chapa-de-granito">tamanho de chapa de granito</a>.</p>

<h2>Erros comuns</h2>
<ul>
<li>Ilha colada no armário sem folga: a gaveta não abre.</li>
<li>Banqueta sem espaço atrás de quem senta: a pessoa encosta na parede ou no fogão.</li>
<li>Tampo alto ou baixo demais para o uso.</li>
</ul>

<h2>Cobrança</h2>
<p>A ilha é cobrada pela pedra (pelo tamanho da peça), mais recortes e acabamento de borda. Escreva no orçamento a altura, a profundidade e se tem balanço. Para a conta completa, veja <a href="/dicas/como-fazer-orcamento-de-bancada-de-granito">orçamento de bancada de granito</a>.</p>
''',
 ['espessura-de-granito-para-bancada','como-medir-bancada-de-granito','como-instalar-bancada-de-granito','granito-ou-quartzo'],
 'Altura, banqueta, balanço e espaço para circular: medidas de ilha antes de cortar.',
 data='2026-11-26')

pg('como-tirar-mancha-de-granito',
 'Como Tirar Mancha de Granito: óleo, café, ferrugem e mancha escura',
 'Como tirar mancha de granito: o que usar em cada tipo e o que nunca passar',
 'Como tirar mancha de óleo, gordura, café, vinho, ferrugem e água do granito branco, claro ou preto, com compressa, passo a passo e cuidados para o marmorista orientar o cliente.',
 'A primeira pergunta não é "qual produto", é "mancha de quê". Óleo, bebida, ferrugem e umidade saem de jeitos diferentes, e o produto errado piora a pedra. Este guia serve para o marmorista atender o cliente com segurança.',
 6,
 '''
<h2>Antes de passar qualquer coisa</h2>
<ul>
<li><b>Pergunte o que caiu</b> na pedra e há quanto tempo.</li>
<li><b>Pingue água ao lado da mancha.</b> Se a pedra escurece em poucos minutos, ela está absorvendo e sem proteção.</li>
<li><b>Teste o produto num canto escondido</b> e espere secar antes de ir para a mancha.</li>
<li><b>Tire foto antes.</b> Ajuda a comparar e a mostrar ao cliente o que melhorou.</li>
</ul>

<h2>Tabela rápida: mancha e o que tentar</h2>
<div class="tab"><table>
<tr><th>Mancha</th><th>Como costuma aparecer</th><th>O que tentar primeiro</th></tr>
<tr><td>Óleo e gordura</td><td>Escura, com contorno marcado</td><td>Detergente neutro e, se ficar, compressa para pedra ou pó absorvente com solvente compatível</td></tr>
<tr><td>Café, vinho, suco</td><td>Amarelada ou avermelhada</td><td>Água com detergente neutro; em pedra clara, compressa com água oxigenada, após teste</td></tr>
<tr><td>Ferrugem</td><td>Laranja ou marrom, onde ficou metal</td><td>Removedor de ferrugem próprio para granito</td></tr>
<tr><td>Água / umidade</td><td>Sombra escura perto da cuba ou da parede</td><td>Achar a origem da água e deixar secar</td></tr>
<tr><td>Marca branca</td><td>Película esbranquiçada</td><td>Pode ser resíduo de sabão ou calcário: limpador próprio para pedra</td></tr>
</table></div>

<h2>Compressa (cataplasma), passo a passo</h2>
<p>É o método que puxa para fora a mancha que entrou na pedra.</p>
<ol>
<li>Limpe a área com detergente neutro e deixe secar.</li>
<li>Faça uma pasta com um pó absorvente branco (talco ou produto pronto de marmoraria) e o líquido indicado para a mancha, no ponto de pasta de dente.</li>
<li>Cubra a mancha passando um pouco da borda, com poucos milímetros de espessura.</li>
<li>Tampe com plástico filme, prenda com fita e faça alguns furinhos.</li>
<li>Espere secar, em geral de um dia para o outro.</li>
<li>Retire com espátula de plástico, limpe com pano úmido e espere secar para avaliar.</li>
<li>Se clareou mas não saiu, repita. Mancha antiga costuma pedir mais de uma aplicação.</li>
</ol>

<h2>Granito branco, claro ou preto muda alguma coisa?</h2>
<ul>
<li><b>Branco e claro</b> (Itaúnas, Siena e parecidos): mancham de forma mais visível e podem ter minerais de ferro que oxidam. Escolha o produto com mais cuidado.</li>
<li><b>Preto e escuro</b> (São Gabriel e parecidos): evite água oxigenada, abrasivo e produto forte, que podem deixar uma área clara ou fosca. Muitas "manchas" no preto são resíduo de produto por cima.</li>
<li><b>Pedra resinada</b>: solvente pode atacar a resina. Confirme com o fornecedor da chapa.</li>
</ul>

<h2>O que nunca passar</h2>
<ul>
<li>Ácido muriático, limpa-pedra ácido ou removedor de ferrugem de uso geral.</li>
<li>Água sanitária e cloro como limpeza de rotina.</li>
<li>Palha de aço (solta ferro e mancha mais) e saponáceo abrasivo.</li>
<li>Mistura de produtos: além de estragar a pedra, pode soltar gás perigoso.</li>
</ul>

<h2>Quando a mancha não sai</h2>
<p>Algumas marcas são da própria pedra (veios, concentração de minerais) ou oxidação que vem de dentro. Umidade que sobe da argamassa ou entra por rejunte falho volta enquanto a causa não for resolvida. Nesses casos, explique ao cliente, avalie polir de novo (veja <a href="/dicas/como-polir-granito">como polir granito</a>) ou trocar a peça. Não prometa que sai.</p>

<h2>Como evitar na próxima</h2>
<p>Secar o que cair, não apoiar lata ou palha de aço sobre a pedra e proteger com <a href="/dicas/impermeabilizante-para-granito">impermeabilizante para granito</a>. Entregue essas orientações por escrito junto com a bancada: evita reclamação.</p>
''',
 ['impermeabilizante-para-granito','como-polir-granito','granito-ou-quartzo','como-instalar-bancada-de-granito'],
 'Óleo, café, ferrugem e umidade: o que tentar em cada mancha e o que nunca passar.',
 data='2026-11-27')

pg('impermeabilizante-para-granito',
 'Impermeabilizante para Granito: qual usar, como aplicar e de quanto em quanto tempo',
 'Impermeabilizante para granito: qual usar, como aplicar e quando refazer',
 'Precisa impermeabilizar granito? Tipos de impermeabilizante, teste da gota d\'água, aplicação passo a passo em pedra branca e preta e como oferecer o serviço na marmoraria.',
 'O impermeabilizante reduz a absorção da pedra e dá tempo de limpar antes de manchar. Ele não deixa o granito à prova de tudo, e isso precisa ficar claro para o cliente.',
 5,
 '''
<h2>Todo granito precisa?</h2>
<p>Depende da pedra. Cada granito absorve de um jeito, e as pedras claras costumam pedir mais atenção. Faça o <b>teste da gota</b>:</p>
<ol>
<li>Com a pedra limpa e seca, pingue um pouco de água.</li>
<li>Observe por alguns minutos.</li>
<li>Se escureceu rápido, ela absorve e vale proteger. Se a gota ficou por cima sem marcar, absorve pouco ou já está protegida.</li>
</ol>

<h2>Tipos de produto</h2>
<div class="tab"><table>
<tr><th>Tipo</th><th>Como age</th><th>Quando faz sentido</th></tr>
<tr><td>Hidrofugante</td><td>Penetra e repele água</td><td>Áreas molhadas com pouca gordura, como banheiro</td></tr>
<tr><td>Hidro e óleo-repelente</td><td>Penetra e repele água e óleo</td><td>Bancada de cozinha e área gourmet</td></tr>
<tr><td>Formador de película ou cera</td><td>Fica por cima da pedra</td><td>Pode riscar, descascar ou amarelar; use só se o fabricante indicar para aquele local</td></tr>
</table></div>
<p>Leia o rótulo: se serve para granito, se pode em superfície que encosta em alimento, se pode em área externa e se muda o tom da pedra (alguns realçam a cor, o chamado efeito molhado).</p>

<h2>Como aplicar, passo a passo</h2>
<p>A ordem geral é esta, mas <b>o prazo e o número de demãos são os do fabricante</b>.</p>
<ol>
<li>Limpe a pedra e tire pó, gordura, cola e cera.</li>
<li>Espere secar bem. Pedra recém-lavada ou recém-assentada ainda guarda umidade.</li>
<li>Teste num canto para ver se muda a cor.</li>
<li>Aplique uma camada fina e uniforme com pano limpo ou pincel macio.</li>
<li>Deixe penetrar pelo tempo do rótulo.</li>
<li><b>Retire todo o excesso</b> antes de secar, senão fica manchado e pegajoso.</li>
<li>Repita se o fabricante pedir e respeite o tempo de cura antes de liberar o uso.</li>
<li>Refaça o teste da gota.</li>
</ol>

<h2>Antes de instalar ou depois?</h2>
<ul>
<li>Muitos marmoristas aplicam na oficina, com a peça seca, incluindo as bordas e os recortes da cuba.</li>
<li>Depois de instalar, faça um retoque nas emendas e nos pontos que foram lixados.</li>
<li>Não aplique antes de colar peças se o produto atrapalhar a aderência: veja <a href="/dicas/como-colar-granito">como colar granito</a>.</li>
</ul>

<h2>Branco e preto</h2>
<p>No granito branco ou claro, a proteção ajuda a evitar mancha de óleo, café e vinho. No preto, muitas pedras absorvem pouco: se a gota não entra, o produto pode ficar por cima e deixar marcas. Teste sempre.</p>

<h2>De quanto em quanto tempo refazer</h2>
<p>Não existe um prazo único. Varia com a pedra, o produto, o uso e a limpeza. Siga o rótulo e repita o teste da gota de tempos em tempos: voltou a escurecer, está na hora.</p>

<h2>Como oferecer e cobrar</h2>
<p>Coloque como item separado no orçamento, calculado por m² ou por peça, somando produto e tempo. Escreva o que ele faz e o que não faz: reduz manchas, mas não protege contra risco, pancada, calor ou produto ácido. Se a mancha já está lá, trate antes (veja <a href="/dicas/como-tirar-mancha-de-granito">como tirar mancha de granito</a>).</p>
''',
 ['como-tirar-mancha-de-granito','granito-ou-quartzo','como-polir-granito','como-fazer-orcamento-de-bancada-de-granito'],
 'Teste da gota, tipos de produto, aplicação e quando refazer a proteção da pedra.',
 data='2026-11-27')

pg('bancada-de-banheiro-medidas',
 'Bancada de Banheiro: medidas, altura e profundidade para cada tipo de cuba',
 'Bancada de banheiro: medidas, altura e profundidade para cada tipo de cuba',
 'Medidas de bancada de banheiro em granito: altura com cuba de apoio, sobrepor, embutir e esculpida, profundidade, duas cubas, bancada acessível, rodabanca e saia.',
 'No banheiro, a altura certa depende da cuba. A mesma pedra a 90 cm fica ótima com cuba de embutir e alta demais com cuba de apoio. Defina a cuba antes de medir.',
 5,
 '''
<h2>Altura conforme a cuba</h2>
<p>O que importa é a altura em que a pessoa lava as mãos, ou seja, a <b>borda da cuba</b>. Os valores abaixo são referências de uso, não regra.</p>
<div class="tab"><table>
<tr><th>Tipo de cuba</th><th>Altura do tampo (referência)</th><th>Conta</th></tr>
<tr><td>De embutir (por baixo)</td><td>85 a 90 cm</td><td>A borda é o próprio tampo</td></tr>
<tr><td>Esculpida na pedra</td><td>85 a 90 cm</td><td>A borda é o próprio tampo</td></tr>
<tr><td>Semi-encaixe ou sobrepor</td><td>Em torno de 80 a 85 cm</td><td>Desconte o que a cuba sobe acima da pedra</td></tr>
<tr><td>De apoio</td><td>Em torno de 70 a 80 cm</td><td>Altura da borda menos a altura da cuba</td></tr>
</table></div>
<p><b>Exemplo:</b> o cliente quer a borda a 90 cm e escolheu cuba de apoio de 14 cm. O tampo fica a 90 − 14 = 76 cm do piso pronto.</p>

<h2>Profundidade e comprimento</h2>
<ul>
<li><b>Profundidade</b>: de 45 a 60 cm é o mais comum. Em lavabo pequeno, pode ser menor, desde que a cuba e a torneira caibam.</li>
<li><b>Comprimento</b>: é o do vão. Deixe pedra sobrando dos dois lados da cuba para apoiar objetos e não enfraquecer o recorte.</li>
<li><b>Duas cubas</b>: a partir de uns 1,20 m já dá para estudar; com 1,40 m ou mais fica mais confortável. Confira a largura das cubas e o espaço entre os centros.</li>
</ul>

<h2>Bancada acessível (PCD)</h2>
<p>Para banheiro acessível, a norma ABNT NBR 9050 trata do lavatório: a referência é a face de cima entre <b>78 e 80 cm</b> e vão livre embaixo de cerca de <b>73 cm</b>, sem armário ou saia alta atrapalhando a cadeira. Confira a versão atual da norma e o projeto do responsável técnico, principalmente em comércio e obra pública.</p>

<h2>Rodabanca, saia e espessura</h2>
<ul>
<li><b>Rodabanca</b>: de 7 a 10 cm é bastante usada; protege a parede atrás. Veja <a href="/dicas/rodabanca-e-frontao">rodabanca e frontão</a>.</li>
<li><b>Saia</b>: de 4 cm para dar aparência de pedra grossa até 15 ou 20 cm para esconder a cuba. Veja <a href="/dicas/saia-de-granito">saia de granito</a>.</li>
<li><b>Espessura</b>: 2 cm é comum; bancada comprida ou solta pede apoio ou mão francesa. Veja <a href="/dicas/espessura-de-granito-para-bancada">espessura de granito</a>.</li>
</ul>

<h2>Como medir, passo a passo</h2>
<ol>
<li>Meça a largura do vão em três pontos (fundo, meio e frente). Parede raramente está no esquadro.</li>
<li>Confirme o piso: se ainda vai assentar, some a espessura.</li>
<li>Peça o modelo da cuba e da torneira, com a folha de medidas do fabricante.</li>
<li>Marque o centro da cuba conforme o ponto de esgoto.</li>
<li>Veja se a torneira é de mesa ou de parede e se o bico alcança o meio da cuba.</li>
<li>Confira porta, box e vaso: a bancada não pode bater nem apertar a passagem.</li>
</ol>

<h2>Erros comuns</h2>
<ul>
<li>Instalar o tampo a 90 cm e só depois colocar cuba de apoio.</li>
<li>Furo de torneira de mesa sem espaço entre a cuba e a rodabanca.</li>
<li>Gaveta do armário batendo no sifão ou no fundo da cuba.</li>
</ul>
''',
 ['cuba-de-embutir-sobrepor-ou-apoio','cuba-esculpida-em-granito','rodabanca-e-frontao','como-medir-bancada-de-granito'],
 'Altura por tipo de cuba, profundidade, duas cubas e bancada acessível.',
 data='2026-11-27')
