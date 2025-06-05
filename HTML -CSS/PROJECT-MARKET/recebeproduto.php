<?php 

include "conectabd.php";

$nome = $_POST['nome'];
$tipo = $_POST['tipo'];
$preco = $_POST['preco'];
$quantidade = $_POST['quantidade'];


$sql = "INSERT INTO produtos (nome,tipo,preco,quantidade) VALUES ('$nome', '$tipo', '$preco', '$quantidade')";

$res = mysqli_query($conn, $sql);


if($res){
    echo "<alert>cadastrado com sucesso</alert>";

}else{
    echo "error". mysqli_error($conn);
}




?>