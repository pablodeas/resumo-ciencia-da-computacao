# Aula 01 - Eficiência e escalabilidade em infraestrutura de TI

**Prof: Everton Juniti Ogura**

## A Época do OnPremises

OnPremises: a empresa detém tudo, como instalações, equipamentos, pessoas, etc.
A empresa precisa comprar (ou construir) seu próprio Data Center.
Aquisição de novos equipamentos às vezes pode levar meses.
Além das pessoas que "cuidam" do Data Center, é necessário investir em segurança.

## Chegada do Hypervisor

Hypervisor: conseguimos gerenciar "mini servidores" dentro de um "servidorzão".
Conseguimos gerenciar servidores virtuais "novos" dentro de um servidor físico.
Começamos a ver o conceito de "Infraestrutura como Seviço".
Uso mais eficiente de recursos.

## Eficiência organizacional: Multi tenancy

Multi tenancy: apartando servidores de forma lógica.
Não só divido um "servidorzão" em "mini servidores", mas segrego os acessos e visibilidade através do "multi tenancy".
Uso de servidor compartilhado aumenta a eficiência na relação de custos, pois eu utilizo o mesmo servidor até o limite.
Não preciso saber onde o servidor físico está, só preciso conseguir acessá-lo.

## Chegada dos Containers

Containers: aproveitando o host para subir uma aplicação isolada em segundos.
Com containers, aproveito o mesmo host (servidor virtual) para não precisar esperar pelo sistema operacional "carregar", possibilitando subir um container em segundos.
Com essa segregação menor, uma aplicação pode ter o mínimo necessário para rodar, sem impactar outras aplicações.
Melhor eficiência em relação à uso do sistema operacional "host".

## Escalabilidade: OnPremises VS Containers

Tudo depende da necessidade da empresa.
Se a empresa vê a necessidade de ter servidores OnPremises, não há problema nenhum.
O uso de containers requer um servidor, seja físico ou virtual. Há a necessidade de estudar o que é possível escalar rápido e o que pode esperar.
Podemos mesclar soluções, basta gerenciar tudo muito bem.