from django import forms


class add_post_form(forms.Form):
    """
    is_boast = models.BooleanField(default=True)
    content = models.CharField(max_length=150)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    submit_time = models.DateTimeField(default=now())

    - only 2 values from the model are needed
    """
    content = forms.CharField(max_length=150)
    is_boast = forms.BooleanField(required=False)
