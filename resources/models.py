from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.utils.translation import gettext_lazy as _
import uuid

from inventory.models import *
from resources.enums.tipo_disco import *
# Create your models here.

class Hardware(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(
        related_name="%(class)s_created_by", null=True, blank=True, editable=False
    )
    updated_by = CurrentUserField(
        on_update=True,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
        editable=False,
    )
    # Validacion en caso de que ya exista el registro
    # unique=True
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

   
    processor = models.CharField(
        max_length=5000,
        blank=False,
        null=False,
        verbose_name="Procesador",
    )

    memory= models.CharField(
        max_length=5000,
        blank=False,
        null=False,
        verbose_name="Memoria Ram",
    )


    tamanio = models.CharField(
        max_length=5000,
        blank=False,
        null=False,
        verbose_name="Tamaño de Disco",
        
       
    )


    tipo_disco = models.CharField(
        max_length=10,
        choices=TipoDisco.OPCIONES,  # Usa las opciones de la clase
        blank=False,
        null=False,
        verbose_name="Tipo de Disco",
    )

    product= models.ForeignKey(
        Product, 
        verbose_name='Producto',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="fk_hardware_product")

    def __str__(self):
        return f"{self.tamanio}"

    class Meta:
        verbose_name_plural = "Recurso"
        db_table = "tb_hardware"
        verbose_name = "Recursos"
    

    
   
class Software(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(
        related_name="%(class)s_created_by", null=True, blank=True, editable=False
    )
    updated_by = CurrentUserField(
        on_update=True,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
        editable=False,
    )
    # Validacion en caso de que ya exista el registro
    # unique=True
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

   
    version = models.CharField(
        max_length=5000,
        blank=False,
        null=False,
        verbose_name="Version",
    )

    edition = models.CharField(
        max_length=5000,
        blank=False,
        null=False,
        verbose_name="Edicion",
    )

    installation_date = models.DateField(
        verbose_name="Fecha de Instalación",
        blank=False,  # Permite que el campo esté vacío
        null=False,   # Permite valores nulos en la base de datos
    )

    licenses = models.BooleanField(
        verbose_name="Tiene Licencia",
        default=False,  # Valor predeterminado: False (no tiene licencia)
    )


    product= models.ForeignKey(
        Product, 
        verbose_name='Producto',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="fk_software_product")

    
    def __str__(self):
        return f"{self.version} ({self.edition})"

    class Meta:
        verbose_name_plural = "Software"
        db_table = "tb_software"
        verbose_name = "Software"



class DisplayName(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(
        related_name="%(class)s_created_by", null=True, blank=True, editable=False
    )
    updated_by = CurrentUserField(
        on_update=True,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
        editable=False,
    )
    # Validacion en caso de que ya exista el registro
    # unique=True
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

   
    name = models.CharField(
        max_length=5000,
        blank=False,
        null=False,
        verbose_name="Nombre del equipo",
    )


    product= models.ForeignKey(
        Product, 
        verbose_name='Producto',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="fk_displayname_product")

    
    def __str__(self):
        return f"{self.name})"

    class Meta:
        verbose_name_plural = "Nombre del Equipo"
        db_table = "tb_displayname"
        verbose_name = "Nombre del Equipo"


class DateOperation(models.Model):

    
      
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(
        related_name="%(class)s_created_by", null=True, blank=True, editable=False
    )
    updated_by = CurrentUserField(
        on_update=True,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
        editable=False,
    )
    # Validacion en caso de que ya exista el registro
    # unique=True
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    product= models.ForeignKey(
        Product, 
        verbose_name='Producto',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="fk_dateoperation_product")

   
    date = models.DateField(
        verbose_name="Fecha del primer uso",
        blank=False,  # Permite que el campo esté vacío
        null=False,   # Permite valores nulos en la base de datos
    )



    running_time = models.CharField(
        max_length=10,
        choices=TiempoFuncionamiento.OPCIONES,  # Usa las opciones de la clase
        blank=True,
        null=True,
        verbose_name=_("Tiempo de funcionamiento"),
    )

   
    
    def __str__(self):
        return f"{self.date}"

    class Meta:
        verbose_name_plural = "Fecha de Operación"
        db_table = "tb_dateoperation"
        verbose_name = "Fecha de Operación"





class IpAssignation(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(
        related_name="%(class)s_created_by", null=True, blank=True, editable=False
    )
    updated_by = CurrentUserField(
        on_update=True,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
        editable=False,
    )
    # Validacion en caso de que ya exista el registro
    # unique=True
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    product= models.ForeignKey(
        Product, 
        verbose_name='Producto',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="fk_ipassignation_product")

    ip = models.GenericIPAddressField(
        verbose_name="Dirección IP",
        blank=False,  # Permite que el campo esté vacío
        null=False,   # Permite valores nulos en la base de datos
    )

    def __str__(self):
        return f"{self.ip}"

    class Meta:
        verbose_name_plural = "Asignación de IP"
        db_table = "tb_ipassignation"
        verbose_name = "Asignación de IP"