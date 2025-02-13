# Guiding assistant for Vietnamese university admissions powered by Advanced RAG

Link dataset : [Link data](https://drive.google.com/drive/folders/1HyF8-EfL4w0G3spBbhcc0jTOqdc4XUhB)

# Table of content

<!--ts-->
- [Guiding assistant for Vietnamese university admissions powered by Advanced RAG](#guiding-assistant-for-vietnamese-university-admissions-powered-by-advanced-rag)
- [Table of content](#table-of-content)
- [Project structure](#project-structure)
- [Getting started](#getting-started)
  - [Prepare enviroment](#prepare-enviroment)
- [Application services](#application-services)
  - [RAG (Retrieval-Augmented Generation)](#rag-retrieval-augmented-generation)
    - [System overview](#system-overview)
    - [RAG flow answering](#rag-flow-answering)
    - [Evaluate](#evaluate)
- [DEMO](#demo)
<!--te-->

# Project structure
```bash

```
# Getting started

To get starte with this project, we need to do the following

## Prepare enviroment 
Install all dependencies dedicated to the project in local

```bash
python -m venv .venv
source .venv/bin/activate
cd src 
pip install -r requirements.txt
```

# Application services 

## RAG (Retrieval-Augmented Generation) 

### System overview


### RAG flow answering



### Evaluate 

The evaluation metrics currently in use are:

- **Recall@k**: Evaluate the accuracy of information retrieval
- **Correctness**:The metric evaluates the answer generated by the system to match a given query reference answer.

The golden dataset I chose for evaluation consists of 1000 samples. Each sample includes 3 fields: query, related_documents, answer


**Recall@k**
|Model               | K=3    | K =5   | K=10    |
|-----------------   |--------|--------|---------|
|BGE-m3              | 55.11% | 63.43% | 72.18%  |
|E5                  | 54.61% | 63.53% | 72.02%  |
|Elasticsearch       | 42.54% | 49.61% | 56.85%  |
|Ensemble            | 68.38% | 74.85% | 80.66%  |
|Ensemble + rerank   | 79.82% | 82,82% | 87.66%  |

**Correctness**



# DEMO       