from django import forms
from .models import Post, Comment
from django.core.exceptions import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'image', 'category', 'tags', 'is_published']
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
            'content': forms.Textarea(attrs={'rows': 6}),
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if 'cấm' in title.lower():
            raise ValidationError("Tiêu đề chứa từ khóa không hợp lệ.")
        return title

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image and image.size > 5 * 1024 * 1024:
            raise ValidationError("Ảnh không được lớn hơn 5MB.")
        return image

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Viết bình luận...'}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content.strip()) < 5:
            raise ValidationError("Nội dung bình luận quá ngắn.")
        return content


