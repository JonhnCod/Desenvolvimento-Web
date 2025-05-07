import React, {Component} from 'react';
import { Link } from 'react-router-dom';
import firebase from '../../Servicos/Firebase';
import NavBar from '../../Components/nav';
import Formulario from '../../Components/formulario';
import pucprImg from '../../Assets/pucpr-enade-2048x1152.jpeg';



class Cadastro extends Component {

    constructor(props){
        super(props);
        this.state = {
            dados:[],
            nome:"",
            sobrenome:"",
            email:"",
            senha:"",
            data_nasc:""


        };
    };

    render(){
        return(
            <main>
                <NavBar props={"Página de Cadastro"} pagina="cadastro" />
                <section className='pag-cadastro'>
                    <div className='container-form'>
                        <img src={pucprImg} alt='img'/> 
                        <Formulario/>
                    </div>
                </section>

                <footer>Jonhn-2025</footer>
            </main>
            
        );
    };
};

export default Cadastro;

//