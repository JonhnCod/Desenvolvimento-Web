import React, { Component } from "react";
import { MenuNav } from "../Componentes/Menunav";
import { Link } from "react-router-dom";
import firebase from '../Firebase';
import { Footer } from "../Componentes/Footer";


class PaginaHome extends Component {
  constructor(props) {
    super(props);
    this.state = {
      nome: "",
      sobrenome: "",
      email: "",
      data_nasc: "",
      logado: false,
      carregando:true
    }
  }

  handleUnload = () => {
    firebase.auth().signOut();
  };
  

  componentDidMount() {

     firebase.auth().onAuthStateChanged((user) => {

      if (user) {
        var uid = user.uid;

        firebase.firestore().collection("usuario").doc(uid).get().then((resultado) => {

          this.setState({
            nome: resultado.data().nome,
            sobrenome: resultado.data().sobrenome,
            data_nasc: resultado.data().data_nasc,
            logado: true,
            carregando:false
          });

        });


      } else {
    
        this.setState({ logado: false,carregando:false }); 
    }
    });

    window.addEventListener("beforeunload", this.handleUnload);

  }

  componentWillUnmount() {
    window.removeEventListener("beforeunload", this.handleUnload);
  }
  

  render() {
    if(this.state.carregando){
      return <div><MenuNav/><br/><br/><p>...</p></div>
    }

    if (!this.state.logado) {
      return <p>Pra acessar essa pagina precisa estar Autenticado <Link to={"/"}>Login</Link></p>;
    }
    return (
      <div>
        <MenuNav />
        

        <div className="Body">
        <table border="1">
          <tbody>
            <tr>
              <td>Nome</td>
              <td>{this.state.nome}</td>
            </tr>
            <tr>
              <td>Sobrenome</td>
              <td>{this.state.sobrenome}</td>
            </tr>
            <tr>
              <td>Data de Nascimento</td>
              <td>{this.state.data_nasc}</td>
            </tr>
          </tbody>
        </table>
        
    </div>
    <Footer/>
     
      </div>
    )};
  }

export default PaginaHome;
