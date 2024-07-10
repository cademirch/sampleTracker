from django.contrib import admin
from .models import CellLine, Infection, CellExperiment, CellPellet

admin.site.register(CellLine)
admin.site.register(Infection)
admin.site.register(CellExperiment)
admin.site.register(CellPellet)
