
from django.db import models
from django_currentuser.db.models import CurrentUserField
from django.utils.translation import gettext_lazy as _ 
import uuid

# Create your models here.

class Floor(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    
    created_by = CurrentUserField(related_name='%(class)s_created_by', null=True, blank=True, editable=False)
    updated_by = CurrentUserField(on_update=True, related_name='%(class)s_updated_by', null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    status = models.BooleanField(default=True)
    description = models.CharField(max_length=5000, blank=False, null=False, verbose_name='Descripción', unique=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name_plural = 'Pisos'
        db_table = 'tb_security_floor'
        verbose_name = 'Piso'


class Department(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(related_name='%(class)s_created_by', null=True, blank=True, editable=False)
    updated_by = CurrentUserField(on_update=True, related_name='%(class)s_updated_by', null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    id_floor = models.ForeignKey(Floor, verbose_name='Piso', on_delete=models.SET_NULL, blank=True, null=True, related_name="fk_departament_floor")
    parent = models.ForeignKey('self', verbose_name='Departamento Padre', on_delete=models.SET_NULL, blank=True, null=True, related_name="children")
    status = models.BooleanField(default=True)
    description = models.CharField(max_length=5000, blank=False, null=False, verbose_name='Descripción', unique=True)

    def __str__(self):
        if self.parent:
            return f"{self.parent.description} -> {self.description}"
        return self.description

    class Meta:
        verbose_name_plural = _('Departamentos')
        db_table = 'tb_security_department'
        verbose_name = _('Departamento')


class Position(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(related_name='%(class)s_created_by', null=True, blank=True, editable=False)
    updated_by = CurrentUserField(on_update=True, related_name='%(class)s_updated_by', null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    status = models.BooleanField(default=True)
    description = models.CharField(max_length=5000, blank=False, null=False, verbose_name=_('Descripción'), unique=True)
    department = models.ForeignKey(Department, verbose_name=('Departamento'), on_delete=models.SET_NULL, blank=True, null=True, related_name="positions")

    def __str__(self):
        return self.description  # Representación legible del puesto

    class Meta:
        verbose_name_plural = _('Cargos')
        db_table = 'tb_security_position'
        verbose_name = _('Cargo')




class Custodiam(models.Model):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    created_by = CurrentUserField(related_name='%(class)s_created_by', null=True, blank=True, editable=False)
    updated_by = CurrentUserField(on_update=True, related_name='%(class)s_updated_by', null=True, blank=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    status = models.BooleanField(default=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=60)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=60)
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name=_('Phone Number'))
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name=_('Address'))
    reference = models.CharField(max_length=100, blank=True, null=True, verbose_name=_('Reference'))
    email = models.EmailField(verbose_name=_("Email Address"), unique=True, db_index=True)
    position = models.ForeignKey(Position, verbose_name=('Cargo'), on_delete=models.SET_NULL, blank=True, null=True, related_name="custodiams")


    def __str__(self):
        position_str = str(self.position) if self.position else "No Position"
        return f"{position_str} -> {self.first_name} {self.last_name}"
    def save(self, *args, **kwargs):
        self.first_name = self.first_name.upper()
        self.last_name = self.last_name.upper()
        self.phone_number = self.phone_number.upper() if self.phone_number else None
        self.address = self.address.upper() if self.address else None
        self.reference = self.reference.upper() if self.reference else None
        self.email = self.email.lower()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = _('Custodios')
        db_table = 'tb_security_custodiam'
        verbose_name = _('Custodio')