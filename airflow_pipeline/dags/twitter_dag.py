import sys
sys.path.append("airflow_pipeline")

from airflow.models import DAG
from datetime import datetime, timedelta
from operators.twitter_operator import TwitterOperator
from os.path import join

with DAG(dag_id = "TwitterDAG", start_date=datetime.now(), schedule_interval="@daily") as dag:

    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"
    end_time = datetime.now().strftime(TIMESTAMP_FORMAT)
    start_time = (datetime.now() + timedelta(-1)).date().strftime(TIMESTAMP_FORMAT)
    query = "datascience"
    to = TwitterOperator(file_path=join("datalake/twitter_datascience",
                                        "extract_date={{ ds }}",  #informacoes em tempo de rodar o codigo
                                        f"datascience_{{ ds_nodasg }}.json"),  #substituir pela data sem barra
                                        query=query, start_time=start_time, end_time=end_time, task_id="twitter_datascience")
       