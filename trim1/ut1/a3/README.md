<center>

# UT1-A3: Trabajo con virtual hosts


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

La actividad cosiste en configurar o crear 4 virtual host en nuestros servidor de nginx y configurar cada uno de forma distinta

#### ***Objetivos***. <a name="id2"></a>

Los objetivos de la practica son variados, en el **1ºSitio web** hay que crear un host virutal donde la pagina tendra una imagen y luego haya otra carpeta que nos enviara a otra pagina donde contendra unos enlaces y dicha ruta no puede utilizar `location`.
En el **2ºSitio web** tenemos que crear un host virtual por un puerto especificado que en este caso sera el `9000` quedaria algo asi: `varlib.marco.me:9000` dentro se encontrar un listado de ficheros y directorios de `/var/lib`.
Despues en el **3ºSitio web** tenemos que crear un host virutal donde nos pida usuario y contraseña para entrar usaremos el fichero `.htpasswd`.
Y finalmente en el **4ºSitio web** tenemos que crear un host virtual llamado `redirect.marco.me` y este nos va redirigir cualquier petición de dominio a `target.marco.me` eso quiere decir que si ponemos `redirect.marco.me/hola/` nos deberia redirigir a `target.marco.me`.Despues nos tenemos que descargar un zip y ponerlo de fichero en nuestra configuracion.Y por ultimo cambiar a donde van dirigidos los log de acceso y de error estos iran dirigido a `/var/log/nginx/redirect`.

#### ***Material empleado***. <a name="id3"></a>

Usamos una máquina virtual de Ubuntu 18.04 en adaptador puente con ip estática con esta ip 172.19.99.112 y una máquina Kali para configurar los DNS (se puede realizar con cualquier otra máquina, pero en mi caso, use esa porque era la que tenía), también en adaptador puente.

Los hosts están configurados de esta forma:
```
172.19.99.112          imw.marco.me
172.19.99.112          varlib.marco.me
172.19.99.112          ssl.marco.me
172.19.99.112          redirect.marco.me
172.19.99.112          target.marco.me
```

#### ***Desarrollo***. <a name="id4"></a>

Teniendo en cuenta que ya estamos conectados por `ssh` a la maquina virtual y tenemos instalado nginx realizaremos los siguiente:
- [Host1](#h1)
- [Host2](#h2)
- [Host3](#h3)
- [Host4](#h4)

### *Host1* <a name="#h1"></a>

Creamos el host virutal:
```
sudo nano /etc/nginx/sites-available/imw.marco.me
```



#### ***Conclusiones***. <a name="id5"></a>

En esta parte debemos exponer las conclusiones que sacamos del desarrollo de la prácica.

