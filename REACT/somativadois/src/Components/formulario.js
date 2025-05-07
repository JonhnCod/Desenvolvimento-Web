import React,{Component}from "react";
import { Link } from "react-router-dom";


class Formulario extends Component{
    constructor(props){
        super(props);
        this.state = {
            nome:"",
            sobrenome:"",
            email:"",
            data_nasc:"",
            senha:"",
            dados:[]

        }
    }


    render(){
        
        return(
                <div className="formulario">
                    <h1 className="titulo-cadastro">Cadastro</h1>
                    <div className="inputs">

                        <label className="label-form">Nome</label>
                        <input type='text' placeholder='nome' onChange={(e) => this.setState({nome: e.target.value})}/>
                        <br/>
                        <label className="label-form">Sobrenome</label>
                        <input type='text' placeholder='sobrenome' onChange={(e) => this.setState({sobrenome: e.target.value})}/>
                        <br/>
                        <label className="label-form">Email</label>
                        <input type='text' placeholder='Email' onChange={(e) => this.setState({email: e.target.value})}/>
                        <br/>
                        <label className="label-form">Data nascimento</label>
                        <input type='text' placeholder='Data Nasc.' onChange={(e) => this.setState({data_nasc: e.target.value})}/>
                        <br/>
                        <label className="label-form">Senha</label>
                        <input type='text' placeholder='Senha' onChange={(e) => this.setState({senha: e.target.value})}/>
                    </div>
                    <button>Cadastrar</button>
                </div>
        )
    }
}

export default Formulario;