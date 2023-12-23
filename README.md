# README do Redimensionador de Imagens

## Visão Geral
Este script em Python utiliza o PyQt6 para criar uma aplicação GUI simples para redimensionar imagens. Os usuários podem escolher um arquivo de imagem, e a aplicação exibe a imagem original juntamente com sua largura e altura. A interface permite que os usuários abram interativamente um arquivo de imagem, visualizem seus detalhes e possivelmente redimensionem.

## Uso
1. Execute o script em um ambiente Python.
2. A janela principal será aberta, apresentando a opção de escolher um arquivo de imagem.
3. Clique no botão "Escolher Arquivo" para abrir um diálogo de arquivo.
4. Selecione um arquivo de imagem para visualizar seus detalhes na interface.
5. A imagem original será exibida com informações de largura e altura.

## Estrutura do Código
- O script utiliza o PyQt6 para a GUI, herdando de QMainWindow e Ui_MainWindow.
- A classe `Redimensiona` lida com a funcionalidade principal.
- O método `abrir_img` conecta o botão "Escolher Arquivo" para abrir um diálogo de arquivo e exibir detalhes da imagem.

## Dependências
- PyQt6: Utilizado para criar os componentes da GUI.
- sys: Fornece acesso a algumas variáveis usadas ou mantidas pelo interpretador Python.
- design: Presumivelmente contém as especificações de design da interface do usuário.

## Fontes
1. [Python GUIs com PyQt6](https://www.pythonguis.com/pyqt6-tutorial/)
2. [Criando seu primeiro aplicativo com PyQt6](https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/)
3. [YouTube - Criando Aplicações GUI em Python com PyQt6](https://www.youtube.com/watch?v=QUen46LXBhc)

Sinta-se à vontade para modificar o script ou incorporá-lo em seus projetos conforme necessário. Para mais detalhes, consulte as fontes fornecidas e a documentação do PyQt6.
