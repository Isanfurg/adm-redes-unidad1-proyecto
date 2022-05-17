# adm-redes-unidad1-proyecto
Proyecto 1 Administración de Redes
Docker y Virtualización
Ricardo Pérez
Introducción
La pandemia que estamos atravesando ha golpeado fuertemente todos los sectores de la economía
a nivel internacional. Particularmente en Chile, las Pymes afectadas representan el 81%, de las
cuales el 45% no han podido seguir operando, producto de las cuarentenas y las restricciones
de movilidad. Ante esta situación, las pequeñas y medianas empresas han tenido que buscar
alternativas de comercio electrónico para poder mantener sus negocios.
Este proyecto tiene como objetivo principal: desplegar una plataforma de comercio electrónico,
que favorezca las ventas de las Pymes en un entorno real. El mismo se basa en la instalación y
configuración de un Marketplace gratuito (Prestashop), dentro de contenedores Docker.
Para su evaluación deberán desplegar desarrollar el proyecto de manera individual y hacer
una presentación del trabajo realizado. Además, cada estudiante deberá estar preparado para
modificar cualquier parámetro de configuración, o responder las preguntas del profesor, para
completar la nota.
A continuación, se detallan los principales elementos que se deben desarrollar:
• Instale Docker en algunas de las alternativas de virtualización vistas en clases (VBox o
Proxmox). Escoja la que otorgue mejores rendimientos a su computador.
• Utilizando docker-compose.yml instale Prestashop (última versión disponible) en el
servidor con Docker. El despliegue tiene que cumplir los requisitos siguientes:
1. Debe tener un contenedor que permita ejecutar el servicio web. Algunas opciones
pueden ser Apache o Nginx.
2. Deberá tener un contenedor independiente, que utilice la imagen del sistema gestor
de base de datos de su preferencia. Algunas alternativas son MySQL, MariaDB o
Postgress. Conecte el contenedor Web con el contenedor del Sistema Gestor de Bases
de Datos.
3. Ambos contenedores deben estar en una red creada solamente para ellos, con el
objetivo de mejorar la seguridad.
• Configure un volumen compartido en el directorio /data/prestashop del servidor local,
que contenga el directorio de instalación de prestashop (en caso que utilice una imagen
pre-construida de Prestashop esa ruta puede ser diferente de /var/www/html).
• Configure un volumen compartido en el directorio /data/prestashop_DB del servidor local,
que contenga una copia de la base de datos que se ejecuta en el contenedor del SGBD.
• Modifique el código de Prestashop (en caso que sea necesario) para cambiar la plantilla
por defecto de la aplicación. El objetivo es que la tienda de la Pyme sea diferente al resto
de sus competidores. Intente que sea lo más atractiva posible.
