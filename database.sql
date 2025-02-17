-- Tabelas principais (Entidades)
CREATE TABLE BackOffice (
    idBackOffice SERIAL PRIMARY KEY,
    descricaoBackOffice VARCHAR(200) NOT NULL
);

CREATE TABLE Membro (
    registroDoAluno INTEGER PRIMARY KEY,
    nomeAluno VARCHAR(100) NOT NULL,
    cursoAluno VARCHAR(100),
    emailAluno VARCHAR(100),
    telefoneAluno VARCHAR(20),
    idBackOffice INTEGER,
    FOREIGN KEY (idBackOffice) REFERENCES BackOffice (idBackOffice)
);

CREATE TABLE Planilhas (
    idPlanilha SERIAL PRIMARY KEY,
    topicoPlanilha VARCHAR(100) NOT NULL,
    descricaoPlanilha VARCHAR(200),
    conteudoPlanilha VARCHAR(200)
);

CREATE TABLE Posts (
    idPost SERIAL PRIMARY KEY,
    assuntoPost VARCHAR(100) NOT NULL,
    tituloPost VARCHAR(100),
    descricaoPost VARCHAR(200),
    anexos VARCHAR(100),
    dataPublicacao DATE
);

CREATE TABLE CelulaDeProjetos (
    idProjeto SERIAL PRIMARY KEY,
    descricaoProjeto VARCHAR(200),
    ODSProjeto VARCHAR(100),
    nomeProjeto VARCHAR(100) NOT NULL
);

CREATE TABLE MateriaPrima (
    idMateriaPrima SERIAL PRIMARY KEY,
    tipoMateriaPrima VARCHAR(100),
    quantidadeMateriaPrima INTEGER,
    precoMateriaPrima FLOAT,
    marcaMateriaPrima VARCHAR(100)
);

CREATE TABLE Produto (
    idProduto SERIAL PRIMARY KEY,
    descricaoProduto VARCHAR(200),
    nomeProduto VARCHAR(100),
    publicoAlvo VARCHAR(100),
    idProjeto INTEGER,
    FOREIGN KEY (idProjeto) REFERENCES CelulaDeProjetos (idProjeto)
);

CREATE TABLE Edital (
    idEdital SERIAL PRIMARY KEY,
    empresa VARCHAR(100),
    dataFinal DATE,
    premio FLOAT,
    requisitos VARCHAR(200)
);

CREATE TABLE LocalOficina (
    idLocal SERIAL PRIMARY KEY,
    tipoLocal VARCHAR(100),
    enderecoLocal VARCHAR(100),
    descricaoLocal VARCHAR(200),
    nomeLocal VARCHAR(100)
);

CREATE TABLE Oficina (
    idOficina SERIAL PRIMARY KEY,
    tipoOficina VARCHAR(100),
    descricaoOficina VARCHAR(200),
    idProjeto INTEGER,
    dataOficina DATE,
    idLocal INTEGER,
    FOREIGN KEY (idProjeto) REFERENCES CelulaDeProjetos (idProjeto),
    FOREIGN KEY (idLocal) REFERENCES LocalOficina (idLocal)
);

CREATE TABLE PessoaAuxiliada (
    idPessoa SERIAL PRIMARY KEY,
    racaPessoa VARCHAR(20),
    cpfPessoa VARCHAR(14) UNIQUE NOT NULL,
    nomePessoa VARCHAR(100) NOT NULL,
    enderecoPessoa VARCHAR(100),
    rendaPessoa FLOAT,
    sexoPessoa VARCHAR(50),
    tamanhoDaFamilia INTEGER,
    chavePix VARCHAR(100)
);

-- Especializações
CREATE TABLE Administracao (
    idBackOffice INTEGER PRIMARY KEY,
    tipo VARCHAR(100),
    FOREIGN KEY (idBackOffice) REFERENCES BackOffice (idBackOffice)
);

CREATE TABLE Marketing (
    idBackOffice INTEGER PRIMARY KEY,
    meioDeComunicacao VARCHAR(100),
    FOREIGN KEY (idBackOffice) REFERENCES BackOffice (idBackOffice)
);

CREATE TABLE ProjetosManufaturantes (
    idProjeto INTEGER PRIMARY KEY,
    localEstoque VARCHAR(100),
    FOREIGN KEY (idProjeto) REFERENCES CelulaDeProjetos (idProjeto)
);

