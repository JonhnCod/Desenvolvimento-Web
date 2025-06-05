<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>W3.CSS</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="estilos.css">
</head>
<body>

<div id="header">
    <button id="openNav" class="w3-button w3-teal w3-xlarge" onclick="w3_open('menuSidebar')">☰</button>
    <h1 class="titulo-nav">System SuperMarket</h1>
</div>

<div class="w3-sidebar w3-bar-block w3-card w3-animate-left" id="menuSidebar">
    <button class="w3-bar-item w3-button w3-large" onclick="w3_close('menuSidebar')">Close ×</button>
    <a href="#" class="w3-bar-item w3-button" onclick="mostrarOpcoes('Produtos')">Produtos</a>
    <a href="#" class="w3-bar-item w3-button" onclick="mostrarOpcoes('Clientes')">Clientes</a>
    <a href="#" class="w3-bar-item w3-button" onclick="mostrarOpcoes('Funcionarios')">Funcionários</a>
</div>

<div class="w3-sidebar w3-bar-block w3-card w3-animate-left" id="submenuSidebar" style="display: none;">
    <button class="w3-bar-item w3-button w3-large" onclick="w3_close('submenuSidebar')">Voltar</button>
    <div class="w3-bar-item w3-button" onclick="mostrarConteudo('listar')">Listar</div>
    <div class="w3-bar-item w3-button" onclick="mostrarConteudo('cadastrar')">Cadastrar</div>
    
</div>

<div id="main">
    <div class="container" id="conteudo" style="display: none;">
    
    </div><!-- Aqui será exibido o conteúdo dinâmico (lista, formulário, etc.) -->
    
</div>

<script src="script.js"></script>
</body>
</html>

