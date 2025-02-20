// services/api.ts
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // URL do backend FastAPI
});

// Membros
export const getMembros = async () => {
  try {
    const response = await api.get('/membro/');
    return response.data;
  } catch (error) {
    console.error('Erro ao buscar Membros', error);
    throw error;
  }
};

export const getMembroById = async (registrodoaluno: number) => {
  try {
    const response = await api.get(`/membro/${registrodoaluno}`);
    return response.data;
  } catch (error) {
    console.error('Erro ao buscar membro', error);
    throw error;
  }
};

export const createMembro = async (membro: any) => {
  try {
    const response = await api.post('/membro/', membro);
    return response.data;
  } catch (error) {
    console.error('Erro ao criar Membro', error);
    throw error;
  }
};

export const updateMembro = async (registrodoaluno: number, membro: any) => {
  try {
    const response = await api.put(`/membro/${registrodoaluno}`, membro);
    return response.data;
  } catch (error) {
    console.error('Erro ao atualizar Membro', error);
    throw error;
  }
};

export const deleteMembro = async (registrodoaluno: number) => {
  try {
    const response = await api.delete(`/membro/${registrodoaluno}`);
    return response.data;
  } catch (error) {
    console.error('Erro ao deletar Membro', error);
    throw error;
  }
};

// MembroProjeto
export const getMembrosProjeto = async (idprojeto: number) => {
  try {
    const response = await api.get(`/membroprojeto/${idprojeto}`);
    return response.data;
  } catch (error) {
    console.error('Erro ao buscar Membros do Projeto', error);
    throw error;
  }
};

export const createMembroProjeto = async (membroProjeto: any) => {
  try {
    const response = await api.post('/membroprojeto/', membroProjeto);
    return response.data;
  } catch (error) {
    console.error('Erro ao adicionar Membro ao Projeto', error);
    throw error;
  }
};

export const deleteMembroProjeto = async (registrodoaluno: number, idprojeto: number) => {
  try {
    const response = await api.delete(`/membroprojeto/${registrodoaluno}/${idprojeto}`);
    return response.data;
  } catch (error) {
    console.error('Erro ao remover Membro do Projeto', error);
    throw error;
  }
};

// Projetos
export const getProjetos = async () => {
  try {
    const response = await api.get('/projetos/');
    return response.data;
  } catch (error) {
    console.error('Erro ao buscar Projetos', error);
    throw error;
  }
};

export const getProjeto = async (idprojeto: number) => {
  try {
    const response = await api.get(`/projetos/${idprojeto}`);
    return response.data;
  } catch (error) {
    console.error('Erro ao buscar Projeto', error);
    throw error;
  }
};

export const createProjeto = async (projeto: any) => {
  try {
    const response = await api.post('/projetos/', projeto);
    return response.data;
  } catch (error) {
    console.error('Erro ao criar Projeto', error);
    throw error;
  }
};

export const updateProjeto = async (idprojeto: number, projeto: any) => {
  try {
    const response = await api.put(`/projetos/${idprojeto}`, projeto);
    return response.data;
  } catch (error) {
    console.error('Erro ao atualizar Projeto', error);
    throw error;
  }
};

export const deleteProjeto = async (idprojeto: number) => {
  try {
    const response = await api.delete(`/projetos/${idprojeto}`);
    return response.data;
  } catch (error) {
    console.error('Erro ao deletar Projeto', error);
    throw error;
  }
};
