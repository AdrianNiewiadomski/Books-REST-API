# Books REST API

## Wykonaj zadanie poniżej według naszych wytycznych:


Na podstawie danych znajdującej się na stronie 
> https://www.googleapis.com/books/v1/volumes?q=Hobbit 

zaprojektować i stworzyć aplikację w wybranym przez siebie frameworku, która będzie posiadała proste REST API:

1. GET /books - lista wszystkich książek (widok powinien pozwalać na filtrowanie i sortowanie po roku 
   przykłady :<br> /books?published_date=1995,<br> /books?sort=-published_date)


2. GET /books?author="Jan Kowalski"&author="Anna Kowalska" - lista książek zadanych autorów


3. GET /books/\<bookId> - wybrana książka 

> {<br>
&nbsp;&nbsp;&nbsp;&nbsp;    "title": "Hobbit czyli Tam i z powrotem",<br>
&nbsp;&nbsp;&nbsp;&nbsp;    "authors": ["J. R. R. Tolkien"],<br>
&nbsp;&nbsp;&nbsp;&nbsp;    "published_date": "2004",<br>
&nbsp;&nbsp;&nbsp;&nbsp;    "categories": [<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        "Baggins, Bilbo (Fictitious character)"<br>
&nbsp;&nbsp;&nbsp;&nbsp;      ],<br>
&nbsp;&nbsp;&nbsp;&nbsp;    "average_rating": 5,<br>
&nbsp;&nbsp;&nbsp;&nbsp;    "ratings_count": 2,<br>
&nbsp;&nbsp;&nbsp;&nbsp;    "thumbnail": "http://books.google.com/books/content?id=YyXoAAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api", <br>
}


4. POST /db z body {"q": "war"}
ściągnąć data set z https://www.googleapis.com/books/v1/volumes?q=war
wrzucić do bazy danych wpisy (aktualizując już istniejące)



## Wysyłając zgłoszenie prześlij nam:

* repozytorium z kodem twojego rozwiązania (github, gitlab, bitbucket, …)

* link do działającej aplikacji (pythonanywhere, heroku, …)


Oceniając zgłoszenia zwracamy przede wszystkim uwagę na dobre praktyki związane w web developmentem w Pythonie oraz znajomość zastosowanych bibliotek. Wizualne elementy frontendu (jeśli takowy jest elementem rozwiązania) nie są oceniane.