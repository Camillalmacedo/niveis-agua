#  🫧Controle de Níveis de água
<div style="display: inline_block"><br>
 <img align="center" alt="Python" height="40" width="40"
src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg"> 
</div> 

📚 No desenvolvimento deste código em **Python**, foram utilizadas duas bibliotecas: **random**, para fazer a escolha aleatória de um nível de água a cada vez que o programa for testado; e **colorama** para personalizar a cor da mensagem ao usuário de acordo com cada nível.


🖊️ O primeiro passo foi a criação da **lista** com as possíveis situações de níveis de água. Então precisei criar duas **funções**. A primeira acessa a biblioteca random e faz a escolha aleatória de um número entre 1 e 5, o qual será armazenado e utilizado posteriormente para representar o nível de água. A segunda função acessa a biblioteca colorama (instalei através do "pip install colorama" no terminal) e usa as estruturas condicionais **if**, **elif** e **else** para decidir a cor de cada nível, ou retornar a mensagem "Nível inválido".


✨ Por fim, o programa mostra o nível sorteado e sua respectiva cor e **desativa** a função da biblioteca colorama, fazendo o terminal retornar à cor padrão.