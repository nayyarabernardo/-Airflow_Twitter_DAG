from airflow.providers.http.hooks.http import HttpHook
import requests
from datetime import datetime, timedelta
import json


class TwitterHook(HttpHook):

    def __init__(self, end_time, start_time, query, conn_id=None): #self padrão conn = conecti id
        self.end_time = end_time #agr quem roda é que define o parametro de tempo q vai ser usado
        self.start_time =  start_time
        self.query = query #agr vc pode definir qual sua query
        self.conn_id = conn_id or "twitter_default"  #usando o nome da conexao que criamos
        super().__init__(http_conn_id=self.conn_id) #super acessa a classe herdada 
    
    def create_url(self):
        
        TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z" 

        end_time = self.end_time
        start_time = self.start_time
        query = self.query

        tweet_fields = "tweet.fields=author_id,conversation_id,created_at,id,in_reply_to_user_id,public_metrics,lang,text"
        user_fields = "expansions=author_id&user.fields=id,name,username,created_at"

        url_raw = f"{self.base_url}/2/tweets/search/recent?query={query}&{tweet_fields}&{user_fields}&start_time={start_time}&end_time={end_time}"

        return url_raw
    
    def connect_to_endpoint(self, url, session):  #agr temos que criar uma função para requestes de conexão
        request = requests.Request("GET", url)  #metodo GET
        prep = session.prepare_request(request)  #preparrar requests com metodo 
        self.log.info(f"URL: {url}") #logs para informar url de requisição
        return self.run_and_check(session, prep, {}) #metodo que existe na classe http hook ja preparado o terceito parametro {} é obrigatorio porem nao precisamos informar qual é o parametro atenção http hook 

    def paginate(self, url_raw, session):
        
        lista_json_response = []
        #imprimir json
        response = self.connect_to_endpoint(url_raw, session) #chamar a função anteriror responsavel por salvar
        json_response = response.json() 
        lista_json_response.append(json_response)  #inserir os dados agr dentro dessa lista
        contador = 1

        # paginate lembrado que é para proximas paginas 
        while "next_token" in json_response.get("meta",{}) and contador<100: #10 o limite de requisições
            next_token = json_response['meta']['next_token']
            url = f"{url_raw}&next_token={next_token}"
            response = self.connect_to_endpoint(url, session) 
            json_response = response.json()
            lista_json_response.append(json_response)
            contador += 1

        return lista_json_response
    
    def run(self):    #função que engloba todas as outras funções 
        session = self.get_conn()   #pedir ma sessão, n somos maisresponsaveis por criar essa sessão
        url_raw = self.create_url()

        return self.paginate(url_raw, session)

if __name__ == "__main__":   #ele ta garantindo toda vez que rodar apenas o que ta dentro do ifem 
    #montando url
    TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.00Z"

    end_time = datetime.now().strftime(TIMESTAMP_FORMAT)
    start_time = (datetime.now() + timedelta(-1)).date().strftime(TIMESTAMP_FORMAT)
    query = "datascience"

    for pg in TwitterHook(end_time, start_time, query).run():
        print(json.dumps(pg, indent=4, sort_keys=True))