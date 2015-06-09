# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Fotos'
        db.create_table(u'glass_fotos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('ruta', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'glass', ['Fotos'])

        # Adding model 'Slide'
        db.create_table(u'glass_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['glass.Fotos'])),
            ('mensaje', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('submensaje', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('valida', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'glass', ['Slide'])

        # Adding model 'Mensajeb'
        db.create_table(u'glass_mensajeb', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mensaje', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('subensaje', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('valida', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'glass', ['Mensajeb'])

        # Adding model 'Info'
        db.create_table(u'glass_info', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('subtitulo', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('informacion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('foto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['glass.Fotos'])),
            ('valida', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'glass', ['Info'])

        # Adding model 'Contactos'
        db.create_table(u'glass_contactos', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('telefono1', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('telefono2', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('telefono3', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('correo1', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('correo2', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('correo3', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('fax1', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('fax2', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'glass', ['Contactos'])

        # Adding model 'Servicios'
        db.create_table(u'glass_servicios', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('foto', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['glass.Fotos'])),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('informacion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('valida', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'glass', ['Servicios'])


    def backwards(self, orm):
        # Deleting model 'Fotos'
        db.delete_table(u'glass_fotos')

        # Deleting model 'Slide'
        db.delete_table(u'glass_slide')

        # Deleting model 'Mensajeb'
        db.delete_table(u'glass_mensajeb')

        # Deleting model 'Info'
        db.delete_table(u'glass_info')

        # Deleting model 'Contactos'
        db.delete_table(u'glass_contactos')

        # Deleting model 'Servicios'
        db.delete_table(u'glass_servicios')


    models = {
        u'glass.contactos': {
            'Meta': {'object_name': 'Contactos'},
            'correo1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'correo2': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'correo3': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'fax1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'fax2': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'telefono1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'telefono2': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'telefono3': ('django.db.models.fields.CharField', [], {'max_length': '500'})
        },
        u'glass.fotos': {
            'Meta': {'object_name': 'Fotos'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'ruta': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'glass.info': {
            'Meta': {'object_name': 'Info'},
            'foto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glass.Fotos']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informacion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'subtitulo': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'valida': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'glass.mensajeb': {
            'Meta': {'object_name': 'Mensajeb'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensaje': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'subensaje': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'valida': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'glass.servicios': {
            'Meta': {'object_name': 'Servicios'},
            'foto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glass.Fotos']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informacion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'valida': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'glass.slide': {
            'Meta': {'object_name': 'Slide'},
            'foto': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['glass.Fotos']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mensaje': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'submensaje': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'valida': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['glass']