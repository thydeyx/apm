# -*- coding: utf-8 -*-
#  !/usr/bin/python

# @author: YangYu
# @date: 15/10/13
# @description:

from django.db import models
import json
# Create your models here.

class AbnormalType(models.Model):
    """
    常量表
    执行任务的类型表
    """
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    type = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class TaskType(models.Model):
    """
    常量表
    执行任务的类型表
    """
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr))  for attr in [f.name for f in self._meta.fields]]))

class NodeType(models.Model):
    """
    常量表
    节点的类型表
    """
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Users(models.Model):
    """
    用户
    """
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=5)
    password = models.CharField(max_length=40)
    id_number = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    real_name = models.CharField(max_length=30)
    department = models.CharField(max_length=30)
    introduction = models.TextField(max_length=200)
    level = models.IntegerField()

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Gpu(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Net(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Disk(models.Model):
    name = models.CharField(max_length=100)
    size = models.FloatField()
    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Node(models.Model):
    """
    节点
    """
    name = models.CharField(max_length=30)
    introduction = models.TextField(max_length=200)
    ip = models.GenericIPAddressField()
    cpu_number = models.IntegerField()
    cpu_frequency = models.FloatField()
    memory = models.FloatField()
    memory_Speed = models.FloatField()
    disk = models.ManyToManyField(Disk)
    gpu = models.ManyToManyField(Gpu)
    net = models.ManyToManyField(Net)
    os = models.CharField(max_length=30)
    uri = models.URLField()

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class Environment(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    node = models.ManyToManyField(Node)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class SimulationEnvironment(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    environment = models.ForeignKey(Environment)
    node = models.ManyToManyField(Node)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

#产品运行模式
class RunMode(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name
    def toJSON(self):
        json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Job(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=30)
    runmode = models.ManyToManyField(RunMode)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class JobStream(models.Model):
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    job_num = models.IntegerField()
    jobs = models.ManyToManyField(Job)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class Parameters(models.Model):
    """
    常量表
    监测并进行计算的所有节点上的参数 CPU IO NET等
    """
    name = models.CharField(max_length=30)
    type = models.CharField(max_length=30)
    collect_name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class EnvironmentJob(models.Model):

    environment = models.ForeignKey(Environment)
    job = models.ForeignKey(JobStream)

    def __unicode__(self):
        return '%s %s' % (self.environment.name, self.job.name)

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))



class ParameterScore(models.Model):
    cpu_all_cpi = models.DecimalField(max_digits=12, decimal_places=2)
    cpu_all_idle = models.DecimalField(max_digits=12, decimal_places=2)
    cpu_all_sywa = models.DecimalField(max_digits=12, decimal_places=2)
    cpu_all_flops = models.DecimalField(max_digits=12, decimal_places=2)
    mem_all_mem_ratio = models.DecimalField(max_digits=12, decimal_places=2)
    mem_all_swap_ratio = models.DecimalField(max_digits=12, decimal_places=2)
    disk_all_write = models.DecimalField(max_digits=12, decimal_places=2)
    disk_all_read = models.DecimalField(max_digits=12, decimal_places=2)
    net_all_recv = models.DecimalField(max_digits=12, decimal_places=2)
    net_all_send = models.DecimalField(max_digits=12, decimal_places=2)
    nfs_all_in = models.DecimalField(max_digits=12, decimal_places=2)
    nfs_all_out = models.DecimalField(max_digits=12, decimal_places=2)
    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class JobAbnormal(models.Model):
	name = models.CharField(max_length=128)
	start_time = models.DateTimeField()
	end_time = models.DateTimeField()
	description = models.CharField(max_length=256)
	parameter = models.CharField(max_length=45)
	hostid = models.CharField(max_length=60)
	jobname = models.CharField(max_length=60)
	def __unicode__(self):
		return self.name

	def toJSON(self):
		return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Benchmark(models.Model):
    benchmark_time_density_score = models.ForeignKey(ParameterScore,related_name='benchmark_time_density_score')
    benchmark_sorted_consume_score = models.ForeignKey(ParameterScore,related_name='benchmark_sorted_consume_score')
    benchmark_total_consume_score = models.ForeignKey(ParameterScore,related_name='benchmark_total_consume_score')
    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))



class StatisticInfo(models.Model):
    max_score = models.ForeignKey(ParameterScore,related_name='max_score')
    min_score = models.ForeignKey(ParameterScore,related_name='min_score')
    average_score = models.ForeignKey(ParameterScore, related_name='average_score')
    curve_score = models.ForeignKey(ParameterScore, related_name='curve_score')

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))


