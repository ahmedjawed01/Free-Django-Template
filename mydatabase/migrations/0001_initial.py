# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Users'
        db.create_table(u'mydatabase_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zaporka', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'mydatabase', ['Users'])

        # Adding model 'Questions'
        db.create_table(u'mydatabase_questions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')(default='', null=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mydatabase.Users'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'mydatabase', ['Questions'])

        # Adding model 'Pages'
        db.create_table(u'mydatabase_pages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('content', self.gf('django.db.models.fields.TextField')(default='', null=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='', max_length=256, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mydatabase.Users'])),
        ))
        db.send_create_signal(u'mydatabase', ['Pages'])


    def backwards(self, orm):
        # Deleting model 'Users'
        db.delete_table(u'mydatabase_users')

        # Deleting model 'Questions'
        db.delete_table(u'mydatabase_questions')

        # Deleting model 'Pages'
        db.delete_table(u'mydatabase_pages')


    models = {
        u'mydatabase.pages': {
            'Meta': {'object_name': 'Pages'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mydatabase.Users']"})
        },
        u'mydatabase.questions': {
            'Meta': {'object_name': 'Questions'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mydatabase.Users']"})
        },
        u'mydatabase.users': {
            'Meta': {'object_name': 'Users'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zaporka': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['mydatabase']