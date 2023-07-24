# Classes Abstratas, Interfaces e Princípios da Orientação a Objetos

- Classe
Conjunto de objetos que poderá ter implementações.

## Classes Abstratas
Usamos para representar grupos que têm características comuns, mas que, em alguns detalhes específicos, agem de maneira diferente.
Possuem uma característica comum e outras característica específicas.
Então dizemos que animal é uma classe abstrata, porque possui algumas características iguais e outras características que possuem detalhes específicos de animais diferentes.
. Não podem ser instanciadas.
. Define atributos e operações que outras classes irão herdar posteriormente.
. Pode possuyir declarações de métodos vazias e/ou métodos implementados.

## Interfaces
Estabelece um contrato entre partes para realizar o mesmo processo.
. Funciona como um Contrato para uma ou mais classes.
. Define comportamento obrigatório que alguma classe deve possuir.
. É implementada, por uma ou mais classes, as quais prometem implementar todos os métodos neça especificados.
. Possui declarações vazias de métodos.
. Todos os métodos na interface são 'abstract' e 'public' por padrão, colocar esses modificadores no código é redundância.
. Toda variável é final. Ou seja, não pode ser alterada.

- Exemplo de interface:

public interface Autenticacao{
	void autenticar();
}

. Nas interfaces, só terei "definição" vazias dos métodos. Não terei implemtentação dos métodos, por isso eles terminaram com ';' ao invés de terem chaves ({}).

- Exemplo de uma classe interligada a outra:

public class Diretor implements Autenticacao{
	public void autenticar(){
		System.out.println("Aqui desenvolvo como o Diretor vai se autenticar!");
	}
}

- Uma diferença entre classes e interfaces é que a classe declara e implementa seus métodos, enquanto a interface apenas declara.


## Encapsulamento
Serve para controlar o acesso aos atributos e métodos de uma classe.
É uma forma eficiente de proteger os dados manipulados dentro da classe, além de determinar onde esta classe poderá ser manipulada.

- Pilares da Orientação a Objeto
. Encapsulamento
. Herança
. Polimorfismo
. Composição

- Princípios da Abstração
. Consiste em focalizar nos aspectos essenciais inerentes a uma entidade e ignorar propriedades acidentais
. Em termos de desenvolvimento de sistemas, isto significa concentrar-se no que um objeto é e faz antes de se decidir como ele será implementado.
. Uma classe é uma abstração de entidades existentes no domínio do sistema de software

O uso de abstração preserva a liberdade para tomar decisões de desenvolvimento ou de implementação apenas quando há um melhor entendimento do problema a ser resolvido.

Modificador de acesso 'private'
Ex:

public class PessoaFisica{
	private int quantidadeFilhos;

	private void quantidadeFilhos(int quantidade){
		quantidadeFilhos = quantidade;
		System.out.println("Imprime a quantidade de filhos" + quantidade);
	} 
}

## Getter and Setters
Controlam o acesso a cada um dos atributos e operações de uma certa classe.
Tem a função de disponibilizar externamente os métodos que alteram e acessam os atributos de uma classe.

- Métodos getters
public String getName(){
	return name;
}
public double getSalario(){
	return salario;
}

- Métodos setters
public void setNome(String nome){
	this.nome = nome;
}
public void setSalario(double salario){
	this.salario = salario;
}

