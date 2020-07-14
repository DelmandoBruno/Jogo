#Bruno Delmando
#Objetivo do jogo: Chegar até o rei e mata-lo em um combate direto para tomar o trono. Para chegar até o topo do castelo onde está o rei, Rasmus precisa derrotar diversos guardas ou passar dispercebido por eles!
#Publico alvo- Jovens
#Se você terminou com 15 pontos, parabéns! Você atingiu a pontuação máxima!
#Se você acertou menos que 15 e mais que 10, você atingiu uma pontuação intermediária.
#Se você acertou menos que 10, tente novamente.

import time
import sys
Nome= str(input("Digite seu Nome:"))
print ("Olá", Nome, "ajude Rasmus a cumprir seu objetivo indicando as melhores decisões.")
print("Dependendo das escolha, Rasmus pode perder ou ganhar pontos")
pontos=0
time.sleep(2)
print ("Vestindo armadura...")
time.sleep(2)
print ("Objetivo do jogo: Chegar até o rei e mata-lo em um combate direto para tomar o trono. Para chegar até o topo do castelo onde está o rei, Rasmus precisa derrotar diversos guardas ou passar dispercebido por eles!.")
time.sleep(4)
print("Escolha sua arma:")
time.sleep(1)
print("Espada")
time.sleep(1)
print("Machado")
time.sleep(1)
print("Arco e flecha")
time.sleep(1)
print("Adagas")
Arma=str(input("Escolha uma arma:"))
Arma = Arma.strip()
Arma = Arma.upper()
if Arma=="ESPADA":
    print("Sua escolha foi a espada")
    letra = 'a'
    possessivo="sua"
elif Arma=="MACHADO":
    letra = 'o'
    possessivo="seu"
    print("Sua escolha foi o machado")
elif Arma=="ARCO E FLECHA":
    letra="o"
    possessivo="seu"
    print("Sua escolha foi arco e flecha")
elif Arma=="ADAGAS":
    print("Sua escolha foi as adagas.")
    letra="as"
    possessivo="suas"
else:
    print("Opção invalida")
    sys.exit()
