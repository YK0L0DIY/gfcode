def _main_():
    saldo = 123421352
    pin = 5432
    tentativas = 3
    br=False
    ePim=False

    while 1:
        print("Indique o seu pim\n")

        try:
            tenativa = int(input())
            ePim = True
        except:
            print("isso nao e um pim\n")

        if ePim:
            if tenativa == pin:

                while 1:

                    print("oque queres de mim????")
                    print("1) consultar o saldo")
                    print("2) levantar dinehrio")
                    print("3) sair\n")

                    try:
                        todo = int(input())
                    except:
                        print("es burro tem de ser um numero de 1 a 3\n")

                    if todo==1:
                        print("tens ",saldo,"euros\n")

                    if todo==2:
                        print("quantia a levantar?\n")

                        try:
                            quantia=int(input())
                            print("quantia inicial ",saldo)

                            saldo=saldo-quantia
                            print("quantia final ",saldo)
                        except:
                            print("nao valido\n")

                    if todo==3 :
                        print("sair\n")
                        br=True
                        break


            elif pin!= tenativa:
                tentativas = tentativas - 1
                if tentativas == 0:
                    print("ja te fodeste que fiquei com o teu cartao")
                    break
                print("tente outra vez as suas tentatiovas: ", tentativas)

            if br:
                break

_main_()
