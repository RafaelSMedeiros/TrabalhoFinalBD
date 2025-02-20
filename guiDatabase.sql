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

CREATE TABLE CelulaDeProjetos (
    idProjeto SERIAL PRIMARY KEY,
    descricaoProjeto VARCHAR(200),
    ODSProjeto VARCHAR(100),
    nomeProjeto VARCHAR(100) NOT NULL
);

-- Relacionamentos
CREATE TABLE MembroProjeto (
    registroDoAluno INTEGER,
    idProjeto INTEGER,
    PRIMARY KEY (registroDoAluno, idProjeto),
    FOREIGN KEY (registroDoAluno) REFERENCES Membro (registroDoAluno),
    FOREIGN KEY (idProjeto) REFERENCES CelulaDeProjetos (idProjeto)
);

INSERT INTO BackOffice (descricaobackoffice) VALUES
('Descrição 1'),
('Descrição 2'),
('Descrição 3'),
('Descrição 4'),
('Descrição 5'),
('Descrição 6'),
('Descrição 7'),
('Descrição 8'),
('Descrição 9'),
('Descrição 10'),
('Descrição 11'),
('Descrição 12'),
('Descrição 13');

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

ALTER TABLE membroprojeto
DROP CONSTRAINT membroprojeto_idprojeto_fkey,
ADD CONSTRAINT membroprojeto_idprojeto_fkey FOREIGN KEY (idprojeto) REFERENCES celuladeprojetos(idprojeto) ON DELETE CASCADE;
