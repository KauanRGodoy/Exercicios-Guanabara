print('============   DESAFIO 044  ============')
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
# À vista: dinheiro/cheque: 10% de desconto ; À vista no cartão: 5% de desconto ; em até 2x no cartão: preço normal ; 3x ou mais no cartão 20% de juros.
cores = {'limpa': '\033[m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'rosa': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m'}
#
str(print('{}Bom Dia!{}'.format('\033[1;30;43m', cores['limpa'])))
str(print('{}Qual produto gostaria de comprar?{}'.format('\033[1;30;43m', cores['limpa'])))
#
def preco(escolha):
    if escolha == 1:
        return int(230)
    elif escolha == 2:
        return int(550)
    elif escolha == 3:
        return int(889)
    elif escolha == 4:
        return int(1380)
    elif escolha == 5:
        return int(240)
    elif escolha == 6:
        return int(340)
    elif escolha == 7:
        return int(150)
    elif escolha == 8:
        return int(24)
    elif escolha == 9:
        return int(120)
#
escolha = int(input(""
                    "{}___________________________________\n"
                    "| 1 - Memória RAM     = R$230,00  |\n"
                    "| 2 - Placa Mãe       = R$550,00  |\n"
                    "| 3 - Processador     = R$889,00  |\n"
                    "| 4 - Placa de Vídeo  = R$1380,00 |\n"
                    "| 5 - SSD             = R$240,00  |\n"
                    "| 6 - Fonte           = R$340,00  |\n"
                    "| 7 - Coolers         = R$150,00  |\n"
                    "| 8 - Ventoinhas      = R$24,00   |\n"
                    "| 9 - Gabinete        = R$120,00  |\n"
                    "-----------------------------------{}\n"
                    ":".format(cores['amarelo'], cores['limpa'])))
#
pagar = int(input(""
                  "{}Qual vai ser a forma de Pagamento?{}\n"
                  "{}_________________________\n"
                  "| 1 - Dinheiro / PIX    |\n"  # 10% de Desconto
                  "| 2 - À vista no cartão |\n"  # 5% de Desconto
                  "| 3 - Parcelado         |\n"  # 2x preço normal ou 3x ou mais 20% de juros
                  "-------------------------{}\n"
                  ":".format('\033[1;30;43m', cores['limpa'], cores['rosa'], cores['limpa'])))
#
def money(pagar):
    #print('Debug: Opção de pagamento selecionada:', pagar)
    if pagar == 1:
        dinheiro = preco(escolha) - (preco(escolha) * 0.10)
        return ('O total com desconto de 10% à vista no PIX será:\n'
                'R${:.2f}').format(dinheiro)
    elif pagar == 2:
        credito = preco(escolha) - (preco(escolha) * 0.05)
        return ('O total com desconto de 5% à vista no cartão de crédito será:\n'
                'R${}'.format(credito))
    elif pagar == 3:
        parcelamento = int(input('{}_________________________________________________________\n'
                                 '| Parcelamos em até 2x sem juros e 12x com juros de 20% |\n'
                                 '| Em quantas vezes deseja pagar?                        |\n'
                                 '---------------------------------------------------------{}\n'
                                 ':'.format(cores['ciano'], cores['limpa'])))
        #print('Debug: Número de parcelas selecionado:', parcelamento)
        preco_total = preco(escolha)
        preco_juros = preco_total * 0.20
        preco_parcela = preco_total / parcelamento
        if parcelamento == 2:
            return 'Você pagará 2x de R${:.2f}'.format(preco_parcela)
        elif 3 <= parcelamento <= 12:
            return ('{}Valor do produto: RS{:.2f}{}\n'
                    '{}Valor do produto com juros: R${:.2f}{}\n'
                    '{}Valor do juros: R${:.2f}.{}\n'
                    '{}Você pagará {}x de R${:.2f}{}'
                    ).format('\033[1;30;46m', preco(escolha),cores['limpa'],'\033[1;30;46m', preco_total + preco_juros,cores['limpa'], '\033[1;30;46m', preco_juros,cores['limpa'],'\033[1;30;46m', parcelamento, (preco_total + preco_juros) / parcelamento, cores['limpa'])
#
preco_final = money(pagar)
print(preco_final)
print('CONCLUIDO!!!')