CREATE TABLE ProjetosNaoManufaturantes (
    idProjeto INTEGER PRIMARY KEY,
    FOREIGN KEY (idProjeto) REFERENCES CelulaDeProjetos (idProjeto)
);

CREATE TABLE ProdutoFisico (
    idProduto SERIAL PRIMARY KEY,
    precoProduto FLOAT,
    quantidadeProduto INTEGER,
    FOREIGN KEY (idProduto) REFERENCES Produto (idProduto)
);

CREATE TABLE ProdutoDigital (
    idProduto SERIAL PRIMARY KEY,
    linguagem VARCHAR(100),
    plataforma VARCHAR(100),
    FOREIGN KEY (idProduto) REFERENCES Produto (idProduto)
);

-- Relacionamentos
CREATE TABLE MembroProjeto (
    registroDoAluno INTEGER,
    idProjeto INTEGER,
    PRIMARY KEY (registroDoAluno, idProjeto),
    FOREIGN KEY (registroDoAluno) REFERENCES Membro (registroDoAluno),
    FOREIGN KEY (idProjeto) REFERENCES CelulaDeProjetos (idProjeto)
);

CREATE TABLE ManufaturantesMateriaPrima (
    idProjeto INTEGER,
    idMateriaPrima INTEGER,
    PRIMARY KEY (idProjeto, idMateriaPrima),
    FOREIGN KEY (idProjeto) REFERENCES CelulaDeProjetos (idProjeto),
    FOREIGN KEY (idMateriaPrima) REFERENCES MateriaPrima (idMateriaPrima)
);

CREATE TABLE MateriaPrimaProdutoFisico (
    idMateriaPrima INTEGER,
    idProduto INTEGER,
    PRIMARY KEY (idMateriaPrima, idProduto),
    FOREIGN KEY (idMateriaPrima) REFERENCES MateriaPrima (idMateriaPrima),
    FOREIGN KEY (idProduto) REFERENCES ProdutoFisico (idProduto)
);

CREATE TABLE OficinaPessoaAuxiliada (
    idOficina INTEGER,
    idPessoa INTEGER,
    PRIMARY KEY (idOficina, idPessoa),
    FOREIGN KEY (idOficina) REFERENCES Oficina (idOficina),
    FOREIGN KEY (idPessoa) REFERENCES PessoaAuxiliada (idPessoa)
);

CREATE TABLE ProjetoEdital (
    idProjeto INTEGER,
    idEdital INTEGER,
    dataSubmissao DATE,
    dadosSubmissao VARCHAR(200),
    PRIMARY KEY (idProjeto, idEdital),
    FOREIGN KEY (idProjeto) REFERENCES CelulaDeProjetos (idProjeto),
    FOREIGN KEY (idEdital) REFERENCES Edital (idEdital)
);

CREATE TABLE ProjetosManufaturantesLocal (
    idProjeto INTEGER,
    idLocal INTEGER,
    PRIMARY KEY (idProjeto, idLocal),
    FOREIGN KEY (idProjeto) REFERENCES CelulaDeProjetos (idProjeto),
    FOREIGN KEY (idLocal) REFERENCES LocalOficina (idLocal)
);

CREATE TABLE BackOfficePosts (
    idBackOffice INTEGER,
    idPost INTEGER,
    PRIMARY KEY (idBackOffice, idPost),
    FOREIGN KEY (idBackOffice) REFERENCES BackOffice (idBackOffice),
    FOREIGN KEY (idPost) REFERENCES Posts (idPost)
);

CREATE TABLE CelulaDeProjetosPosts (
    idProjeto INTEGER,
    idPost INTEGER,
    PRIMARY KEY (idProjeto, idPost),
    FOREIGN KEY (idProjeto) REFERENCES CelulaDeProjetos (idProjeto),
    FOREIGN KEY (idPost) REFERENCES Posts (idPost)
);

CREATE TABLE MembroPosts (
    idMembro INTEGER,
    idPost INTEGER,
    PRIMARY KEY (idMembro, idPost),
    FOREIGN KEY (idMembro) REFERENCES Membro (registroDoAluno),
    FOREIGN KEY (idPost) REFERENCES Posts (idPost)
);

CREATE TABLE PlanilhasBackOfficeMembro (
    idPlanilha INTEGER,
    idBackOffice INTEGER,
    idMembro INTEGER,
    PRIMARY KEY (idPlanilha, idBackOffice, idMembro),
    FOREIGN KEY (idPlanilha) REFERENCES Planilhas (idPlanilha),
    FOREIGN KEY (idBackOffice) REFERENCES BackOffice (idBackOffice),
    FOREIGN KEY (idMembro) REFERENCES Membro (registroDoAluno)
);

