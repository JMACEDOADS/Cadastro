# instalar o bd no termianal: pip install sqlalchemy

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

# conexão com o banco de dados
engine = create_engine('sqlite:///usuarios.db', echo=True)

Base = declarative_base()

# Definir o modelo da classe de usuário.db
class User(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    sobrenome = Column(String)
    email = Column(String, unique=True)
    senha = Column(String)

Base.metadata.create_all(engine)

# Criar uma sessão para interagir com o banco de dados
Session = sessionmaker(bind=engine)
session = Session()

# Função para adicionar um novo usuário ao banco de dados
def adicionar_usuario(nome, sobrenome, email, senha):
    novo_usuario = User(nome=nome, sobrenome=sobrenome, email=email, senha=senha)
    session.add(novo_usuario)
    try:
        session.commit()
        print("Usuário adicionado com sucesso!")
    except IntegrityError:
        session.rollback()
        print("Erro: Este e-mail já está em uso.")

# Add usuario
adicionar_usuario('Caio', 'Jose', 'caiojose@viagens.com', '11062024')