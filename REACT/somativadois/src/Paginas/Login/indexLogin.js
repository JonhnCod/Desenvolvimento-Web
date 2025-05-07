import React, {Component} from 'react';
import { Link } from 'react-router-dom';
import firebase from 'firebase';
import NavBar from '../../Components/nav';

class Login extends Component{
    constructor(props){
      super(props);
    }

    render(){
      return(
        <div className='main'>
            <NavBar Titulo="Pagina Login"  pagina="login"/>
        </div>
      )
    }
}

export default Login;