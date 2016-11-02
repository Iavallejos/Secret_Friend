from django.contrib import admin
from django.core.mail import send_mail

from .models import User, Pair
import random


def create_pairs(modeladmin, request, queryset):
    users_list = []
    for user in User.objects.all():
        users_list.append(user.email)

    pair_list = list(users_list)
    # run this until it generates a valid result
    valid = False
    while not valid:
        # randomize the pairList
        random.shuffle(pair_list)
        # validate them
        round_valid = True
        for aUser, aPair in zip(users_list, pair_list):
            round_valid = round_valid and aUser != aPair  # and aUser.aPair != aPair
        valid = round_valid
    paired = zip(users_list, pair_list)
    for pair in paired:
        Pair.objects.create(
            userEmail=pair[0],
            pairEmail=pair[1], )


def notify_pairs(modeladmin, request, queryset):
    for remitent in queryset:
        to_mail = remitent.userEmail
        to_name = User.objects.filter(email=remitent.pairEmail)[0].name
        print to_mail + " - " + to_name
        send_mail('Amigo Secreto', 'Hola,\n Tu amigo secreto es ' + to_name + ".\n \n Saludos.",
                  'SENDER_MAIL', [to_mail], fail_silently=False)


class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    actions = [create_pairs]


class PairAdmin(admin.ModelAdmin):
    list_display = ['userEmail', 'pairEmail']
    actions = [notify_pairs]


admin.site.register(User, UserAdmin)
admin.site.register(Pair, PairAdmin)
