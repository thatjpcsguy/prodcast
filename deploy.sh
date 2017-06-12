mkdir prodcast

cp -R config prodcast/.
rm -rf *.pyc
cp -R *.py prodcast/.
cp -R static prodcast/.
rm -rf prodcast/static/mp3

zip -r -X prodcast.zip prodcast

rm -rf prodcast

scp prodcast.zip ubuntu@theprodcast.com.au:/var/www/app/prodcast.zip
rm prodcast.zip

ssh ubuntu@theprodcast.com.au 'cd /var/www/app; rm -rf prodcast; unzip prodcast.zip; rm prodcast.zip; sudo service uwsgi reload; sudo service nginx reload;'

