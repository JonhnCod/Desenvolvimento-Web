<?php
include "conectabd.php";

$nome = "";
$tipo = "";
$preco = "";
$quantidade = "";

if(isset($_GET['id'])){
    $id = $_GET['id'];
    $sql = "SELECT * FROM produtos WHERE id = $id";
    $res = mysqli_query($conn, $sql);
    $row = mysqli_fetch_assoc($res);

    // Verifica se a consulta retornou um resultado
    if ($row) {
        // Atribui os valores às variáveis
        $nome = $row['nome'];
        $tipo = $row['tipo'];
        $preco = $row['preco'];
        $quantidade = $row['quantidade'];
    } else {
        // Caso o ID não exista ou não retorne resultados
        echo "Produto não encontrado.";
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <title>Cadastro/editar funcionarios</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="estilos.css">
</head>
<body>
    <div id="header">
        <h1 class="titulo-nav">System SuperMarket</h1>
    </div>
    <div id="main">
        <div class="container" id="conteudo" style="display: 'none';">
            <form action="recebeproduto.php" method="POST">
                <h2>Cadastrar</h2>
                <div class="input">
                    <label for="nome">Nome</label>
                    <input type="text" name="nome" id="nome" value="<?php echo $nome; ?>" require > 
                </div>

                <div class="input">
                    <label for="tipo">Tipo</label>
                    <input type="text" name="tipo" id="tipo"  value="<?php echo $tipo; ?>"require> 
                </div>

                <div class="input">
                    <label for="preco">Preco(R$)</label>
                    <input type="text" name="preco" id="preco" value="<?php echo $preco; ?>"> 
                </div>


                <div class="input">
                    <label for="quantidade">Quantidade(Un)</label>
                    <input type="number" name="quantidade" id="quantidade" value="<?php echo $quantidade; ?>"> 
                </div>

                    
                <div class="input" id="btn">
                    <button type="submit">Cadastrar</button>
                </div>

            </form>

        
        </div>
    </div>
</body>
</html>
