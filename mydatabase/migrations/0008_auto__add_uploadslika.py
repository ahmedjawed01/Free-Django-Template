# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'UploadSlika'
        db.create_table(u'mydatabase_uploadslika', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slika', self.gf('django.db.models.fields.files.ImageField')(default='media/no-img.jpg', max_length=100)),
        ))
        db.send_create_signal(u'mydatabase', ['UploadSlika'])


    def backwards(self, orm):
        # Deleting model 'UploadSlika'
        db.delete_table(u'mydatabase_uploadslika')


    models = {
        u'mydatabase.answers': {
            'Meta': {'object_name': 'Answers'},
            'answer': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mydatabase.Questions']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mydatabase.Users']"})
        },
        u'mydatabase.fiksnapolja': {
            'Meta': {'object_name': 'FiksnaPolja'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naziv': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'unos': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        u'mydatabase.pages': {
            'Meta': {'object_name': 'Pages'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_descr': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'mydatabase.questions': {
            'Meta': {'object_name': 'Questions'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'solved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mydatabase.Users']"})
        },
        u'mydatabase.seo_optimizacija': {
            'Meta': {'object_name': 'SEO_OPTIMIZACIJA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_naslov': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'meta_opis': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "'/Unesi-URL'", 'max_length': '256'})
        },
        u'mydatabase.uploadslika': {
            'Meta': {'object_name': 'UploadSlika'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slika': ('django.db.models.fields.files.ImageField', [], {'default': "'media/no-img.jpg'", 'max_length': '100'})
        },
        u'mydatabase.users': {
            'Meta': {'object_name': 'Users'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'banuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zaporka': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['mydatabase']