# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Answers'
        db.create_table(u'mydatabase_answers', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256, null=True)),
            ('answer', self.gf('django.db.models.fields.TextField')(default='', null=True)),
            ('users', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mydatabase.Users'])),
            ('questions', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mydatabase.Questions'])),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'mydatabase', ['Answers'])

        # Deleting field 'Questions.user'
        db.delete_column(u'mydatabase_questions', 'user_id')

        # Adding field 'Questions.title'
        db.add_column(u'mydatabase_questions', 'title',
                      self.gf('django.db.models.fields.CharField')(max_length=256, null=True),
                      keep_default=False)

        # Adding field 'Questions.users'
        db.add_column(u'mydatabase_questions', 'users',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['mydatabase.Users']),
                      keep_default=False)

        # Adding field 'Questions.slug'
        db.add_column(u'mydatabase_questions', 'slug',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=256, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Pages.user'
        db.delete_column(u'mydatabase_pages', 'user_id')


    def backwards(self, orm):
        # Deleting model 'Answers'
        db.delete_table(u'mydatabase_answers')

        # Adding field 'Questions.user'
        db.add_column(u'mydatabase_questions', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['mydatabase.Users']),
                      keep_default=False)

        # Deleting field 'Questions.title'
        db.delete_column(u'mydatabase_questions', 'title')

        # Deleting field 'Questions.users'
        db.delete_column(u'mydatabase_questions', 'users_id')

        # Deleting field 'Questions.slug'
        db.delete_column(u'mydatabase_questions', 'slug')

        # Adding field 'Pages.user'
        db.add_column(u'mydatabase_pages', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['mydatabase.Users']),
                      keep_default=False)


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
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True'}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mydatabase.Users']"})
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