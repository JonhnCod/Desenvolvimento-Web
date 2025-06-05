import React, { Component } from "react";
import { FaGithub, FaLinkedin } from 'react-icons/fa';



export class Footer extends Component{


    render(){

        return(

            <footer>
            
                <a href="https://github.com/jonhncod" target="_blank">
                    <FaGithub size={30} />
                </a>
                <a href="https://linkedin.com/in/jonathanarruda34" target="_blank">
                    <FaLinkedin size={30} color="#0e76a8" />
                </a>
            
            </footer>
        )

        
    }
}
 