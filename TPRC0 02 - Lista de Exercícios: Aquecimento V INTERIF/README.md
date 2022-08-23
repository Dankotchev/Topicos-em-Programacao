# Lista de Exercícios: Aquecimento V Maratona de Programação INTERIF 2022

## Problema A: _Esteganografia_

_Por Cássio Agnaldo Onodera (IFSP – campus Birigui)_

Pouco tempo após o surgimento da escrita se viu a necessidade de disfarçar mensagens de forma que somente o destinatário pudesse compreender. Durante as guerras que ocorreram na antiguidade, os generais precisavam dar ordens a seus soldados sem que essas pudessem ser interceptadas e compreendidas por seus inimigos. Este é apenas um exemplo, mas a necessidade de disfarçar mensagens pode ser encontrada em diversas áreas, tal como um político trocar mensagens com seus aliados, um namorado enviando cartas para sua namorada etc. Duas técnicas foram utilizadas para disfarçar mensagens: a criptografia e a esteganografia. A criptografia altera a mensagem original e mesmo que o opositor tenha acesso a ela, não conseguiria entendêla de imediato. Já na esteganografia a mensagem se mantém a mesma, e são utilizadas técnicas para escondêla. Heródoto conta a história de um grego que precisava transmitir uma mensagem secretamente, então ele raspa o cabelo do mensageiro, tatua a mensagem na cabeça raspada e espera que o cabelo cresça novamente. Ao chegar ao destinatário, o mensageiro raspa a cabeça, revelando a mensagem. Obviamente que esta técnica é totalmente inviável. Com o advento dos computadores e algoritmos modernos várias técnicas foram criadas, que permitiram esconder textos em arquivos com outra finalidade, tal como esconder textos em arquivos de imagens, áudio, vídeo etc.

Em 1605, Francis Bacon criou o método de esteganografia conhecido como Código de Bacon, em que utiliza um texto falso para injetar uma mensagem. Nesta técnica, cada letra da mensagem é substituída por um conjunto de 5 caracteres binários que pode ser “A” e “B”.

![Tabela - Código de Bacon](https://images2.imgbox.com/b2/fa/XcCiFsoI_o.png)

Desta forma, substituímos o “A” da mensagem por “AAAAA”, um “B” por “AAAAB” e assim sucessivamente. Por exemplo, se desejamos esconder a palavra “IFSP”, ficaria assim:

Mensagem original: I F S P

Mensagem cifrada: ABAAA AABAB BAABA ABBBB

Desta forma, podemos esconder a mensagem em um texto falso substituindo a letra “A” por uma letra minúscula e a letra “B” por uma letra maiúscula. Por exemplo:

Mensagem cifrada: ABAAA AABAB BAABA ABBBB

Texto falso: REDE FEDERAL DE EDUCACAO

Texto final: rEde fedErAL de EduCACAo

O destinatário que receber a mensagem deve transformar cada letra minúscula na letra “A” e cada letra maiúscula na letra “B” e separar em grupos de 5 letras. Utilizando a tabela do Código de Bacon, transformar cada grupo de letras com “A” e “B” em uma letra e terá a mensagem original.

Este método foi criado 1605 quando não existia computadores e as conversões eram feitas de forma manual. Além disto, utilizando blocos binários com 5 caracteres, só seria possível representar 32 símbolos diferentes, o que seria impossível de representar as letras maiúsculas e minúsculas, os números, os caracteres especiais etc. Atualmente os computadores já possuem um código para cada letra do alfabeto (maiúsculas e minúsculas), números e outros caracteres (conhecido como Tabela ASCII) e para representá-los são utilizados 8 bits que permitem a representação de 256 símbolos diferentes.

Utilizando o código ASCII, em binário, de cada caractere, podemos adaptar o Código de Bacon para inserir mensagens secretas em textos falsos.

Bob, recebeu uma mensagem de Alice escondida dentro de um texto falso inserido através desta adaptação do Código de Bacon e está com dificuldade para obtê-la. Faça um programa que receba um texto e obtenha a mensagem secreta. 

**Entrada:** A única entrada do programa é um texto com até 2500 caracteres.

**Saída:** A saída é a mensagem secreta.

## Problema A: _Otto e seus Palíndromos_

_Por Jorge Francisco Cutigi (IFSP – campus São Carlos)_

Otto gosta muito de estudar. Na aula de português ele aprendeu o conceito de palíndromo. Ele ficou muito feliz, já que percebeu que seu nome também se tratava de um palíndromo. A professora explicou que uma palavra é um palíndromo se ela pode ser invertida e não modificar a palavra original. Por exemplo, a palavra ARARA é um palíndromo. 

Agora Otto vive procurando palavras palíndromas. Ele acha que já conseguiu listar todas as existentes na língua portuguesa. Não satisfeito, agora Otto tem um novo passatempo. A cada palavra, ele verifica se rearranjando os caracteres, ela poderia ser um palíndromo. Por exemplo, a palavra MORARAM pode ter os caracteres rearranjados para formar a palavra MARORAM, que é um palíndromo. 

Otto está aprendendo a programar e como exercício decidiu criar um programa que, dado uma palavra, informa se ela pode ser rearranjada para formar um palíndromo ou não.

**Entrada:** A entrada consiste de apenas uma linha que contém uma string S. Assuma que todas as letras de S não terão acentos e serão todas maiúsculas ou todas minúsculas.

**Saída:** Seu programa deve imprimir o número inteiro 1 caso a string S possa ser rearranjada para formar um palíndromo e 0 caso contrário.

**Restrições: **1 ≤ |S| ≤ 50.

## Problema D: _Problema de Syracuse_

_Por Claudio Haruo Yamamoto (IFSP – campus Salto)_

Existe um problema chamado Problema de Syracuse, que consiste em aplicar duas regras a um número inteiro. Primeira regra: se o número for par, então divida-o por 2. Segunda regra: se o número for ímpar, então multiplique-o por 3 e some 1. Seguindo esta regra sucessivamente, sempre se chega ao número 1 (pelo menos para os números menores que 19 * 2^58). Tomando o número 11, por exemplo, aplica-se a primeira regra: 11 * 3 + 1 = 34. 34 é par, então 34 / 2 = 17. Por sua vez, 17 é ímpar, então 17 * 3 + 1 = 52. E desta maneira seguem 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1. A partir daí, começa o ciclo 4, 2, 1, 4, 2, 1, 4, 2, 1. 

Dado um número N, determine a quantidade de passos, aplicando-se as regras do Problema de Syracuse, até chegar ao número 1 pela primeira vez.

**Entrada:** A entrada é composta por vários casos de teste. Cada caso de teste contém um número inteiro N (1 <= N <= 10^6 ). A entrada termina com EOF.

**Saída:** A saída consiste em uma linha para cada caso de teste contendo a quantidade de passos, aplicando-se as regras do Problema de Syracuse, até chegar ao número 1 pela primeira vez.
