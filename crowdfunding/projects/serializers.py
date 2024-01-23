from rest_framework import serializers

from .models import Project, Pledge


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')

    class Meta:
        model = Project
        fields = '__all__'


class PledgeSerializer(serializers.ModelSerializer):
    project = serializers.ReadOnlyField(source='project.id')
    supporter = serializers.ReadOnlyField(source='supporter.id')

    class Meta:
        model = Pledge
        fields = '__all__'


class ProjectDetailSerializer(ProjectSerializer):
    pledges = PledgeSerializer(many=True, read_only=True)
    is_deleted = serializers.BooleanField(default=False, write_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get(
            'date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        # Soft delete handling
        is_deleted = validated_data.get('is_deleted', False)

        if is_deleted:
            instance.is_deleted = True
            instance.save(update_fields=['is_deleted'])
        else:
            instance.is_deleted = False
            instance.save()
        instance.save()
        return instance


class PledgeDetailSerializer(PledgeSerializer):
    supporter = serializers.ReadOnlyField(source='supporter.id')
    project = ProjectSerializer(read_only=True)

    def update(self, instance, validated_data):
        instance.amount = validated_data.get('amount', instance.amount)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get(
            'anonymous', instance.anonymous)
        # instance.project = validated_data.get('project', instance.project)
        instance.supporter = validated_data.get(
            'supporter', instance.supporter)
        return instance
