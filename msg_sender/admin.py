from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.contrib import admin
from django import forms
from django.template.defaultfilters import truncatechars
from .models import Service, Notification_group, Channel, Notification, NTF_type_for_channel
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ServiceForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Service
        fields = '__all__'


class ServiceAdmin(admin.ModelAdmin):
    form = ServiceForm
    list_display = ('id','service_names', 'image', 'description')


class NotificationForm(forms.ModelForm):
    message = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Notification
        fields = '__all__'


class NotificationAdmin(admin.ModelAdmin):
    form = NotificationForm
    list_display = ('id','title', 'status', 'ntf_group',
                    'url', 'message', 'created_at')


class Notification_groupForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Notification_group
        fields = '__all__'


class Notification_groupAdmin(admin.ModelAdmin):
    form = Notification_groupForm
    list_display = ('id','service_name', 'group_name', 'description')


class NTF_type_for_channelForm(forms.ModelForm):
    templates_for_massage = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = NTF_type_for_channel
        fields = '__all__'


# class NTF_type_for_channelAdmin(admin.ModelAdmin):
#     form = NTF_type_for_channelForm
#     list_display = ('ntf_group', 'channel', 'templates_for_massage')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Notification_group, Notification_groupAdmin)
admin.site.register(Channel)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(NTF_type_for_channel, )