time.sleep(2)
print("Se prepare que a batalha irá começar.")
time.sleep(2)
print ("Rasmus tem que invadir o castelo e precisa de sua ajuda.")
time.sleep(2)
print("Para pular o muro, digite muro")
print("Para atravessar o rio, digite rio")
Caminho=str(input("Escolha um caminho:"))
Caminho = Caminho.strip()
Caminho = Caminho.upper()
if Caminho=="MURO":
    print("Rasmus irá pular o muro.")
    time.sleep(2)
    pontos=pontos+4
    print("Rasmus ganha pontos por escolher o caminho certo, sua pontuação agora é:", pontos) 
    time.sleep(2)
    print("Rasmus encontrou um guarda ao pular o muro e agora tem que lutar.")
    time.sleep(2)
    print("Rasmus puxa ", letra, Arma," e ataca o guarda.")
    time.sleep(2)
    print("Lutando...")
    time.sleep(4)
    print ('Após derrotar o primeiro guarda Rasmus entra no castelo, e tem 2 opções de caminho,subir as escadas ou entrar na porta grande')
    time.sleep(2)
    print("Para pular o subir as escadas, digite escadas.")
    print("Para entrar na porta grande, digite porta.")
    Escolha1=str(input("Escolha uma direção:"))
    Escolha1 = Escolha1.strip()
    Escolha1 = Escolha1.upper()
    if Escolha1=="ESCADAS":
                 print ('Rasmus sobe a escada e se depara com 3 guardas distaídos.')
                 time.sleep(2)
                 print ('Rasmus agora tem 2 opções, lutar com os 3 guardas ou passar em silêncio.')
                 time.sleep(2)
                 print ('Para passar em silêncio digite, passar')
                 print ('Para lutar com os guardas digite, lutar')
                 time.sleep(2)
                 PassarLutar=str(input("Escolha lutar ou passar:"))
                 PassarLutar = PassarLutar.strip()
                 PassarLutar = PassarLutar.upper()
                 if PassarLutar=='PASSAR':
                     pontos=pontos+2
                     print("Rasmus escolhe a opção certa novamente e agora tem", pontos,"pontos") 
                     print ("Rasmus passa despercebido pelos guardas e chega ao outro andar do castelo!")
                     time.sleep(1)
                     print("Rasmus chega ao último andar da torre e se depara com a sala do Rei trancada.")
                     time.sleep(1)
                     print("Rasmus precisa achar a chave da sala!")
                     time.sleep(1)
                     print("Para procurar embaixo do tapete, digite tapete.")
                     time.sleep(1)
                     print("Para procurar dentro do vaso, digite vaso.")
                     time.sleep(1)
                     VasoTapete=str(input("Procurar no tapete ou vaso?:"))
                     VasoTapete = VasoTapete.strip()
                     VasoTapete = VasoTapete.upper()
                     if VasoTapete=="VASO":
                         print("Rasmus vasculha os vasos a sua volta, porém acaba derrubando um, chamando atenção dos guardas.")
                         time.sleep(2)
                         print("Rasmus é preso! VOCÊ PERDEU, Fim de jogo!")
                         print("Rasmus ficou com",pontos,"pontos")
                         sys.exit()
                     elif VasoTapete=="TAPETE":
                        pontos=pontos+2
                        print("Rasmus escolhe a opção certa e ganha 2 pontos, Rasmus fica com",pontos,"pontos")
                        time.sleep(2)
                        print("Rasmus acha a chave embaixo de um dos tapetes, e abre a porta.")
                        time.sleep(2)
                        print("Rasmus se depara com o Rei sentada em seu trono!")
                        time.sleep(2)
                        print("Rasmus se aproxima do Rei para uma batalha.")
                        time.sleep(2)
                        print("Rasmus utiliza" , possessivo, Arma, "para atacar o Rei!")
                        time.sleep(2)
                        print("Os guardas estão chegando, mate o rei o mais rapido possível!!")
                        time.sleep(2)
                        print("Rasmus possui 2 ataques")
                        time.sleep(2)
                        print("Para usar o ataque 1, digite ataque1.")
                        time.sleep(2)
                        print("Para usar o ataque 2, digite ataque2.")
                        Ataques=str(input("Escolha um ataque!"))
                        Ataques = Ataques.strip()
                        Ataques = Ataques.upper()
                        if Ataques=="ATAQUE1":
                            pontos=pontos-3
                            print("Rasmus erra o ataque e os guardas chegam a tempo e os salvam!")
                            time.sleep(2)
                            print("Rasmus é preso!")
                            time.sleep(2)
                            print("Por ser preso Rasmus perde 3 pontos e fica com",pontos,"pontos")
                            time.sleep(2)
                            print("VOCÊ PERDEU, FIM DE JOGO!")
                            time.sleep(2)
                            print("Rasmus termina o jogo com",pontos,"pontos")
                            sys.exit()
                        elif Ataques=="ATAQUE2":
                            pontos=pontos+6
                            print("Rasmus acerta o ataque e mata o Rei! E ganha 6 pontos e fica com",pontos,"pontos")
                            time.sleep(2)
                            print("Rasmus toma o poder e torna-se Rei!.")
                            time.sleep(2)
                            print("Você ganhou e ficou com",pontos,"pontos, parabéns!!")
                            sys.exit()
                        else:
                            print("Opção Inválida!")
                            sys.exit()
                     else:
                         print("Opção Inválida!")
                         sys.exit()
                         
                 elif PassarLutar=="LUTAR":
                     pontos=pontos-2
                     print("Rasmus derrota os 3 guardas, mas perde o braço!")
                     time.sleep(2)
                     print("Rasmus perde 2 pontos e fica com",pontos,".")
                     time.sleep(2)
                     print("Rasmus perde muito sangue e morre no corredor.")
                     time.sleep(2)
                     print("FIM DE JOGO, você perdeu!")
                     time.sleep(2)
                     print("Rasmus ficou com apenas",pontos,"pontos")
                     sys.exit()
                 else:
                     print ("Opção inválida!")
                     sys.exit()
    elif Escolha1=='PORTA':
        print("Rasmus abre a porta...")
        time.sleep(2)
        print("E se depara com a Rainha!")
        time.sleep(2)
        print("Para fazer a Rainha de refém, digite refém")
        time.sleep(2)
        print("Para matá-la, digite degolar")
        DegolarRefem=str(input("Fazer de refém ou degolar?:"))
        DegolarRefem = DegolarRefem.strip()
        DegolarRefem = DegolarRefem.upper()
        if DegolarRefem=="REFEM" or DegolarRefem=="REFÉM":
            pontos=pontos+1
            print("Rainha agora é refém de Rasmus! Rasmus ganha 1 ponto por manter a cautela e fica com",pontos,"pontos.")
            time.sleep(2)
            print("Rasmus obriga a Rainha a leva-lo a passagem secreta até onde o Rei está!")
            time.sleep(2)
            print("Rasmus, junto com a Rainha, chega a sala do Rei e se depara com o Rei em seu trono.")
            time.sleep(2)
            print("Para se aproximar do Rei e enfrenta-lo, digite Aproximar.")
            time.sleep(2)
            print("Para matar a Rainha na frente do Rei, digite Matar.")
            MatarAproximar=str(input("Aproximar-se ou matar a Rainha?:"))
            MatarAproximar = MatarAproximar.strip()
            MatarAproximar = MatarAproximar.upper()
            if MatarAproximar=="APROXIMAR":
                    print("Rasmus se aproxima do Rei para uma batalha.")
                    time.sleep(2)
                    print("Rasmus utiliza" , possessivo, Arma, "para atacar o Rei!")
                    time.sleep(2)
                    print("Os guardas estão chegando, mate o rei o mais rapido possível!!")
                    time.sleep(2)
                    print("Rasmus possui 2 ataques")
                    time.sleep(2)
                    print("Para usar o ataque 1, digite ataque1.")
                    time.sleep(2)
                    print("Para usar o ataque 2, digite ataque2.")
                    Ataques=str(input("Escolha um ataque!"))
                    Ataques = Ataques.strip()
                    Ataques = Ataques.upper()
                    if Ataques=="ATAQUE1":
                        pontos=pontos-2
                        print("Rasmus erra o ataque e os guardas chegam a tempo e os salvam!")
                        time.sleep(2)
                        print("Rasmus é preso! E perde 2 pontos e fico com",pontos,"pontos.")
                        time.sleep(2)
                        print("VOCÊ PERDEU, FIM DE JOGO!")
                        print("Rasmus ficou com apenas",pontos,"pontos.")
                        sys.exit()
                    elif Ataques=="ATAQUE2":
                        pontos=pontos+10
                        print("Rasmus acerta o ataque e mata o Rei!")
                        time.sleep(2)
                        print("Rasmus toma o poder e torna-se Rei! E ganha 10 pontos e fica com",pontos,"pontos")
                        time.sleep(2)
                        print("Você ganhou, parabéns!!")
                        time.sleep(2)
                        print("Rasmus ficou com",pontos,"pontos!")
                        sys.exit()
                    else:
                        print("Opção Inválida!")
                        sys.exit()
            elif MatarAproxima=="MATAR":
                pontos=pontos-1
                print("Ao matar a Rainha, o irmão do Rei chega de surpresa e mata Rasmus pelas costas! Você perdeu 1 ponto e ficou com",pontos,"pontos")
                time.sleep(2)
                print("VOCÊ PERDEU! Fim de jogo.")
                time.sleep(2)
                print("Rasmus ficou com apenas",pontos,"pontos")
                sys.exit()
            else:
                print("Opção inválida!")
                sys.exit()  
                   
        elif DegolarRefem=="DEGOLAR":                           
                 print("Antes de degolar a Rainha, ela grita e chama a atenção de todos os guardas.")
                 time.sleep(2)
                 pontos=pontos-3
                 print("Rasmus perde 3 pontos por chamar a atenção dos guardas e fica com",pontos,"ponto(s)!")
                 time.sleep(2)
                 print("A Rainha é morta, porém os guardas prendem Rasmus!")
                 time.sleep(2)
                 print("Rasmus é preso! VOCÊ PERDEU, Fim de jogo!")
                 time.sleep(2)
                 print("Rasmus ficou com",pontos,"pontos!")
                 sys.exit()
        else:
                print("Opção inválida!")
                sys.exit()
    else:
        print("Opção invalida")
        sys.exit()
     
elif Caminho=="RIO":
    print("Rasmus irá atravessar o rio.")
    time.sleep(2)
    print("Rasmus calcula errado o tempo de ronda dos guardas e ao sair do rio, se depara com 5 guardas esperando ele.")
    time.sleep(1)
    print("Rasmus é preso! VOCÊ PERDEU, Fim de jogo!")
    time.sleep(2)
    print("Rasmus perde o jogo com",pontos,"pontos")
    sys.exit()

else:
    print("Opção invalida.")
    sys.exit()








