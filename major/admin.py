from django.contrib import admin
from major.models import Parameters, TaskType, NodeType, Users, Node, AbnormalType,RegressionAbnormal,PhaseType
from major.models import Tasks, JobStream, Job, Template, Environment, EnvironmentJob, SimulationEnvironment
from major.models import ParameterScore,JobAbnormal,Benchmark,StatisticInfo,JobInfo,Suggestion, Disk ,Gpu ,Net ,Logs, CmpConfigT
# Register your models here.

admin.site.register(AbnormalType)
admin.site.register(Parameters)
admin.site.register(TaskType)
admin.site.register(NodeType)
admin.site.register(Users)
admin.site.register(Node)
admin.site.register(Tasks)
admin.site.register(Job)
admin.site.register(JobStream)
admin.site.register(Template)
admin.site.register(Environment)
admin.site.register(EnvironmentJob)
admin.site.register(SimulationEnvironment)
admin.site.register(ParameterScore)
admin.site.register(JobAbnormal)
admin.site.register(Benchmark)
admin.site.register(StatisticInfo)
admin.site.register(JobInfo)
admin.site.register(Suggestion)
admin.site.register(RegressionAbnormal)
admin.site.register(PhaseType)
admin.site.register(Disk)
admin.site.register(Gpu)
admin.site.register(Net)
admin.site.register(Logs)
admin.site.register(CmpConfigT)
