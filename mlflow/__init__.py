import os

# Necessary workaround for this issue:
# https://github.com/google/protobuf/issues/3002#issuecomment-325459597
os.environ['PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION'] = 'python'

# pylint: disable=wrong-import-position
import mlflow.projects as projects # noqa
import mlflow.tracking as tracking  # noqa

log_param = tracking.log_param
log_metric = tracking.log_metric
log_artifacts = tracking.log_artifacts
log_artifact = tracking.log_artifact
active_run = tracking.active_run
start_run = tracking.start_run
end_run = tracking.end_run
get_artifact_uri = tracking.get_artifact_uri
set_tracking_uri = tracking.set_tracking_uri
get_tracking_uri = tracking.get_tracking_uri
create_experiment = tracking.create_experiment
list_experiments = tracking.list_experiments


run = projects.run


# get project relative path
def _relpath(*rel_path_elms):
    return os.path.join(os.path.abspath(os.path.dirname(__file__)), *rel_path_elms)


__all__ = ["log_param", "log_metric", "log_artifacts", "log_artifact", "active_run",
           "start_run", "end_run", "get_artifact_uri", "set_tracking_uri", "create_experiment"]
