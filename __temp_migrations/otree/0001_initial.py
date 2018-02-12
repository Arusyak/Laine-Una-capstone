# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-02-04 20:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.common_internal
import otree.db.models
import otree.db.serializedfields
import otree.models.varsmixin
import otree_save_the_change.mixins
import time


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrowserBotsLauncherSessionCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('is_only_record', models.BooleanField(default=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(max_length=255)),
                ('nickname', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('timestamp', models.FloatField(default=time.time)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedGroupWaitPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_index', models.PositiveIntegerField()),
                ('id_in_subsession', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='CompletedSubsessionWaitPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_index', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FailedSessionCreation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pre_create_id', models.CharField(db_index=True, max_length=100)),
                ('message', models.CharField(max_length=300)),
                ('traceback', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='PageCompletion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_name', models.CharField(max_length=300)),
                ('page_index', models.PositiveIntegerField()),
                ('page_name', models.CharField(max_length=300)),
                ('time_stamp', models.PositiveIntegerField()),
                ('seconds_on_page', models.PositiveIntegerField()),
                ('subsession_pk', models.PositiveIntegerField()),
                ('auto_submitted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='PageTimeout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_index', models.PositiveIntegerField()),
                ('expiration_time', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vars', otree.db.serializedfields._PickleField(default=dict)),
                ('label', otree.db.models.StringField(max_length=50, null=True)),
                ('id_in_session', otree.db.models.PositiveIntegerField(null=True)),
                ('payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('time_started', otree.db.models.DateTimeField(null=True)),
                ('mturk_assignment_id', otree.db.models.StringField(max_length=50, null=True)),
                ('mturk_worker_id', otree.db.models.StringField(max_length=50, null=True)),
                ('_index_in_subsessions', otree.db.models.PositiveIntegerField(default=0, null=True)),
                ('_index_in_pages', otree.db.models.PositiveIntegerField(db_index=True, default=0, null=True)),
                ('_waiting_for_ids', otree.db.models.StringField(max_length=300, null=True)),
                ('code', otree.db.models.StringField(default=otree.common_internal.random_chars_8, max_length=16, null=True, unique=True)),
                ('visited', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], db_index=True, default=False)),
                ('ip_address', otree.db.models.GenericIPAddressField(null=True)),
                ('_last_page_timestamp', otree.db.models.PositiveIntegerField(null=True)),
                ('_last_request_timestamp', otree.db.models.PositiveIntegerField(null=True)),
                ('is_on_wait_page', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_current_page_name', otree.db.models.StringField(max_length=200, null=True, verbose_name='page')),
                ('_current_app_name', otree.db.models.StringField(max_length=200, null=True, verbose_name='app')),
                ('_round_number', otree.db.models.PositiveIntegerField(null=True)),
                ('_current_form_page_url', otree.db.models.URLField(null=True)),
                ('_max_page_index', otree.db.models.PositiveIntegerField(null=True)),
                ('_browser_bot_finished', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_is_bot', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('is_browser_bot', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
            ],
            options={
                'ordering': ['pk'],
            },
            bases=(otree.models.varsmixin._SaveTheChangeWithCustomFieldSupport, otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='ParticipantLockModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_code', models.CharField(max_length=16, unique=True)),
                ('locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantRoomVisit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=50)),
                ('participant_label', models.CharField(max_length=200)),
                ('tab_unique_id', models.CharField(max_length=20, unique=True)),
                ('last_updated', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantToPlayerLookup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant_code', models.CharField(max_length=20)),
                ('page_index', models.PositiveIntegerField()),
                ('app_name', models.CharField(max_length=300)),
                ('player_pk', models.PositiveIntegerField()),
                ('subsession_pk', models.PositiveIntegerField()),
                ('session_pk', models.PositiveIntegerField()),
                ('url', models.CharField(max_length=300)),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Participant')),
            ],
        ),
        migrations.CreateModel(
            name='RoomToSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vars', otree.db.serializedfields._PickleField(default=dict)),
                ('config', otree.db.serializedfields._PickleField(default=dict, null=True)),
                ('label', otree.db.models.StringField(blank=True, help_text='For internal record-keeping', max_length=300, null=True)),
                ('experimenter_name', otree.db.models.StringField(blank=True, help_text='For internal record-keeping', max_length=300, null=True)),
                ('ready_for_browser', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('code', otree.db.models.StringField(default=otree.common_internal.random_chars_8, max_length=16, null=True, unique=True)),
                ('mturk_HITId', otree.db.models.StringField(blank=True, help_text='Hit id for this session on MTurk', max_length=300, null=True)),
                ('mturk_HITGroupId', otree.db.models.StringField(blank=True, help_text='Hit id for this session on MTurk', max_length=300, null=True)),
                ('mturk_num_participants', otree.db.models.IntegerField(default=-1, help_text='Number of participants on MTurk', null=True)),
                ('mturk_use_sandbox', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, help_text='Should this session be created in mturk sandbox?')),
                ('archived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], db_index=True, default=False)),
                ('comment', otree.db.models.LongStringField(blank=True, null=True)),
                ('_anonymous_code', otree.db.models.StringField(db_index=True, default=otree.common_internal.random_chars_10, max_length=10, null=True)),
                ('_pre_create_id', otree.db.models.StringField(db_index=True, max_length=255, null=True)),
                ('is_demo', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_admin_report_app_names', otree.db.models.LongStringField(default='', null=True)),
                ('_admin_report_num_rounds', otree.db.models.StringField(default='', max_length=255, null=True)),
                ('num_participants', otree.db.models.PositiveIntegerField(null=True)),
            ],
            options={
                'ordering': ['pk'],
            },
            bases=(otree.models.varsmixin._SaveTheChangeWithCustomFieldSupport, otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='UndefinedFormModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='roomtosession',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session'),
        ),
        migrations.AddField(
            model_name='participant',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session'),
        ),
        migrations.AddField(
            model_name='pagetimeout',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Participant'),
        ),
        migrations.AddField(
            model_name='pagecompletion',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Participant'),
        ),
        migrations.AddField(
            model_name='pagecompletion',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session'),
        ),
        migrations.AddField(
            model_name='completedsubsessionwaitpage',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session'),
        ),
        migrations.AddField(
            model_name='completedgroupwaitpage',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otree.Session'),
        ),
        migrations.AddField(
            model_name='chatmessage',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages_core', to='otree.Participant'),
        ),
        migrations.AlterUniqueTogether(
            name='participanttoplayerlookup',
            unique_together=set([('participant', 'page_index')]),
        ),
        migrations.AlterIndexTogether(
            name='participanttoplayerlookup',
            index_together=set([('participant', 'page_index')]),
        ),
        migrations.AlterIndexTogether(
            name='participant',
            index_together=set([('session', 'mturk_worker_id', 'mturk_assignment_id')]),
        ),
        migrations.AlterIndexTogether(
            name='pagetimeout',
            index_together=set([('participant', 'page_index')]),
        ),
        migrations.AlterIndexTogether(
            name='completedsubsessionwaitpage',
            index_together=set([('page_index', 'session')]),
        ),
        migrations.AlterIndexTogether(
            name='completedgroupwaitpage',
            index_together=set([('page_index', 'session', 'id_in_subsession')]),
        ),
        migrations.AlterIndexTogether(
            name='chatmessage',
            index_together=set([('channel', 'timestamp')]),
        ),
    ]
