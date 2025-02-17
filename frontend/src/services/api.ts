// services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // URL do seu backend FastAPI
});

export const getUsuarios = async () => {
  try {
    const response = await api.get('/usuarios/');
    return response.data;
  } catch (error) {
    console.error('Erro ao buscar usuários', error);
    throw error;
  }
};

export const createUsuario = async (nome: string, email: string) => {
  try {
    const response = await api.post('/usuarios/', { nome, email });
    return response.data;
  } catch (error) {
    console.error('Erro ao criar usuário', error);
    throw error;
  }
};
