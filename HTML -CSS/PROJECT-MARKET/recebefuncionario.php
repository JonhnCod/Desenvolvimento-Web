<?php 

include "conectabd.php";

$nome = $_POST['nome'];
$cpf = $_POST['cpf'];
$rg = $_POST['rg'];
$datanasc = $_POST['datanasc'];
$telefone = $_POST['telefone'];
$endereco = $_POST['endereco'];
$genero = $_POST['genero'];
$cargo = $_POST['cargo'];


$sql = "INSERT INTO funcionarios (nome,cpf,rg,telefone,datanasc,cargo,endereco,genero) VALUES ('$nome', '$cpf', '$rg', '$telefone', '$datanasc', '$cargo','$endereco', '$genero')";



$res = mysqli_query($conn, $sql);


if($res){
    echo "<alert>cadastrado com sucesso</alert>";

}else{
    echo "error". mysqli_error($conn);
}




?>