-- Inserindo dados em Membro
INSERT INTO Membro (registroDoAluno, nomeAluno, cursoAluno, emailAluno, telefoneAluno, idBackOffice)
VALUES 
(1, 'Alice Silva', 'Engenharia Biomédica', 'alice@email.com', '11987654321', 1),
(2, 'Bruno Souza', 'Ciência da Computação', 'bruno@email.com', '11976543210', 2),
(3, 'Carlos Lima', 'Ciência e Tecnologia', 'carlos@email.com', '11965432109', 3),
(4, 'Daniela Costa', 'Engenharia da Computação', 'daniela@email.com', '11954321098', 4),
(5, 'Eduardo Moreira', 'Ciência da Computação', 'eduardo@email.com', '11943210987', 5),
(6, 'Fernanda Rocha', 'Engenharia Biomédica', 'fernanda@email.com', '11932109876', 6),
(7, 'Gabriel Santos', 'Engenharia de Materiais', 'gabriel@email.com', '11921098765', 7),
(8, 'Helena Martins', 'Ciência e Tecnologia', 'helena@email.com', '11910987654', 8),
(9, 'Igor Almeida', 'Ciência da Computação', 'igor@email.com', '11909876543', 9),
(10, 'Juliana Mendes', 'Matemática Computacional', 'juliana@email.com', '11908765432', 10);

-- Inserindo dados em Planilhas
INSERT INTO Planilhas (topicoPlanilha, descricaoPlanilha, conteudoPlanilha, idBackOffice)
VALUES 
('Financeiro', 'Controle de custos', 'Dados de despesas', 1),
('Projetos', 'Gerenciamento de projetos', 'Cronograma de atividades', 2),
('Gestão de Pessoas', 'Cadastro de membros', 'Informações pessoais', 3),
('Marketing', 'Campanhas publicitárias', 'Estratégias de redes sociais', 4),
('Eventos', 'Planejamento de eventos', 'Lista de tarefas', 5),
('Patrocínio', 'Controle de patrocinadores', 'Dados de empresas', 6),
('Produtos', 'Controle de estoque', 'Entradas e saídas', 7),
('Editais', 'Submissões de projetos', 'Histórico de envios', 8),
('Pesquisa e Inovação', 'Ideias para novos projetos', 'Descrição de ideias', 9),
('Impacto', 'Medição de impacto social', 'Estatísticas de beneficiados', 10);

-- Inserindo dados em Posts
INSERT INTO Posts (assuntoPost, tituloPost, descricaoPost, anexos, dataPublicacao)
VALUES 
('Sustentabilidade', 'Dicas ecológicas', 'Melhores práticas ambientais', 'anexo1.jpg', '2025-02-01'),
('Empreendedorismo', 'História de sucesso', 'Jornada de um empreendedor', 'anexo2.jpg', '2025-02-02'),
('Engajamento', 'Voluntariado', 'Como ajudar a comunidade', 'anexo3.png', '2025-02-03'),
('Educação', 'Cursos gratuitos', 'Lista de cursos online', 'anexo4.png', '2025-02-04'),
('Saúde', 'Dicas de bem-estar', 'Hábitos saudáveis', 'anexo5.png', '2025-02-05'),
('Tecnologia', 'Tendências do setor', 'Inovações em IA', 'anexo6.jpg', '2025-02-06'),
('Eventos', 'Enactus Summit', 'Convite para evento', 'anexo7.jpg', '2025-02-07'),
('Carreira', 'Mercado de trabalho', 'Como se destacar', 'anexo8.png', '2025-02-08'),
('Projetos', 'Novos desafios', 'Início de um novo projeto', 'anexo9.png', '2025-02-09'),
('Impacto Social', 'Resultados alcançados', 'Relatório de impacto', 'anexo10.jpg', '2025-02-10');

-- Inserindo dados em CelulaDeProjetos
INSERT INTO CelulaDeProjetos (descricaoProjeto, ODSProjeto, nomeProjeto)
VALUES 
('Neuroplasticidade em idosos', 'ODS 3', 'Ativamente'),
('Empreendedorismo feminino', 'ODS 8, 10, 12', 'Revalorize'),
('Biogás e biofertilizante', 'ODS 13', 'Organogás'),
('Reciclagem de plástico', 'ODS 13', 'PlastiRec'),
('Educação financeira', 'ODS 8', 'FinEduca'),
('Acesso à água potável', 'ODS 6', 'AquaLife'),
('Inclusão digital', 'ODS 4', 'Tech4All'),
('Saúde mental', 'ODS 3', 'MindCare'),
('Moradia acessível', 'ODS 11', 'HomeForAll'),
('Energia renovável', 'ODS 7', 'SolarPower');

