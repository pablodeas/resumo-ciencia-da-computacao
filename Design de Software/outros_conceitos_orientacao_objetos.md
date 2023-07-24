# Outros Conceitos de Orientação a objetos

# Abstração
Em orientação a objetos, busca-se um olhar isolado ao objeto de uma forma gera, definindo o que deve ser feito e não o como deve se fazer. A abstração é aplicada com as classes abstratas e interfaces, que definem um contrato com outras classes relacionadas.

# Encapsulamento
Os dados na OO são protegidos atravpes do acesso somente pelos seus atributos (identificadores) e métodos (comportamento). à essa proteção denominamos Encapsulamento. Analogicamente podemos pensar em um ovo, onde a gema seria os dados e a clara os métodos e atributos que os cerca.


# Herança
Mecanismo que permite definir uma nova classe (subclasse) a partir de uma classe que já existe (superclasse).
Classe "filha" herda comportamentos e atributos da classe "pai".
Relacionamento de herança chamamos de É-UM.
- Exemplo: Diretor é um Funcionário; Professor é um funcionário.

# Tipos de Herança
Herança Simples:
		Uma classe pode ser filha de apenas uma classe
Herança Múltipla:
		Uma classe que pode ser filha de mais de uma classe
	
# Exercícios Sobre Herança
Em programação orientada a objetos, é correto afirmar que herança múltipla...
		Permite que uma classe herde atributos e métodos de duas ou mais classes. Em programação orientada a objetos, a herança serve para criar classes que incorporem propriedades e métodos de outras classes. Assim, é possível construir uma classe a partir de outra sem ter de reescrevê-la.
-
No contexto de programação orientada a objetos podemos dizer que:
	Objetos são instâncias de classes.
	Herança é uma relação entre classes.
	Mensagens são formas de executar métodos.
	Classe é como se fosse uma forma para a criação de objetos.
	Interface é um contrato que uma classe pode implementar.

# Polimorfismo
Poli = muitas, morfo = formas
Polimorfimso é a capacidade de um objeto poder ser referenciado de várias formas.
Quando duas ou mais classes distintas tem métodos com o mesmo nome.
Polimorfismo pode existir graças ao conceito de Herança.

- Existem dois tipos de Polimorfismo: Dinâmico e Estático.

## Dinâmico
Está diretamente relacionada com a herança. Com a sobrescrita, conseguimos especializar os métodos herdados das superclasses, alterando (redefinindo) o seu comportamento nas subclasses por um mais específico.
Mesmo nome de método e argumentos iguais.
Decisão de qual método é chamado é feita em tempo de execução.
Identificado com sobrescrita (override, binding dinâmico).
Com a sobrescrita, conseguimos especializar os métodos herdados das superclasses, alterando (redefinindo) o seu comportamento nas subclasses por um mais específico.
Mesmo nome de método e argumentos iguais.
Um exemplo de sobrescrita é o método calculoSalario() nas classes Coordenador e Professor. Ambas as classes sobrescrevem o método calculoSalario().
Uma outra característica da sobrescrita é que a escolha do método a executar é realizada em tempo de execução para o objeto instanciado.

## Estático
Está diretamente relacionada com ao polimorfismo. Mesmo nome de método e argumentos diferentes (tipo de retorno ou número de parâmetros).
Estamos contruindo um novo comportamento e não redefinindo o comportamento (Sobrescrita).
Ocorre em tempo de compilação.
Identificado como sobrecarga(overloading). Está diretamente relacionado com o polimorfismo. Mesmo nome de método e argumentos diferentes (tipo de retorno ou número de parâmetros). A ideia é construir um novo comportamento e não redefinir o comportamento (Sobrescrita). Neste caso, a escolha do método a ser executado ocorre em tempo de execução.

# Composição
Uma maneira de se combinar objetos simples para formar objetos mais complexos.
Relacionamento "tem-um".
Muito usada em padrões de projeto.
Mais flexível que herança.
	Herança causa uma dependência grande entre as classes 'filhas' e a classe 'pai'.

# Análise e Projeto OO
Antes de escrever o código, é necessário analisar os requisitos (o quê) de seu projeto e projetar uma solução (como) satisfatória.
		Pode poupar muitas horas de trabalho e dinheiro.
Quando esta análise envolve um ponto de vista de OO, chamamos de análise e projeto orientados a objetos.
Idealmente, membros de um grupo de desenvolvimento devem definir um processo para resolver um determinado problema e uma maneira uniforma para comunicar os resultados deste processo para outro.
Uma linguagem gráfica utilziada para comunicação de qualquer processo de análise e projeto OO é a "Unified Modeling Language".

# Requisitos
Constituem uma especificação das características e propriedades do sistema.
Uma descrição do que o sistema deve fazer, de como ele deve se comportar, bem como das suas restrições de operação.
É importante ressaltar que os requisitos descrevem "o que o sistema deve fazer" - e também "o que ele não deve fazer" - sem dizer "o como fazer".

## Desenvolvimento
Requisitos Funcionais;
		Descrevem o que um sistema deve fazer.
Requisitos não Funcionais;
		São restrições sobre os serviços ou funções oferecidas pelo sistema.
		Não dizem respeito diretamente às funções específicas do sistema e suas restrições. Mas não deixam de estar relacionadas.
Requisitos de Domínio;
		São as regras de negócio.

## Evolução e Manuntenção
Requisitos Permanentes;
		Requisitos que não mudam.
Requisitos Voláteis;
	Mutáveis;
		Se modificam por causa do ambiente do sistema.
	Emergentes;
		Surgem à medida que a compreensão do cliente do sistema se desenvolve.
	Consequentes;
		Resultam da introdução do sistema no ambiente do usuário.
	Compatibilidade;
		São os requisitos que dependem de outro equipamento ou processo. Conforme muda esse equipamento, os requisitos também mudam.
		
## Outros Requisitos
Requisitos de usuário são declarações, em uma linguagem natural com diagramas para que qualquer um possa entender.
		O que ele faz (Funcionais)?
		Como ele faz (Não Funcionais)?
Requisitos de sistema são descrições mais detalhadas das funções, serviçoes e restrições operacionais do sistema de software.
		O que ele faz (Funcionais)?
		Como ele faz (Não Funcionais)?
	
## Problema da Análise de Requisitos
Stakeholders(cliente) em geral não sabem o que querem;
Stakeholders expressam requisitos em sua terminologia;
Stakeholders diferentes podem gerar requisitos conflitantes;
Fatores políticos e oprganizacionais podem influenciar os requisitos do sistema;
Requisitos mudam durante o processo de análise. Stakeholders novos podem surgir e o ambiente de trabalho muda;

# Validação dos Requisitos
Será que realmente entendi o que cliente deseja?;
Devo me certificar de que não houve falha em nossa interação;
Demonstrar que os requisitos definem o sistema que o cliente realmente deseja;
Custos com erros de requisitos altos;
		Consertar um erro de requisitos após entrega do sistema pode custar mais de 100 vezes o custo de um erro de implementação.
		

