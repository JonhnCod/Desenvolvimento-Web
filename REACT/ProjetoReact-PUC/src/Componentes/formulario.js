import React, { Component } from "react";
import { InputTexto, InputEmail, InputSenha,InputDataNascimento} from './inputs'
import firebase from '../Firebase';
import { Link } from "react-router-dom";

/* Formulario De Cadastro*/
class FormularioCadastro extends Component {
    constructor(props) {
        super(props);
        this.state = {
            nome: "",
            sobrenome: "",
            email: "",
            data_nasc: "",
            senha: "",
            cadastrado:false,
            nomeCadastrado:"",
            mensagemErro:""
        };

        this.gravar = this.gravar.bind(this);
        this.limparMensagemErro = this.limparMensagemErro.bind(this)
        
    }

   

    limparMensagemErro() {

        if (this.state.mensagemErro) {
          this.setState({ mensagemErro: "" });
        }
      }

    async gravar(){

        const { nome, sobrenome, email, data_nasc, senha } = this.state;

        if (!nome || !sobrenome || !email || !data_nasc || !senha) {
            this.setState({ mensagemErro: "Preencha todos os campos." });
            
            return;
          }

       await firebase.auth().createUserWithEmailAndPassword(this.state.email, this.state.senha).then((retorno)=>{
             firebase.firestore().collection("usuario").doc(retorno.user.uid).set({
             nome, sobrenome, data_nasc
         
        });

        this.setState({ 
            cadastrado: true,
            nomeCadastrado: nome,
            nome: "",
            sobrenome: "",
            email: "",
            data_nasc: "",
            senha: ""
        });

        setTimeout(() => {
            this.setState({ cadastrado: false });
          }, 3000);
        });
    }

    render() {
        return (
            <div className="formulario-cadastro">

                <div className="inputs">

                    <InputTexto
                        label="Nome"
                        onChange={(e) => {this.setState({ nome: e.target.value }); this.limparMensagemErro();}}
                        value={this.state.nome}
                        placeholder="Nome"
                    />
                    <InputTexto
                        label="Sobrenome"
                        onChange={(e) => {this.setState({ sobrenome: e.target.value }); this.limparMensagemErro();}}
                        value={this.state.sobrenome}
                        placeholder="Sobrenome"
                    />
                    <InputDataNascimento
                        label="Data de Nascimento"
                        onChange={(e) => {this.setState({ data_nasc: e.target.value }); this.limparMensagemErro();}}
                        value={this.state.data_nasc}
                        placeholder="Data nascimento"
                    />
                    <InputEmail
                        label="Email"
                        onChange={(e) => {this.setState({ email: e.target.value }); this.limparMensagemErro();}}
                        value={this.state.email}
                        placeholder="Email"
                    />
                    <InputSenha
                        label="Senha"
                        onChange={(e) => {this.setState({ senha: e.target.value }); this.limparMensagemErro();}}
                        value={this.state.senha}
                        placeholder="Senha"
                    />
                    <button onClick={this.gravar}>Cadastrar</button>
                    {this.state.mensagemErro && (<p style={{ color: 'red' }}>{this.state.mensagemErro}</p>)}
                    {this.state.cadastrado &&(<p>{this.state.nomeCadastrado}, foi cadastrado com sucesso </p>)}

                </div>
                
            </div>
        );
    }
}

/*--------------------------------------------------------------------------------------------------------------------------------------------------*/

/* Formulário Lgin*/

class FormularioLogin extends Component{
    constructor(props) {
        super(props);
        this.state = {
            email:"",
            senha: "",
        };

        this.acessar = this.acessar.bind(this)
    }

    async acessar(){

        const { email, senha } = this.state;

        if (!email || !senha) {
            alert("Preencha todos os campos");
            return;
        }

        await firebase.auth().signInWithEmailAndPassword(this.state.email, this.state.senha).then((retorno)=>{
            
            window.location.href = "/home";
              

        }).catch((erro)=>{
            alert("usuário ou senha não existe ou invalidos")

        })

        
    }
    render(){
        return(
            <div className="formulario-login">

                <div className="inputs">

                    <InputEmail
                        label="Email"
                        onChange={(e) => this.setState({ email: e.target.value })}
                        value={this.state.email}
                        placeholder="Email"
                    />
                    <InputSenha
                        label="Senha"
                        onChange={(e) => this.setState({ senha: e.target.value })}
                        value={this.state.senha}
                        placeholder="Senha"
                    />
                    
                </div>

                <button className="botao-login" onClick={this.acessar}>Login</button>
                <p className="message-login">Não tem cadastro? Clique <Link to="/cadastro">aqui</Link></p>
            </div>

        )
    }
}

export {FormularioCadastro,FormularioLogin};





    
    
    














