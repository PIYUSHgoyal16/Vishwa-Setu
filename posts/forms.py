"""Posts forms"""

# Django
from django import forms

# Models
from posts.models import Post


class PostForm(forms.ModelForm):
	"""Post model form"""

	class Meta:
		"""Form settings."""
		model = Post
		fields = ('profile', 'title', 'photo')

class PostForm2(forms.Form):
	literature = forms.CharField(widget=forms.Textarea(attrs={'class':'transliterate_input_sn'}))
	
class PostForm3(forms.Form):
	photo = forms.ImageField()
	caption = forms.CharField(widget=forms.Textarea(attrs={'class':'transliterate_input_sn'}))
	choice = forms.ChoiceField(choices=[("Object Detection", "Object Detection"),("Extract text","Extract text"), ("Original", "Original Photo")])