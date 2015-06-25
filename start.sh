uwsgi --master --socket /tmp/uwsgi_wechat.sock --process 2 --uid 1000 --chdir /var/www/wechat --module wechat.wsgi:application
