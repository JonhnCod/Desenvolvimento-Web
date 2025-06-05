<?php 

include "conectabd.php";


$sql = "SELECT * FROM produtos"; // variavél para solicitação dos Ids na tabela de clientes !

$res = mysqli_query($conn, $sql);//Variavel que recebe valores da funcao onde recebe por paramentro a conexão com o BD e solicita valores de id feito na solicitção guardada na variavel $sql 

if ($res) {
    echo "<table border='1'>
            <tr>
                <th>ID</th>
                <th>nome</th>
                <th>tipo</th>
                <th>preco</th>
                <th>quantidade</th>
                
            </tr>";

    while ($row = mysqli_fetch_assoc($res)) {
        echo "<tr>
                <td>".$row['id']."</td>
                <td>".$row['nome']."</td>
                <td>".$row['tipo']."</td>
                <td>".$row['preco']."</td>
                <td>".$row['quantidade']."</td>
                <td><a href='cadproduto.php?id=" . $row['id'] . "'>Editar</a></td>
                
                
              </tr>";
    }

    echo "</table>";
} else {
    echo 'Erro na consulta: ' . mysqli_error($conn);
}

mysqli_close($conn);

?>