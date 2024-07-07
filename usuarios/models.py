from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    tipoUsuario = models.CharField(max_length=40, choices=[
        ('ADMIN', 'Administrador'),
        ('MOZO', 'Mozo'),
        ('CLIENTE', 'Cliente')
    ], default='CLIENTE')

    REQUIRED_FIELDS = ['tipoUsuario']

    class Meta:
        db_table = 'usuarios'


class CategoriaModel(models.Model):
    # en la bd creara un varchar con 50 caracteres de longitud maxima
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = 'categorias'


class PlatoModel(models.Model):
    # id = models.AutoField(primary_key= True, null=False)
    nombre = models.CharField(max_length=50, unique=True, null=False)
    precio = models.FloatField()
    disponibilidad = models.BooleanField(default=True)
    # auto_now_add > cada vez que cree un nuevo registro su valor sera la hora y fecha actual del servidor de base de datos por lo que ya no nos tenemos que preocupar en colocar la fecha
    # db_column > indicar como se tiene que llamar esta columna en la base de datos solamente si queremos cambiar el nombre del atributo
    fechaCreacion = models.DateTimeField(
        auto_now_add=True, db_column='fecha_creacion')
    # Forma de indicar que accion debe tomar cuando se elimine el 'padre'
    # https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.ForeignKey.on_delete
    # CASCADE > Cuando se elimine una categoria en forma de cascada se eliminaran todos los platos
    # PROTECT > Evita la eliminacion de la categoria si esta tiene platos que dependan de ella, emitira un error ProtectedError
    # RESTRICT > Restinge la eliminacion, es lo mismo que el PROTECT solo que emitira un error de tipo RestrictedError
    # SET_NULL > permite la eliminacion de la categoria y a los platos que dependan de ella les cambiar su valor por NULL
    # SET_DEFAULT > permite la eliminacion de la categoria y les cambiar el valor a un valor por defecto
    # DO_NOTHING > permite la eliminacion PERO no hace nada osea mantiene el mismo numero de categoria en el plato a pesar que este no exista generando un problema de integridad

    # related_name > sirve para poder acceder a todos los registros desde la otra entidad, es decir desde categoria poder acceder a todos sus platos, si es que no se define su valor sera puesto por django con el nombre de la clase TODO EN MINUSCULAS seguido de la palabra _set 'platomodel_set'
    categoria = models.ForeignKey(
        to=CategoriaModel, on_delete=models.PROTECT, db_column='categoria_id', related_name='platos')

    class Meta:
        db_table = 'platos'
