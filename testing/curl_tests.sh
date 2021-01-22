echo 'Testing GET method for /api/posts/ endpoint...'
curl --header "Content-Type: application/json" \
  --request GET \
 http://127.0.0.1:5000/api/posts/

echo ''
echo ''
echo 'Testing POST method for /api/posts/ endpoint...'
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"title":"Weeee!","content":"testing testing 123","author":"Mel"}' \
http://127.0.0.1:5000/api/posts/

echo ''
echo ''
echo 'Done!'
