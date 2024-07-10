from django.urls import path
from .views import (
    create_cell_experiment,
    experiments_home,
    edit_cell_experiment,
    delete_cell_experiment,
)


app_name = "samples"

urlpatterns = [
    path("create/", create_cell_experiment, name="create_cell_experiment"),
    path(
        "edit/<int:experiment_id>/", edit_cell_experiment, name="edit_cell_experiment"
    ),
    path(
        "delete/<int:experiment_id>/",
        delete_cell_experiment,
        name="delete_cell_experiment",
    ),
    path("", experiments_home, name="experiments_home"),
]
