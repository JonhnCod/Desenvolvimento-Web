import React, {Component} from 'react';
import { Link } from 'react-router-dom';
import firebase from 'firebase';
import NavBar from '../../Components/nav';

class Principal extends Component{
    constructor(props){
      super(props);
    }

    render(){
      return(
        <div className='main'>
            <NavBar Titulo="Pagina Login"  pagina="principal"/>
        </div>
      )
    }
}

export default Principal;