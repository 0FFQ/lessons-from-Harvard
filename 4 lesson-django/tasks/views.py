from django.shortcuts import render

tasks = ["foo", "asdaodddo", "foaasdasdo", ]
# Create your views here.
def index(request):
    return render(request, "tasks/index.html"), {

    }