-- Inserindo dados em MateriaPrima
INSERT INTO MateriaPrima (tipoMateriaPrima, quantidadeMateriaPrima, precoMateriaPrima, marcaMateriaPrima)
VALUES 
('Plástico reciclado', 100, 50.00, 'EcoPlastic'),
('Madeira sustentável', 50, 120.00, 'GreenWood'),
('Tecido ecológico', 30, 75.50, 'EcoFabric'),
('Papel reciclado', 200, 25.00, 'RePaper'),
('Vidro reutilizado', 40, 90.00, 'ReGlass'),
('Metal reciclado', 60, 200.00, 'ReMetal'),
('Bambu', 25, 130.00, 'BambooTech'),
('Óleo', 100, 25.00, 'EcoOil'),
('Tinta ecológica', 80, 95.00, 'EcoPaint'),
('Borracha reciclada', 150, 110.00, 'ReRubber');

-- Inserindo dados em Produto
INSERT INTO Produto (descricaoProduto, nomeProduto, publicoAlvo, idProjeto)
VALUES 
('Vela aromática', 'Vela aromática', 'Todos', 2),
('Sabonete', 'Sabonete', 'Todos', 2),
('Esfoliante', 'Esfoliante', 'Todos', 2),
('Jogo da memória', 'Jogo da memória', 'Idosos', 1),
('Aplicativo financeiro', 'FinApp', 'Adultos', 5),
('Biodigestor', 'Biodigestor', 'Empresas', 3),
('Filtro de água portátil', 'PureWater', 'Comunidades rurais', 6),
('Plataforma de apoio psicológico', 'MindHelp', 'Público geral', 8),
('Casas modulares', 'ModuHome', 'População vulnerável', 9),
('Painel solar portátil', 'SolarGo', 'Campistas', 10);

-- Inserindo dados em Edital
INSERT INTO Edital (empresa, dataFinal, premio, requisitos)
VALUES 
('Empresa A', '2025-03-01', 50000.00, 'Projetos sustentáveis'),
('Empresa B', '2025-04-10', 75000.00, 'Reciclagem'),
('Empresa C', '2025-05-15', 100000.00, 'Educação financeira'),
('Empresa D', '2025-06-20', 25000.00, 'Inclusão digital'),
('Empresa E', '2025-07-05', 60000.00, 'Empreendedorismo feminino'),
('Empresa F', '2025-08-30', 45000.00, 'Marcenaria sustentável'),
('Empresa G', '2025-09-15', 85000.00, 'Horta comunitária'),
('Empresa H', '2025-10-01', 30000.00, 'Capacitação de jovens'),
('Empresa I', '2025-11-12', 90000.00, 'Energia renovável'),
('Empresa J', '2025-12-25', 110000.00, 'Cosméticos naturais');

-- Inserindo dados em LocalOficina
INSERT INTO LocalOficina (tipoLocal, enderecoLocal, descricaoLocal, nomeLocal)
VALUES
('Casa de repouso', 'Rua A', 'Casa de Repouso', 'Casa de Repouso Vó Laura'),
('Associação', 'Rua B', 'Associação', 'Associação Fênix'),
('Escola', 'Rua C', 'Espaço para oficinas educacionais', 'Escola'),
('Centro Comunitário', 'Rua D', 'Local de apoio para projetos sociais', 'Centro Comunitário'),
('Biblioteca', 'Rua E', 'Sala de eventos para palestras', 'Biblioteca'),
('Espaço CoWorking', 'Rua F', 'Ambiente colaborativo para empreendedores', 'Espaço CoWorking'),
('Parque', 'Rua G', 'Área ao ar livre para eventos sustentáveis', 'Parque'),
('Universidade', 'Rua H', 'Laboratório de fabricação para projetos', 'UNIFESP'),
('Fábrica', 'Rua I', 'Espaço adaptado para oficinas de reciclagem', 'Fábrica'),
('Casa de Cultura', 'Rua J', 'Salão para eventos culturais e educativos', 'Casa de Cultura');

