from django import forms

from studentsHW.models import Teachers, Group


class TeachersCreateForm(forms.ModelForm):
    class Meta:
        model = Teachers
        fields = (
            'first_name',
            'last_name',
            'age',
        )


class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = (
            'first_name',
            'last_name',
            'scores_in_group',
        )
#class GroupCreateForm(forms.ModelForm):
 #   class Meta:
  #      model = Group
   #     fields = (
    #        'first_name',
     #       'last_name',
      #      'scores_in_group',
       # )
