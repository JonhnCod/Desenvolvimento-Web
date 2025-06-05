<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>Cadastro/editar funcionarios</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <div class="container" id="conteudo">
        <form action="recebefuncionario.php" method="POST">
            <div class="input">
                <label for="nome">Nome</label>
                <input type="text" name="nome" id="nome" require > 
            </div>

            <div class="input">
                <label for="cpf">CPF</label>
                <input type="number" name="cpf" id="cpf" require> 
            </div>

            <div class="input">
                <label for="rg">RG</label>
                <input type="number" name="rg" id="rg"> 
            </div>

            <div class="input">
                <label for="telefone">TELEFONE</label>
                <input type="tel" name="telefone" id="telefone"> 
            </div>


            <div class="input">
                <label for="datanasc">DATA NASCIMENTO</label>
                <input type="date" name="datanasc" id="datanasc"> 
            </div>

            <div class="input">
                <label for="cargo">CARGO</label>
                <input type="text" name="cargo" id="cargo"> 
            </div>

            <div class="input">
                <label for="endereco">ENDERECO</label>
                <input type="text" name="endereco" id="endereco"> 
            </div>

            <div class="input-genero" id="sexo">
                <label for="genero">GENERO</label>
                <div class=input-opcao>
                    <input type="radio" name="genero" id="genero" value="M"> Masculino 
                    <input type="radio" name="genero" id="genero" value="F"> Femenino 
                </div>
            </div>
                
            <div class="input" id="btn">
                <button type="submit">Cadastrar</button>
            </div>

        </form>
        
    </div>



</body>
</html>