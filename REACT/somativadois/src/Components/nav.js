import React from "react";
import links from "./links";
import '../Estilos/Rotas.css';
import logo_puc from '../Assets/logo_puc-pr_eIXsWO.png';


const NavBar = ({props,pagina}) =>{
    return(
        
        <div className="header">
            <img className='logo-nav' src={logo_puc} alt='img'/>
            <ul className="div-ul"> 
                {links[pagina].map((link) => (
                    link
                ))}
            </ul>
        </div>
    )
}



export default NavBar;