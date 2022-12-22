import sys
sys.path.append("airflow_pipeline")  #onde ele vai procurar o arquivo hook 

from airflow.models import BaseOperator, DAG, TaskInstance
from hook.twitter_hook import TwitterHook
import json
from datetime import datetime, timedelta
from os.path import join
from pathlib import Path

class TwitterOperator(BaseOperator):

    template_fields = ["query", "file_path", "start_time", "end_time"]

    def __init__(self, file_path, end_time, start_time, query, **kwargs):  #kwargs base importante necessaria
        self.end_time = end_time
        self.start_time = start_time
        self.query = query
        self.file_path = file_path
        super().__init__(**kwargs)   #metodo construtor obrigatorio 

    def create_parent_folder(self): #criação da pasta
        (Path(self.file_path).parent).mkdir(parents=True,exist_ok=True) #garante que cria as pastas anteriores

    def execute(self, context):  #context - metodo esperado no execute 
        end_time = self.end_time
        start_time = self.start_time
        query = self.query

        self.create_parent_folder() #chamando função

        with open(self.file_path, "w") as output_file:  #w white .. as output_file  quando quiser citar esse arquivo chamar esse parametro
            for pg in TwitterHook(end_time, start_time, query).run():
                json.dump(pg, output_file, ensure_ascii=False)  #ensure_ascii=False tratamento a questão de caracter e acentuação e emojis sem erros 
                output_file.write("\n")   #quebra de pagina 

if __name__ == "__main__":   #ele ta garantindo toda vez que rodar apenas o que ta dentro do ifem 
    #montando url
    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"

    end_time = datetime.now().strftime(TIMESTAMP_FORMAT)
    start_time = (datetime.now() + timedelta(-1)).date().strftime(TIMESTAMP_FORMAT)
    query = "datascience"

    with DAG(dag_id = "TwitterTest", start_date=datetime.now()) as dag:
        to = TwitterOperator(file_path=join("datalake/twitter_datascience",
                                            f"extract_date={datetime.now().date()}",
                                            f"datascience_{datetime.now().date().strftime('%Y%m%d')}.json"),
                                            query=query, start_time=start_time, end_time=end_time, task_id="test_run")
        ti = TaskInstance(task=to)
        to.execute(ti.task_id)
