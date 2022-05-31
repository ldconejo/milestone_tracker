from django.shortcuts import render
from datetime import date, timedelta
from milestones.models import ProjectsTable, MilestonesTable

# Create your views here.
def main_view(request):
    results_dict = {}
    in_two_weeks = date.today() + timedelta(days=14)
    projects = ProjectsTable.objects.all()

    for project in projects:
        results_dict[project.project] = {}

        completed = MilestonesTable.objects.all().filter(
            project__exact=project, status__exact="2"
        )
        overdue = (
            MilestonesTable.objects.all()
            .filter(project__exact=project, due_date__lt=date.today())
            .exclude(status="2")
        )
        due_soon = (
            MilestonesTable.objects.all()
            .filter(
                project__exact=project,
                due_date__gte=date.today(),
                due_date__lt=in_two_weeks,
            )
            .exclude(status="2")
        )
        started = MilestonesTable.objects.all().filter(
            project__exact=project, status__exact="1"
        )

        results_dict[project.project]["completed"] = completed
        results_dict[project.project]["overdue"] = overdue
        results_dict[project.project]["due_soon"] = due_soon
        results_dict[project.project]["started"] = started

    context = {"results_dict": results_dict}
    return render(request, "milestones/welcome_screen.html", context)