-- Inserindo dados em Oficina
INSERT INTO Oficina (tipoOficina, descricaoOficina, idProjeto, dataOficina, idLocal)
VALUES 
('Empreendedorismo', 'Workshop sobre criação de negócios sustentáveis', 2, '2025-03-10', 2),
('Reciclagem', 'Oficina de reaproveitamento de materiais plásticos', 3, '2025-04-15', 3),
('Educação Financeira', 'Aula sobre planejamento financeiro pessoal', 3, '2025-05-20', 3),
('Jogos', 'Oficina de jogos para desenvolver neuroplasticidade', 1, '2025-06-05', 1),
('Artesanato Sustentável', 'Criação de produtos artesanais com materiais recicláveis', 2, '2025-07-12', 2),
('Reciclagem Básica', 'Noções básicas de reciclagem', 4, '2025-08-18', 9),
('Produção de Cosméticos Naturais', 'Criação de sabonetes e cremes artesanais ecológicos', 2, '2025-09-22', 2),
('Horta Comunitária', 'Técnicas de plantio e cultivo de alimentos orgânicos', 3, '2025-10-30', 3),
('Empreendedorismo feminino', 'Workshop sobre criação de negócios sustentáveis para mulheres', 2, '2025-11-15', 2),
('Marcenaria Sustentável', 'Oficina de criação de móveis ecológicos', 4, '2025-12-05', 9);

-- Inserindo dados em PessoaAuxiliada
INSERT INTO PessoaAuxiliada (racaPessoa, cpfPessoa, nomePessoa, enderecoPessoa, rendaPessoa, sexoPessoa, tamanhoDaFamilia, chavePix)
VALUES 
('Parda', '123.456.789-01', 'Ana Souza', 'Rua A', 1200.50, 'Feminino', 4, 'ana.souza@email.com'),
('Branca', '234.567.890-12', 'Carlos Lima', 'Rua B', 1500.75, 'Masculino', 3, 'carlos.lima@pix.com'),
('Preta', '345.678.901-23', 'Mariana Silva', 'Rua C', 800.00, 'Feminino', 5, 'mariana.silva@pix.com'),
('Indígena', '456.789.012-34', 'João Pereira', 'Rua D', 950.60, 'Masculino', 2, 'joao.pereira@email.com'),
('Amarela', '567.890.123-45', 'Fernanda Takahashi', 'Rua E', 1100.90, 'Feminino', 4, 'fernanda.taka@email.com'),
('Branca', '678.901.234-56', 'Roberto Mendes', 'Rua F', 1350.30, 'Masculino', 3, 'roberto.mendes@pix.com'),
('Preta', '789.012.345-67', 'Tatiane Oliveira', 'Rua G', 700.00, 'Feminino', 6, 'tatiane.oliveira@email.com'),
('Parda', '890.123.456-78', 'Lucas Nascimento', 'Rua H', 980.20, 'Masculino', 5, 'lucas.nascimento@pix.com'),
('Indígena', '901.234.567-89', 'Gabriela Costa', 'Rua I', 1020.00, 'Feminino', 4, 'gabriela.costa@email.com'),
('Branca', '012.345.678-90', 'Eduardo Almeida', 'Rua J', 1600.40, 'Masculino', 2, 'eduardo.almeida@pix.com');

-- Inserindo dados em Administração
INSERT INTO Administracao (idBackOffice, tipo)
VALUES
(1, 'Gestão de Pessoas'),
(2, 'Financeiro'),
(3, 'Núcleo de Inovação e Pesquisa');

-- Inserindo dados em Marketing
INSERT INTO Marketing (idBackOffice, area, meioDeComunicacao)
VALUES
(4, 'Enactus UNIFESP SJC', 'Instagram'),
(5, 'Ativamente', 'Instagram'),
(6, 'Revalorize', 'Instagram'),
(7, 'Organogás', 'Instagram'),
(8, 'PlasticRec', 'Instagram'),
(9, 'FinEduca', 'Instagram'),
(10, 'AquaLife', 'Instagram'),
(11, 'Tech4All', 'Instagram'),
(12, 'MindCare', 'Instagram'),
(13, 'SolarPower', 'Instagram');

-- Inserindo dados em ProjetosManufaturantes
INSERT INTO ProjetosManufaturantes (idProjeto, localEstoque)
VALUES
(2, 'Rua A'),
(3, 'Rua B'),
(4, 'Rua C'),
(6, 'Rua E'),
(9, 'Rua H'),
(10, 'Rua I');

-- Inserindo dados em ProjetosNaoManufaturantes
INSERT INTO ProjetosNaoManufaturantes (idProjeto)
VALUES
(1),
(5),
(7),
(8);

