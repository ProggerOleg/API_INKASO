from rest_framework import serializers
from .models import *


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('id', 'login')


class ExampleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Credits
        fields = "__all__"

    def to_representation(self, instance):
        if isinstance(instance, Credits) and not instance.actual_return_date == '1000-01-01':
            return super().to_representation(instance)

        result = dict(is_closed=instance.actual_return_date, another_custom_field=instance.is_private)

        return result

class UserCreditsSerializer_true(serializers.ModelSerializer):
    is_closed = serializers.SerializerMethodField('is_credit_closed')  # поле в api
    # sum_platezh = serializers.SerializerMethodField('sum_plat_body')

    class Meta:
        model = Credits
        ordering = ('return_date',)
        fields = ('issuance_date', 'is_closed', 'actual_return_date', 'body', 'percent',) #'sum_platezh')

    def payment_date(self, *args):
        for i in args:
            res = i.actual_return_date - i.return_date
            res = res/24/60/60
        return res

    def is_credit_closed(self, *args):
        for i in args:
            if str(i.actual_return_date) == '1000-01-01':
                is_it_closed = False
            else:
                is_it_closed = True
        return is_it_closed

    # def sum_plat_body(self, *args):
    #     for i in args:
    #         print(Payments.objects.filter(credit_id=Credits.objects.get(id=i.id)).only('sum'))
    #     all_body_p = sum([i.id for i in args])
    #     return all_body_p


class UserCreditsSerializer_false(serializers.ModelSerializer):
    is_closed = serializers.SerializerMethodField('is_credit_closed')  # поле в api
    payment_late = serializers.SerializerMethodField('payment_date')
    # sum_plat_b = serializers.SerializerMethodField('sum_plat_body')
    # sum_plat_per = serializers.SerializerMethodField('sum_plat_body')

    class Meta:
        model = Credits
        ordering = ('return_date',)
        fields = ('issuance_date', 'is_closed', 'return_date', 'payment_late', 'body', 'percent',)
                  #'sum_plat_b', 'sum_plat_per')

    def payment_date(self, *args):
        for i in args:
            res = i.actual_return_date - i.return_date
            res = res/24/60/60
        return res

    def is_credit_closed(self, *args):
        for i in args:
            if str(i.actual_return_date) == '1000-01-01':
                is_it_closed = False
            else:
                is_it_closed = True
        return is_it_closed

    # def sum_plat_body(self, *args):
    #     for i in args:
    #         print(Payments.objects.filter(credit_id=Credits.objects.get(id=i.id)).only('sum'))
    #     all_body_p = sum([i.id for i in args])
    #     return all_body_p


class FileSerializer(serializers.ModelSerializer):

    class Meta():
        model = File
        fields = ('file', 'remark', 'timestamp')