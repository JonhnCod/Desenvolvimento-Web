import React, {Component} from 'react';
import { Link } from 'react-router-dom';
import firebase from '../../Servicos/Firebase';
import NavBar from '../../Components/nav';

class Contato extends Component{
    constructor(props){
      super(props);
    }

    render(){
      return(
        <div className='main'>
            <NavBar Titulo="Pagina Contato" pagina="contato" />
        </div>
      )
    }
}

export default Contato;