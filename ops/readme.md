python manage.py startapp polls

######create sql files

python manage.py migrate


######create table auth ..
python manage.py makemigrations
> 相当于在该app下建立 migrations目录，并记录下你所有的关于modes.py的改动，比如0001_initial.py， 但是这个改动还没有作用到数据库文件



######将该改动作用到数据库文件，比如产生table，修改字段的类型等
python manager.py migrate

##### create admin user
python manage.py createsuperuser


######如果migrate失败了，可以用sqlmigrate调试
python manage.py sqlmigrate  cmdb 0001