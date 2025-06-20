# Generated by Django 5.0.2 on 2024-02-17 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0005_alter_chat_model_doc_cno_alter_chat_model_doc_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='history_Model',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('u_id', models.IntegerField(null=True)),
                ('message', models.CharField(max_length=50)),
                ('reply_msg', models.CharField(default='NA', max_length=50)),
                ('status', models.CharField(default='not seen', editable=False, max_length=50)),
            ],
            options={
                'db_table': 'chathistory',
            },
        ),
    ]
