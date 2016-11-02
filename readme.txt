Creador: Ignacio Vallejos
Correo: iavallejos93@gmail.com

Para iniciar el projecto:

	1)Ir a /secretFriend y ejecutar el comando "python manage.py runserver"


Para agregar usuarios:
	
	1)Ir a la siguiente dirección: "http://127.0.0.1:8000/users/".

Nota: Para lo que sigue se necesita una cuenta con privilegios de administrador (se puede crear una ejecutando el comando "python manage.py createsuperuser" en la carpeta /secretFriend)


Para crear Parejas:
	
	1)Ir a la siguiente dirección: "http://127.0.0.1:8000/admin/users/".
	2)Ir a Users.
	3)Seleccionar algún usuario.
	4)Ejecutar la acción "Create pairs", ésto creará parejas distintas y las agregará a una base de datos.

	5)Ir a la siguiente dirección: "http://127.0.0.1:8000/admin/users/".
	6)Ir a Pairs.
	7)Ver las parejas creadas.

Para mandar correos informando a cada usuario quien es su pareja:(es necesario setear el servidor primero, ver fin del documento).
	
	1)Ir a la siguiente dirección: "http://127.0.0.1:8000/admin/users/".
	2)Ir a Pairs.
	3)seleccionar a la pareja que se le quiera notificar.
	4)Ejecutar la acción "Notify pairs" (sólo se notificará al usuario seleccionado sobre quién es su pareja).



Como setear el servidor para enviar Correos:

	1)Abrir "settings.py" en el directorio /secretFriend/secretFriend.
	2)Ir a la línea 15 e ingresar el host, nombre de usuario y contraseña.
	3)Abrir "admin.py" en el directorio /secretFriend/users.
	4)Ir a la línea 37 y modificar SENDER_MAIL con el correo con el cuál se mandarán los correos a los usuarios.