class Suggestion(models.Model):
    description = models.CharField(max_length=512)
    type = models.IntegerField()

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class RegressionAbnormal(models.Model):
    abnormal_type = models.ForeignKey(AbnormalType)
    abnormal_num = models.IntegerField()
    phase_names = models.CharField(max_length=1024)

    def __unicode__(self):
        return  self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [ f.name for f in self._meta.fields]]))

class PhaseType(models.Model):
    nullType = models.IntegerField()
    nullTypeName = models.CharField(max_length=1024)
    cpuType = models.IntegerField()
    cpuTypeName = models.CharField(max_length=1024)
    networkType = models.IntegerField()
    networkTypeName = models.CharField(max_length=1024)
    diskType = models.IntegerField()
    diskTypeName = models.CharField(max_length=1024)
    memoryType = models.IntegerField()
    memoryTypeName = models.CharField(max_length=1024)

    def __unicode__(self):
        return  self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [ f.name for f in self._meta.fields]]))

class JobInfo(models.Model):
    runtime = models.IntegerField()
    phase_names = models.CharField(max_length=2048)
    p_tag = models.IntegerField()
    schedule_num = models.IntegerField()
    job_type = models.IntegerField()
    job_name = models.CharField(max_length=255)
    job_number = models.CharField(max_length=255)
    main_feature = models.ForeignKey(ParameterScore)
    benchmark = models.ForeignKey(Benchmark)
    abnormal = models.ManyToManyField(JobAbnormal)
    statistic = models.ForeignKey(StatisticInfo)
    Suggestion = models.ManyToManyField(Suggestion)
    runmode = models.ForeignKey(RunMode, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Tasks(models.Model):
    """
    监测 分析的任务表
    """
    name = models.CharField(max_length=30)
    introduction = models.TextField(max_length=200)
    type = models.ForeignKey(TaskType)
    audit = models.CharField(max_length=30,default='unaudit')
    start_date = models.CharField(max_length=30)
    end_date = models.CharField(max_length=30)
    start_time = models.CharField(max_length=30)
    end_time = models.CharField(max_length=30)
    process = models.CharField(max_length=10)
    user = models.ForeignKey(Users)
    nodes = models.ManyToManyField(EnvironmentJob)
    simulationEnvironments = models.ManyToManyField(SimulationEnvironment)
    parameterconfigs = models.ManyToManyField(Parameters)
    app_type = models.IntegerField()
    main_feature = models.ForeignKey(ParameterScore)
    benchmark = models.ForeignKey(Benchmark)
    statistic = models.ForeignKey(StatisticInfo)
    p_tag = models.IntegerField()
    run_time = models.IntegerField()
    data_type = models.CharField(max_length=30, null=True, blank=True)
    JobInfo = models.ManyToManyField(JobInfo)
    Suggestion = models.ManyToManyField(Suggestion)
    regression_start_time = models.CharField(max_length=30, default="")
    regression_end_time = models.CharField(max_length=30,default="")
    regression_jobstream = models.ForeignKey(JobStream,null=True,blank=True)
    regression_reportType = models.ForeignKey(PhaseType,null=True,blank=True)
    regression_abnormalType = models.ManyToManyField(RegressionAbnormal, null=True, blank=True)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Template(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    parameter = models.ManyToManyField(Parameters)

    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class Logs(models.Model):
    task = models.ForeignKey(Tasks)
    timestamp = models.DateTimeField()
    level = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    info = models.CharField(max_length=255)
    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))

class CmpConfigT(models.Model):
    taskid = models.IntegerField()
    jobname = models.CharField(max_length=255)
    nodename = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    time = models.IntegerField()
    def __unicode__(self):
        return self.name

    def toJSON(self):
        return json.dumps(dict([(attr, getattr(self, attr)) for attr in [f.name for f in self._meta.fields]]))
