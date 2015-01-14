// create admin superuser
$ python manage.py createsuperuser
-------------------------------------------------------------------------------------------------------------------
// start the server, go to localhost:8000/admin
// the polls, Question, Choice, they're not there.
// change admin.py to this:

//---------------------admin.py-------------------//

from django.contrib import admin
from polls.models imort Question, Choice

admin.site.register(Question)

//-----------------------------------------------//

// now you will see polls, Question.


----------------------------------------------
----------------------------------------------
----------------------------------------------

// change the order of the fields in the admin
// Replace this line: 
admin.site.register(Question)
//with:

//--------------------admin.py--------------------//

from django.contrib import admin
from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)

//-------------------------------------------------//

