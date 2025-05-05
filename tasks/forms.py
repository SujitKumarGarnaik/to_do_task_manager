from django import forms
# Importing the 'forms' module from Django, which provides tools for creating and handling forms.

from .models import Task
# Importing the 'Task' model from the current app's 'models.py' file. This model will be used to define the form.

class TaskForm(forms.ModelForm):
    # Defining a form class named 'TaskForm' that inherits from 'forms.ModelForm'.
    # 'ModelForm' is a Django class that automatically creates a form based on a model.

    class Meta:
        # The 'Meta' class is used to specify metadata for the form, such as the model it is based on and the fields to include.

        model = Task
        # Specifies that this form is based on the 'Task' model.

        fields = ['title', 'description', 'due_date', 'priority', 'status']
        # Specifies the fields from the 'Task' model that should be included in the form.

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            # Customizes the 'due_date' field to use an HTML5 date input widget.
            # The 'attrs' dictionary allows you to set HTML attributes for the widget.
        }
