
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