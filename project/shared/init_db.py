from project.shared.database import Base, engine
from project.news.new import New  # asegúrate de importar todos los modelos

Base.metadata.create_all(bind=engine)