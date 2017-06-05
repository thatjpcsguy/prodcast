scp -r * ubuntu@theprodcast.com.au:~/prodcast/
ssh ubuntu@theprodcast.com.au 'sudo service uwsgi reload; sudo service nginx reload;'
