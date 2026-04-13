passwdmd5=`echo -n TestTest |md5sum|cut -d" " -f1`
sqlite3 /data/turin/web/datas/memohi.db "UPDATE users SET password = '$passwdmd5' WHERE username = 'superadmin'";
