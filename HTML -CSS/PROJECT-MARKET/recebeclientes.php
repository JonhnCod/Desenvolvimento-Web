<?php 

include "conectabd.php";


$nome = $_POST['nome'];
$cpf = $_POST['cpf'];
$datanasc = $_POST['datanasc'];
$telefone = $_POST['telefone'];
$endereco = $_POST['endereco'];
$genero = $_POST['genero'];


$sql = "INSERT INTO clientes (nome,datanasc,cpf,telefone,endereco,genero) VALUES ('$nome', '$datanasc', '$cpf', '$telefone', '$endereco', '$genero')";


$res = mysqli_query($conn, $sql);


if($res){
    echo "<alert>cadastrado com sucesso</alert>";

}else{
    echo "error". mysqli_error($conn);
}




?>