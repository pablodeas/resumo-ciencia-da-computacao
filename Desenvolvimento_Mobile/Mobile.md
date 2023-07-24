# Activity, View e o Método setContentView(view)

- Activity ou Atividade:
É um ponto de entrada para o aplicativo;
Fornece a janela por onde será desenhada a Interface de Usuário;

- View:
Ocupa uma área retangular da tela, e é responsável pelo desenho de widgets e seus eventos;
A classe administra os widgets referenciados no arquivo de layout;

- Método setContentView:
Recebe como parâmetro a referência de um arquivo de layout;
Ele irá atribuir a Activity, MainActivity o layout activity_main e, assim, criando uma View.

* Ciclo de Vida de uma Activity
Descreve as etapas que a Activity passa desde sua criação;
É dividido em várias etapas, na seguinte ordem: onCreate() / onStart() / onResume() / onPause() / onStop() / onRestart() / onDestroy();

# A classe R
Classe gerada automaticamente pelo android studio. É responsável por relacionar os recursos do projeto em códigos, para serem compilados.


