from django.contrib.auth.models import AbstractUser
from django.db import models


class Position(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TaskType(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    teams = models.ManyToManyField(Team, related_name='projects')


class Worker(AbstractUser):
    position = models.ForeignKey(
        Position,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='workers')
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='members'
    )


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Urgent", "Urgent"),
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    name = models.CharField(max_length=256)
    description = models.TextField()
    deadline = models.DateTimeField()
    is_completed = models.BooleanField(default=False)
    priority = models.CharField(choices=PRIORITY_CHOICES, max_length=20, default="Medium")
    task_type = models.ForeignKey(
        TaskType,
        on_delete=models.SET_NULL,
        null=True,
        related_name="tasks",
    )
    assignees = models.ManyToManyField(Worker, related_name='assignees')
    tags = models.ManyToManyField(Tag, related_name='tasks', blank=True)
    project = models.ForeignKey(
        Project,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tasks'
    )

    def formatted_deadline(self):
        return self.deadline.strftime("%d-%m-%Y")

    def __str__(self):
        return (f"{self.name} "
                f"({self.priority}, due {self.deadline}) - "
                f"{'Completed' if self.is_completed else 'In Progress'}"
                )
