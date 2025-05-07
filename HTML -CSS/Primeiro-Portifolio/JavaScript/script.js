function getParameters() {

    var params    = new Array();
    var paramsRet = new Array();
    var url = window.location.href;     
    var paramsStart = url.indexOf("?"); 
 
    if(paramsStart != -1){ 
     
      var paramString = url.substring(paramsStart + 1); 
      paramString = decodeURIComponent(paramString);    
      var params = paramString.split("&"); 
      for(var i = 0 ; i < params.length ; i++) {
        var pairArray = params[i].split("="); 
        if(pairArray.length == 2){
            var key = pairArray[0];
            var decodedValue = pairArray[1]; 
            paramsRet[key] = decodedValue;
        }
 
      }
      return paramsRet;
    }
    return null; 
 }

 // Função Para estilizar o menu Nav //
function todosElementos(){
  const elementos = document.querySelectorAll('*');
  elementos.forEach(elemento => {
    elemento.style.transition = 'all 0.3s ease-in-out'; 
  });

}

function SublinharNav(){
  const titulos = document.querySelectorAll(".header-index a");
  const links = document.querySelectorAll(".contatos li a")
  const todosElementos = Array.from(titulos).concat(Array.from(links));

  todosElementos.forEach(titulo => {
    titulo.addEventListener('mouseover', function() {
      
      this.style.textDecoration = 'underline';
      this.style.color = '#d8c099' ;
      this.style.fontSize = '30px'
    });
    
    titulo.addEventListener('mouseout', function() {
      this.style.textDecoration = 'none';
      this.style.color ='';
      this.style.transform = 'scale(1)'
      this.style.fontSize = ''
    });
  });

  }


  function estilizarFoto(){
    const foto = document.querySelectorAll('.imagem img');

    foto.forEach(imagem=>{
      imagem.addEventListener('mouseover', function() {
        this.style.boxShadow = '2px 2px 5px #fafafa'
        
        this.style.transform = 'scale(1.1)'
        

      });

      imagem.addEventListener('mouseout', function() {
        this.style.boxShadow = ''
        this.style.transform = 'scale(1)'
        

      });
    })

  }



