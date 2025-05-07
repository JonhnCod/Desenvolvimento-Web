import React, {Component} from 'react';
import { Link } from 'react-router-dom';
import firebase from '../../Servicos/Firebase';
import NavBar from '../../Components/nav';

class Home extends Component{
    constructor(props){
      super(props);
    }

    render(){
      return(
        <div className='main'>
            <NavBar Titulo="Página Home" pagina="home"></NavBar>
        </div>
      )
    }
}

export default Home;