-- Inserindo dados em ProdutoFisico
INSERT INTO ProdutoFisico (idProduto, precoProduto, quantidadeProduto)
VALUES
(1, 12.0, 15),
(2, 10.0, 25),
(3, 20.0, 7),
(6, 600.0, 2),
(7, 300.0, 6),
(9, 0.0, 1),
(10, 700.0, 8);

-- Inserindo dados em ProdutoDigital
INSERT INTO ProdutoDigital (idProduto, linguagem, plataforma)
VALUES
(4, 'Python', 'Click Jogos'),
(5, 'JavaScript', 'Play Store'),
(8, 'Python', 'Play Store');

-- Inserindo dados em MembroProjeto
INSERT INTO MembroProjeto (registroDoAluno, idProjeto)
VALUES
(1, 2),
(2, 5),
(3, 4),
(4, 1),
(5, 1),
(6, 2),
(7, 3),
(8, 2),
(9, 3),
(10, 9);

-- Inserindo dados em ManufaturantesMateriaPrima
INSERT INTO ManufaturantesMateriaPrima (idProjeto, idMateriaPrima)
VALUES
(4, 1),
(9, 2),
(2, 3),
(10, 4),
(9, 5),
(9, 6),
(2, 7),
(2, 8),
(2, 9),
(2, 10);

-- Inserindo dados em MateriaPrimaProdutoFisico
INSERT INTO MateriaPrimaProdutoFisico (idMateriaPrima, idProduto)
VALUES
(1, 3),
(2, 9),
(3, 1),
(4, 2),
(5, 9),
(6, 10),
(7, 9),
(8, 2),
(9, 1),
(10, 9);

-- Inserindo dados em OficinaPessoaAuxiliada
INSERT INTO OficinaPessoaAuxiliada (idOficina, idPessoa)
VALUES
(1, 1),
(2, 2),
(3, 3),
(9, 4),
(5, 5),
(6, 6),
(3, 7),
(1, 8),
(9, 9),
(8, 10);

-- Inserindo dados em ProjetoEdital
INSERT INTO ProjetoEdital (idProjeto, idEdital, dataSubmissao, dadosSubmissao)  
VALUES  
(3, 1, '2025-03-10', 'Projeto de sustentabilidade urbana submetido com plano detalhado.'),  
(4, 2, '2025-04-15', 'Iniciativa de reciclagem apresentada com orçamento e parceiros.'),  
(5, 3, '2025-05-20', 'Educação financeira para comunidades carentes enviado.'),  
(7, 4, '2025-06-05', 'Projeto de inclusão digital submetido com análise de impacto.'),  
(2, 5, '2025-07-12', 'Empreendedorismo feminino com plano de aceleração anexado.'),  
(9, 6, '2025-08-18', 'Oficina de marcenaria sustentável enviada com custos previstos.'),  
(3, 7, '2025-09-22', 'Horta comunitária submetida com estudo de viabilidade.'),  
(7, 8, '2025-10-30', 'Capacitação de jovens em programação enviada com cronograma.'),  
(10, 9, '2025-11-15', 'Projeto de energia renovável submetido com plano de execução.'),  
(2, 10, '2025-12-05', 'Produção de cosméticos naturais enviada com proposta financeira.');  

-- Inserindo dados em ProjetosManufaturantesLocal
INSERT INTO ProjetosManufaturantesLocal (idProjeto, idLocal)  
VALUES  
(2, 2),
(3, 9),
(4, 9),
(9, 4),
(10, 9);

-- Inserindo dados em MarketingPosts
INSERT INTO MarketingPosts (idBackOffice, idPost)
VALUES
(4, 3),
(4, 7),
(4, 9),
(4, 10),
(8, 1),
(6, 2),
(9, 4),
(5, 5),
(11, 6),
(6, 8);

-- Inserindo dados em CelulaDeProjetosPosts
INSERT INTO CelulaDeProjetosPosts (idProjeto, idPost)
VALUES
(4, 1),
(2, 2),
(7, 3),
(5, 4),
(8, 5),
(7, 6),
( , 7),
(2, 8),
( , 9),
(10, 10);

-- Inserindo dados em MembroPosts
INSERT INTO MembroPosts (idMembro, idPost)
VALUES
(4, 1),
(2, 2),
(7, 3),
(5, 4),
(8, 5),
(7, 6),
(8, 7),
(2, 8),
(9, 9),
(10, 10);