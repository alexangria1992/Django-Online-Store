from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.forms import ModelForm, TextInput, Textarea
# Create your models here.
class Setting(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    company = models.CharField(max_length=50)
    address = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=50, blank = True)
    smtpserver = models.CharField(max_length=50, blank=True)
    smtpemail = models.CharField(max_length=50, blank = True)
    smtppassword = models.CharField(max_length=10, blank = True)
    smtpport = models.CharField(max_length=5, blank = True)
    icon = models.ImageField(blank = True, upload_to='images/')
    facebook = models.CharField(max_length=50, blank = True)
    instagram = models.CharField(max_length=50, blank = True)
    twitter = models.CharField(max_length=50, blank = True)
    youtube = models.CharField(max_length=50, blank = True)
    aboutus = RichTextUploadingField(blank = True)
    contactus = RichTextUploadingField(blank = True)
    references = RichTextUploadingField(blank = True)
    status = models.CharField(max_length=10, choices = STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
     return self.title

class ContactMessage(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Read', 'Read'),
        ('Closed', 'Closed'),
    )
    name = models.CharField(blank = True, max_length=20)
    email = models.CharField(max_length=50, blank = True)
    subject = models.CharField(max_length=50, blank = True)
    message = models.CharField(max_length=255, blank = True)
    status = models.CharField(max_length=10, choices = STATUS, default='New')
    ip = models.CharField(max_length=20, blank = True)
    note = models.CharField(max_length=100, blank = True)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ContactForm(ModelForm):
    class Meta: 
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name' : TextInput(attrs={'class': 'input', 'placeholder':'Name & Sirname'}),
            'subject' : TextInput(attrs={'class': 'input', 'placeholder': 'Subject'}),
            'email' : TextInput(attrs={'class': 'input', 'placeholder': 'Email Address'}),
            'message' : Textarea(attrs={'class': 'input', 'placeholder': 'Your Message', 'rows':'5'}),


        }
