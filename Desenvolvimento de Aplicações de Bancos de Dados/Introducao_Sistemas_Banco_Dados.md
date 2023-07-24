## Aula 01

# Dados x Informação x Conhecimento
	"Dado é o novo Petrólio" (Clive Humby, 2066)
Os dados, juntos, formam um conjunto de informações.
Informações são usadas para adquirir o conhecimento.
O conhecimento, por definição, é nosso entendimento sobre as informações.

# Sistema baseado em Arquivos
- O que são arquivos?:
"Reunião dos dados de um computador que, com registro individual e organizados sob um formato específico, contém textos, tabelas, imagens, sons, etc."
Cada software tem o seu próprio formato (extensão) de arquivo.
Os arquivos contém instruções sequenciais para o software de como devem ser lidos.
Arquivos guardam dados e informações.
Podemos armazenar qualquer informação em um sistemas de arquivos.
- Inconsistência e redundância de dados:
Aplicações evoluem com o tempo e há formatos demais, gerando, muitas vezes, repetições de dados.
- Dificuldade de acesso aos dados:
Os dados nos arquivos normalmente só podem ser acessados de uma forma, e as vezes, isso pode atrasar o acesso à informação.
- Isolamento dos dados:
Muitas vezes o compartilhamento de dados pode ser dificultado pois nem sempre quem os recebe possui o mesmo software (e/ou versão) para acessar.
- Falta de integridade:
Realizar buscas de dados em arquivos pode resultar em dados duplicados ou ignorados, devido ao formato de como são gerados ou guardados.
- Falta de atomicidade: 
Nem sempre existem mecanismos de tratamento de erros (causados por qualquer motivo) em arquivos e os dados podem ser perdidos.
- Falta de segurança: 
Muitas vezes a proteção dos arquivos é responsabilidade do sistema operacional e, muitas vezes, dados sensíveis são rapidamente acessados.

# Banco de Dados
São sistemas criados exclusivamente para armazenamento de dados.
Também chamados de databases.
O armazenamento ocorre de forma organizada, em estruturas específicas(tabelas).
- História:
Na década de 60 a IBM percebeu que os sistemas de arquivos tinham muitos problemas e começou a desenvolver pesquisas de como solucioná-los.
Em 1970 Edgar Todd(IBM) apresentou um artigo sobre um modelo relacional de armazenamento de informações. 
"A Relational Model of Data for Large Shared Data Banks"
Mas somente na década de 80 que a IBM apresentou seu primeiro sistema de bancos de dados: projeto System R -> SQL/DS -> DB2
Depois disso, várias empresas começaram a surgir com propostas muito parecidas. Oracle, por exemplo.
Mas foi no final de século XX, com o "boom" da internet que os bancos de dados realmente começaram a ganhar espaço.
A tecnologia estava evoluindo muito rápido. Novas linguagens, hardwares cada vez mais poderosos impulsionaram as pesquisas.
- Motivações Importantes:
Os sistemas de bancos de dados surgem para resolver os principais problemas dos sistemas baseados em arquivos.
Isso ocorre devido à sua estrutura, capacidade e desempenho.
- Servem X Não Servem:
Bancos de dados servem para armazenar dados.
Não servem para armazenar conhecimento.
Qualquer tipo de dado pode ser armazenado num banco de dados.
Não é necessariamente mais barato do que sistemas de arquivos.
Servem para armazenar dados que podem ser usados por qualquer aplicação.
A implementação a manutenção não é trivial.

# Banco de Dados: Principais Características
- Princípio:
Os dados ficam armazenados em tabelas!
É muito comum chamarmos tabelas de entidades.
- Toda entidade precisa ter:
Nome / Conjunto de colunas(atributos).
Os atributos são as características que seus dados podem assumir, neste determinado contexto.

## Aula 02 - Projeto de Banco de Dados

# O que é um projeto?
"É um esforço temporário empreendido para criar um produto, serviço ou resultado exclusivo" (PMBOK, PMI, 2017)
- Ciclo de vida:
Iniciação / Planejamento / Execução / Encerramento
- Ciclo de vida/<Iniciação>:
Justificativa do Projeto; 
Objetivo do Projeto; 
Definição do time; 
Identificação dos Stakeholders; 
Características do produto, serviço ou resultado; 
Quais serão as entregas; Como cada entrega é aceita; 
Expectativas de custos e prazos; Alinhamento com as partes interessadas.
- Ciclo de vida/<Iniciação/Stakeholders>: 
Indivíduo ou organização que, de alguma forma, é impactado pelas ações de uma determinada empresa. Clientes, fornecedores, funcionários, comunidades e investidores são exemplos.
- Ciclo de vida/<Planejamento>:
Metologia de gestão; Detalhamento de escopo e riscos; Estrutura Analítica do Projeto (EAP); Levantamento de recursos; Planejamento de aquisições; Previsão detalhada de custos; Cronograma de atividades;
- Ciclo de vida/<Execução>:
Colocar em prática;
Monitorar;
Corrigir;
Atualizar;
- Ciclo de vida/<Encerramento>:
Encerramento de contratos;
Entrega dos resultados;
Aprovação dos resultados;
O que deu certo?;
O que deu errado?;
Arquivamento;

# Análise de Requisitos
Assim como qualquer projeto, os bancos de dados também precisam de um processo bem definido para implementação.
- Projeto de Banco de Dados
Mundo Real(O contexto, o mundo onde nosso projeto está inserido);
Análise de Requisitos;
Modelo Conceitual;
Modelo Lógico;
Modelo Físico;

# Modelo Conceitual
A finalidade do modelo conceitual de dados é capturar os requisitos de informação e regras de negócio sob o ponto de vista do negócio. Para isto, torna-se necessário o entendimento e a correta aplicação dos mecanismos de abstração, utilizados na modelagem conceitual de dados.

# Modelo Lógico e Físico
- Modelo Lógico:
Nesta fase que definimos o tipo e tamanho do dado, chaves primárias, etc. Derivado do modelo conceitual.
- Modelo Físico:
Descreve como será feita a armazenagem no banco, se escolhe o sistema gerenciador, etc.

## Aula 03 - O que é um sistema

# Princípios básicos de um sistema
"Reunião de elementos concretos ou abstratos que se interligam de modo a formar um todo organizado" (Dicionário)
- Sistema, em nossa área:
Um sistema é um conjunto de elemenstos interconectados, de modo a formar um todo organizado.
Um sistema sempre tem uma ou mais entradas e uma ou mais saídas.
Sistemas interagem com o meio através de suas entradas e saídas.
Sistema é uma grande caixa que tem uma ou mais entradas e uma ou mais saídas.
Sistema é formado de Hardware, Software, Banco de Dados e qualquer outras informações necessárias, pertinentes ao sistema.

# Por que as pessoas usam sistemas de TI?
Os usuários tem metas e necessidades e muitas vezes elas só podem ser resolvidas se utilizando um sistema criado pelos profissionais de TI.
- Outros:
Automatiza o trabalho do usuário
Organização
Melhorias nos processos
Agilidade
Redução da sensação de distanciamento
redução no uso de papel
Entretenimento

# Por que planejar um sistema é importante
---

# Como você quer o seu sistema?
Muitas vezes os clientes não conseguem explicar suas metas e necessidades.
Nós temos que adentrar os processos específicos de nossos clientes.
Complexidade em nossa área está atrelada à complexidade do cliente.
Temos que ter processos muito bem definidos.
Planejamento contínuo -> Melhoria contínua.
Metologias modernas de gestão geram melhores resultados.
Times empenhados e unidos.

