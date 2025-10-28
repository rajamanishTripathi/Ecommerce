
ON DELETE CASCADE	If a parent row is deleted → all child rows referencing it are automatically deleted.
ON UPDATE CASCADE	If the parent’s key is updated → child rows are updated automatically.
SET NULL	Child foreign key is set to NULL if parent is deleted/updated.
SET DEFAULT	Child foreign key is set to its default value.
NO ACTION / RESTRICT	Prevents deletion/update if any child exists.

A Primary Key
It must be unique (no two rows can have the same value).
It cannot be NULL.
Each table can have only one primary key, but it can consist of multiple columns (composite key).

if venv doesnot start
then close terminal and select from view -> command platte again
 & "C:/Users/RAJA MANISH/.virtualenvs/Project-F36nJwST/Scripts/Activate.ps1"

 or run 
 pipenv shell


 after making db changes i run 
 python .\manage.py makemigrations
 python .\manage.py migrate

 Undo/revert last  migration
to 0004 from 0005
 python manage.py migrate store 0004
then delete previous migration files and remove previous code

OR

we can do it by git 
git log --oneline
then to go to previous commit 
git reset --hard HEAD~1


creating empty migrations
python manage.py makemigrations store --empty

creating & deleting migration
 migrations.RunSQL(""""
            INSERT INTO store_collection (title)
            VALUES ('collection1')
        ""","""
            DELETE FROM store_collection
            WHERE title = 'collection1'
        """)

then run 
python manage.py migrate   
to apply migration
then to downgrade run
python manage.py migrate store 0004

New setup

pipenv install
pipenv shell
& "C:/Users/RAJA MANISH/.virtualenvs/Project-F36nJwST/Scripts/Activate.ps1"
python manage.py migrate



After changes in DB tables run below commands in order
python manage.py makemigrations
python manage.py migrate


After changing complete or creating new Db
pipenv shell
python manage.py makemigrations
python manage.py migrate
then import db
then run  python manage.py runserver
then create user  python manage.py createsuperuser