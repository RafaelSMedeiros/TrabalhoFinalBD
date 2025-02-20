import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import enactus_logo from '../assets/enactus_logo.png';
import { getProjetos, createProjeto } from '../services/api';
import { styles } from '../styles/app_styles';

interface Projeto {
  id: number;
  nome: string;
  descricao: string;
}

function App() {
  const [projetos, setProjetos] = useState<Projeto[]>([]);
  const [hoveredId, setHoveredId] = useState<number | null>(null);
  const [showForm, setShowForm] = useState(false); // Controle de visibilidade do formulário
  const [newProjeto, setNewProjeto] = useState({ nomeprojeto: '', descricaoprojeto: '', odsprojeto: '' });
  const navigate = useNavigate();

  const fetchProjetos = async () => {
    try {
      const response = await getProjetos();
      setProjetos(response.map((projeto: any) => ({
        id: projeto.idprojeto,
        nome: projeto.nomeprojeto,
        descricao: projeto.descricaoprojeto,
      })));
    } catch (error) {
      console.error('Erro ao buscar Projetos', error);
    }
  };

  useEffect(() => {
    fetchProjetos();
  }, []);

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setNewProjeto((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const projetoData = {
        nomeprojeto: newProjeto.nomeprojeto,
        descricaoprojeto: newProjeto.descricaoprojeto,
        odsprojeto: newProjeto.odsprojeto,
      };
      const createdProjeto = await createProjeto(projetoData);
      fetchProjetos();
      setNewProjeto({ nomeprojeto: '', descricaoprojeto: '', odsprojeto: '' });
      setShowForm(false);
    } catch (error) {
      console.error('Erro ao criar Projeto', error);
    }
  };

  return (
    <div className="App">
      <header style={styles.header}>
        <img src={enactus_logo} alt="Enactus Logo" style={styles.logo} />
      </header>
      <div style={styles.content}>
        <h1 style={styles.title}>PROJETOS</h1>
        <div style={styles.projectsBox}>
          {projetos.map((projeto) => (
            <button
              key={projeto.id}
              style={{
                ...styles.projectCard,
                ...(hoveredId === projeto.id ? styles.projectCardHover : {}),
              }}
              onMouseEnter={() => setHoveredId(projeto.id)}
              onMouseLeave={() => setHoveredId(null)}
              onClick={() => navigate(`/project/${projeto.id}`)}
            >
              <div style={styles.projectCardContent}>
                <h2 style={styles.projectName}>{projeto.nome}</h2>
                <p style={styles.projectDescription}>{projeto.descricao}</p>
              </div>
            </button>
          ))}

          <div
            style={{
              ...styles.projectCard,
              ...(showForm ? styles.projectCardHover : {}),
            }}
            onClick={() => setShowForm(!showForm)} // Alterna a visibilidade do formulário
          >
            <div style={styles.projectCardContent}>
              <span style={styles.plusIcon}>+</span>
            </div>
          </div>
        </div>

        {showForm && (
          <form style={styles.form} onSubmit={handleSubmit}>
            <input
              type="text"
              name="nomeprojeto"
              value={newProjeto.nomeprojeto}
              onChange={handleInputChange}
              placeholder="Nome do Projeto"
              style={styles.input}
              required
            />
            <input
              type="text"
              name="descricaoprojeto"
              value={newProjeto.descricaoprojeto}
              onChange={handleInputChange}
              placeholder="Descrição do Projeto"
              style={styles.input}
              required
            />
            <input
              type="text"
              name="odsprojeto"
              value={newProjeto.odsprojeto}
              onChange={handleInputChange}
              placeholder="ODS do Projeto"
              style={styles.input}
            />
            <button type="submit" style={styles.button}>Criar Projeto</button>
          </form>
        )}
      </div>
    </div>
  );
}

export default App;
