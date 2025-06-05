<?php 

include "conectabd.php";


$sql = "SELECT * FROM clientes"; // variavél para solicitação dos Ids na tabela de clientes !

$res = mysqli_query($conn, $sql);//Variavel que recebe valores da funcao onde recebe por paramentro a conexão com o BD e solicita valores de id feito na solicitção guardada na variavel $sql 

if ($res) {
    echo "<table border='1'>
            <tr>
                <th>ID</th>
                <th>Data de Nascimento</th>
                <th>CPF</th>
                <th>Telefone</th>
                <th>Nome</th>
                <th>Gênero</th>
            </tr>";

    while ($row = mysqli_fetch_assoc($res)) {
        echo "<tr>
                <td>".$row['id']."</td>
                <td>".$row['datanasc']."</td>
                <td>".$row['cpf']."</td>
                <td>".$row['telefone']."</td>
                <td>".$row['nome']."</td>
                <td>".$row['genero']."</td>
                <td><a href='#'>Editar</a></td>
                <td><a href='#'>Excluir</a></td>
              </tr>";
    }

    echo "</table>";
} else {
    echo 'Erro na consulta: ' . mysqli_error($conn);
}

mysqli_close($conn);






?>