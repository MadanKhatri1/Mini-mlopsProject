import dagshub
import mlflow


dagshub.init(repo_owner='madankh00123', repo_name='Mini-mlopsProject', mlflow=True)


mlflow.set_tracking_uri('https://dagshub.com/madankh00123/Mini-mlopsProject.mlflow/')


with mlflow.start_run():
  

  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1) 