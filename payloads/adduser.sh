passwdmd5=`echo -n TestTest |md5sum|cut -d" " -f1`
sqlite3 /data/turin/web/datas/memohi.db "delete from users where id='69'"
sqlite3 /data/turin/web/datas/memohi.db "INSERT INTO users ('id', 'username', 'password', 'roletype', 'firstlogin') VALUES (69, 'supertest', '$passwdmd5', 'admin', false);"

