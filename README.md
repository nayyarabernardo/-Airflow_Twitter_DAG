# Apache Airflow: extração de dados da API do Twitter 

[![PyPI version](https://badge.fury.io/py/apache-airflow.svg)](https://badge.fury.io/py/apache-airflow)
[![GitHub Build](https://github.com/apache/airflow/workflows/CI%20Build/badge.svg)](https://github.com/apache/airflow/actions)
[![Documentation Status](https://readthedocs.org/projects/airflow/badge/?version=latest)](https://airflow.readthedocs.io/en/latest/?badge=latest)
[![License](http://img.shields.io/:license-Apache%202-blue.svg)](http://www.apache.org/licenses/LICENSE-2.0.txt)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/apache-airflow.svg)](https://pypi.org/project/apache-airflow/)


O [Apache Airflow](https://airflow.apache.org/docs/stable/) (ou simplesmente Airflow) é uma plataforma para criar, agendar e monitorar fluxos de trabalho de forma programática.

Quando os fluxos de trabalho são definidos como código, eles se tornam mais fáceis de manter, versáveis, testáveis e colaborativos.
Use o Airflow para criar fluxos de trabalho como gráficos acíclicos direcionados (DAGs) de tarefas. O agendador do Airflow executa suas tarefas em uma matriz de trabalhadores enquanto segue as dependências especificadas. Utilitários avançados de linha de comando facilitam a realização de cirurgias complexas em DAGs.

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Índice**

- [Ferramentas Utilizadas](#ferramentas-utilizadas)
- [Instalação](#instalação)
- [Links](#links)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Ferramentas Utilizadas
Apache Airflow is tested with:

|              | Master version |
| ------------ | -------------- |
| Python       | 3.9            |
| MySQL        | 8.0            |

## Instalação

```bash
pip install apache-airflow==1.10.12 \
 --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-1.10.12/constraints-3.7.txt"
```


## Links

- [Documentation Apache Airflow](https://airflow.apache.org/docs/stable/)
- [Documentation API Twitter](https://developer.twitter.com/en/docs)
- [More](https://cwiki.apache.org/confluence/display/AIRFLOW/Airflow+Links)
