
import javax.swing.*;

class Prog05
{
	public static void main (String entrada[])
	{
		int n1, n2, multi = 0;
		char op = 0;
		String msg = "", msgEntr = "Digite 1 para adição\nDigite 2 para multiplicação\n";
		
		n1 = Integer.parseInt(JOptionPane.showInputDialog("Digite um número inteiro: "));
		n2 = Integer.parseInt(JOptionPane.showInputDialog("Digite outro número inteiro: "));
		op = (JOptionPane.showInputDialog(msgEntr)).charAt(0);
		
		switch(op)
		{
			case '1':
			{
				if(n1 % 2 == 0 && n1 % 2 == 0)
				{
					multi = n1 + n2;
					msg = msg + "Soma de " + n1 + " por " + n2 + " = " + multi + "\n\n";
				}
				break;
			}
			case '2':
			{
				for (int i = 1; i <= n2; i = i + 1)
				{
					multi = multi + n1;
				}
				msg = msg + "Multiplicação de " + n1 + ", " + n2 + " vezes eh: " + multi + "\n\n";
				break;
			}
			default: JOptionPane.showMessageDialog(null, "Opção inválida, cálculo não realizado");
		}
		
		if (op >= '1' && op <= '3')
		{
			JOptionPane.showMessageDialog(null, msg);
		}
		System.exit(0);
	}
}
		
		