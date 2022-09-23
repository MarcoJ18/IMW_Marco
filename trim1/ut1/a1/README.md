<center>

# TÍTULO DE LA PRÁCTICA


</center>

***Nombre:*** Marco José Gopar Mühlbacher
***Curso:*** 2º de Ciclo Superior de Administración de Sistemas Informáticos en Red.

### ÍNDICE

+ [Introducción](#id1)
+ [Objetivos](#id2)
+ [Material empleado](#id3)
+ [Desarrollo](#id4)
+ [Conclusiones](#id5)


#### ***Introducción***. <a name="id1"></a>

Lo que realizaremos en esta práctica será descargar **nginx** y configurar lo para que al abrirse una página del navegador y acceder 'http://marco.me/serires/'. Dentro de dicha página se encontrará la portada de nuestras series favoritas que al clic-ar sobre esa imagen nos redirigirá a la página de [IMDB](https://www.imdb.com/).

#### ***Objetivos***. <a name="id2"></a>

Los objetivos de esta práctica era realizar una configuración básica de nginx donde tendremos alojado nuestro sitio web donde se encontrara unas imágenes de nuestras películas favoritas.

#### ***Material empleado***. <a name="id3"></a>

Usamos una máquina virtual de Ubuntu 18.04 y una máquina Kali para configurar los DNS (se puede realizar con cualquier otra máquina, pero en mi caso, use esa porque era la que tenía)
#### ***Desarrollo***. <a name="id4"></a>

Primero nos conectamos por SSH a la máquina remota:
```
ssh your_name@your_ip
```

Después debemos instalar Ngnix
```
sudo apt update
```
```
sudo apt install -y nginx
```
Una vez instalado vemos si el servicio funciona correctamente
```
sudo systemctl status nginx
```
Ahora debemos crear nuestro sitio, para eso necesitamos crear dentro de `/etc/nginx/sites-available`:
```
sudo nano /etc/nginx/sites-available/your_name.me 
```
La configuración será esta:
```
server {

        server_name marco.me;       #Esta directiva es para darle nombre al server que vamos a crear
        location /series {          #Esta directiva sirve para localizar la carpeta /series dentro de la ruta raíz que le damos 

                root /var/www/html; #Esta directiva nos indica la ruta raíz que va a usar

        }

}
```
Una vez configurada vamos a realizar un enlace simbólico para que esté disponible nuestro sitio web, esto se encuentra en `/etc/nginx/sites-enabled`:
```
cd /etc/nginx/sites-enabled
```
```
ln -s ../sites-available/your_name.me
```
**Podemos borrar el fichero `default` para que no nos dé problema:**
```
sudo rm default
```

Ahora toca crear los archivos 'index.html' y otros archivos, si es necesario en mi caso yo cree un 'style.css' y una carpeta con imágenes todo eso dentro de `/var/www/html/series`:
```
cd /var/www/html/series
```
```
sudo nano index.html
```
Estos son los ficheros que yo tengo:

[mis-ficheros](https://github.com/MarcoJ18/IMW_Marco/tree/main/trim1/ut1/a1/document)

Comprobamos si el fichero está bien y reiniciamos el servicio:
```
sudo nginx -t
```
```
sudo systemctl reload nginx 
```

Resultado:

![web-page](img/html.png)

#### ***Conclusiones***. <a name="id5"></a>

Las conclusiones finales sacadas con esta práctica han sido la posibilidad de crear un host virtual de forma completamente personalizada y también se ha aprendido a usar, manejar por los directorios más importantes del servicio web de nginx.