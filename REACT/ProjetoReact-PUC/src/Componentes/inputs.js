import React from "react";

//INPUTS//
export const InputTexto = ({ label,value, onChange, placeholder }) =>{
    return (
      <div>
        <label>{label}</label><br />
        <input
          type="text"
          onChange={onChange}
          value={value}
          placeholder={placeholder} 
        />
      </div>
    );
  }

export const InputEmail = ({ label,value, onChange, placeholder,}) => {
    return (
      <div>
          <label>{label}</label><br />
          <input
            type="email"
            onChange={onChange}
            value={value}
            placeholder={placeholder}
            
          />
        </div>
      );
    }
    
export const InputSenha = ({ label,value, onChange, placeholder})=> {
    return (
      <div>
          <label>{label}</label><br />
          <input
            type="password"
            onChange={onChange}
            value={value}
            placeholder={placeholder}
            
          />
        </div> 
    );
}

export const InputDataNascimento = ({ label,value, onChange, placeholder}) => {
    return (
      <div>
            <label>{label}</label><br />
            <input
              type="date"
              onChange={onChange}
              value={value}
              placeholder={placeholder}
              
            />
        </div>
    );
};