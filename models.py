# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AlertHistory(models.Model):
    id = models.AutoField()
    factory_id = models.IntegerField()
    message = models.CharField(max_length=-1)
    alert_type = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'alert_history'


class AlgorithmAccuracies(models.Model):
    task = models.ForeignKey('LabelTasks', models.DO_NOTHING, blank=True, null=True)
    algorithm = models.ForeignKey('Algorithms', models.DO_NOTHING)
    algorithm_type = models.CharField(max_length=-1)
    accuracy = models.TextField()  # This field type is a guess.
    tags = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'algorithm_accuracies'


class Algorithms(models.Model):
    algorithm_type = models.CharField(max_length=-1)
    algorithm_name = models.CharField(max_length=-1)
    function_name = models.CharField(max_length=-1)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'algorithms'


class AlgorithmsActive(models.Model):
    datasource = models.ForeignKey('Datasources', models.DO_NOTHING)
    algorithm_type = models.CharField(max_length=-1)
    active_algorithm = models.ForeignKey(Algorithms, models.DO_NOTHING)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'algorithms_active'


class AuthTokens(models.Model):
    id = models.AutoField()
    user_id = models.IntegerField()
    last_used = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_tokens'


class ClusterModels(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField()
    model_file_name = models.CharField(max_length=50)
    state_algorithm = models.ForeignKey('StateAlgorithms', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cluster_models'


class CountCyclesAlgorithmActive(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField(unique=True)
    active_count_cycles_algorithm = models.ForeignKey('CountCyclesAlgorithms', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'count_cycles_algorithm_active'


class CountCyclesAlgorithms(models.Model):
    id = models.AutoField(unique=True)
    algorithm_name = models.CharField(unique=True, max_length=-1)
    algorithm_func_name = models.CharField(unique=True, max_length=-1)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'count_cycles_algorithms'


class CountCyclesDatasources(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField()
    algorithm_id = models.CharField(max_length=20)
    window_size = models.IntegerField()
    active_flag = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'count_cycles_datasources'


class CountCyclesHistory(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField()
    algorithm_id = models.CharField(max_length=20)
    cycle_counts = models.IntegerField()
    time_occurred = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'count_cycles_history'


class CountCyclesHistoryNew(models.Model):
    id = models.AutoField()
    datasource = models.ForeignKey(CountCyclesAlgorithmActive, models.DO_NOTHING)
    counts = models.IntegerField()
    time_occurred = models.DateTimeField()
    count_algorithm = models.ForeignKey(CountCyclesAlgorithms, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'count_cycles_history_new'


class CurrentSignatures(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField()
    val = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'current_signatures'


class CycleTimesAlgorithmActive(models.Model):
    datasource_id = models.IntegerField(unique=True)
    active_cycle_time_algorithm = models.ForeignKey('CycleTimesAlgorithms', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cycle_times_algorithm_active'


class CycleTimesAlgorithms(models.Model):
    algorithm_name = models.CharField(max_length=-1)
    algorithm_func_name = models.CharField(max_length=-1)
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'cycle_times_algorithms'
        unique_together = (('algorithm_name', 'algorithm_func_name'),)


class CycleTimesHistoryNew(models.Model):
    datasource = models.ForeignKey(CycleTimesAlgorithmActive, models.DO_NOTHING)
    cycle_time = models.IntegerField()
    time_occurred = models.DateTimeField()
    cycle_time_algorithm = models.ForeignKey(CycleTimesAlgorithms, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cycle_times_history_new'


class DailySummaryHistory(models.Model):
    id = models.AutoField()
    user = models.ForeignKey('Users', models.DO_NOTHING)
    event_type = models.CharField(max_length=-1)
    created_at = models.DateTimeField(blank=True, null=True)
    last_sent = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'daily_summary_history'


class DatasourceChangepoints(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField()
    changepoints = models.TextField(blank=True, null=True)  # This field type is a guess.
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datasource_changepoints'


class DatasourceConfig(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField()
    field = models.CharField(max_length=-1, blank=True, null=True)
    value = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datasource_config'


class Datasources(models.Model):
    machine_id = models.CharField(max_length=-1)
    clamp_id = models.CharField(max_length=10)
    created_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    active = models.NullBooleanField()
    description = models.CharField(max_length=200, blank=True, null=True)
    machine_type = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'datasources'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DowntimeAlerts(models.Model):
    title = models.CharField(max_length=-1, blank=True, null=True)
    active = models.NullBooleanField()
    factory = models.ForeignKey('Factory', models.DO_NOTHING)
    machine = models.ForeignKey(Datasources, models.DO_NOTHING)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    threshold = models.IntegerField()
    alert_recipients = models.TextField()  # This field type is a guess.
    notification_arn = models.CharField(max_length=-1)
    created_at = models.DateTimeField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    deleted = models.NullBooleanField()
    timed_out = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'downtime_alerts'


class DowntimeAlertsHistory(models.Model):
    id = models.AutoField()
    alert = models.ForeignKey(DowntimeAlerts, models.DO_NOTHING)
    event_type = models.CharField(max_length=-1)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'downtime_alerts_history'


class DowntimeHistory(models.Model):
    id = models.AutoField(unique=True)
    datasource_id = models.IntegerField()
    time_occurred = models.DateTimeField()
    avg_current = models.FloatField()

    class Meta:
        managed = False
        db_table = 'downtime_history'


class DowntimeMonitorDatasources(models.Model):
    id = models.AutoField(unique=True)
    datasource_id = models.IntegerField()
    threshold = models.FloatField()
    timeout = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'downtime_monitor_datasources'


class Factory(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory'


class FactoryAlerts(models.Model):
    id = models.AutoField()
    ds_id = models.IntegerField()
    type = models.CharField(max_length=-1)
    config = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    active = models.NullBooleanField()
    live = models.NullBooleanField()
    interval = models.IntegerField(blank=True, null=True)
    timed_out = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'factory_alerts'


class FactoryConfig(models.Model):
    id = models.AutoField()
    factory_id = models.IntegerField()
    field = models.CharField(max_length=20, blank=True, null=True)
    value = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory_config'


class FactoryNotifications(models.Model):
    id = models.AutoField()
    factory_id = models.IntegerField()
    callback_id = models.CharField(max_length=-1)
    is_sent = models.NullBooleanField()
    message = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory_notifications'


class FactoryRoles(models.Model):
    factory = models.ForeignKey(Factory, models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory_roles'


class FactoryShifts(models.Model):
    id = models.AutoField()
    factory_id = models.IntegerField()
    name = models.CharField(max_length=-1)
    start_minute = models.IntegerField()
    end_minute = models.IntegerField()
    dotw = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'factory_shifts'


class Feature(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feature'


class FeatureFlags(models.Model):
    id = models.AutoField()
    feature_id = models.IntegerField()
    factory_id = models.IntegerField()
    has_feature = models.NullBooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'feature_flags'


class Heartbeater(models.Model):
    id = models.AutoField()
    service = models.CharField(max_length=100, blank=True, null=True)
    event_name = models.CharField(max_length=100, blank=True, null=True)
    active = models.NullBooleanField()
    timeout = models.IntegerField(blank=True, null=True)
    last_received = models.DateTimeField(blank=True, null=True)
    timed_out = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'heartbeater'
        unique_together = (('service', 'event_name'),)


class HotSwapCurrent(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField()
    val = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hot_swap_current'


class Invitations(models.Model):
    email = models.CharField(max_length=-1)
    factory_id = models.IntegerField()
    token = models.CharField(max_length=-1)
    created_at = models.DateTimeField(blank=True, null=True)
    open = models.NullBooleanField()
    activated_at = models.DateTimeField(blank=True, null=True)
    invited_by = models.IntegerField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=-1, blank=True, null=True)
    last_name = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invitations'


class LabelTasks(models.Model):
    task_type = models.CharField(max_length=-1)
    datasource = models.ForeignKey(Datasources, models.DO_NOTHING, blank=True, null=True)
    graph_link = models.CharField(max_length=-1, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    task_configuration = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'label_tasks'


class LabeledCycles(models.Model):
    task = models.ForeignKey(LabelTasks, models.DO_NOTHING, unique=True, blank=True, null=True)
    labeled_cycle_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    labeler = models.ForeignKey('Labelers', models.DO_NOTHING, blank=True, null=True)
    submitted_at = models.DateTimeField(blank=True, null=True)
    correct = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'labeled_cycles'


class LabeledStates(models.Model):
    task = models.ForeignKey(LabelTasks, models.DO_NOTHING, unique=True, blank=True, null=True)
    labeled_state_data = models.TextField(blank=True, null=True)  # This field type is a guess.
    labeler = models.ForeignKey('Labelers', models.DO_NOTHING, blank=True, null=True)
    submitted_at = models.DateTimeField(blank=True, null=True)
    correct = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'labeled_states'


class LabeledTasksForAccuracies(models.Model):
    task = models.ForeignKey(LabelTasks, models.DO_NOTHING, blank=True, null=True)
    task_type = models.CharField(max_length=-1)
    labeler = models.ForeignKey('Labelers', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labeled_tasks_for_accuracies'


class LabelerInvitations(models.Model):
    id = models.AutoField()
    email = models.CharField(max_length=-1)
    token = models.CharField(max_length=32)
    open = models.NullBooleanField()
    created_at = models.DateTimeField(blank=True, null=True)
    activated_at = models.DateTimeField(blank=True, null=True)
    types = models.TextField(blank=True, null=True)  # This field type is a guess.
    factories = models.TextField(blank=True, null=True)  # This field type is a guess.
    datasources = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'labeler_invitations'


class LabelerTypes(models.Model):
    id = models.AutoField()
    labeler = models.ForeignKey('Labelers', models.DO_NOTHING, blank=True, null=True)
    task_type_filter = models.TextField()  # This field type is a guess.
    task_type_filter_active = models.BooleanField()
    factories_filters_active = models.BooleanField()
    datasources_filters = models.TextField()  # This field type is a guess.
    datasources_filters_active = models.BooleanField()
    factories_filters = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'labeler_types'


class Labelers(models.Model):
    username = models.CharField(max_length=-1, blank=True, null=True)
    pw_hash = models.CharField(max_length=-1, blank=True, null=True)
    access_token = models.CharField(max_length=32, blank=True, null=True)
    last_used = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'labelers'


class MachineScreenshots(models.Model):
    id = models.AutoField()
    type = models.CharField(max_length=30, blank=True, null=True)
    s3_key = models.CharField(max_length=156, blank=True, null=True)
    ds_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    day = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'machine_screenshots'


class Machines(models.Model):
    id = models.AutoField()
    name = models.CharField(max_length=100, blank=True, null=True)
    key = models.CharField(max_length=-1, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    factory_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'machines'


class PlotlyStreams(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField()
    stream_key = models.CharField(max_length=-1)
    active = models.NullBooleanField()
    graph_url = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plotly_streams'


class ReportData(models.Model):
    id = models.AutoField()
    uuid = models.CharField(max_length=32)
    report_type = models.CharField(max_length=-1)
    factory_id = models.IntegerField()
    s3_key = models.CharField(max_length=-1)
    report_date = models.CharField(max_length=-1)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_data'


class Reports(models.Model):
    id = models.AutoField()
    type = models.CharField(max_length=30, blank=True, null=True)
    s3_key = models.CharField(max_length=100, blank=True, null=True)
    factory_id = models.IntegerField()
    day = models.CharField(max_length=8, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reports'


class ResetRequests(models.Model):
    id = models.AutoField()
    user_id = models.IntegerField()
    token = models.CharField(max_length=-1)
    open = models.NullBooleanField()
    requested_at = models.DateTimeField(blank=True, null=True)
    reset_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reset_requests'


class SchemaVersion(models.Model):
    installed_rank = models.IntegerField(primary_key=True)
    version = models.CharField(max_length=50, blank=True, null=True)
    description = models.CharField(max_length=200)
    type = models.CharField(max_length=20)
    script = models.CharField(max_length=1000)
    checksum = models.IntegerField(blank=True, null=True)
    installed_by = models.CharField(max_length=100)
    installed_on = models.DateTimeField()
    execution_time = models.IntegerField()
    success = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'schema_version'


class StateAlgorithmActive(models.Model):
    datasource_id = models.IntegerField(unique=True)
    active_state_algorithms = models.ForeignKey('StateAlgorithms', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'state_algorithm_active'


class StateAlgorithms(models.Model):
    algorithm_name = models.CharField(unique=True, max_length=50)
    algorithm_func_name = models.CharField(unique=True, max_length=30)
    active = models.NullBooleanField()
    window_size = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'state_algorithms'


class StateHistory(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField()
    state = models.CharField(max_length=20)
    time_occurred = models.DateTimeField()
    throughput = models.IntegerField(blank=True, null=True)
    cycle_times = models.TextField(blank=True, null=True)  # This field type is a guess.
    state_from_cluster = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state_history'


class StateHistoryNew(models.Model):
    datasource = models.ForeignKey(StateAlgorithmActive, models.DO_NOTHING)
    state = models.CharField(max_length=20)
    time_occurred = models.DateTimeField()
    state_algorithm = models.ForeignKey(StateAlgorithms, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'state_history_new'


class StateMonitorDatasources(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField()
    off_threshold = models.FloatField()
    idle_threshold = models.FloatField()
    std_threshold = models.FloatField()
    time_window = models.IntegerField()
    active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'state_monitor_datasources'


class StateThresholds(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField(unique=True)
    off_threshold = models.FloatField()
    idle_threshold = models.FloatField()

    class Meta:
        managed = False
        db_table = 'state_thresholds'


class TasksAssignments(models.Model):
    task = models.ForeignKey(LabelTasks, models.DO_NOTHING, blank=True, null=True)
    labeler = models.ForeignKey(Labelers, models.DO_NOTHING, blank=True, null=True)
    assigned_at = models.DateTimeField(blank=True, null=True)
    completed = models.NullBooleanField()
    skipped = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'tasks_assignments'


class TestMigrations(models.Model):
    id = models.AutoField()
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_migrations'


class Timeouts(models.Model):
    id = models.AutoField()
    hb_id = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    resolved_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'timeouts'


class Unitcount(models.Model):
    id = models.AutoField()
    datasource_id = models.IntegerField()
    algo_source = models.IntegerField()
    part_id = models.IntegerField(blank=True, null=True)
    startat = models.DateTimeField(blank=True, null=True)
    endat = models.DateTimeField(blank=True, null=True)
    cycles = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'unitcount'


class UnitcountMotif(models.Model):
    id = models.AutoField()
    algo_source = models.IntegerField()
    datasource_id = models.IntegerField()
    payload = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unitcount_motif'


class UserRoles(models.Model):
    user = models.ForeignKey('Users', models.DO_NOTHING, blank=True, null=True)
    role = models.ForeignKey(FactoryRoles, models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_roles'


class Users(models.Model):
    factory_id = models.IntegerField()
    username = models.CharField(max_length=100, blank=True, null=True)
    pin_code = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    pw_hash = models.CharField(max_length=-1, blank=True, null=True)
    email = models.CharField(max_length=-1, blank=True, null=True)
    phone = models.CharField(max_length=-1, blank=True, null=True)
    first_name = models.CharField(max_length=-1, blank=True, null=True)
    last_name = models.CharField(max_length=-1, blank=True, null=True)
    daily_summary = models.NullBooleanField()
    daily_summary_notification_arn = models.CharField(max_length=-1, blank=True, null=True)
    daily_summary_notification_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
