
function w3_open(sidebarID) {
    document.getElementById("main").style.marginLeft = "15%";
    document.getElementById("main").style.backgroundSize = "max-content";
    document.getElementById(sidebarID).style.width = "15%";
    document.getElementById(sidebarID).style.display = "block";
    document.getElementById("openNav").style.display = 'none';
}

function w3_close(sidebarID) {
    document.getElementById(sidebarID).style.display = "none";
    
    if (sidebarID === 'submenuSidebar') {
        document.getElementById("menuSidebar").style.display = "block";
        document.getElementById('conteudo').style.display = 'none'; // Limpa o conteúdo ao fechar o submenu
        document.getElementById("openNav").style.display = 'none';
    } else if (sidebarID === 'menuSidebar') {
        document.getElementById("main").style.marginLeft = "0%";
        document.getElementById("openNav").style.display = "inline-block";
    }
}

function mostrarOpcoes(opcao) {
    var submenu = document.getElementById("submenuSidebar");
    w3_open('submenuSidebar');

    // Lógica para exibir as opções do submenu baseado na opção selecionada no menu principal
    submenu.innerHTML = `<button class="w3-bar-item w3-button w3-large" onclick="w3_close('submenuSidebar')">Voltar</button>
        <div class="w3-bar-item w3-button" onclick="mostrarConteudo('cadastrar-${opcao}')">Cadastrar ${opcao}</div>
        <div class="w3-bar-item w3-button" onclick="mostrarConteudo('listar-${opcao}')">Listar ${opcao}</div>`
        
}

function mostrarConteudo(opcao) {

    if(opcao === 'cadastrar-Clientes'){
        var conteudo = document.getElementById("conteudo");
        conteudo.style.display = "block"

        

    }else if(opcao === 'cadastrar-Produtos'){
        var conteudo = document.getElementById("conteudo");
        conteudo.style.display = "block"

        fetch('cadproduto.php')
        .then(response => response.text())
        .then(data => {
            conteudo.innerHTML = data;
            conteudo.style.display = "block"; // Mostrar o conteúdo após carregar
        })
        .catch(error => console.error('Erro ao obter dados:', error));





    }else if(opcao === 'cadastrar-Funcionarios'){
        var conteudo = document.getElementById("conteudo");
        conteudo.style.display = "block"

        fetch('cadfuncionario.php')
        .then(response => response.text())
        .then(data => {
            conteudo.innerHTML = data;
            conteudo.style.display = "block"; // Mostrar o conteúdo após carregar
        })
        .catch(error => console.error('Erro ao obter dados:', error));

    
        

    }else if (opcao === 'listar-Produtos') {
        var conteudo = document.getElementById("conteudo");
        conteudo.style.display = "block"

        fetch('listarproduto.php')
        .then(response => response.text())
        .then(data => {
            conteudo.innerHTML = data;
            conteudo.style.display = "block"; // Mostrar o conteúdo após carregar
        })
        .catch(error => console.error('Erro ao obter dados:', error));




        
    }else if (opcao === 'listar-Funcionarios') {
        var conteudo = document.getElementById("conteudo");
        conteudo.style.display = "block"

        fetch('listarfuncionario.php')
        .then(response => response.text())
        .then(data => {
            conteudo.innerHTML = data;
            conteudo.style.display = "block"; 
        })
        .catch(error => console.error('Erro ao obter dados:', error)); 



    
        
    }else if (opcao === 'listar-Clientes') {
        var conteudo = document.getElementById("conteudo");
        conteudo.style.display = "block"

        fetch('listaclientes.php')
        .then(response => response.text())
        .then(data => {
            conteudo.innerHTML = data;
            conteudo.style.display = "block"; // Mostrar o conteúdo após carregar
        })
        .catch(error => console.error('Erro ao obter dados:', error)); 

    }

    
}
