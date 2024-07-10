from django.db import models
from django.conf import settings


class CellLine(models.Model):
    """
    Represents a cell line used in experiments.
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Infection(models.Model):
    """
    Represents an infection used in experiments.
    """

    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class CellExperiment(models.Model):
    """
    Represents a cell culture experiment.
    Holds metadata regarding the experiment, including cell lines, infections, etc.
    Individual pellets will be associated with their experiment.

    An experiment can have 1 cell line, but multiple infections.
    These are represented as foreign keys to the respective models.
    """

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    cell_line = models.ForeignKey(CellLine, on_delete=models.CASCADE)
    infections = models.ManyToManyField(Infection, blank=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class CellPellet(models.Model):
    """
    Represents a cell pellet associated with a cell experiment.
    """

    experiment = models.ForeignKey(
        CellExperiment, related_name="pellets", on_delete=models.CASCADE
    )
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    date_extracted = models.DateField(blank=True, null=True)
    split_date = models.CharField(max_length=20)
    replicate = models.CharField(max_length=1)
    unique_id = models.CharField(max_length=100, unique=True)
    storage_location = models.CharField(max_length=100)
    metadata = models.JSONField(blank=True, null=True)
    timepoint = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.metadata:
            self.metadata = self.experiment.metadata
        super().save(*args, **kwargs)

    def __str__(self):
        return self.unique_id
