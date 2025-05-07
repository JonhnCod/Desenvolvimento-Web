import {BrowserRouter, Routes, Route} from "react-router-dom";
import Cadastro from "../Paginas/Cadastro/indexCad";
import Contato from "../Paginas/Contato/indexCont";
import Home from "../Paginas/Home/indexHome";
import Sobre from "../Paginas/Sobre/indexSobre";
import Login from "../Paginas/Login/indexLogin";
import Principal from "../Paginas/Principal/indexPrinci";


const Rotas = () => {
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/sobre" element={<Sobre />} />
                <Route path="/contato" element={<Contato />} />
                <Route path="/cadastro" element={<Cadastro/>} />
                <Route path="/login" element={<Login/>} />
                <Route path="/principal" element={<Principal/>} />
            </Routes>
        </BrowserRouter>
    );
};

export default Rotas;