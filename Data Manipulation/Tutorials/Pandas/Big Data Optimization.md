# Advanced Pandas: Big Data Optimization
## Introduction
#### When working on Data Science or Data Analytics projects, you may be working with very large datasets (think one million rows+). Although these datasets provide a lot of value, they make it very difficult for your CPU to process the information in a reasonable amount of time. The main issue with working with large datasets is the presence of the _OutOfMemory_ Error. How do we solve this problem? Let's dive into the topic of _Parallel Processing_.
## What is Parallel Processing?
#### The main limitation associated with Pandas is its relationship with Memory. _Memory_ is the amount of computing resources being used by your local machine's CPU for a given task. When working with massive datasets, your CPU may run out of memory and throw an _OutOfMemory_ Error. To help relieve this problem, Python offers solutions that allow you to execute _Parallel Processing_ is the concept of running multiple tasks simultaneously while dividing the tasks among your CPUs various workers. 
#### Because Pandas is such as widely used library, various developers have created sister libraries that can work in conjunction with Pandas while allowing parallel processing. Some of the more popular libraries include: PySpark, Pandarallel, Terality, and Dask. For the purposes of this tutorial, we will be comparing Pandas and PySpark.
## Introduction to Spark and PySpark
### What is Apache Spark?
#### **_Apache Spark_** is a distributed clustering framework based on the Hadoop MapReduce deployment model. The purpose of Spark is to speed up big data analytics and provide developers with a comprehensive GUI to deal with large datasets effectively. Spark initially collects all your data into a **_cluster_** and then divides that cluster into **_partitions_** to distribute the workload among different workers. Spark is popular due to its comprehensive use cases related to batch processing tasks, interactive querying features, and real-time stream processing frameworks. 
### What is PySpark?
#### **_PySpark_** is a Python API that connects to your locally installed Spark cluster. This library has a lot of similarties with Pandas in that it enables uses to interact with, query, and transform DataFrames of any size. Spark is built using a Java-based language known as Scala, therefore PySpark's syntax is a bit different than Pandas, though if you know Pandas, PySpark is an easy transition.
## Getting Started with PySpark
### <ins>Installing Spark on Windows</ins>
#### To install Apache Spark on your Windows device, complete the following steps:
##### 1. Download [Anaconda Navigator](https://www.anaconda.com/products/distribution)
##### 2. Launch the "Powershell Prompt" Terminal from Anaconda Navigator
##### 3. In the Terminal, enter the following code:
    conda create --name spark_env python=3.9 -y
    conda activate spark_env
##### 4. Once your Environment is activated, enter the following code:
    conda install -c conda-forge numpy pandas jupyter jupyterlab
    pip install pyspark
##### 5. 
