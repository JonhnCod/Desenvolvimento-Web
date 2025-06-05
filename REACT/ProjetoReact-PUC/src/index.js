import React from 'react';
import ReactDOM from 'react-dom/client';
import Rotas from './Rotas/Rotas';
import reportWebVitals from './reportWebVitals';
import './Estilos/styles.css';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Rotas/>
  </React.StrictMode>
);

reportWebVitals();
