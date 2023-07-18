### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
A data base managing system where you can create and manage dbs structually 
- What is the difference between SQL and PostgreSQL?
SQL communicates with dbs while postgres manages dbs
- In `psql`, how do you connect to a database?
-d DATABASENAME
- What is the difference between `HAVING` and `WHERE`?
WHERE filters rows before grouped and operates on rows. HAVING filters group after and used after grouped by 
- What is the difference between an `INNER` and `OUTER` join?
Inner join joins matching rows, like related data. OUTER joins join matching and rows and all others
- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
left returns all left or first tables. while right returns the second table 
- What is an ORM? What do they do?
- ORMS provide relationships for objects in database so you can connect one table to another
- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
- with requests you have to make sure you serialize the data and translate it to json 
- What is CSRF? What is the purpose of the CSRF token?
- cross site request forgery
to stop or mitigate csfr attacks so people arent getting tricked into performing unwanted acts once a form is filled out
- What is the purpose of `form.hidden_tag()`?
includes csrf but hides it from client side