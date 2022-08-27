# Lista de Exercícios: Aquecimento V Maratona de Programação INTERIF 2022

## [Problema A: _Esteganografia_](https://github.com/Dankotchev/Topicos-em-Programacao/blob/main/TPRC0%2002%20-%20Lista%20de%20Exerc%C3%ADcios:%20Aquecimento%20V%20INTERIF/esteganografia.py)

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

## Problema B: _Otto e seus Palíndromos_

_Por Jorge Francisco Cutigi (IFSP – campus São Carlos)_

Otto gosta muito de estudar. Na aula de português ele aprendeu o conceito de palíndromo. Ele ficou muito feliz, já que percebeu que seu nome também se tratava de um palíndromo. A professora explicou que uma palavra é um palíndromo se ela pode ser invertida e não modificar a palavra original. Por exemplo, a palavra ARARA é um palíndromo. 

Agora Otto vive procurando palavras palíndromas. Ele acha que já conseguiu listar todas as existentes na língua portuguesa. Não satisfeito, agora Otto tem um novo passatempo. A cada palavra, ele verifica se rearranjando os caracteres, ela poderia ser um palíndromo. Por exemplo, a palavra MORARAM pode ter os caracteres rearranjados para formar a palavra MARORAM, que é um palíndromo. 

Otto está aprendendo a programar e como exercício decidiu criar um programa que, dado uma palavra, informa se ela pode ser rearranjada para formar um palíndromo ou não.

**Entrada:** A entrada consiste de apenas uma linha que contém uma string S. Assuma que todas as letras de S não terão acentos e serão todas maiúsculas ou todas minúsculas.

**Saída:** Seu programa deve imprimir o número inteiro 1 caso a string S possa ser rearranjada para formar um palíndromo e 0 caso contrário.

**Restrições: **1 ≤ |S| ≤ 50.

## Problema C: _Organograma_

_Por Tiago Alexandre Dócusse (IFSP – campus Barretos)_

A escola em que você estudou durante toda a sua infância precisa fazer um relatório dos seus setores. No entanto, eles não possuem esses dados digitalizados, e precisam de um programa que faça isso de maneira rápida e prática. Como você é um excelente programador e tem um carinho especial pela sua escola, resolveu ajudá-los nesta questão. A escola possui setores organizados de maneira hierárquica, sendo representados como um organograma, onde cada setor é responsável por zero ou mais setores, que podem ter setores sob sua responsabilidade. Abaixo é exibido um exemplo de um organograma, onde a seta indica responsabilidade de um setor para o outro.

**Entrada:**

**Saída:** 

## [Problema D: _Problema de Syracuse_](https://github.com/Dankotchev/Topicos-em-Programacao/blob/main/TPRC0%2002%20-%20Lista%20de%20Exerc%C3%ADcios:%20Aquecimento%20V%20INTERIF/syracuse.py)

_Por Claudio Haruo Yamamoto (IFSP – campus Salto)_

Existe um problema chamado Problema de Syracuse, que consiste em aplicar duas regras a um número inteiro. Primeira regra: se o número for par, então divida-o por 2. Segunda regra: se o número for ímpar, então multiplique-o por 3 e some 1. Seguindo esta regra sucessivamente, sempre se chega ao número 1 (pelo menos para os números menores que 19 * 2^58). Tomando o número 11, por exemplo, aplica-se a primeira regra: 11 * 3 + 1 = 34. 34 é par, então 34 / 2 = 17. Por sua vez, 17 é ímpar, então 17 * 3 + 1 = 52. E desta maneira seguem 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1. A partir daí, começa o ciclo 4, 2, 1, 4, 2, 1, 4, 2, 1. 

Dado um número N, determine a quantidade de passos, aplicando-se as regras do Problema de Syracuse, até chegar ao número 1 pela primeira vez.

**Entrada:** A entrada é composta por vários casos de teste. Cada caso de teste contém um número inteiro N (1 <= N <= 10^6 ). A entrada termina com EOF.

**Saída:** A saída consiste em uma linha para cada caso de teste contendo a quantidade de passos, aplicando-se as regras do Problema de Syracuse, até chegar ao número 1 pela primeira vez.

## Problema E: _Matemática_

_Por Tiago Alexandre Dócusse (IFSP – campus Barretos)_

Rafael é um brilhante aluno e adora matemática. Um dia, fazendo um treinamento para a olimpíada de matemática, se deparou com o seguinte problema: Uma função _f_ é definida da seguinte forma:

