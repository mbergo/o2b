import requests
import json

print(
    requests.post(
        "https://o2b.onrender.com/",
        json={
            "from_email": "John@o2b.com.br",
            "content": """
              ## Transcript

  00:00 Bertino Algebaile Da Silva, Fernanda: What I do?
00:00 Felipe Carpanezi: Not the small blockage to the Bay.
00:02 Marcus Bergo: But the yourself.
00:02 Eduardo Dutra - O2B: But there's been so.
00:04 Kaique Correia: What that? But that
00:06 Bertino Algebaile Da Silva, Fernanda: To set up Don't settle.
00:09 Felipe Carpanezi: May.
00:09 Marcus Bergo: To watch what are you?
00:09 Eduardo Dutra - O2B: Towards setup.
00:11 Bertino Algebaile Da Silva, Fernanda: Mentally Then leave that through. Kilo is hailed a passive position in minutes. OK.
00:20 Israel Antonio Pereira: Not Upper shoulder Bruno. Sonos So nostris.
00:22 Bertino Algebaile Da Silva, Fernanda: Yeah, it Now you do a functional to be famous again or system.
00:26 Eduardo Dutra - O2B: Or not OPA there was no it's not.
00:29 Bertino Algebaile Da Silva, Fernanda: Yeah.
00:30 Eduardo Dutra - O2B: No. So no, exactly.
00:30 Bertino Algebaile Da Silva, Fernanda: Thank you. Back onto Zio's request change.
00:33 Eduardo Dutra - O2B: Filippi condo. Zia equal puedo Virgo Marcus vergo? Also technology, Melissa.
00:39 Bertino Algebaile Da Silva, Fernanda: Beliza. Show a as in staying on mobile sites. Your kids see. And Fazil hands on the Kubernetes my stomach aches. Should thing is interesting, Adolf Days, sobriquet, location to search. You can't raise a child.
01:00 Israel Antonio Pereira: I Eat some It's amazing, you know, you can.
01:03 Bertino Algebaile Da Silva, Fernanda: But shellmouth now. Michael
01:05 Israel Antonio Pereira: No, no colburns.
01:06 Bertino Algebaile Da Silva, Fernanda: Ah, back on in town. Ever since, so for it was in traffic I catching it. What they show you feel difficult as this sucker, the bigger presence agrava epost gravati deposition airport. She compassion like so? Uh, quite say.
01:25 Felipe Carpanezi: Let's see.
01:26 Israel Antonio Pereira: Really prefer you got this.
01:26 Bertino Algebaile Da Silva, Fernanda: Right.
01:27 Eduardo Dutra - O2B: For missing domain.
01:28 Bertino Algebaile Da Silva, Fernanda: So why don't you solumbra comic Going to
02:23 Bertino Algebaile Da Silva, Fernanda: Nada que isso olha, então já estamos gravando, estamos já aqui com a transcrição, vou passar a palavra então para o Felipe, é a intenção. É mesmo apresentar, tá? O ambiente de coubert net e, como o nome diz, né? O hands-on, assim, é é tirar as dúvidas da da usabilidade mesmo, tá gente, fiquem à vontade para as perguntas é, Felipe, você compartilha a tela? Se você Secco, Você comanda aí.
02:48 Felipe Carpanezi: Sim, vou compartilhar a tela com vocês aqui, ó.
02:50 Bertino Algebaile Da Silva, Fernanda: Perfeito.
02:50 Marcus Bergo: É primeiro. Só queria falar para vocês, que e escorreu aí o máximo, né? Aqui, infelizmente, Welder, eles. Eles saíram da empresa. E aí ele, pô, teve o esforço de passar todo conhecimento. Sexta, final de semana. E, pô, ele dá um apoio assim, fantástico, para ajustar, poder estar aqui.
03:21 Eduardo Dutra - O2B: O exato é na verdade OOO Welder, né? Executou ali todo o projeto, também junto com o apoio do do gusta, né? Por isso que ele já está, vai entrar e também para dar um apoio. É, mas que nem o Bill comentou, aí ele acabou saindo na sexta passada, né? Que a gente iria ter o hands-on, mas a gente fez aí a passagem. Então, os técnicos aí, Oo Bergo e o e o Felipão aí também estão de prontidão aí para tirar as dúvidas, pessoal.
03:50 Felipe Carpanezi: O que vocês tão vendo a minha tela aqui já?
03:51 Israel Antonio Pereira: Beleza.
03:53 Eduardo Dutra - O2B: O par, estamos sim.
03:54 Israel Antonio Pereira: Ainda não?
03:56 Felipe Carpanezi: No Eu vendo até lá, beleza, não?
03:56 Eduardo Dutra - O2B: Ainda não, boa.
03:58 Israel Antonio Pereira: Agora sim, agora sim.
04:00 Felipe Carpanezi: Bom, pessoal, vou. Vou começar aqui. É até o primeiramente, é prazer em conhecer vocês. Eu acho que eu já tive em alguma outra atividade com a Fernanda, ajudei na questão da tupperware lá, né? Trabalhei já com ela em outra oportunidade, o Israel. Acho que a primeira vez que estou falando, então prazer, eu vou tentar aqui compartilhar com vocês AO que o Andre me passou, assim como vocês já ouviram, não ele.
04:29 Felipe Carpanezi: Ele partiu para um outro, um outro, um outro objetivo aí na carreira dele, né? Enfim, outro desafio, então. Mas ele deixou bem esquematizado aqui tudo para passar para mostrar para vocês, então, AAO que ele já até colocou aqui para a gente De bacana no projeto que foram as pessoas que não é do time que participou logo no início. Aqui, a galera que contribuiu com esse projeto, então a gente teve o Eduardo Dutra aí, né? AO Gustavo como Edu acabou de comentar aí e Welder, que foi o Claudinei, né? Cara, que que trabalhou e fez com que esse projeto que acontecesse, tá, tá? E aí a gente tem aqui já de forma bem Clara e bacana aqui AO projeto, né? Uma visão geral do projeto aqui com os acessos, tá? Deixou os acessos há, segundo que ele comentou comigo também.
05:23 Felipe Carpanezi: Aí já passou os excessos para vocês, não é a? Mas se tiver alguma dúvida, pode me procurar. Ele ainda deixou o contato para eu entrar em contato com eles, precisar de alguma coisa, tiver alguma dúvida, tá? Então aqui a gente tem os acessos, arquitetura da infra-estrutura e as localidades também. A gente tem essa informação aqui na nossa documentação sobre as redes, não é a ele. Ele passou também e eu também tenho isso aqui que ele deixou anotado aqui na nessa estrutura, não é? Passou algumas outras informações que eu posso compartilhar com vocês.
05:55 Felipe Carpanezi: Se não foi compartilhado ainda, tá? A. Então, fora essa essa parte de da lista aqui das redes e tudo mais, ele também deixou aqui para a gente algumas informações sobre sobre DNS, tá? Então está tudo documentado. As máquinas que que foram criadas também ele aqui, ele já deixou bem. Cê paradinho, tá? Os grupos, né? As 2 máquinas aqui pro h, proxi AO grupo aqui de management, né? Então, com todos os ips, as CPU IP, né? EP, CPU, memória, disco, SOE tudo mais da mesma forma, para o grupo de homolog, para o grupo de produção há e também tem até aqui 11 desenho da arquitetura aqui que ele deixou com a gente. Vou até aumentar um pouco para vocês aqui para vocês.
06:48 Felipe Carpanezi: Deram uma olhada, né? Como que está sua comunicação aqui, né? Dos DNS com Farol. Aqui hj proxy e com os clusters k à é uma coisa também que ele já deixou até conectei aqui para mostrar para vocês. Já foi o próprio rancher, né? Acredito que já tenha passado os acessos para vocês também. Caso não tenha, a só me falar que que há, eu corro atrás e passo, mas acredito que sim, né?
07:14 Israel Antonio Pereira: A Passou, não, ela traz. Machuquei?
07:16 Felipe Carpanezi: Do os acessos já foram passados, né?
07:18 Eduardo Dutra - O2B: Do hacker, não.
07:20 Israel Antonio Pereira: Não, não, aqui não.
07:20 Felipe Carpanezi: Doente ou não?
07:20 Eduardo Dutra - O2B: Smart Renan um beleza. A gente passa ali por e-mail.
07:24 Felipe Carpanezi: Tá bom, é, a gente passa pra você, tá, tá?
07:25 Israel Antonio Pereira: Beleza.
07:26 Marcus Bergo: Intec?
07:28 Felipe Carpanezi: E aí a no, no ranger. Aqui a gente já consegue ver também, né? O. Os ambientes aqui que ele criou, ele também até comentou aqui que ele já deixou um teste aqui funcionando de uma aplicação aqui, deixa eu mostrar para vocês aqui que foi. Ele colocou um em Jinx mesmo aqui para teste, não é? Ele deixou funcionando aqui, caso vocês queiram, já sim, veio funcionando. Enfim, né? Já deixou habilitado aqui não é um teste para vocês, então a eu tenho essa planilha aqui também.
07:59 Felipe Carpanezi: É onde ele deixou bem Aonde ele deixou bem é destrinchada aqui. Algumas informações dos clusters que ele criou, né? Então eu tenho aqui OOO De homologue, tem o management? Tenho de Project também essas 2 máquinas aqui, né? São as 2 h. Prox tá, tá, Eu Acredito tá que é? Todas as informações que vocês precisarem, a gente tem documentado hoje também. Aqui ele deixou certinho e também é um ambiente aqui que eu preciso passar para vocês aqui.
08:29 Felipe Carpanezi: A questão da a dos acessos, Eu Acredito que seria isso da minha parte para mostrar e compartilhar com vocês a do trabalho que ele fez, tá? EE. Vou abrir aqui para para perguntas para questionamento, se vocês tiverem alguma dúvida, enfim.
08:48 Eduardo Dutra - O2B: O pessoal, um ponto também para levantar é Israel, é ele enviou, é um e-mail.
08:49 Israel Antonio Pereira: Beleza.
08:55 Eduardo Dutra - O2B: No dia 18 de julho é um título, acessos, ferramentas, mais orientações. É nesse e-mail não consta a os acessos para o rancher.
09:04 Israel Antonio Pereira: Você dá uma Dá uma olhadinha aqui. Espera aí.
09:07 Eduardo Dutra - O2B: Porque pelo que eu estou acessando aquele, ele colocou, é em anexo, ali em PDF e também em ponto. IA mal para poder acessar lá, Oo rancher também. Os usuários ali, sem aquele, criou. Foi no dia 18, às 14 e 14 da tarde.
09:29 Marcus Bergo: É, eu vou passar aqui. Eu vou passar Só deixa eu ver aqui. É? Meu. E? Um. Acessos?
09:55 Felipe Carpanezi: Oi, Israel, se você precisar também aqui, eu tenho os seus acessos, tá? Os
09:57 Marcus Bergo: Acho A senhora.
09:59 Felipe Carpanezi: Ele deixou aqui é tem os seus acessos aí do do rancher tudo mais, tá bom?
10:01 Israel Antonio Pereira: Aí? A. Achei aqui do Welder, né?
10:08 Felipe Carpanezi: Isso.
10:09 Israel Antonio Pereira: Eu amo você saltar smart.
10:10 Eduardo Dutra - O2B: Isso. Aham. Boa.
10:13 Israel Antonio Pereira: Bem, choveu PDF aqui.
10:15 Bertino Algebaile Da Silva, Fernanda: De toda forma, é Do no final aqui desta sessão, eu vou passar um e-mail com a gravação, né?
10:15 Marcus Bergo: É?
10:15 Eduardo Dutra - O2B: Isso. Aham.
10:15 Felipe Carpanezi: Oo.
10:16 Israel Antonio Pereira: Tá, beleza.
10:22 Bertino Algebaile Da Silva, Fernanda: Avô, anexar a gravação ou botar link? Depende do tamanho e aí vou pedir em resposta pra vocês.
10:26 Eduardo Dutra - O2B: O.
10:30 Bertino Algebaile Da Silva, Fernanda: Anexaremos acesso se a documentação da do do ambiente para ponto que aí fica tudo num mesmo e-mail show.
10:33 Eduardo Dutra - O2B: Sim, o RU não pode deixar.
10:34 Felipe Carpanezi: Não é bacana, o run.
10:36 Eduardo Dutra - O2B: Sim, não, tranquilo, beleza.
10:42 Marcus Bergo: É de você que eu não estou no. Eu estou com domínio diferente, então estamos chat para mandar mensagem.
10:53 Israel Antonio Pereira: Um.
10:54 Marcus Bergo: A deixa eu ver como é que eu vou fazer aquilo quando a mensagem. Não tem como mandar mensagem.
11:06 Felipe Carpanezi: Você vai fazer o que agora?
11:07 Bertino Algebaile Da Silva, Fernanda: Qual Aumentar. Agem que cê quer mandar.
11:12 Marcus Bergo: A Amanda hoje, quem quis aqui com um sumário? Mas só um segundo. Oi.
11:18 Bertino Algebaile Da Silva, Fernanda: Daí daí. Não IA falar?
11:24 Israel Antonio Pereira: Vou conseguir lugar aqui no ranger.
11:27 Felipe Carpanezi: O.
11:27 Israel Antonio Pereira: É, aí eu tenho algumas dúvidas, como referenciar ao ao Painel de gerenciamento aqui, uma vez que a gente usava, pois CS então muda um pouco aqui o conceito em principal mesmo, mas o lugar das coisas eu tenho algumas dúvidas com todos variáveis de ambiente, porta, entendeu?
11:42 Felipe Carpanezi: Entendi, mas De compartilha com a gente no momento favor.
11:42 Marcus Bergo: Assim.
11:46 Israel Antonio Pereira: Isso não quer dizer que.
11:49 Marcus Bergo: É assim, é dá uma explicação inteira do Da de todas as funcionalidades. É. Porque Tem que olhar também.
11:59 Israel Antonio Pereira: É, vou.
12:00 Marcus Bergo: É que eu estou sem acesso, mas conforme você vai tendo dúvidas, é.
12:02 Israel Antonio Pereira: Eu.
12:07 Marcus Bergo: Você Se você quiser a cara, pode até pegar meu WhatsApp. Para.
12:13 Bertino Algebaile Da Silva, Fernanda: Não, mas vamos tirar o máximo de Do
12:13 Israel Antonio Pereira: Eu vou comer a.
12:16 Bertino Algebaile Da Silva, Fernanda: Não, mas vamos tirar o máximo de dúvidas.
12:17 Marcus Bergo: A? Não é? Sim, sim, mas é.
12:17 Bertino Algebaile Da Silva, Fernanda: Agora vamos fazer, né? O hands-on aqui, sim.
12:18 Marcus Bergo: É que eu é que eu quis dizer o seguinte, é a pergunta é muito aberta, entendeu?
12:18 Israel Antonio Pereira: Mesmo daqui?
12:24 Marcus Bergo: Seria quisesse perguntar, como é que eu faço deploy ou como eu faço?
12:25 Bertino Algebaile Da Silva, Fernanda: Perfeito.
12:29 Marcus Bergo: É o push para o registro. Eu coisa assim, aí é mais acionado, entendeu? Como é que é diferente a diferença de ter nem é Nanci.
12:36 Israel Antonio Pereira: Isso. Quanto tempo da minha casa durar, tem?
12:40 Marcus Bergo: Essas coisas assim é isso. Daí eu posso quebrar aqui para você, não segundo aqui.
12:43 Israel Antonio Pereira: Eu vou comer o pão, já fui lá na frente lá, mas eu vou começar pelo básico aqui.
12:45 Marcus Bergo: Que até porque eu tenho que olhar?
12:47 Israel Antonio Pereira: Eu quero fazer o deploy nesse imagem como ali, no chat aqui. Como que eu faço para dar o qual que é o Regis try? Como que eu faço para subir essa imagem, publicar lá, fazendo a pular?
12:53 Marcus Bergo: É? É. É.
12:58 Israel Antonio Pereira: Entendendo loucura de comer tudo.
12:59 Marcus Bergo: É, vou ver aqui. Eu tenho Você tem que olhar pra morar também. Eu tenho que olhar numa outra. Eu também não estou no meu p. Eu estou sem usar acessos ainda. Gente, perdão.
13:11 Israel Antonio Pereira: Beleza, beleza tranquilo.
13:12 Gustavo Esser: Pode Deixa eu compartilhar a tela aqui que vocês pessoal, minutinho, eu já mostro essa pá muito bom, boa tarde aí, pessoal.
13:16 Eduardo Dutra - O2B: Boa.
13:20 Marcus Bergo: É?
13:22 Israel Antonio Pereira: Boa tarde, gente, se vocês puderem me orientar, eu fazer aqui, acho que é melhor.
13:22 Gustavo Esser: Bom para quem não me conhece. Aham, não pode ser Anrão pode ser, mas é.
13:28 Israel Antonio Pereira: Toda vida mudou.
13:28 Gustavo Esser: É bem tranquilo, acho que é mais fácil dar um overview do ranger primeiro. Bem tranquilo, é Aí a gente faz, aí eu faço contigo e aí você quero te mostra aqui.
13:33 Marcus Bergo: Meu Deus.
13:33 Israel Antonio Pereira: Show de bola tocando.
13:37 Gustavo Esser: Bom, o rancher. Bom, primeiramente, né? Pessoal que não conhece o Gustavo é, tô aqui à frente hoje do time de plataforma de engenharia aqui da da o To Be a. Hoje, toda a parte de deploy do RKE parte de deploy de clusters. Um crime, se hoje ela tá sob a minha responsabilidade, esse projeto não foi diferente, né? Então, só para contextualizar, a gente tem 3 clusters aí a cober net. Todos eles já estão, não, 28, tá é o processo. Ele já segue o padrão do RKE 2, que acho que a gente tinha conversando ali na.
14:05 Gustavo Esser: Nas questões de pré-venda é e o grupo de nós? Ele foi muito definido aí com vocês, né? É, mas hoje a gente tem aí basicamente a, por exemplo, em management, e a gente tem 9 nós, né? Então a gente tem 3 nossa e desde de cá, dos ao elástico, que ao elástico é a parte do que banais elastic surge, logs, teste toda essa. Esse, essa, essa Stack De de serviços.
14:29 Marcus Bergo: Uma Multi usar, não.
14:30 Gustavo Esser: E aí a gente tem a parte do uma máquina reservada por Harvard, que é a parte do contêiner. Registro, né? Que vocês vão utilizar aí de maneira privada é? Ele é bem similar ao ao ECR Da da Amazon. Não sei se já utilizaram a também. A gente vai passar o login aí na sequência, AE aí, basicamente ele tem uma série de filtros bem legais que também a gente pode marcar um segundo bate-papo só para falar sobre ele que ele. Ele é bem extenso, mas o hardware, basicamente essa parte de contêiner, registro e aí a gente tem 3 máquinas reservada. Saí pro master.
15:01 Gustavo Esser: Aonde estão? AA partir do dos serviços do master do **, bernette, né? A partir do clube que ai coordene esse kube proxy, toda essa parte do dos componentes do ** bernette que rodam no master e tcd, né? Ao todo, a partir do controle Ou todo o partido? Control plane. A gente tenha partidos works, né? Que são as máquinas, as máquinas aqui do sistema private que são dedicadas ali ao ao e presente, né? Que Sao certo? Manjeri futuramente, se vocês quiserem colocar um lixo, alguma coisa nesse sentido, a ferramentas de gestão ali do sistema, né? Então vocês vão poder utilizar essa tag e sempre, quando vocês fizerem deploy a no cober net, vocês vão ter que passar essa label, né? É identificando o grupo que você quer que essa que esse recurso suba, né? Vou pegar um exemplo de produção aqui e até para a gente a passar pela interface do rancher amp.
15:50 Gustavo Esser: Basicamente nessa tela principal a gente tem os 3 clusters a entrando aqui em management, por exemplo, a gente tem aqui a parte dos demais, passei e ele tem um recurso a mais, é o coubert nets. Ele trabalha no sentido de organização por nem espaciais, né? AO rancher, ele agrega um a mais, porque. Porque ele tem toda a parte de projetos atrás dele, não é? Então toda essa parte de projetos, então, por exemplo, eu posso criar um projeto aqui relacionado a minha aplicação é XTT.
16:19 Gustavo Esser: Ó, por exemplo, né? E eu quero, por exemplo, que um usuário específico tenha permissão de owner, né? Então eu não sei qual os usuários estão criados aqui. Deixa eu tentar listar AA que Israel estava estava legal, então eu posso dar permissão exclusivamente para esse projeto, não é? É, e aí? Dentro desse projeto, ele vai estar listado aqui embaixo. Eu consigo adicionar um espaço, né? Então, por exemplo, eu posso pegar esses nomes. Passei aqui do elástico Islas tech.
16:44 Gustavo Esser: Eu posso E eu posso mover para dentro, aqui do meu XPTO, né? Posso simplesmente fazer isso aqui, né? E aí, só quem tiver permissão nesse projeto aqui vai ter visualização nesse nesse espaço, então ele tem esse recurso a mais chamado projetos que não é um recurso do bernette. SIM, 1 recurso do ranger a para gerenciamento, de permission amento. E os demais. Passei, eles estão. É, eles são já um conceito do cubo net de organização, né? Então, dentro do dentro de um projeto, vai ter um Lemos passei, tá? Então é bem importante esse ponto aqui, porque futuramente, quando vocês quiserem gerenciar permissões, é dessa forma que vocês vão fazer AA partir de cluster de projetos.
17:22 Gustavo Esser: Aqui a tem a basicamente as pessoas que têm permissão na mento, né? É em quais projetos essas pessoas é? Qual que é o nível, né? De de permissionário que ela tem dentro do projeto, a então basicamente AA gente consegue atrelar uma pessoa, um cluster, né? A parte de gestão de usuários, ele está numa aba aqui apartada, que é a parte de usuários, autenticação, e aqui eu posso adicionar um usuário, né? E também AO que a gente costuma fazer muito é fazer a parte do half provider, né? Que é basicamente aqui, a parte de você integrar com Elda π um Active directory, caso vocês têm alguma coisa nesse sentido, o próprio Google aqui clock todo. Esse. Essas técnicas ferramentas é o da p.
17:59 Gustavo Esser: Que a gente consegue fazer essa integração para você gerenciar isso a nível de organização, né? Não sei, é o que que vocês utilizam hoje se utilizam. Esse modelo é, mas futuramente, caso vocês queiram integrar, é bem tranquilo também, por exemplo, da pessoa você passar as informações ali relacionadas AA partir de grupo. É a partir de atributos lado AD também é bem similar. Como você entrega qualquer outra ferramenta ali de de de autenticação a vocês conseguem fazer por aqui se não você pode criar usuário diretamente aqui no ranger e permissionário da maneira que você quer, né? Então há quero que o usuário de usuário lado deve lá da minha Squad, tenha permissão, por exemplo, só em homolog, né? Um usuário mais Junior é um usuário mais pleno. Ali tem a permissão numa determinada feature.
18:42 Gustavo Esser: É, eu consigo que ele tenha consigo dar essa permissão aqui, descendo um pouco aqui a gente tem a parte de eventos, né? Então, são eventos relacionados ao cluster, então, a se der alguma falha, alguma coisa nesse sentido, ele vai estar listado na aba de eventos e também vai estar listado aqui nessa interface principal que a interface do cluster, que tem uma série de informações, não é? Qual que é o provider que ele está utilizando? Qualquer versão do ** Bernardes quando que ele foi criado? O total de máquinas total de deployments, toda a parte de é capacete aqui do cluster, né? É os eventos e os alertas também, que daí é um ponto que a gente fala na sequência, falando um pouquinho de prometer os ali a descendo aqui tem a parte da das 10 do graf Anna, mas aqui é um ponto que a gente fala na sequência aqui, quando eu passar pela água do prometeu por Claude, né? Então, a diferente, um pouco do e CS lá que a gente tem as testes, né? No **, bernette.
19:31 Gustavo Esser: A gente tem a questão dos workload, né? Os tipos de workload, então que a gente que a gente tem a gente tem ali OA parte do cron job tem a parte do daemon. Set do deployment dos t fun 7 dos jobs, né? Para gente ter uma série de De A gente tem uma série de de tipos de workload, não é isso aqui vai variar muito no quando vocês trouxerem aplicação de vocês para cá, a os 2 mais usados aqui seria o deployment full set, então é basicamente o os 2 principais aqui. Esse aqui é um conceito do ** bernette, mesmo cada cada, cada work load do cober net ele tem AA sua personalidade, como você já me falou alguma coisa.
20:07 Marcus Bergo: A Eva dele Aí a vaga dele. Não é falar para alta disponibilidade.
20:16 Gustavo Esser: Isso. Aham, tem. Tem essa questão da alta disponibilidade, né? Um é, por exemplo, aqui o Steel set é o Da emo 7, né? O replicate, como pessoal, chama ele, por exemplo, roda é um, pode em cada uma das máquinas do cluster é. É, tem também ali, a partir do Steel set, né? Tipo que permite que você execute é um ou mais pode, né? É dentro do cluster também com a gente. Trabalha também com a partir do Persistent volume, então é uma é realmente é adequar o cenário de vocês, mas para um cenário mais simples, recomendo utilizar o deployment que AA carga de trabalho mais é mais fácil ali de lidar ela e sem estado e tudo mais.
20:52 Gustavo Esser: Então é bem tranquilo ali de de você trabalhar com ela é, não tem muitos, muitos conceitos ali para, para, para. É, vamos dizer, agregar em cima dela, hã? Então, passando aqui, pelo que Loud, né? Então, aqui também você pode ver que estava no default, mas se eu jogar e não ao namespace daqui, ele vai trazer todos os workload do cluster, né? Então, por exemplo, aqui a deployments, né? Eu tenho, aqui é os meus deployments aqui, basicamente são algumas coisas relacionadas a que ao quieto system, a coisas do sistema, né? Por exemplo, ao certo manager, ao ingressar o cubs, Esther, né? Então, todas essas ferramentas vão estar aqui. Tenho que ver, não aqui também tem o mongo, por exemplo.
21:29 Gustavo Esser: Mongo, aqui é um exemplo de deployment, né? A gente tem alguns exemplos aqui de startups e também, né? Então, como por exemplo posso próprio, plásticos Teca, que é um Steel 7, é, então a gente tem aqui a partir do quê? Tô monitorando. Like system, então existe vários tipos de por que Los? Acho que é importante. Vocês entrarem um pouquinho nesse conceito. Depois, quando vocês fizerem o depois da aplicação para entender qual que faz sentido aí para vocês? Falando da parte do eps, aqui é basicamente um catálogo de de é um charts que a gente disponibiliza, né? Então, para facilitar realmente algumas instalações, né? Então, por exemplo, a quero instalar aqui 11 parte de banco de dados, por exemplo, um database.
22:12 Gustavo Esser: Eu tenho um mongo por aqui direto, né? Então eu posso estar lá por aqui. É mais uma, um plus ali que o que o senhor oferece algumas ferramentas é legal. Senhora, está lá por aqui para testar, né? Era Então, por exemplo, no vector é uma solução. É da própria ranger, relacionado à segurança, ao estilo. É bem legal também para a parte do service mesh e tem a parte dos benchmarks.
22:32 Gustavo Esser: Se vocês precisarem algum dia passar, por exemplo, por uma PSI, ai é apreciar ela RE quer essa parte dos seus 20? Mark é numa simples instalação aqui dos 6 20 mar que ele consegue gerar esse relatório. Integrar é entregar para vocês aí esse esse PDF com o que está provado, que está reprovado ali e as correções também é bem legal, ahn, falando um pouco de service Discovery, né? Descendo aqui, a gente tem a parte da HP, então o nosso horizontal pode altos Calleri a então basicamente aqui é onde você define o seu número de réplicas minica réplica máximas, né? Então, aqui a parte de escalabilidade também, então toda essa parte de escalabilidade do hpa, ela vai estar centralizada aqui, por exemplo, aqui a gente tem um hpa do inglês, né? Se a gente não edite aqui, a gente consegue ter a, por exemplo, definir o número de réplicas.
23:18 Gustavo Esser: Mímicas, o número de máximas, né? Então a gente consegue definir os behaviours aqui também, né? Então é com quais métricas eles vão escalar, né? Então, por exemplo, aqui eu estou definindo que o ele vai escalar quando ele estiver é acima de 50% de uso de utilização a partir de CPU aqui também. Então, é. É bem bacana. A gente tem a parte do inglês aqui também, que é a parte de a vamos dizer se vão expor isso ao ao, ao mundo, né? Então é quando realmente estiver um front end ali para expor nesse caso aqui AO pessoal fez o deploy de um and next. É já com front Zinho dele aqui, ó.
23:52 Gustavo Esser: Informações estáticas AE, aí ele, ele vai ficar aqui? Nessa parte do ingres e toda essa parte de de gestão de URL s, né? A gente tem a parte dos serviços, que é basicamente onde vocês a ele está muito relacionado ao índice também, porque aqui é onde você vai expor a porta do serviço, né? Vou pegar. Por exemplo, isso não de nexo para mostrar como é que fica aqui.
24:14 Gustavo Esser: A então, por exemplo, né? Ele tem aqui o serviço do índio, Nexa que ele está expondo. Só voltar aqui para uma visão melhor aqui a aquele tá expondo o meu serviço, né? Então você está. Eu estou dando o nome aqui pro meu serviço, estou dizendo que ele vai ser exposto na porta 80, né? Então, aqui que você vai passar as informações a seria bem similar ao ao portfólio de é aquele esquema que a gente faz No No docker, né? De de portfólio de lá que você fala qual porta com o serviço a rodando.
24:39 Marcus Bergo: Nós pega.
24:42 Gustavo Esser: É como 11.
24:44 Marcus Bergo: Nessa cega também, para que é muita gente.
24:46 Gustavo Esser: Hã? Não sei se regata. É parte desse ch também, então é bem, é bem realmente você fala, por que que você quer, né? O serviço ali, hã? A gente tem a parte do histórias Da e essa aqui é a parte do services, né? Então, a partida como você vai expor o serviço e como você vai escalar ele vão ficar aqui dentro? A gente tem a parte do histórico realmente Da e aqui a parte, a basicamente de persistência, né? Então, se algum algum contêiner de vocês um dia precisar persistir algum, algum PF, né? Alguma, alguma entrada, ela vai ficar nessa estrutura aqui, vocês podem utilizar também outras soluções.
25:20 Gustavo Esser: É agregadas junto aqui, né? Como por exemplo, a 11 long Horn e você pode utilizar via impedir direto na máquina, né? Você pode mapear o perfil da máquina aqui, então, basicamente essa aqui é toda a classe de histórias, né? E junto aqui com a parte de histórias, a gente tem 11 coisa bem importante, que é a parte dos config maps, né? Que é a parte dos arquivos de configuração, então toda aquela parte de informação que você precisa é pra se passar, é pro teu, é pra tua aplicação.
25:48 Gustavo Esser: Leia ali, como por exemplo, é uma PE uma PE, por exemplo, externa lá que você precisa passar como variável, você vai passar nesse arquivo config map e a gente? A gente tem 2 conceitos no cober Netuno, que é o config map, outro que é o secret secret, Secco, do você passa dados mais sensíveis, né? Então, por exemplo, a URL do banco é usuário e senha do banco, né? Usuários, sempre a aplicação poder conectar no banco, você passa. É como secret, e o que não é sensível.
26:16 Gustavo Esser: A gente recomenda passar a como config map, né? Como por exemplo, uma pia externa pública lá, uma peixe, por exemplo, no Google, né? Que vocês vão precisam utilizar para consumir alguma coisa, então vocês vão passar nessa nesses arquivos aqui. E aí falando um pouco, tem a parte de policy, né? Então isso aqui é é um pouco conceito, um pouco mais avançado, mas é basicamente para você que é apólice relacionadas à segurança, AO cober net.
26:39 Gustavo Esser: Se ele tem um conceito chamado network policy, que é basicamente você, restringir a é o uso, né? Restringir usos ali é do teu, Do no **, bernette. Então você implementa camadas de segurança a nível de network e políticas realmente de segurança, né?
26:53 Marcus Bergo: E é OEO eixo também.
26:54 Gustavo Esser: Pode falar.
26:59 Marcus Bergo: Ele trabalha na cia, mesma camada ela adicionando aí mais segurança com o mutual TLS, e também ele controla acesso de serviços frana, nível de rede e ele também o controle de gráfico de tráfego, né?
27:13 Gustavo Esser: Isso é também.
27:18 Marcus Bergo: Observabilidade 3. Sim, cadê a Da? Para divulgar também o lixo é uma ferramenta bem bem ampla na ela dá pra?
27:26 Israel Antonio Pereira: Eu gostei O que é você?
27:28 Marcus Bergo: É, já dá pra você fazer vários tipos de deploy, né? Como Canary que você faz o deploy para 11 percentual seus clientes para testar o blue green, que na verdade se faz acesso a 2 versões. É uma nova, uma velha e. Como Observabilidade, né? Telemetria, dashboard.
27:55 Gustavo Esser: Boa.
27:56 Marcus Bergo: E também acho que tem hit, limite também uma coisa assim.
28:00 Gustavo Esser: Isso, hã. Hã? Tem parte de hit, limite é, é basicamente, ele tem uma série de funções bem legais. Aí, partir do moto TLS é. São recursos bem avançados ali de comunicação entre, pode e tudo mais, né?
28:12 Marcus Bergo: É?
28:13 Gustavo Esser: É, e essa parte do network policy é mais antiga, né?
28:14 Marcus Bergo: Mas é.
28:17 Gustavo Esser: O recurso mais antigo ali, mais antigo, não? Mas ele é mais. É, ele é pouco utilizado ali, mas utilizado em cenários realmente que você precisa isolar alguma coisa ali, a de comunicação, a nível do cluster, tudo mais, né? Então ele. Ele é um conceito um pouco a que hoje, por exemplo, estou consegue atender melhor e atender de uma maneira mais fácil, não é, hã?
28:40 Israel Antonio Pereira: Vou Gustavo esse esse policy limite, ranger, limite ranger.
28:40 Gustavo Esser: Um dos Uns boa.
28:45 Israel Antonio Pereira: Se ele é só a nível de cluster, ele vai a nível de pode também.
28:47 Gustavo Esser: Ele pode ser a nível de pode também, tá? Ele pode ser a nível de pode, ele pode ser.
28:50 Israel Antonio Pereira: A bacana?
28:52 Gustavo Esser: É o coubert net. Ele trata a arquitetura dele, ele é baseada não em camadas, mas ele tem um nome que agora me me fugiu. O nome conceito de arquitetura do governante, mas ele trata de cada componente do cober nets ali, a como modo que você consegue isolar, né? Então você consegue isolar, por exemplo, comunicações até nível de pode, né? Então você consegue fazer a distribuição do, por exemplo, da comunicação ali, a nível do do pode também é? Não só a nível do clube, do do do espectador SPACE que você comete, seria o Lemos.
29:20 Israel Antonio Pereira: Work SPACE, não. É o espaço é um pouco mais amplo que o namespace.
29:26 Gustavo Esser: Passei, é o nimes, passei. A esse Do rackspace eu não, não me recordo, mas a nível de namespace ali, ele. Ele consegue, hã, a nível do Do nem, especially ele consegue.
29:37 Israel Antonio Pereira: Está Tá, beleza.
29:40 Gustavo Esser: Ele tem algumas default por aqui, né? Mas é realmente só alguma coisa que eles ele cria ali por padrão, na hora da implementação você consegue trabalhar com cotas também, então você consegue limitar ali a parte é, por exemplo, a quero limitar é a criação de um meme. SPACE, né? Então eu vou pegar um exemplo aqui, obviamente, AO melhor cenário, não é você criar um meme espaço por aqui? Você criar na mão, né? Mas, por exemplo, quero fazer toda essa parte do limite.
30:05 Gustavo Esser: Aqui eu consigo também, né? Então eu consigo falar aqui que é esse nome SPACE, ele vai começar com reservado, sem me vai ter de memória aqui 256 e aí ele pode chegar, por exemplo, meio corte que pode chegar a 1000 GB, que também a então eu consigo criar essas policy também De é limite, não é de limite de recursos também.
30:27 Gustavo Esser: Esse é um ponto legal. Geralmente a gente trata isso ao nível de aplicação e nunca trabalhei num cenário que a gente utiliza a nível de namespace que nem a gente está fazendo aqui, mas depois eu mostro um cenário ali, com um arquivo de deployment. É boa, vamos, tem bastante coisa pra gente falar, mas vamos para o partido monitoring aqui. Por padrão a nós, até que ela já vem integrada a parte do monitore, e aí eu preciso mostrar uma coisa pra vocês, pra fazer sentido antes. Deixa eu só acessar o nosso site. Lábio aqui.
30:57 Gustavo Esser: A? Smart ruim aqui, beleza, esse carinha aqui, hã? Dentro do repositório de vocês é, a gente colocou um arquivo lá em cada um dos clusters, né? Eu vou pegar, por exemplo, aqui o De homolog e aqui dentro do tools, não sei se está aqui dentro de eu ver, tá? No system, nós não está no sistema também te pegar aqui. Onde que fica o. Aqui, prometheus, eztec à tá dentro do sistema, hã? A gente colocou lá os a parte dos alertas, então basicamente a gente tem um modelo de implementação utilizando prometeu, né? Então o prometheus, ele fica tudo nessa interface aqui do monitore, né? É, e aí a gente tem aqui as URL s para, por exemplo, você quer chegar lá na? No prometheus é no Graph, Na Na gráfica, ele e você consegue chegar nesse carinha aqui, né? Mas pra facilitar essa parte de alertas e tudo mais, a gente criou esse carinho aqui, né? Então, por exemplo, aqui está toda a parte de alertas relacionados.
31:54 Gustavo Esser: Ele está dividido em 3 categorias, containers cober. Nesse nomes, falando um pouco de contêiner, ele vai pegar toda a parte realmente de contêineres, né? Então esse aqui é uma regra que a gente criou, por exemplo, pra quando pode bater 85% de uso. Vocês souberem disso, né? Então, claro, isso aqui, depois a gente pode personalizar. É bem tranquilo, é só realmente alterar os parâmetros nesse arquivo de configuração e dar um cube.
32:17 Gustavo Esser: Aplicou carregar o arquivo ali no lixo que ele já vai estar valendo, tá? Então, basicamente aqui a gente tem toda a parte de alertas relacionados AA basicamente aqui seria um p 2, né? Então a gente tem aqui um p 2 relacionado a 85% e a gente pode ter um p um aqui relacionado a 95% de uso de CPU, né? Essa severidade a gente passa por aqui também, ó, tem a gente, pode passar a outras.
32:42 Gustavo Esser: Lei, bolsa aqui, né? Mas o que a gente costuma utilizar é o tipo e a severidade AE aí ele vai bater aqui nessa, nessa, nesse alerta, caso ele tenha essa essa utilização, né? E aqui tem uma série de alertas, né? Tem relacionados à memória no mesmo sentido, né? Na mesmo parametriza ção a quando o pode, ele não está rodando, né? Então ele está no status, no Twitter ou por algum motivo ele parar de funcionar, ele vai trazer um alerta também.
33:08 Gustavo Esser: AA partir de réplicas mínimas, né? As vezes ele tá, ele não Às vezes ele está. Ele não está aqui no número de réplicas mínimas possível, ele vai trazer um alerta também a então a gente mapeou, a gente tem é mapeados em todos os erros que a gente pega constantemente na nossa operação e transformou ele num alerta. Então isso aqui tem é quase que anos aí de de filtros que a gente vem fazendo e refinando a para chegar no cenário mais adequado possível, a de de cenários que podem é dar problema no governantes, não é? Então, por exemplo, o bipe aí fora, cor DNS, fora state o state metro, fora over commit, né? Que acontece com uma certa frequência.
33:45 Gustavo Esser: Memória over commit a partir de disco, né? Então, pô, tá, tá. É abaixo de 20 GB, é tá menos de 10%, né? Tal ou abaixo abaixo de 20%, menos de 10% a que AA gente tem alertas também já a De outras stacks, né? Como por exemplo, o ingresso. Então a gente tem aqui é falhas que podem vir a acontecer. No ingress, certificado expirado é uma coisa que a gente pega também, que é dificilmente a gente vai ter problema com isso, porque o certo menger a eu não sei se vocês conhecem, certamente, mas depois a gente pode falar um pouquinho. Ele trabalha com essa renovação automática, então ele dificilmente ele deixa isso acontecer. Então, nesse cenário nosso aqui, ele não vai ter tanto esse problema. A quantidade de erros 500.
34:25 Gustavo Esser: Tem, então tô tá tomando muito erro. 500 ali no inglês, ele vai reportar isso para gente. Erro 400, a gente tem alguns alertas que estão é comentados aqui. Eles estão relacionados a backup e a gente pode ativar também a click. Luke, eu acho que vocês não tem ali, então a é está está desabilitado. Rabbit Mikel, né? Se vocês utilizarem alguma coisa no futuro, tem alguns alertas aqui para o padrão, né? Então, realmente já já fica na eztec aqui. Redes também é um exemplo. A então tem uma série de alertas aqui que a gente precisa que, caso a gente precise só realmente habilitar.
34:59 Gustavo Esser: E esses que estão aqui já estão habilitados, tá isso falando?
35:02 Israel Antonio Pereira: Esses alertas, eles têm alguma ação de reciclagem do do pódio? Alguma coisa assim, ou ele é só um alerta e a gente tem que Marcelo, ou Da pronto matizar na casa?
35:09 Gustavo Esser: Não, ele é ele. Ele, nesse momento, ele é só um alerta, é AO que que a gente pode fazer AO que a gente costuma fazer, né? A no nosso cenário é a gente enviar esse alerta, a De pegar aqui Deus e se ver aqui alerting aqui, routers aqui que a gente costuma fazer a enviar esse alerta de alguma forma, não é? Então, pô, seja via e-mail, seja via através de um open Sidney, um PG Alves.
35:40 Gustavo Esser: Leque, né? Um canal de comunicação no Teams, alguma coisa assim, então a gente tem integrações que a gente já fez, né? Para a pessoa receber esse alerta, mas ele não tem nenhuma ação, né? Então, por exemplo, se um pode estar batendo ali 85%, ele vai emitir aquele alerta, pode ser que a esse p 2 não faça sentido. Agora que ele vai ficar só o alerta ali não é bem similar ao sabe que não é aquela interface antiga do sabes que o alerta pingava lá e ficava lá até eles se resolveu você resolver, não é? É, e aí? OP. Um, por exemplo, a eu quero que todo OP um chegue para mim no meu canal do Teams, por exemplo, não sei se utilizam a isso.
36:14 Gustavo Esser: É Tim, seu slack, mas por exemplo, eu quero viar lá pro meu slack para um canal específico. Eu consigo realmente enviar, pegar esse alerta, enviar para aquele canal, aduz. Leque e aí eu tenho que tomar uma ação manual em realmente sentar e resolver ali, né? Ele não tem. É uma ação de correção, né? Ele é realmente só 11. Alerta ali é para uma tomada de ação manual, né? Ou é? E aí falando em automação, né? AA gente pode A gente pode ter cenário de automação no futuro, como por exemplo a, sei lá tem um a. Não num cenário de a agora me fugiu o nome da ferramenta, ela que faz umas ações bem legais.
36:54 Gustavo Esser: Eu Hands to, né? É, pô. Me fugiu agora o nome, mas tem uma ferramenta. Tinha bem legal. É que você consegue deixar aí scripts prontos para executar, né? Hã? E aí nessa, nessa ferramenta, eu posso ter sim a, por exemplo, fazer o que? O que que Com que determinado alerta, né? É quando esse alerta acontecer, por exemplo, ele executar uma ação ou ele aumentar o recurso diminuir, né? A então eu posso ter algumas automações, mas aí eu estou falando, André, que isso?
37:19 Marcus Bergo: É o renda que houver dade.
37:23 Gustavo Esser: André, que é ele, ele já é.
37:23 Marcus Bergo: Ele foi adquirido agora pela empresa lá do e-mail a do Sandy.
37:30 Gustavo Esser: Acende Sendmail boa.
37:31 Marcus Bergo: E-mail, tá, mas é tá na mesma empresa.
37:34 Gustavo Esser: Legal, boa é o onde é que o pessoal costuma utilizar bastante para esses cenários? Mas assim, esse. Esse aí já é um cenário um pouco mais elaborado, né? A gente tá falando de automação, é? Tem que ter cuidado também com o processo que vai ser executado, porque é tipo a beleza bateu 95% ali, ou será que é o melhor cenário?
37:43 Marcus Bergo: É? Exato.
37:52 Gustavo Esser: Reis tartar, tudo num às vezes não, porque tem a realmente tem que estão ali, por exemplo, de pessoas conectadas na aplicação. Então, esse cenário de autor de automatização eles tem que ser bem elaborados, bem pensados e é uma coisa que leva um pouco mais de tempo que realmente, às vezes é.
38:06 Marcus Bergo: É?
38:07 Gustavo Esser: Não faz sentido. RE startup não é tudo o cenário ali.
38:10 Marcus Bergo: É, não, eu sei que não vem ao caso agora, mas talvez para a situação, não sei se você já ouviu falar do cônsul da resposta.
38:17 Gustavo Esser: Como ser Você é legal também.
38:17 Marcus Bergo: Ele. É, mas depois a gente fala disso, beleza?
38:22 Gustavo Esser: Boa é tem. Tem cenários bem legais aí, que dá para fazer, mas aumente assim. Solução realmente não falta. O cônsul também é uma boa, mas é tem que ser tomar um certo cuidado ali, porque qualquer ação que é feita ali pode pode gerar um problema, né? Então geralmente a gente executa de maneira manual mesmo a. O meu Como eu tinha a pode considerar a tá bom? Possível mensagem que mais tranquilo. Bom, basicamente dos alertas, é isso, então a gente pode configurar.
38:52 Gustavo Esser: Depois dessa parte ajudar vocês, né? Configurar essa parte de à quero receber via e-mail quero receber via é lá que eu IA tins ali, então é bem tranquilo. E aí, falando do voltando a falar dos alertas aqui rapidamente, a gente tem então a nível de contêiner, a nível de Cuba e a nível de números, né? Então a nível das máquinas ali, né? Então a máquina está batendo 85%, tá batendo 90, tá batendo todo esse cenário de utilização AO, por exemplo, a máquina ficou fora, né? Ou está com os De disco muito alto, então ela tem uma séries aqui, tem até é alertas relacionados ao i know, disse. Aqui, então tem uma série de alertas mesmo até de ntp, não sincronizado, que a gente mapeou também.
39:31 Gustavo Esser: Já foi problema, então isso aqui são alguns alertas, esses alertas, eles podem é variar. Também é de prioridade. Só que depois essa documentação vai se mandada para vocês. E depois vocês precisarem de ajuda para refinar por pessoal. Não, não gostei aqui. Acho que isso aqui não faz sentido. CP 2, ou isso aqui não faz sentido? CP um, ou quer aumentar o 3 shows, né? Quero deixar ali a 95%. Quero diminuir, aumentar isso aqui. Depois a gente ajusta com vocês. É bem tranquilo. Se precisarem ajustar também é. É realmente é só mudar o parâmetro aqui e aplicar. Não tem muito, o erro não está bem tranquilo. A gente tem uma série de testes, é para.
40:08 Marcus Bergo: Roubar, que também.
40:11 Gustavo Esser: Como?
40:12 Marcus Bergo: O back Rubex.
40:14 Gustavo Esser: Legal, o ruim também, hã? A gente tem uma série também de 10 x aí que a gente irá imputa lá e aí eu vou mostrar aqui na, Na Na tela que fica mais legal monitoring aqui novamente. E aí a gente tem aqui o graf Anna, né? A prometheus, ele. Ele tem uma sintaxe aqui para você fazer uma quer e não é, então você consegue trazer, por exemplo, uma carinha aqui. Depois vocês vão ver que não é nada muito difícil. É bem tranquilo de fazer.
40:42 Gustavo Esser: Daí ele traz a partida desta aqui, mas o legal, a Do prometheus, é você realmente entregar? É entregar, né? Entregar o ta dificil hoje, mas fazer essa integração, né? Entre o prometheus e o e o graf Anna, que aí você tem uma série de testes bem legais, por exemplo. Aqui, quero ver a parte de nold, né? Então, tem toda a parte de CPU ZG aqui não é a parte de cotas em toda a parte de do que que está sendo utilizado, né? Então, o que que está sendo utilizado? O que que não tá? A gente tem a parte dos doutos também, que é uma dash bem legal também.
41:13 Gustavo Esser: Deixa eu pegar aqui dos 12, a gente tem a parte do Snowden, né? O que está sendo utilizado ali tem uma série de destas aqui a gente consegue fazer isso por nold, né? A gente consegue pegar isso por qualquer. Consegue pegar até da própria aplicação, então, por exemplo, aqui deixa eu só pagar aqui pegar do deployment. Gostando? Tem deployment general porque por que Luis? Quero pegar, por exemplo, do work load.
41:37 Gustavo Esser: Então quero pegar lá, por exemplo, do meu inglês, não é? Quero ver quanto o meu inglês está consumindo. Consigo ter uma visão aqui de utilização de CPU, memória, networking, então quero ver se está batendo muita requisição no meu inglês. Vai ser por aqui que eu vou conseguir trazer esses dados, né? Então aqui ele pega também no time zone do Brasil. E aí, aqui eu consigo ter um histórico disso aí. A por padrão, a gente está aguardando.
41:59 Gustavo Esser: Se eu não me engano, 90 dias nesse projeto e aí é? Acho que tem 30 e poucos dias que o cluster está de pé, então só vai ter dados de 30 dias aí, mas por padrão, a gente guarda histórico. Se eu não me engano, 90 dias que está definido ali para a gente guardar, né? Depois de 90 dias, ele limpa ali, ele vai limpando, vai deixando somente as Datas dos últimos 90 dias e a gente consegue pegar aí dos nesse período aqui, né? A bom aqui está para a gente.
42:25 Gustavo Esser: Não se delongar tanto, eu vou deixar depois para vocês darem uma olhada nessa parte dos destes, né? Então vai ter uma série de desses aqui. Vocês vão poder a utilizar para fazer trabalho, chute e tudo mais. E essas 10 também está lá no repositório e por padrão, já estão todas implementadas aqui, né? Então, tem a parte também do kube proxy tem do cube pia, né? Então, tem uma série de testes aqui pra vocês importarem. Destes aqui também é bem tranquilo. E a gerenciarem tudo isso é bem tranquilo, hã.
42:51 Gustavo Esser: Em gerenciar E aí depois vocês dão uma olhada nessa parte com calma que aí realmente tem bastante coisa que pode utilizar, né? Que vocês podem utilizar aí pra a fazer parte de trabucho Tim pode importar desta que também tem a parte do tcd aqui também, que é, bem. É um oi. T. CD é um componente muito importante quando a gente fala, principalmente quando a gente fala de cober net é um primas, né? É, a gente está falando de cober net, onde administração dos Masters está sob nossa responsabilidade. Oi, t.
43:22 Gustavo Esser: CD, é como se fosse o coração, né? O banco dessa, dessa, dessa, desse cluster. Então, aqui também tem alguns dados relacionados ao ao ETCD. E beleza, acho que da da parte de monitoramento é isso. Não vou me enrolar tanto que a gente tem bastante coisa aqui ainda. AE, até falando um pouco aqui da implementação, acho que a gente não acabou não passando nela, né? Voltando um pouco atrás, mas deixa eu pegar aqui é bom tudo implementação que nem eu cometi, né? Ela segue utilização é de RKE.
43:53 Gustavo Esser: Ela está toda documentada aqui, né? É o é rica, e ele é só um. Ele é um simples serviço que eu consigo instalar ele com curry, né? E eu consigo passar basicamente o tipo de de de dia. Gente que eu quero que ele está lhe AE, aí eu tenho alguns arquivos de configuração, não é como por exemplo, aqui o do sistema, a LDU harber do elástico, né? Tem aqui o cluster mesmo.
44:15 Gustavo Esser: Então, aqui seria o arquivo de configuração do cluster, né? Então, tem basicamente aqui as minhas CDR aqui que eu que eu defini para esse projeto, tem a alguns recursos aqui que estão desabilitado, alguns estão habilitados, né? Isso aqui são recursos que a gente entende que alguns não faz sentido deixar habilitado, hã? Alguns que a gente deixa desabilitado na instalação, né? Como por exemplo, a gente não, a gente não deixa desabilitado aqui. O indie nex aí eu já vou explicar o porquê.
44:41 Gustavo Esser: A gente já deixa desabilitado quem? Eu também que a gente faz uma instalação à parte AA gente tem um toque, né? Esse token aqui, ele é gerado para você poder ingressar. Mais máquinas no cluster, então já vou mostrar. Na sequência, a até a parte dos novos leitos, né? Que eu comentei lá que as lei busque, cada máquina tem sua lei. Bom, né? Então, por exemplo, sei que é master e a gente tem uma coisa bem legal aqui que é basicamente OOETC, ds, né? Pixote, né? Então, como eu comentei ali do tcd, me recordei que tem esse.
45:07 Gustavo Esser: A gente tem a retenção desses Snap shots na máquina, né? Nesse momento, ele está está sendo tirado e armazenado direto na máquina, mas a gente pode pegar, por exemplo, criar um job que envia. É esse esse tcd nessa? Esse backup DT CD, por exemplo, um bronquite para um banquete S3, hã. E aí que a gente também tem algumas alguns argumentos, né? Que a gente passa aqui reservados porco Bernardes, né? Então, quantidade máxima de podes, memória, CPU a partir de histórias ali para ele consumir.
45:37 Gustavo Esser: Então a gente passa alguns algumas coisas aqui, tá, né? Todo o processo de instalação ele está documentado aqui nesse repositório. Não é nada muito complexo, a então é. É bem tranquilo também. Se vocês precisarem atualizar isso no futuro, é bem tranquilo. AE, aqui está bem certinho. Cada arquivo de configuração de cada ano de grupo que eu comentei lá, né? Então a gente tem os nossos grupos de nossa, cada um deles está aqui.
46:00 Gustavo Esser: EEA gente tem também a instalação do kali cookie, né? Que é o nosso, é CNI, que é o nosso. É container, interface network lá, né? A partir de network do **, bernette, ela é instalado à parte, até porque a gente tem uma série de parâmetros que a gente gosta de passar, né? Então a gente, a gente faz essa instalação à parte, a gente não faz, né? Junto com Junto com a rica e eu comentei também da instalação do inglês, não é? A gente também faz uma instalação à parte do inglês, deixa eu pegar aqui, ó system, aqui inglês, a gente passa uma série de parâmetros, né, né? Desse, desse do ingresso.
46:31 Gustavo Esser: Então a gente tem uma série de recursos aí que a gente passa a que a gente gosta de passar, por exemplo, pra gente não ter entregar isso depois com elástico, para trazer uma visão bem legal de requisições ali que estão batendo No No ingresso. Então, a gente passa essa série de valores é personalizados, né? Então vocês podem ver, por exemplo, que o inglês ele está rodando aqui na parte da das máquinas system in private, né? Hã? E aí, basicamente, toda essa parte, ela está. É. É rodando ali no sistema private, todos os ingleses.
47:03 Gustavo Esser: Eles rodam no system private com esse arquivo de configuração, né? E aí também todo o modelo de implementação, o nosso modelo. Ele segue um modelo de helmi charts, então é bem importante salientar isso, que numa é atualização é bem mais tranquilo de você fazer essa atualização. É, então, você utilizar o char de uma boa prática de mercado, porque você consegue consultar versões, né? Então, a por exemplo, aqui já deixou o comando pra você puxar as versões do ramo chart, né? A gente instalou aqui, por exemplo, na 483, que é uma das últimas versões aí já disponíveis AE aí vocês quiserem atualizar isso futuramente, só realmente alterar esse parâmetro aqui e aplicar o comando de novo, né? Vale vale salientar que, às vezes, pode ter alguma mudança.
47:47 Gustavo Esser: Algum parâmetro aqui mudou, né? Ou às vezes muda o nome? Dificilmente isso acontece no ingresso que ele é uma. Ele é um projeto que é. É bem estável, né? É os comitês, eles. Eles são. É todas releases, né? Dele, eles são seguindo um padrão bem legal. É, então eles dificilmente vai ter problema, não é? Você vai ter Você vai ter esse problema de um parâmetro quebrar, mas em aplicações mais vou pegar um exemplo.
48:11 Gustavo Esser: Aqui, por exemplo, o elástico, né? O certo certo medo de também é. Bem, é bem estável, eles não mudam tanto, mas, por exemplo, o elasti aqui, o hardware pode ser que às vezes eles mudam o parâmetro outro, aí você tem que atualizar no teu arquivo também, porque ele aí ele vai falar esse parâmetro aqui não existe mais. Dá uma olhada no teu velozes aí que não faz mais sentido.
48:29 Gustavo Esser: Hã? Bom, seguindo o mesmo padrão Helm chart. Tá pessoal, então é bem importante. Essa, esse ponto, e aí basicamente todo modelo de implementação a depois a gente vai passar todos os acessos, tudo mais, né? Tem a parte do elástico aqui também temos toda a eztec do elástico, Como Ela É implementada e tudo mais, toda a parte de policy in gestes ali, então, tem bastante coisa para para passar para vocês. É bom, pessoal, acho que eu falei bastante coisa, mas só até agora.
48:56 Gustavo Esser: Tem algum ponto aí? Alguma dúvida relacionada a essa parte da arquitetura do do rancher? Aqui a até pra comentar aqui basicamente de recursos principais são esses, tá? Tem uma série de outros recursos aqui no maior resurs, né? Como por exemplo, certamente daqui AO tenho meu cluster lixo aqui também a é 11 recurso que eu vou utilizar para poder gerar o meu certificado, né? Então eu vou pegar um exemplo aqui só para mostrar para vocês. Deixa eu ver se aqui naquele inglês lá que o pessoal deploy ou esse é o dor deixou o exemplo aqui, acho que vai ficar mais fácil. Espera aí. 8 em cima das mistos, nos que eu não sei se ele deixou aqui em algum lugar um.
49:46 Gustavo Esser: Bom, mas aqui pelo Harbour já vou conseguir mostrar uma coisa, o cenário legal, beleza, a árvore. Ele tem um endereço, tá pessoal, então vocês podem acessar através desse endereço aqui, depois se passar do usuário e tudo mais. E vocês podem ver que ele estava com certificado, né? Então, aqui, basicamente ele está com certificado válido, LED encripta pro certificado funcionar a vocês têm que passar uma annotation, né? Então essa anotation ela se chama, é certo manter? Então, essa certa maneira, um projeto não é um projeto do ali, do boletim cryptic, faz toda essa parte de gestão, de certificados e tudo mais. Projeto bem bacana a gente já utiliza ele aí alguns anos eu aí vai para mais de 10 anos.
50:28 Gustavo Esser: Que que eu utilizo? Ele não, não tive problemas, só uma vez bati no hit limite de geração de certificado. Aqui aconteceu um problema, mas é um projeto bem legal. O projeto bem tranquilo também de de de gerenciar. Aí ele é bem instável também, então ele teve as versões deles. Suporta versões também muito antigas do cobertor ou muito pra frente, então é bem bacana que esse modelo de compatibilidade dele a dificilmente vai precisar atualizar. Ele não é, mas também é bem tranquilo. Se precisar atualizar, não é um modelo de instalação dele aqui, ó, é bem tranquilo. Ele também já segue o modelo de RAM charts. Também é bem legal.
51:03 Gustavo Esser: E aí falando um pouco de como surte cada gerado, né? Então, basicamente, ele tem todo um processo, acho que até na tela principal dele é que ele fala, não é? Então ele pega lá do inglês, né? Então ele gera, ele bate no nosso serviço DNS, ele vê se aquela entrada corresponde ao load balancer que ele tem ali, e ele faz esse desafio. E aí, com esse desafio dando certo, ele consegue gerar o certificado válido aqui, né? Então, basicamente, o que a gente precisa para gerar um nosso certificado aqui é basicamente ter essa anotation aqui em todo o nosso arquivo do inglês, tá? Nosso tipo inglês aqui vai ter que ser passada essa anotation, e a gente tem um parâmetro bem importante também, que é o ingress, class.
51:41 Gustavo Esser: DM, né, que é? Qual que vai ser o meu class? Name é nosso caso aqui, eu De nex, a gente pode ter mais class name, né? A gente pode ter outros. Outras ferramentas que façam essa essa solução para gente, mas a mais utilizada que a gente costuma utilizar é o ingresso tá, que é o que está implementado no cluster de vocês? Beleza e aqui a gente consegue também já ter 11 visão aqui, hã? Por exemplo, do certificado não é? Então, é o ingress clesa que comentei, né? Tem a parte dos leigos aqui, ó. Por exemplo, a lei dos Sergio, ele vai ter que estar aqui com isso. Com esses parâmetros, ele consegue gerar esse certificado. É boa, deixa eu ver se tem mais algum ponto do maior isso.
52:22 Gustavo Esser: Rse tem uma série de recursos aqui, mas a parte de RBAC a tem a parte dos cover. Mas é basicamente, tem bastante coisa aqui que vocês não vão acabar utilizando diariamente. É, dificilmente também vão utilizar a partir do RBAC alguma coisa nesse sentido, mas são recursos que estão aqui, né? São aplicações que estão instaladas ou para para encher aqui, né? A integrações aqui que a gente pode habilitar, você pode ver que eles estão na ativa, mas a gente pode habilitar a IA e cada um tem uma. É, tem o seu. Sua estrutura ali de de.
52:54 Gustavo Esser: É de de configurações, não é? Então ela tem sua estrutura de configurações e aí, por exemplo, o chat aqui tem os rumos que estão instalados e tudo mais, né? É todo o cluster, ele vai seguir essa mesma lógica, tá pessoal? Hã? Então é bem legal aqui essa parte. AE falando um pouco do dia a dia, né? É, vocês vão começar a utilizar o ranger aí a ponto legal, a quero acessar aqui.
53:17 Gustavo Esser: O site major deploy aqui uma aplicação eu consigo ter aqui, visam do meu viu log? Então eu tenho toda a parte de viu logo aqui, hã, deixa eu pegar um que tem a loja aqui, né? Esqueça aqui já está muito tempo criado. Ele não tem nada, só deve ter o log Stardust dele. Cadê aquele aquele inglês, esse cara aqui, hã? Então, tem toda a parte de viu login aqui, né? De requisição, então, por exemplo, se eu quiser bater nesse cara aqui, trazer aqui 11 requisição, ele vai trazer aqui na tela, né? Deixa eu Deixa eu abrir uma outra tela aqui, ó, um Monte de eficiente, ele vai trazer aqui a parte do input do log.
53:52 Gustavo Esser: Isso vai variar da aplicação de vocês também, né? O que que vocês querem imputar no console log? Então, basicamente, o que vocês quiserem imputar no console log, ele vai trazer aqui também, tá? Então isso aqui é bem relacionado a aplicação de vocês. Quero fazer um tribo. Chute, né? É, a gente não recomenda muito, mas quero fazer um trombo chute aqui inicial, né? Ó, quero ver ainda do meu contêiner, quero ver o que que está, por exemplo, a dentro do erci docker entre ponte aqui, né? OPA, docker, docker. Entre ponte por tch, por exemplo.
54:24 Gustavo Esser: Hã? Eu consigo fazer alterar arquivo local aqui sem precisar fazer toda uma Stack de deploy, tá? Eu não sei se vocês estão utilizando hoje. Cenário, a De deploy é esse é um ponto importante. Tem todo falando um pouco de de como vocês vão deploy as aplicações, né? Que era o tema inicial, a existe, toda uma abordagem que precisa ser feita. A gente pode passar arquivos de exemplo para vocês, mas o ideal é que você tenha toda uma eztec, né? É junto ali para construir essa esteira de deploy, não é? Então eu vou pegar um exemplo aqui de um arquivo. Ele aqui Da tema que o rei me recordo fácil, amp. Aplicações aqui, por exemplo, de deploy aqui.
55:07 Gustavo Esser: Aqui tem todo um exemplo de deploy, né? Então, tudo que eu preciso passar para mim, aplicação meu leitos. Passei amp ou o meu nome da minha aplicação não é a imagem ali, então é você, comentou a como é que eu faço ali deploy é utilizando a imagem x pto lá do docker hub. É, então eu votei se arquivo de deployment aqui, o ideal já é. Vocês trabalharem num cenário utilizando Real michard? Está, então a gente pode. É isso aí. Acho que pode ser um segundo momento. Eu não sei se está incluso no projeto, mas a gente recomenda construir um chat do Sophia. São. Não sei se já vem utilizando cober net já esse é o primeiro contato. É, vai, vai ter todo um trabalho para criar esses arquivos.
55:46 Gustavo Esser: Aqui tá, e realmente criar uma Stack diplóide. E aí, vocês deploy harém, né? Tudo. Eu estou desse ponto que eu comentei, a gente consegue vim aqui, por exemplo, criar um pode é utilizando uma imagem simples aqui, então eu posso vir aqui criar um. Pode, por exemplo, aqui com a posso ser contêiner zero, mas por exemplo, de pegar uma imagem aqui do do in box, por exemplo. Ilze box.
56:12 Gustavo Esser: A mais oficial? Posso pegar aqui a imagem do Bill e box, por exemplo, deploy an aqui seria muito simples. Só vim fazer isso aqui, mas não é o cenário ideal, não é? OPA. Ele fala que precisa de um nome, né? Hã, eu igual A ilze box, e aí eu posso simplesmente vim aqui e realmente colocar essa nessa parte aqui. A subiu um contêiner, né? Mas também não é o cenário ideal, tá, pessoal? O cenário ideal é que você realmente tem uma estrutura de deploy, né? Tem uma estrutura ali de de basicamente que vocês consigam entregar aplicações de vocês por aqui. Eu não sei como é que estão isso de vocês hoje.
56:53 Gustavo Esser: Não sei se já utilizam co bernex, né? E aí vou abrir um pouco para perguntas aí só pra mim entender o cenário de vocês também. Eu desculpa, não estava vendo a mãozinha tá daí não viesse porque só levantou ali agora que eu mudei para a tela do tênis aqui.
57:07 Bertino Algebaile Da Silva, Fernanda: Ói, não eu que levantei a pé porque eu fui olhar a hora já me dá 3 e aí assim eu acho que é um tema que não se finda, né? É bastante detalhe, né? E a gente estava numa expectativa de até fazer uma coisa, mesmo executar juntos. Aí eu queria saber se a gente continua ou se de repente a gente pode marcar uma outra sessão dessa para amanhã é mais Na Na prática, queria saber o sentimento aí de cada um, entendeu?
57:38 Gustavo Esser: Boa, boa é. Bom, acho da minha parte é não sei como é que tá a agenda do pessoal ali, mas é da minha parte, é tranquilo, é tem bastante coisa dessa parte realmente teórica do como foi feito. Por que que foi feito? Né? Que é importante a gente passar, é até para vocês terem contextualização essa parte prática.
57:54 Bertino Algebaile Da Silva, Fernanda: Segundo. Sim.
57:58 Gustavo Esser: Ela também consome bastante tempo, então é realmente era.
58:00 Bertino Algebaile Da Silva, Fernanda: E?
58:01 Gustavo Esser: É dividida essas agendas, né? É porque essa parte teórica é importante também para realmente lá na frente de algum problema.
58:07 Bertino Algebaile Da Silva, Fernanda: É.
58:08 Gustavo Esser: Chute, né?
58:09 Bertino Algebaile Da Silva, Fernanda: É exatamente isso, é o que que que tu, que que tu acha?
58:10 Gustavo Esser: É, e aonde?
58:16 Bertino Algebaile Da Silva, Fernanda: Assim, enquanto recebedor da entrega.
58:19 Israel Antonio Pereira: É, então o que que eu acho assim? Hoje foi bacana, né? Explica mais um overview aí da ferramenta das práticas foram utilizadas para implementar.
58:22 Marcus Bergo: É?
58:27 Israel Antonio Pereira: Só que eu tinha uma expectativa de já colocar a mão na massa e subir alguns serviços e replicar alguns serviços que eu tenho rodando em uma locação do meu lado e testar em um blog ação e do lado da Síria.
58:38 Bertino Algebaile Da Silva, Fernanda: EE.
58:38 Israel Antonio Pereira: Aí, como a janela de hoje não foi possível, já gostaria de se possível, se a gente puder marcar uma manhã, que a minha expectativa é talvez até sábado já está com toda a minha oração. Rodela na Cirion, aí eu entorno tem em torno de 100, explica.
58:48 Bertino Algebaile Da Silva, Fernanda: Li, tchau.
58:50 Israel Antonio Pereira: Serviço aí então, por isso eu queria fazer alguns. Aí a 4 mãos. Ele, depois do klement à migração, com time de cintura aqui.
58:58 Bertino Algebaile Da Silva, Fernanda: Você prefere amanhã, então, em vez de continuar agora.
59:04 Israel Antonio Pereira: Pra mim, posso continuar, não tem problema.
59:07 Bertino Algebaile Da Silva, Fernanda: Esqui. Sabem, gente, me falem aí. Onde cada Um de cada vez.
59:14 Israel Antonio Pereira: Ou se quiserem, se o pessoal da Chubb quiser voltar amanhã te marcou o horário e o pessoal já vem preparada pra gente botar a mão na massa.
59:14 Bertino Algebaile Da Silva, Fernanda: Não precisa falar todo mundo.
59:15 Eduardo Dutra - O2B: Ô.
59:18 Gustavo Esser: É?
59:18 Marcus Bergo: Autor. Leandro, colega da área.
59:21 Israel Antonio Pereira: Não tem problema.
59:23 Eduardo Dutra - O2B: Que que tu acha melhor, Gu?
59:26 Gustavo Esser: Para Ora, por mim é tranquilo. Eu acho que a gente pode vocês puderem estender mais uns 20 minutos ali só para a gente terminar essa parte e amanhã a gente já começa essa nova. Da parte do é dessa parte da aplicação de vocês, até pra gente não acabar é envolvendo os assuntos, então é importante também.
59:38 Bertino Algebaile Da Silva, Fernanda: E? E?
59:42 Eduardo Dutra - O2B: Pode ser?
59:43 Gustavo Esser: CS um ponto tá bem lapidado.
59:43 Bertino Algebaile Da Silva, Fernanda: Então vamos isso. Vamos faz assim, fica mais 20 minutos para terminar a parte teórica. Daí vocês me passam a documentação, né? Do do projeto eu passo pro Israel junto com o vídeo dessa sessão de hoje e os acessos bem lembrado.
59:53 Eduardo Dutra - O2B: De meu? Os acessos, o run.
01:00:00 Bertino Algebaile Da Silva, Fernanda: E aí, amanhã a gente volta, que horas para para a mão na massa? Quero que vocês querem que a gente já deixa os negócios, Combinado?
01:00:06 Eduardo Dutra - O2B: Pode Qual a disponibilidade a Israel?
01:00:10 Israel Antonio Pereira: Eu estou por falta do projeto, era que falar entre Marcos. Desculpa no mês pra A desculpa do mês pra mim, pra esse aí. Eu acho que vai surgir mais dúvidas depois que a gente realmente botar a mão na massa e começar a replicar as coisas.
01:00:22 Bertino Algebaile Da Silva, Fernanda: O run?
01:00:24 Israel Antonio Pereira: Conte agora, mas é, eu tenho um conhecimento um pouco básico sobre o bernette ou com o básico sobre ranger, mas é como a mexer no open source, né? O. Esse vocês usam, não há? Então não sei se muda muito, mas acredito que vai surgir mais dúvidas durante a mão na massa mesmo.
01:00:36 Eduardo Dutra - O2B: Beleza.
01:00:39 Marcus Bergo: É, então.
01:00:40 Eduardo Dutra - O2B: Beleza, você acha que uma janela de 1 hora, 1 hora e meia Gu.
01:00:44 Gustavo Esser: É, acho que a gente pode marcar 3, não sei como é que está a agenda de vocês às 3 da manhã.
01:00:44 Marcus Bergo: É, não é assim.
01:00:49 Gustavo Esser: Eu consigo as 3.
01:00:50 Bertino Algebaile Da Silva, Fernanda: 3 da manhã?
01:00:52 Gustavo Esser: Não, não a 6 da tarde.
01:00:52 Eduardo Dutra - O2B: Às 15:00 da tarde?
01:00:53 Gustavo Esser: É 15 É 15 horas. É.
01:00:56 Marcus Bergo: Então eu acho que assim é.
01:00:56 Israel Antonio Pereira: Eu.
01:00:57 Gustavo Esser: Oh, você está bem também.
01:00:58 Marcus Bergo: É. Foi. Foi o que eu falei no início. É. É uma, é um componente que ele, ele tem cursos que demora um Diaz, né?
01:01:08 Bertino Algebaile Da Silva, Fernanda: É.
01:01:09 Marcus Bergo: Para você entender.
01:01:09 Bertino Algebaile Da Silva, Fernanda: É, vamos fazer então amanhã, 3 da tarde.
01:01:11 Marcus Bergo: S.
01:01:12 Eduardo Dutra - O2B: Pode ser?
01:01:13 Marcus Bergo: Está. Está bem completo, então não fique frustrado se não pegar de primeira.
01:01:15 Bertino Algebaile Da Silva, Fernanda: Tá?
01:01:15 Israel Antonio Pereira: Bem perfeito. Não, não, tranquilo, fica tranquilo.
01:01:19 Bertino Algebaile Da Silva, Fernanda: Beleza, então eu vou fazer o convite de amanhã, 3 da tarde, mas vamos terminar então. A teórica hoje pra gente conseguir, né? E de de é é concluindo cada etapa, beleza, vou ficar quietinha de novo.
01:01:33 Gustavo Esser: Show de bola então beleza. Então tá marcado, é bom só pra gente matar aqui. Então, bom, basicamente da parte do ranger, um pouco disso tá? Que nem eu cometei ele. Ele não é uma ferramenta difícil. Vocês vão ver que é bem tranquilo em toda essa parte de gestão ali do swrc load e tudo mais. A parte de gestão dos usuários também pra passar acesso a tem uma série de extensões aqui também que a gente pode habilitar configurações.
01:02:00 Gustavo Esser: Pode personalizar, né? Então, hã. Quero por aqui, quero mudar, por exemplo, a. Cadê? Tem o banner aqui que é legal, aqui tem a parte dos banners, né? Quero mudar logo. Cortam ele. É, bem, é bem legal, eu quero por aqui, por exemplo, a RE encher smart brinco, por exemplo, né? Então quero por aqui, quero que fique dessa maneira aqui. Por exemplo, Martins ruim? OPA, Bruno aqui, deal a quero por minha logo customizado consigo por também. Então depois dá pra vocês brincarem aí e aí ele já fica aqui, por exemplo, com smart brain. Duhem, tira um pouco disso. É, eu vou passar o acesso aí para vocês. A dei uma olhada. Login, podem fuçar a essa.
01:02:42 Gustavo Esser: Não deletem o nem o nem me despeço aqui é tem que ter um cuidado também é com com o nível de comissionamento, né? Porque se eu deletar, por exemplo, aqui AA nível de nimes, passei a se eu pagar, por exemplo, namespace aqui, né? Eu apago toda a estrutura que está abaixo dele, né? O coubert net. Se ele segue uma estrutura ali de errar que a de deleção é, deixa eu até pegar um exemplo aqui, eu acho que eu tenho aqui um desenho bem legal, hã?
01:03:05 Marcus Bergo: Um.
01:03:08 Gustavo Esser: Deixa eu ver se eu acho fácil aqui no meus arquivos. Mas ele tem uma estrutura de.
01:03:12 Marcus Bergo: Estou te olhando os preços. O senhor lembra
01:03:16 Gustavo Esser: Ele tem uma estrutura ali AA nível de deleção que tem que ter um certo cuidado, né? Então, só achar que rapidamente a Da talvez, tipo aqui. Ops, aqui. Ó Correntes Meiji, só aqui aqui achei uma estrutura aqui, hã? A cura Então, aqui é uma estrutura que eu mesmo desenhei. Não tenho nada escrito em Pedra aqui, mas é basicamente uma estrutura similar a isso, né? Então, por exemplo, se eu deletar o no nem ou se eu deleto a nível de lãs, passei, ele deleta o deployment no pódio.
01:03:54 Gustavo Esser: Contêiner seu deleto deployment daqui ele vai deletar o pódio contêiner, né? Então é assim que funciona, né? Então, esse. Esse modelo de deleção, ele tem que ter um certo cuidado, porque tudo que está abaixo dele, ele deleta conseguindo essa estrutura aí de deleção a bom, falando rapidamente, e tem também um outro desenho aqui também, que eu costumo utilizar, né? Que é a parte de escalabilidade do coubert net, é o principal diferencial.
01:04:18 Gustavo Esser: EOO principal objetivo que o pessoal vem migrando para cober net é a questão da escalabilidade, né? Então, claro, aplicação tem todo conceitos, né? Que a aplicação tem que a atingir para ser escalável. Questão de persistência de sessão, aí tem um documento bem legal que se chama é to factor. Se a alguma coisa assim, isso aqui, tipo, é o factor rap, depois eu passo isso aqui é mais a nível de deve, não é? Então é um conceito bem legal que aborda alguns dos pilares aí que é que uma aplicação ela deveria ter, né? Como.
01:04:52 Gustavo Esser: Como vamos dizer assim, boas práticas? Ela ser uma aplicação é alto, disponível é ser uma aplicação à escalável, ser uma aplicação resiliente, né? Acho que tem pontos. Tem contribuição de muita gente muito legal do mercado, né? Galera que fez aplicações aí gigantescas, então é bem legal passar isso aqui. Primo De deve eles darem uma olhada, acho que a maioria dos devs já conhece, mas é só batendo de novo na Pedra que para ter tudo esse modelo de escalabilidade que eu vou comentar aqui, ele tem que seguir alguns pilares, né? Crime deve Falando ali do HPA, né? AOHP é o principal que vocês vão ter contato? Ele é baseado num componente chamado Matrix server. Ele coleta essas métricas aqui e com essas métricas que ele coleta da aplicação, ele faz essa escalabilidade.
01:05:36 Gustavo Esser: Como o próprio nome diz, né? O HP ali, ele é de uma maneira horizontal, então ele escala em pode, né? Então ele vai realmente escalando aqui as caixinhas, né? É, então ele vai escalando, por exemplo, meu pode ter uma réplica, ele pode começou a ter muita requisição, começou a utilizar muito. Ele vai para 23 e aí eu defino a quantidade de réplicas, o quanto meu cluster é o quanto meu cluster tiver De capaz de eu consigo escalar minha aplicação e ela ficar mais performática, né? A gente tem um conceito também do VP aqui também. Ele é baseado no metrics server. Que esse aqui é um conceito bem legal, é que aí você não está falando de aumentar o número de réplica.
01:06:12 Gustavo Esser: É, mas você está falando de dar mais recurso, então, por exemplo, a minha aplicação, ela tem 1 GB de recursos, né? E ela está batendo esse 1 GB. Ela está batendo 1 GB. Eu quero aumentar para 12 para 2, então com base no metro que serve, eu consigo ter uma ética. É 111, regra que quando ela bateu 1 GB é eu faço esse esse recurso aumentar, por exemplo, para 2 GB, então ele vai deixando aquele aquela aquele contêiner mais é parrudão, né? Então não é o ideal, é o ideal, é sempre se trabalhar com HP.
01:06:46 Gustavo Esser: Alvo Ipea é último caso porque Oo vpl segue um modelo muito do monolito, né? Como a gente já trabalhava no passado lá de o Da mais recursos para esse Da mais recursos ali pro para a máquina Linux live ou não é o cenário ideal para a gente.
01:06:58 Marcus Bergo: Eu vejo o futuro repetir o passado.
01:06:59 Gustavo Esser: Já vai ver, né? É. É. Não, não, isso aqui não deveria existir, mas ele existe porque a gente trabalha, querendo ou não, a gente tem um uns uns uns monolitos ali dentro do ** bernette. Ainda que só estão mascarados, né? Mas é, ele realmente existe, porque é existe a necessidade e realmente é último caso, né? Então esses são os 2 modelos principais e aí a gente tem um modelo que não vai se aplicar aqui é o cenário de vocês, tá? Ele é um cenário mais De cloud, mas ele é um cenário, disse.
01:07:29 Gustavo Esser: A que é o câncer aos calor? É esse cenário que ele não funciona no modelo cloud, então é, é no modelo, claro, ele funciona no modelo Cláudio, de uma maneira mais simples. Né? Que é quando você define ali quantas máquinas eu quero ter, um cluster caso meu cluster bata uma capacidade. Fiz pto lá, ele vai lá, OPA, toma mais uma máquina aí pro teu cluster, toma mais 2, 3. Esse é o cenário que funciona melhor em cloud, num Prime. Se ele não é tão simples para o nosso cenário, aqui é a máquina.
01:07:56 Gustavo Esser: Ela não não escala, né? Ela não escala de uma maneira mais fácil, tem todo um processo de ingressar mais máquinas. A gente está falando de uma infra-estrutura, um crimes. Está debaixo de um ví, Cláudio, não é então, realmente tem que criar a máquina seguindo. Um template, colocar ela no cluster, então não é um processo. Esse processo, se a não se aplica tanto, mas só para contextualização. O modelo de Sea é um modelo de clustering skyler, que é onde você escala o now como um todo, né? Você fala, OPA, toma mais uma máquina aí e segue a vida. Então esse aqui é do gato. É importante também essa contextualização. Sei se tinha esse conhecimento, mas é. É legal porque é bem importante essa parte.
01:08:32 Gustavo Esser: O bom até para a gente não tomar muito mais tempo, hã? Eu acho que de maneira geral, um pouco do do do que eu queria passar do Reich, da da, do que foi implementado e tudo mais é, segue esse modelo, tá pessoal? A gente nem conseguiu falar de aprox. A gente não conseguiu falar de Harvard, por exemplo. De las, que surge tem muita coisa é, mas acho que, a grosso modo, falando Deco bernette, falando de como que vocês vão colocar a mão na massa? É.
01:08:57 Gustavo Esser: É um pouco disso, é um pouco de do que foi implementado, do que está sendo entregue, né? E aí a abro para perguntas. Aí se tem alguma questão relacionada à implementação, a componente e tudo mais. Como que está aí o?
01:09:11 Marcus Bergo: É gastou te mandar um link aí no chat, no nosso, se você puder ver se ajuda.
01:09:28 Gustavo Esser: A não sei se o Israel está cometendo algum ponto.
01:09:33 Israel Antonio Pereira: Não, não.
01:09:33 Marcus Bergo: Não. Gostou?
01:09:35 Israel Antonio Pereira: Na verdade, estou aguardando o link também que eu vou dá uma lida aqui que vai Marcus ou mandar.
01:09:38 Marcus Bergo: É, eu te passei o link. Eu estava no chat do Google.
01:09:41 Gustavo Esser: Há, pô, a legal.
01:09:42 Israel Antonio Pereira: Eu estou.
01:09:43 Marcus Bergo: É que. Eu não estou podendo, eu estou usando domínio diferente.
01:09:48 Israel Antonio Pereira: A defesa não para encher as dúvidas que ele vai ser presa na massa mesmo.
01:09:48 Gustavo Esser: Ã, hã, eu pegar ligar aqui.
01:09:53 Israel Antonio Pereira: Vai ser durante o processo, ele talvez algumas dúvidas pontuais, né? De ter exemplo a persistência de volume é. Oi. Entendi que o ranger ele, quando você faz o deploy das aplicações ele já sugere, né? Ele já gera um DNS automático ali, mas em De atender nesse pronto para os clientes, então não?
01:10:07 Marcus Bergo: Não.
01:10:13 Israel Antonio Pereira: Sim, no padrão do do ranking. Como é que o senhor funcionar? É como eu falei, vai surgir lá na hora de fazer o rendição, menos.
01:10:20 Gustavo Esser: Oo boa. Hoje, vocês já tem uma esteira, disse. As side a pronta, como é que hoje vocês estão saindo do SS, né? Vocês não utilizavam o bernette no caso, né?
01:10:31 Israel Antonio Pereira: E não, a gente só usava essa planta. Bora tório, não é bem implementar, mas acabou a gente migrando para Cirion em contratamos a solução já pronta.
01:10:33 Gustavo Esser: É ja. O run?
01:10:39 Israel Antonio Pereira: E a gente usa jinkings como se esse De.
01:10:44 Gustavo Esser: O run?
01:10:44 Marcus Bergo: E ele faz todo a conexão Gate, Ops, parâmetro Goethe, Ops, tipo, bem a.
01:10:50 Israel Antonio Pereira: Sim, presidente do Comite até o deploy.
01:10:55 Marcus Bergo: E aí roda unitários, íntegra, sono, et cetera, et cetera, et cetera. E vira um micro serviços depois.
01:11:03 Israel Antonio Pereira: Sim.
01:11:05 Marcus Bergo: Entendi uma coisa, o helmi sou uma coisa que o réu me também faz, o réu me dá pra usar pela linha de comando também, apesar dele ser culpado pelo ente.
01:11:06 Gustavo Esser: É Oo.
01:11:06 Marcus Bergo: A.
01:11:16 Gustavo Esser: O
01:11:16 Israel Antonio Pereira: Tá legal, eu acho que.
01:11:17 Gustavo Esser: Um.
01:11:18 Marcus Bergo: E aí, inclusive, você deixar tem alguma de ferramentas?
01:11:20 Israel Antonio Pereira: Isso.
01:11:21 Marcus Bergo: Daí a gente comando, porque você tem que deixar configurado. Que é bom, que é o cube histérico bi de mim é.
01:11:25 Israel Antonio Pereira: Teve, tipo. Se a gente pu
01:11:31 Marcus Bergo: É conta que se essas coisas assim é sempre legal ter.
01:11:36 Israel Antonio Pereira: A legal. Ops, *****, *****. *****, aqui.
01:11:40 Marcus Bergo: Passar a lista.
01:11:43 Gustavo Esser: É? Boa é o ramo chat é um modelo, o pessoal vem utilizando bastante.
01:11:43 Marcus Bergo: Eu Você.
01:11:47 Gustavo Esser: É, eu acho que talvez nesse cenário, eu não sei se a gente vai conseguir abraçar ele, porque assim
01:11:49 Marcus Bergo: Tem muito.
01:11:55 Gustavo Esser: É, eu acho que talvez nesse cenário, eu não sei se a gente vai conseguir abraçar ele, porque assim a. Ele. Ele é muito. Ele é muito extenso. Tá, então assim tem todo boas práticas ali. Eu acho que é um. É 11, coisa mais que eu acho que não, não estava incluso, mas a gente consegue seguir um modelo de deployment. É que depois vocês conseguem transformar isso num é uma charge, é EE é legal do do deployment falidos service, porque é ali que vocês vão realmente conseguir parametrizar aplicação de vocês.
01:12:09 Marcus Bergo: É
01:12:20 Gustavo Esser: Eu vou deixar um modelo pronto, eu vou encaminhar pra vocês também já darem uma olhada e vi ali já.
01:12:24 Israel Antonio Pereira: Oo.
01:12:25 Gustavo Esser: Já aparece finalizar e amanhã a gente mete a mão na massa. Eu, a gente vai aí e a cria esse deployment e pega 11 contêiner, registro aí de vocês ali. E aí pega um contêiner que já está pronto e tenta mudar toda essa estrutura. Depois vocês levam a isso aí para dentro do do Jenkins de vocês, né? Essa automação?
01:12:44 Israel Antonio Pereira: Bacana essas primeiras aplicações a gente vai tentar fazer normal.
01:12:45 Gustavo Esser: Boa.
01:12:50 Israel Antonio Pereira: Aí funcionou, entendeu?
01:12:50 Gustavo Esser: Sim, sim.
01:12:51 Israel Antonio Pereira: Bem com todos, solução funciona e depois a gente vai ser integração com De.
01:12:53 Gustavo Esser: Um, e isso, aham, isso aí a gente faz na mão uma ali. E aí a gente, a gente consegue, vocês vão entender bem ali, a partir de parametriza ção que que a gente precisa passar e tudo mais, feito isso vocês vão conseguir jogar isso para dentro de Enrique?
01:13:08 Israel Antonio Pereira: Você
01:13:09 Gustavo Esser: Sali, automatizar bem tranquilo.
01:13:09 Israel Antonio Pereira: Se você desligou para me dar melhor.
01:13:12 Gustavo Esser: Fechou, pessoal, acho que do do que eu queria passar um pouco disso. É aí que é bastante coisa aí, mas a gente vai ficar a disposição aí para tirar dúvidas. Tem todo o time aí que que nos apoia aí com com essa frente tem um medo aí também que faz o nosso, o nosso front end aí com a com a Cirion, né? Na parte de projetos, então, qualquer dúvida, mais direcional também no meio do caminho. A gente tem todo o contato aí para para ir se esclarecendo bem tranquilo.
01:13:34 Bertino Algebaile Da Silva, Fernanda: Um e também OOO time, ative também é fica à frente da sustentação desse ambiente, então é melhor dos mundos, né?
01:13:43 Gustavo Esser: Isso, isso aí.
01:13:44 Bertino Algebaile Da Silva, Fernanda: Que se implantam sustentam. Enfim, agora vou. Vou voltar lá naquela minha pergunta e Joel, sua dúvida sobre esse certificado, qual que era?
01:13:56 Israel Antonio Pereira: É, acho que o foi o é o desculpa. Não sei se você está o nome sem cerol em Deus. Ele falou, instalou o certificado na no servidor? Eu não entendi exatamente o que ele quis dizer com isso, mas no nosso servidor de s já tem outro de cada instalado, importado, bonitinho. Então, vê se ele tinha uma dúvida. Assim que tinham certificado lá, ou se ele sugeriu instalação de uma outra maneira, Mano, importação de uma outra maneira.
01:14:23 Bertino Algebaile Da Silva, Fernanda: Você quer compartilhar o as instruções que Welder passou só pra pessoa entender de?
01:14:23 Gustavo Esser: É eu.
01:14:28 Israel Antonio Pereira: Welder.
01:14:29 Eduardo Dutra - O2B: Bom, eu tenho, eu tenho aqui, eu posso compartilhar o e-mail aqui só para entendimento, né?
01:14:33 Israel Antonio Pereira: É? Celular.
01:14:34 Eduardo Dutra - O2B: Porque o histórico estava com com Welder, né?
01:14:34 Bertino Algebaile Da Silva, Fernanda: É só pra. Hã, rã.
01:14:37 Eduardo Dutra - O2B: Deixa eu compartilhar a tela aqui.
01:14:39 Bertino Algebaile Da Silva, Fernanda: É?
01:14:47 Eduardo Dutra - O2B: Já estão vendo?
01:14:49 Israel Antonio Pereira: Sim.
01:14:50 Eduardo Dutra - O2B: O OPA, boa, bom então, né? Esse trâmite de e-mail aqui rodou ali desde o dia 22 de julho, né? É, até pelo meu entendimento. Não, não ser muito técnico, mas pelo que o Welder tinha passado aqui, era sobre a instalação, né, do certificado lá por por ISS, então ele.
01:15:07 Israel Antonio Pereira: De papai?
01:15:10 Eduardo Dutra - O2B: Ele tramitou aqui, um dos últimos e-mails é sobre a instalação, né?
01:15:13 Israel Antonio Pereira: Porque?
01:15:15 Eduardo Dutra - O2B: Parte do apontamento ali no DNS e tudo mais, AE aquele De ele disse, envia também não é 11 link com um tutorial a para a configuração e instalação.
01:15:17 Israel Antonio Pereira: Tem uma forma? Tá indo para Cirion falar diferente, ser melhor.
01:15:28 Eduardo Dutra - O2B: Aí ficou essa dúvida em aberto, estou certo, né Israel?
01:15:29 Israel Antonio Pereira: Tabela do padrão sentir isso aí que que só pra você entender a gente já usa OIS já já está implementado, está rodando aqui, a gente já tem um site, alguém sabe de algum site is é que obedece? Apontando diretamente, só que eu tenho mais de 300 sites, como que eu uso isso? Hoje, a gerência desse certificados. Culpa no meu aplicativo, não De Balanço. Então, eu não preciso atualizar em 300 site. Só quando eu viro certificado, sou bolado 3 meu application ou de Balanço no lugar, só que todo mundo é dessa fatura. São aí quando eu levar isso para dentro da Cirion é, foi a que eu coloquei. Não gostaria que o.
01:16:09 Israel Antonio Pereira: OON Dinho próprios e reverso, ali ele pudesse fazer esse mesmo trabalho, de gerenciar os certificados para mim eu não tenho trabalho do que tentar usar em 300 sites.
01:16:21 Marcus Bergo: Não, não, não.
01:16:21 Israel Antonio Pereira: Aí ele mandou esse esse e-mail com essa documentação. Não consegui, não consegui entender, entendeu?
01:16:25 Marcus Bergo: Hã, eu posso fazer outra se quiser e te mandar.
01:16:31 Israel Antonio Pereira: Fazer outro quer dizer que eu sou sim.
01:16:32 Marcus Bergo: Alô? Outra documentação sobre isso? Para ir?
01:16:37 Israel Antonio Pereira: Então, mas aí eu não tenho.
01:16:41 Marcus Bergo: É, eu entendi, eu consegui dizer, mas na verdade você está certo.
01:16:41 Israel Antonio Pereira: Para Ora.
01:16:44 Marcus Bergo: Você não precisa ficar atualizando no site, ele fica ali na frente mesmo.
01:16:50 Israel Antonio Pereira: Vaga prox, né?
01:16:50 Marcus Bergo: Tanto é que é se você usar o Google, né? OGCP, ele cria um load load balancer?
01:16:56 Israel Antonio Pereira: A legal.
01:17:00 Marcus Bergo: Na verdade, como deixa eu inglês, então?
01:17:04 Israel Antonio Pereira: Exato, conceito é exatamente esse.
01:17:07 Marcus Bergo: É, então aí é, é tudo gerenciado ali mesmo.
01:17:11 Israel Antonio Pereira: Show de bola, é isso.
01:17:11 Marcus Bergo: O que ele fez foi isso, é auto renovação que aí faz o seguinte, é um comando, não é uma linha de comando que tem, na verdade, ele vem com um desafio que viam a é um campo de justiano DNS que aí ele vai inserir lá e vai conseguir atualizar, entendeu?
01:17:32 Israel Antonio Pereira: Oo.
01:17:34 Marcus Bergo: Por favor.
01:17:35 Israel Antonio Pereira: Aí, assim, viu como deu uma sitema, deu uma enroscada. Eu prefiro tocar primeiro a ser o cober net saído ranger a gente já colocar para funcionar, conseguir levar os serviços, aí a gente volta no IS. Depois fala aí preferidos, priorizar ele e a gente priorizar a migração dos contêineres.
01:17:50 Marcus Bergo: Cara.
01:17:54 Israel Antonio Pereira: Esportes?
01:17:59 Marcus Bergo: É? Tá, entendi, é você quer?
01:18:01 Bertino Algebaile Da Silva, Fernanda: AA gente pode andar em paralelo?
01:18:04 Marcus Bergo: Quer fazer um grupo, um grupo de pra gente melhorar? Em vez de a gente fazer a reunião, a gente podia fazer uma boa comunicação.
01:18:08 Israel Antonio Pereira: Entendi.
01:18:12 Marcus Bergo: Às 5 Assim, Duran, tipo.
01:18:13 Bertino Algebaile Da Silva, Fernanda: Como a gente vai fazer o seguinte, Marcos, a gente vai tratar os temas em paralelo, então a gente segue, né? Com essa questão do coubert net é com o Gustavo Na Na casa de amanhã e tudo, e aí, se você puder compartilhar essa outra documentação no e-mail que eu vou passar, a gente anda em paralelo, entendeu?
01:18:21 Israel Antonio Pereira: Falar? Tá com funcionários do gato?
01:18:35 Marcus Bergo: Hã, entendi, mas eu estou dizendo que de repente faz sentido a gente botar este, criar um grupo para vocês no nosso slack.
01:18:45 Bertino Algebaile Da Silva, Fernanda: É. Não, não, isso não faz parte dos nossos, das nossas regras aqui de comunicação e compliance.
01:18:46 Marcus Bergo: O que que é? Há sim, é verdade.
01:18:51 Bertino Algebaile Da Silva, Fernanda: E a A gente precisa nessa tentar elas. Então é, vamos fazer assim. Está como Jael falou. A prioridade é o **, bernette, mas só pra não ficar parado, se você puder compartilhar essa documentação que você falou, e aí o Jael, ele dá o tom aqui de quando a gente pode falar em fim de novo, tá bom?
01:19:06 Marcus Bergo: Eu vou.
01:19:12 Israel Antonio Pereira: Que bom.
01:19:13 Marcus Bergo: Tudo bem, é o eu estou.
01:19:15 Bertino Algebaile Da Silva, Fernanda: Beleza.
01:19:17 Marcus Bergo: Eu só me pingar, né? No caso.
01:19:19 Bertino Algebaile Da Silva, Fernanda: Tá?
01:19:21 Marcus Bergo: É eu. Eu estou respondendo na hora.
01:19:26 Bertino Algebaile Da Silva, Fernanda: Beleza, é?
01:19:26 Israel Antonio Pereira: E Foi bom?
01:19:28 Bertino Algebaile Da Silva, Fernanda: Gente, queria agradecer. Amanhã a gente está de volta, então já coloquei o convite aí na agenda de todo mundo. Para a parte mais, mas prática está. Eu tenho 2 assuntos que são diretamente com Jael, se tu puder ficar mais 5 minutinhos e aí eu libero, aí eu tive a tive.
01:19:47 Israel Antonio Pereira: Com certeza.
01:19:49 Eduardo Dutra - O2B: OPA, beleza. Também queria agradecer pessoal, a participação aí do Gustavo. Parabéns aí, Felipão também pelo pela, pela apresentação aí do Rizoma. Obrigada a Israel também é, e pode contar com a gente. A mãe está na qual é então?
01:20:03 Israel Antonio Pereira: Eu De bola eu fui gradeço vocês aí todo mundo achou Bill Marcos.
01:20:03 Bertino Algebaile Da Silva, Fernanda: Tá ótimo.
01:20:04 Felipe Carpanezi: Grande, pessoal.
01:20:08 Israel Antonio Pereira: Aí tal, aguardam seus a mente aí pra gente poder botar a mão na massa e fazer esse serviço funcionário.
01:20:12 Eduardo Dutra - O2B: Boa, Bora beleza.
01:20:15 Felipe Carpanezi: Olha, pessoal, obrigado, até mais.
01:20:16 Israel Antonio Pereira: Valeu, gente. Um abraço boa tarde aí.
01:20:17 Bertino Algebaile Da Silva, Fernanda: Valeu, obrigadão. Tchau.
01:20:17 Gustavo Esser: Eu pessoal, boa tarde, boa tarde.
01:20:18 Israel Antonio Pereira: Tchau, tchau.
01:20:18 Kaique Correia: Tchau, tchau.
            """                
        }
    ).json()
)