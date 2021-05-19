# 使用celery
from __future__ import absolute_import
from celery import Celery
import time
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test1.settings")
django.setup()


# 创建一个Celery类的实例对象
app = Celery('celery_task.tasks', broker='redis://127.0.0.1:6379/8')


# 定义任务函数
@app.task
def send_register_active_email():
    '''发送激活邮件'''
    # 组织邮件信息
    time.sleep(5)
    print("222222222")
    return



@app.task
def generate_static_index_html():
    time.sleep(10)
    print("eeeeeeeeeeeeeeeeeee")



