import {BrowserRouter, Routes, Route} from "react-router-dom";
import PaginaCadastro from "../Paginas/Cadastro"
import PaginaHome from "../Paginas/Home"
import PaginaLogin from "../Paginas/Login"

const Rotas = () => {
    return(
        <BrowserRouter>
            <Routes>
                <Route path="/home" element={<PaginaHome />} />
                <Route path="/cadastro" element={<PaginaCadastro/>} />
                <Route path="/" element={<PaginaLogin/>} />
            </Routes>
        </BrowserRouter>
    );
};

export default Rotas;