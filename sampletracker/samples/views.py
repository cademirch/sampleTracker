from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CellExperiment
from .forms import CellExperimentForm


@login_required
def experiments_home(request):
    experiments = CellExperiment.objects.all()
    return render(request, "experiments/home.html", {"experiments": experiments})


@login_required
def create_cell_experiment(request):
    if request.method == "POST":
        form = CellExperimentForm(request.POST)
        if form.is_valid():
            cell_experiment = form.save(commit=False)
            cell_experiment.created_by = request.user
            cell_experiment.save()
            form.save_m2m()  # Save the many-to-many data for the form
            return redirect("samples:experiments_home")
    else:
        form = CellExperimentForm()

    return render(request, "experiments/create_exp.html", {"form": form})


@login_required
def edit_cell_experiment(request, experiment_id):
    experiment = get_object_or_404(CellExperiment, id=experiment_id)
    if request.method == "POST":
        form = CellExperimentForm(request.POST, instance=experiment)
        if form.is_valid():
            form.save()
            return redirect("samples:experiments_home")
    else:
        form = CellExperimentForm(instance=experiment)

    return render(
        request,
        "experiments/create_exp.html",
        {"form": form, "edit": True},
    )


@login_required
def delete_cell_experiment(request, experiment_id):
    experiment = get_object_or_404(CellExperiment, id=experiment_id)
    if request.method == "POST":
        experiment.delete()
        return redirect("samples:experiments_home")
    return render(
        request, "experiments/confirm_delete.html", {"experiment": experiment}
    )
