docker pull tiangolo/nginx-rtmp

docker run -d -p 1935:1935 --name nginx-rtmp tiangolo/nginx-rtmp

docker cp nginx.conf nginx-rtmp:/etc/nginx/nginx.conf
