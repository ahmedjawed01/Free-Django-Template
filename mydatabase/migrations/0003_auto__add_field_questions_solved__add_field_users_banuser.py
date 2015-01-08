# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Questions.solved'
        db.add_column(u'mydatabase_questions', 'solved',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'Users.banuser'
        db.add_column(u'mydatabase_users', 'banuser',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Questions.solved'
        db.delete_column(u'mydatabase_questions', 'solved')

        # Deleting field 'Users.banuser'
        db.delete_column(u'mydatabase_users', 'banuser')


    models = {
        u'mydatabase.answers': {
            'Meta': {'object_name': 'Answers'},
            'answer': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mydatabase.Questions']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mydatabase.Users']"})
        },
        u'mydatabase.pages': {
            'Meta': {'object_name': 'Pages'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'content': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'})
        },
        u'mydatabase.questions': {
            'Meta': {'object_name': 'Questions'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {'default': "''", 'null': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'solved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mydatabase.Users']"})
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