// create admin superuser
$ python manage.py createsuperuser
-------------------------------------------------------------------------------------------------------------------
// start the server, go to localhost:8000/admin
// the polls, Question, Choice, they're not there.
// change admin.py to this:

//---------------------polls/admin.py-------------------//

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

//--------------------polls/admin.py--------------------//

from django.contrib import admin
from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)

//-------------------------------------------------//

// You’ll follow this pattern – create a model admin object,
// then pass it as the second argument to admin.site.register() – any time you
// need to change the admin options for an object.

-------------------------------------------------------------------------------------------------------


And speaking of forms with dozens of fields, you might want to split the form up into fieldsets:

//------------------------polls/admin.py----------------------//
from django.contrib import admin
from polls.models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)

//----------------------------------------------------------------//
