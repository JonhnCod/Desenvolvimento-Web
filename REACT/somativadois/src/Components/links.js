import { Link } from "react-router-dom"

const links = {
    home: [
        <Link to="/Login" key="login">Login</Link>,
        <Link to="/Cadastro" key="cadastro">Cadastro</Link>
    ],

    cadastro: [
        <Link to="/Login" key="login">Login</Link>,
        <Link to="/" key="home">Home</Link>
    ],

    contato: [
        <Link to="/Sobre" key="sobre">Sobre</Link>,
        <Link to="/" key="home">Home</Link>
    ],

    login: [
        <Link to="/Cadastro" key="cadastro">Cadastro</Link>,
        <Link to="/" key="home">Home</Link>
    ],

    sobre: [
        <Link to="/Contato" key="contato">Contato</Link>,
        <Link to="/" key="home">Home</Link>
    ]
};

export default links;