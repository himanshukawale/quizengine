# from quizengine.quizengine.main.models import User
import openpyxl
from pathlib import Path
import django

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quizengine.settings')
django.setup()

from main.models import User, Question


def populate_db():
    xlsx_file = Path('quizengine\quizengine\media\excel\Data.xlsx')
    wb_obj = openpyxl.load_workbook(xlsx_file) 

    sheet = wb_obj['Users']

    rows = sheet.rows

    user_data = {}

    x = next(rows)
    while x :
        user_data[x[0].value] = x[1].value
        try:
            x = next(rows)
        except:
            break

    for key, val in user_data.items():
        if key == "Name":
            continue
        
        user = User()
        user.Name = key
        user.Email = val
        user.save()



    sheet = wb_obj['Bank']
    rows = sheet.rows
    x = next(rows)

    while x :
        if x[0].value == "Question ID":
            x = next(rows)
        
        if x[0].value != None:
            que = Question()
            que.Question_ID = x[0].value
            que.Image_file = x[1].value
            que.Question_type = x[2].value
            que.Questio_text = x[3].value
            que.Option_A = x[4].value
            que.Option_B = x[5].value
            que.Option_C = x[6].value
            que.Option_D = x[7].value
            que.Answer = x[8].value
            que.save()
        try:
            x = next(rows)
        except:
            break
    
def read_db():
    pass





