import React from "react";
import { FormularioCadastro } from "../Componentes/formulario";
import { MenuNav } from "../Componentes/Menunav";
import { Link } from "react-router-dom";
import { Footer } from "../Componentes/Footer";


const PaginaCadastro = () => {
  return (
    <div>
      <MenuNav />
      <div className="Body">
        <FormularioCadastro />
        <p>Voltar para o <Link to="/">Login</Link></p>
     
      </div>
      
      <Footer/>
    </div>
  );
};

export default PaginaCadastro;