![Definição da funçao f](https://images2.imgbox.com/4f/f7/GsybEiXq_o.png)

Rafael até conseguiu calcular o resultado da função para alguns valores de x. No entanto, ele não possui todas as respostas, e pediu a sua ajuda para criar um programa que calcule as respostas da função. Você consegue ajudar Rafael no seu treinamento?

**Entrada:** A entrada é formada por um único número inteiro x que deve ser usado para calcular o resultado da função, sendo 0 < x < 20.000.000.

**Saída:** A saída exibe o resultado da função para o número de entrada fornecido

## [Problema F: _Combustível_](https://github.com/Dankotchev/Topicos-em-Programacao/blob/main/TPRC0%2002%20-%20Lista%20de%20Exerc%C3%ADcios:%20Aquecimento%20V%20INTERIF/combustivel.py)

_Por Felipe Gobo Bruno (IFSP – campus Boituva)_

O IFSP Campus Boituva está buscando economizar o máximo possível no abastecimento dos veículos oficiais.

Buscando uma solução para esse problema, um servidor do campus encontrou uma matéria ensinando uma maneira para descobrir qual combustível (etanol ou gasolina) é mais rentável financeiramente, mas ele não possui conhecimento computacional para tornar essa análise eficaz.

O servidor relatou que para o etanol ser mais vantajoso ele deve custar menos que 70% do valor da gasolina, ou seja, dividindo o valor do etanol pelo valor da gasolina o quociente deverá ser menor que 0,7.

De acordo com as informações fornecidas acima, ajude o IFSP Campus Boituva por meio do desenvolvimento de uma solução computacional para descobrir qual combustível (etanol ou gasolina) é mais rentável financeiramente.

**Entrada:** A primeira linha da entrada possui um número ponto flutuante (reais) com precisão simples V (0 ≤ V ≤ 10^38), representando o valor da gasolina.

A segunda linha da entrada possui um número ponto flutuante (reais) com precisão simples T (0 ≤ T ≤ 10^38), representando o valor do etanol.

**Saída:** A saída deve exibir uma única linha contendo GASOLINA para os casos em que a gasolina seja mais vantajosa ou ETANOL para os casos em que o etanol seja mais vantajoso.

## [Problema G: _Super Múltiplos de 3_](https://github.com/Dankotchev/Topicos-em-Programacao/blob/main/TPRC0%2002%20-%20Lista%20de%20Exerc%C3%ADcios:%20Aquecimento%20V%20INTERIF/multiplos.py)

_Por Márcio Kassouf Crocomo (IFSP – campus Piracicaba)_

Luigi é um entusiasta da matemática que um dia descobriu uma coisa que achou fantástica: uma forma de verificar se um número é divisível por três a partir da soma de seus algarismos. A regra é que um número é divisível por 3 se, e somente se, a soma de seus algarismos é um número múltiplo de 3. Luigi percebeu que, a partir dessa regra, era possível verificar se números muito grandes eram divisíveis por 3. Não contente com o novo conhecimento adquirido, Luigi começou a tentar compreender a relação entre os números e chamou seu irmão, Mario, para ajudá-lo com uma atividade. Dado um número, seu irmão Mario realizava a soma de todos os algarismos pares desse número e verificava se esta soma era um múltiplo de três. Por sua vez, Luigi repetia a verificação, mas levando em conta a soma apenas dos algarismos ímpares. Como pretendiam repetir o experimento para uma grande quantidade de números, os irmãos pediram sua ajuda para criar um programa que automatize a tarefa explicada. 

**Entrada:** Um número inteiro representado por no mínimo 1 e no máximo 20 dígitos decimais.

**Saída:** Duas linhas, sendo que na primeira linha deve estar escrito a letra S caso a soma dos dígitos pares do número em questão seja um valor divisível por 3, ou a letra N caso contrário. Na segunda linha a letra S deve aparecer caso a soma dos dígitos ímpares do número em questão seja um valor divisível por 3, ou a letra N caso contrário.

## [Problema H: _Vacinômetro_](https://github.com/Dankotchev/Topicos-em-Programacao/blob/main/TPRC0%2002%20-%20Lista%20de%20Exerc%C3%ADcios:%20Aquecimento%20V%20INTERIF/vacinometro.py)

_Por Felipe Gobo Bruno (IFSP – campus Boituva)_

A população da cidade de Boituva solicitou à secretaria de saúde do município que fosse criado um mecanismo para disponibilizar a porcentagem de habitantes vacinados na cidade.

Para atender a demanda da população boituvense foi idealizado o Vacinômetro, uma ferramenta que exibe a porcentagem de habitantes vacinados na cidade.

As secretarias de saúde das cidades vizinhas ficaram sabendo dessa ferramenta, agora a secretaria de saúde de Boituva precisa da sua ajuda para desenvolver essa solução computacional para disponibilizar a todas as cidades interessadas em exibir essa informação para sua população.

**Entrada:** A primeira linha da entrada possui um número inteiro N (1 ≤ N ≤ 2.147.483.647), representando a quantidade de habitantes da cidade.

A segunda linha da entrada possui um número inteiro V (1 ≤ V ≤ 2.147.483.647), representando a quantidade de habitantes vacinados na cidade.

**Saída:** A saída deve exibir uma única linha contendo um número ponto flutuante com precisão de 1 (uma) casa decimal P (0 ≤ P ≤ 10`38), representando a porcentagem de vacinados na cidade, seguido do símbolo %.

## [Problema I: *N-ésimo Termo*](https://github.com/Dankotchev/Topicos-em-Programacao/blob/main/TPRC0%2002%20-%20Lista%20de%20Exerc%C3%ADcios:%20Aquecimento%20V%20INTERIF/termo.py)

_Por Claudio Haruo Yamamoto (IFSP – campus Salto)_

Em uma espiral de triângulos, cada triângulo compartilha um lado com dois outros, conforme apresentado na figura.

![Espiral de triângulos equiláteros com comprimentos de lado seguindo a sequência de Padovan.](https://upload.wikimedia.org/wikipedia/commons/c/cd/Padovan_triangles_%281%29.png)

Assim, é formada a sequência 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16, ... 

Dado um número N, encontre o N-ésimo termo desta sequência.

**Entrada:** A entrada é composta por vários casos de teste. Cada caso de teste contém um número inteiro N (1 ≤ N ≤ 159). A entrada termina com EOF.

**Saída:** A saída consiste em uma linha para cada caso de teste contendo o N-ésimo termo da sequência apresentada.

## [Problema J: _Pega Varetas_](https://github.com/Dankotchev/Topicos-em-Programacao/blob/main/TPRC0%2002%20-%20Lista%20de%20Exerc%C3%ADcios:%20Aquecimento%20V%20INTERIF/varetas.py)

_Por Edmar Santos (IFSP – campus Birigui)_

Em um dia chuvoso, sem saber o que fazer, três sobrinhos de Miguel resolveram brincar de “pega varetas” na grande varanda da casa em frente ao jardim. No jogo de “pega varetas” o objetivo é retirar as varetas do monte sem mexer as demais, a fim de somar o maior número de pontos do que os oponentes. Depois que as varetas são espalhadas em um monte, o jogador que inicia o jogo remove quantas varetas puder evitando mexer nas demais. Assim que o jogador mexe numa vareta que não seja a que está retirando, perde a vez, e o próximo jogador inicia sua tentativa de retirada. O jogo termina quando não houver mais varetas e ganha quem somar mais pontos. Como nenhum deles possuía um jogo de varetas completo, eles decidiram juntar o que cada um tinha nas suas latinhas. Também decidiram que cada vareta amarela valeria 5 pontos, as verdes 10, azuis 15, vermelhas 20 e as pretas 50 pontos. Ao ver os garotos brincando, Miguel, que já cursou disciplinas de programação, resolveu fazer um programa para contabilizar as jogadas dos meninos para apresentar o ganhador e sua pontuação, ou mesmo se houve empate. Ajude Miguel a desenvolver esse programa.

**Entrada:** A entrada possui vários casos de testes. Cada caso de teste é composto por duas linhas. Na primeira linha do caso de teste há somente um número inteiro N (1 ≤ N ≤ 3), que indica qual jogador iniciará a rodada ou N = (-1) o que significa que não há mais rodadas para contabilizar e o programa deverá ser encerrado. A segunda linha contém vários números inteiros V (-1 ≤ V ≤ 5) separados por um espaço onde: V = 1 representa a retirada de uma vareta amarela pelo jogador atual, V = 2 uma vareta verde, V = 3 uma vareta azul, V = 4 uma vareta vermelha, V = 5 uma vareta preta. Quando V = 0 indica que o jogador atual mexeu o monte de varetas perdendo a vez, então a jogada seguinte deverá ser do próximo jogador. O valor V = (-1) representa que não há mais varetas para ser retirado e é o fim da rodada atual.

**Saída:** A saída consiste em três linhas para cada caso de teste. A primeira linha mostra o número da rodada. A segunda linha mostra a pontuação do ganhador (ou dos ganhadores se houver empate). Já a terceira linha mostra o(s) ganhador(es). Todas as linhas devem ser formatadas conforme o exemplo de saída. Deve ser deixado uma linha em branco somente entre os casos de teste.

_Exemplo de Saída:_

```
RODADA 1
Ganhador com 20 pontos
Jogador 3
RODADA 2
Empate com 75 pontos
Jogador 2, Jogador 3
RODADA 3
Ganhador com 80 pontos
Jogador 1
RODADA 4
Ganhador com 250 pontos
Jogador 1
```

