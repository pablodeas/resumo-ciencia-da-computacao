
import javax.swing.*;

class Prog08
{
	public static void soma (int vet[])
	{
		int s = 0;
		
		for (int i = 0; i < vet.length; i++)
		{
			s = s + vet[i];
		}
		
		JOptionPane.showMessageDialog(null, "O Resultado da Soma é: " + s);
	}
	
	public static int produto (int vet[])
	{
		int p = 1;
		
		for (int i = 0; i < vet.length; i++)
		{
			p = p * vet[i];
		}	
	
		return p;
	}
	
	public static void main (String entrada[])
	{
		int s = 0, vt[] = {5, 6, 7, 8, 9};
		int r;
		
		soma (vt);
		r = produto (vt);
		JOptionPane.showMessageDialog(null, "O Produto é: " + r);
		System.exit(0);
	}
}
