import React from 'react';
import ReactDOM from 'react-dom/client'; // Importação correta
import AppRouter from './AppRouter';
import './index.css';


const root = ReactDOM.createRoot(document.getElementById('root') as HTMLElement);
root.render(
  <React.StrictMode>
    <AppRouter />
  </React.StrictMode>
);
