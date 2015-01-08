# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SEO_OPTIMIZACIJA'
        db.create_table(u'mydatabase_seo_optimizacija', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('meta_naslov', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('meta_opis', self.gf('django.db.models.fields.TextField')(default='', null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='/Unesi-URL', max_length=256)),
        ))
        db.send_create_signal('mydatabase', ['SEO_OPTIMIZACIJA'])

        # Adding model 'Users'
        db.create_table(u'mydatabase_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('zaporka', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('email', self.gf('django.db.models.fields.CharField')(unique=True, max_length=255)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('banuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('mydatabase', ['Users'])

        # Adding model 'Questions'
        db.create_table(u'mydatabase_questions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('question', self.gf('django.db.models.fields.TextField')(default='', null=True)),
            ('users', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mydatabase.Users'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('solved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='', max_length=256, null=True, blank=True)),
        ))
        db.send_create_signal('mydatabase', ['Questions'])

        # Adding model 'Answers'
        db.create_table(u'mydatabase_answers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('answer', self.gf('django.db.models.fields.TextField')(default='', null=True)),
            ('users', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mydatabase.Users'])),
            ('questions', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mydatabase.Questions'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('mydatabase', ['Answers'])

        # Adding model 'Pages'
        db.create_table(u'mydatabase_pages', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('short_descr', self.gf('django.db.models.fields.CharField')(max_length=256, null=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(default='', null=True)),
            ('slug', self.gf('django.db.models.fields.CharField')(default='', max_length=256, null=True, blank=True)),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('mydatabase', ['Pages'])

        # Adding model 'FiksnaPolja'
        db.create_table(u'mydatabase_fiksnapolja', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naziv', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('unos', self.gf('django.db.models.fields.TextField')(default=None, null=True, blank=True)),
        ))
        db.send_create_signal('mydatabase', ['FiksnaPolja'])

        # Adding model 'UploadSlika'
        db.create_table(u'mydatabase_uploadslika', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('slika', self.gf('django.db.models.fields.files.ImageField')(default='media/no-img.jpg', max_length=100)),
        ))
        db.send_create_signal('mydatabase', ['UploadSlika'])

        # Adding model 'Test'
        db.create_table(u'mydatabase_test', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('naziv', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('mydatabase', ['Test'])


    def backwards(self, orm):
        # Deleting model 'SEO_OPTIMIZACIJA'
        db.delete_table(u'mydatabase_seo_optimizacija')

        # Deleting model 'Users'
        db.delete_table(u'mydatabase_users')

        # Deleting model 'Questions'
        db.delete_table(u'mydatabase_questions')

        # Deleting model 'Answers'
        db.delete_table(u'mydatabase_answers')

        # Deleting model 'Pages'
        db.delete_table(u'mydatabase_pages')

        # Deleting model 'FiksnaPolja'
        db.delete_table(u'mydatabase_fiksnapolja')

        # Deleting model 'UploadSlika'
        db.delete_table(u'mydatabase_uploadslika')

        # Deleting model 'Test'
        db.delete_table(u'mydatabase_test')


    models = {
        'mydatabase.answers': {
            'Meta': {'unique_together': '()', 'object_name': 'Answers', 'index_together': '()'},
            'answer': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mydatabase.Questions']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mydatabase.Users']"})
        },
        'mydatabase.fiksnapolja': {
            'Meta': {'unique_together': '()', 'object_name': 'FiksnaPolja', 'index_together': '()'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naziv': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'unos': ('django.db.models.fields.TextField', [], {'default': 'None', 'null': 'True', 'blank': 'True'})
        },
        'mydatabase.pages': {
            'Meta': {'unique_together': '()', 'object_name': 'Pages', 'index_together': '()'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'short_descr': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        'mydatabase.questions': {
            'Meta': {'unique_together': '()', 'object_name': 'Questions', 'index_together': '()'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'solved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mydatabase.Users']"})
        },
        'mydatabase.seo_optimizacija': {
            'Meta': {'unique_together': '()', 'object_name': 'SEO_OPTIMIZACIJA', 'index_together': '()'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'meta_naslov': ('django.db.models.fields.CharField', [], {'max_length': '256'}),
            'meta_opis': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "'/Unesi-URL'", 'max_length': '256'})
        },
        'mydatabase.test': {
            'Meta': {'unique_together': '()', 'object_name': 'Test', 'index_together': '()'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'naziv': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'mydatabase.uploadslika': {
            'Meta': {'unique_together': '()', 'object_name': 'UploadSlika', 'index_together': '()'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slika': ('django.db.models.fields.files.ImageField', [], {'default': "'media/no-img.jpg'", 'max_length': '100'})
        },
        'mydatabase.users': {
            'Meta': {'object_name': 'Users'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'banuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'email': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'zaporka': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['mydatabase']