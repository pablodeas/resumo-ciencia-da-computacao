import java.util.Scanner;

class Media {
    public static void main(String[] args) {
        double[] Num = new double[50];
        double media, soma = 0;
        Scanner scanner = new Scanner(System.in);
        
        for (int i = 0; i < 50; i++) {
            System.out.println("Digite um número:");

            
            Num[i] = scanner.nextDouble();
            soma += Num[i];
        }
        
        media = soma / 50;

        System.out.println("A média das 50 notas digitadas é: " + media);
    }
}
