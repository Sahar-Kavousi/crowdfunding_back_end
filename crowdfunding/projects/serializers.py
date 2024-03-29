from rest_framework import serializers
from .models import Project, Pledge
from django.db.models import Sum


class PledgeSerializer(serializers.ModelSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    # New field added to get the supporter's name
    supporter_username = serializers.CharField(source='supporter.username', read_only=True)
    supporter_firstname = serializers.CharField(source='supporter.first_name', read_only=True)
    supporter_lastname = serializers.CharField(source='supporter.last_name', read_only=True)

    class Meta:
        model = Pledge
        fields = '__all__'


class PledgeDetailSerializer(PledgeSerializer):
    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get(
            'anonymous', instance.anonymous)
        instance.project = validated_data.get('project', instance.project)
        instance.supporter = validated_data.get(
            'supporter', instance.supporter)
        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    pledges = PledgeSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = '__all__'

    def amount_to_raise(self, instance):
        sum_of_pledges = instance.pledges.aggregate(Sum('amount'))[
            'amount__sum']
        if sum_of_pledges is not None:  # an integer and 'none' value math operation is not supported by python
            amount_to_go = instance.goal - sum_of_pledges
        else:
            amount_to_go = instance.goal
        return amount_to_go


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description',
                                                  instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created',
                                                   instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance

    def amount_to_raise(self, instance):
        sum_of_pledges = instance.pledges.aggregate(Sum('amount'))[
            'amount__sum']
        if sum_of_pledges is not None:  # an integer and 'none' value math operation is not supported by python
            amount_to_go = instance.goal - sum_of_pledges
        else:
            amount_to_go = instance.goal
        return amount_to_go
