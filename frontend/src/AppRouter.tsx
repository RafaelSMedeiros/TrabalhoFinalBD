import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import App from './app/App';
import Project from './app/project';

function AppRouter() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<App />} />
        <Route path="/project/:projetoId" element={<Project />} />
      </Routes>
    </Router>
  );
}

export default AppRouter;
