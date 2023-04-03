from database import Database
from crud import BookModel
from save_json import writeAJson

db = Database(database="Relatorio5", collection="Livros")
data = db.collection.find()
bookModel = BookModel(db)

#Realizando a insercao de livros
newBook = bookModel.create_book("Aristoteles e Dante Descobrem os segredos do universo", "Benjamin Alire", 2012, 16.70)
newBook1 = bookModel.create_book("Tartarugas ate la embaixo", " John Green", 2017, 28.90)
newBook2 = bookModel.create_book("Pessoas normais", "Sally Roones", 2020, 30.50)
newBook3 = bookModel.create_book("Cartas perto do coracao", " Clarice Lispector", 2001, 50.00)

#Realizando a leitura dos livros
read_book = bookModel.read_book_by_id(newBook)
read_book1 = bookModel.read_book_by_id(newBook1)
read_book2 = bookModel.read_book_by_id(newBook2)
read_book3 = bookModel.read_book_by_id(newBook3)
writeAJson((read_book,read_book1,read_book2, read_book3), "LivrosInseridos")

#Realizando a atualizacao de dados de um determinado livro
updatebook = bookModel.update_book(newBook, "A logica inexplicavel da minha vida", 23.45)
updatebook1 = bookModel.update_book(newBook2, "Quem e voce Alaska", 19.99)

#Realizando a exclusao de um livro do Bando de Dados
delete_book = bookModel.delete_book(newBook3)
