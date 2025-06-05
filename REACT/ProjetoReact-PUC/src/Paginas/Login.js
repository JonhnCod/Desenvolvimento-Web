import React from "react";
import {FormularioLogin} from "../Componentes/formulario";
import { MenuNav } from "../Componentes/Menunav";
import { Footer } from "../Componentes/Footer";

const PaginaLogin = () => {
    return (
      <div>
        <MenuNav />
        <div className="Body">
          <FormularioLogin />
        </div>
        <Footer/>
      </div>
    );
  };
  
  export default PaginaLogin;