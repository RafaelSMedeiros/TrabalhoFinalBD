import { useParams, useNavigate } from 'react-router-dom';
import React, { useEffect, useState } from 'react';
import { getProjeto, updateProjeto, deleteProjeto, getMembrosProjeto, getMembroById } from '../services/api';
import enactus_logo from '../assets/enactus_logo.png';
import { styles } from '../styles/project_styles';

interface ProjetoDetalhe {
  idprojeto: number;
  nomeprojeto: string;
  descricaoprojeto: string;
  odsprojeto: string;
}

interface Membro {
  id: number;
  nome: string;
  curso: string;
}

function Project() {
  const { projetoId } = useParams<{ projetoId: string }>();
  const navigate = useNavigate();
  const [projeto, setProjeto] = useState<ProjetoDetalhe | null>(null);
  const [editando, setEditando] = useState(false);
  const [novoNome, setNovoNome] = useState('');
  const [novaDescricao, setNovaDescricao] = useState('');
  const [novaOds, setNovaOds] = useState('');
  const [membros, setMembros] = useState<Membro[]>([]);

  useEffect(() => {
    const fetchProjeto = async () => {
      try {
        const response = await getProjeto(Number(projetoId));
        setProjeto(response);
        setNovoNome(response.nomeprojeto);
        setNovaDescricao(response.descricaoprojeto);
        setNovaOds(response.odsprojeto);
      } catch (error) {
        console.error('Erro ao buscar projeto', error);
      }
    };

    const fetchMembros = async () => {
      try {
        const membrosResponse = await getMembrosProjeto(Number(projetoId));
        const membrosCompletos = await Promise.all(
          membrosResponse.map(async (response: any) => {
            const membro = await getMembroById(response.registrodoaluno);
            return {
              id: membro.registrodoaluno,
              nome: membro.nomealuno,
              curso: membro.cursoaluno,
            };
          })
        );
        setMembros(membrosCompletos);
      } catch (error) {
        console.error('Erro ao buscar membros do projeto', error);
      }
    };

    if (projetoId) {
      fetchProjeto();
      fetchMembros();
    }
  }, [projetoId]);

  const handleSave = async () => {
    if (!projeto) return;

    try {
      await updateProjeto(Number(projetoId), {
        nomeprojeto: novoNome,
        descricaoprojeto: novaDescricao,
        odsprojeto: novaOds,
      });
      setProjeto({
        ...projeto,
        nomeprojeto: novoNome,
        descricaoprojeto: novaDescricao,
        odsprojeto: novaOds,
      });
      setEditando(false);
      alert('Projeto atualizado com sucesso!');
    } catch (error) {
      console.error('Erro ao atualizar projeto', error);
      alert('Erro ao atualizar o projeto.');
    }
  };

  const handleDelete = async () => {
    if (!projeto) return;

    const confirmacao = window.confirm('Tem certeza que deseja excluir este projeto?');

    if (confirmacao) {
      try {
        await deleteProjeto(Number(projetoId));
        alert('Projeto excluído com sucesso!');
        navigate('/');
      } catch (error) {
        console.error('Erro ao excluir projeto', error);
        alert('Erro ao excluir o projeto.');
      }
    }
  };

  if (!projeto) {
    return <div>Carregando...</div>;
  }

  return (
    <div>
      <div style={styles.header}>
        <img src={enactus_logo} alt="Enactus Logo" style={styles.logo} />
      </div>
      <div style={styles.container}>
        <div style={styles.content}>
          {editando ? (
            <>
              <input
                type="text"
                value={novoNome}
                onChange={(e) => setNovoNome(e.target.value)}
                style={styles.input}
              />
              <textarea
                rows={5}
                value={novaDescricao}
                onChange={(e) => setNovaDescricao(e.target.value)}
                style={styles.textarea}
              />
              <input
                type="text"
                value={novaOds}
                onChange={(e) => setNovaOds(e.target.value)}
                style={styles.input}
              />
            </>
          ) : (
            <>
              <h1>{projeto.nomeprojeto}</h1>
              <p>{projeto.descricaoprojeto}</p>
              <p><strong>{projeto.odsprojeto}</strong></p>
            </>
          )}

          <div style={styles.buttonContainer}>
            {editando ? (
              <button style={{ ...styles.button, ...styles.saveButton }} onClick={handleSave}>
                Salvar
              </button>
            ) : (
              <button
                style={{ ...styles.button, ...styles.editButton }}
                onClick={() => setEditando(true)}
              >
                Editar
              </button>
            )}
            <button style={{ ...styles.button, ...styles.deleteButton }} onClick={handleDelete}>
              Excluir
            </button>
            <button style={{ ...styles.button, ...styles.backButton }} onClick={() => navigate('/')}>
              Voltar
            </button>
          </div>

          <div style={styles.membrosList}>
            <h2>Membros do Projeto</h2>
            <ul>
              {membros.map((membro) => (
                <li key={membro.id} style={styles.membroItem}>
                  <div style={styles.membroInfo}>
                    <span style={styles.membroNome}>{membro.nome}</span>
                    <span style={styles.membroCurso}>{membro.curso}</span>
                  </div>
                </li>
              ))}
            </ul>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Project;
