<center>

# TÍTULO DE LA PRÁCTICA


</center>

***Nombre:*** Marco José Gopar Mühlbacher
<br>
***Curso:*** 2º de Ciclo Superior de Administración de Sistemas Informáticos en Red.

### ÍNDICE

+ [Introducción](#id1)
+ [Objetivos](#id2)
+ [Material empleado](#id3)
+ [Desarrollo](#id4)
+ [Conclusiones](#id5)


#### ***Introducción***. <a name="id1"></a>

Lo que realizaremos en esta practica será descargar **nginx** y configurar lo para que al abrirse una pagina del navegador y acceder `http://marco.me/serires/`.Dentro de dicha pagina se encontrara la portada de nuestras series favoritas que al clic-ar sobre esa imagen nos redirigirá a la pagina de [IMDB](https://www.imdb.com/).

#### ***Objetivos***. <a name="id2"></a>

Los objetivos de esta practica era realizar una configuración basica de nginx donde tendremos alojado nuestro sitio web donde se encontrara unas imagenes de nuestras peliculas favoritas.

#### ***Material empleado***. <a name="id3"></a>

Usamos una maquina virtual de ubuntu 18.04 y una maquina Kali para configurar los dns (se puede realizar con cualquier otra maquina pero en mi caso use esa por que era la que tenia)

#### ***Desarrollo***. <a name="id4"></a>

Primero nos conectamos por ssh a la maquina remota:
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
Ahora debemos crear nuestro sitio para eso necesitamos crear dentro de `/etc/nginx/sites-available`:
```
sudo nano /etc/nginx/sites-available/your_name.me 
```
La configuración sera esta:
```
server {

        server_name marco.me;       #Esta directiva es para darle nombre al server que vamos a crear
        location /series {          #Esta directiva sirve para localizar la carpeta /series dentro de la ruta raiz que le damos 

                root /var/www/html; #Esta directiva nos indica la ruta raiz que va usar

        }

}
```
Una vez configurada vamos a realizar un enlace simbolico para que este disponible nuestro sitio web esto se encuentra en `/etc/nginx/sites-enabled`:
```
cd /etc/nginx/sites-enabled
```
```
ln -s ../sites-available/your_name.me
```
**Podemos borrar el fichero `default` para que no nos de problema:**
```
sudo rm default
```

Ahora toca crear los archivos `index.html` y otros archivos si es necesario en mi caso yo cree un `style.css` y una carpeta con images todo eso dentro de `/var/www/html/series`:
```
cd /var/www/html/series
```
```
sudo nano index.html
```
Estos son los ficheros que yo tengo:

[mis-ficheros](https://github.com/MarcoJ18/IMW_Marco/tree/main/trim1/ut1/a1/document)

Comprobamos si el fichero esta bien y reinciamos el servicio:
```
sudo nginx -t
```
```
sudo systemctl reload nginx 
```

Resultado:

![web-page](img/html.png)

#### ***Conclusiones***. <a name="id5"></a>

En esta parte debemos exponer las conclusiones que sacamos del desarrollo de la prácica.
