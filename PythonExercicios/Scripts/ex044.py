print('Bem Vindo a nossa loja!\nNos Temos os seguintes produtos em Oferta:\n'
      '\033[1;33;40m 1 - Geladeira Refrigerador Electrolux Duplex DC35A 260L - Branco por \033[1;32mR$ 2.139,00\033[m'
      '\n\033[1;34;40m 2 - Fritadeira Elétrica Sem Óleo Air Fryer Mondial New Pratic AF31 3,5 L – Preto por \033[1;32mR$ 399,90\033[m'
      '\n\033[1;35;40m 3 - Smart TV LED 43” Full HD AOC Roku por \033[1;32;40mR$ 1.999,00\033[m')
escolha=int(input('Qual dos 3 produtos você quer?'))
if escolha==1:
      produto='a Geladeira'
      valor=2139
elif escolha==2:
      produto='a Air Fryer'
      valor=399.90
elif escolha==3:
      produto='a TV 43”'
      valor==1999
else:
      escolha=int(input('Produto não identificado, escolha um dos 3:'))
      if escolha == 1:
            produto = 'a Geladeira'
            valor = 2139
      elif escolha == 2:
            produto = 'a Air Fryer'
            valor = 399.90
      elif escolha == 3:
            produto = 'a TV 43”'
            valor == 1999
      else:
            print('Obigado por visitar nossa loja!')
print('\033[1;31;40mVocê escolheu {}\033[m'.format(produto))
pagamento=int(input('Qual a forma de pagamento?'
                    '\n1-Dinheiro ou cheque(10% de desconto)'
                    '\n2-Cartão à vista(5% de desconto)'
                    '\n3-2x no Cartão(sem juros)'
                    '\n4-de 3 a 12x no Cartão(20% de Juros)\n'))
if pagamento==1:
      print('O preço do produto será R$ {:.2f}'.format(valor-(valor*0.1)))
elif pagamento==2:
      print('O valor do produto será R$ {:.2f}'.format((valor-(valor*0.05))))
elif pagamento==3:
      print('O valor do produto será R$ {:.2f}'.format(valor))
elif pagamento==4:
      parcela=int(input('Em quantas parcelas o pagamento será dividido? '))
      print('O pagamento será de {} parcelas de R${:.2f} por mês'.format(parcela,(valor*1.2)/parcela))







