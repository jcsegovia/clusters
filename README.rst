Warm Start
==========

1. copy already sampled data:

.. code-block:: bash

    python clone_directory.py 0_data_step_2_withtout_classify 0_run_1

``0_run_1`` directory will be created


2. copy properties

.. code-block:: bash

    python copy_properties.py 0_run_1

Copy properties from ``0_properties_base`` into ``0_run_1``

Update properties if required (properties can be passed by command line too)


3. run

To run all default clusters for all algorithms (**preferred way**):

.. code-block:: bash

    python launcher.py

To run specific cluster and algorithm

.. code-block:: bash

    python main.py -dir=./test_1/AA_618_A59 -task=classify -cluster=UBC17_a -model=OPTICS

To run specific clustar and all algorithms

.. code-block:: bash

    python main.py -dir=./test_1/AA_618_A59 -task=classify -cluster=UBC17_a -model=all

To pass specific properties for an algorithm:

.. code-block:: bash

    python main.py -dir=./test_1/AA_618_A59 -task=classify -cluster=UBC17_a -model=OPTICS -CLASSIFIER.OPTICS="min_cluster_size=0.5,xi=0.05"


Cold Start
==========

1. Copy work data (no samples, only source data)

.. code-block:: bash

    python clone_directory.py 0_data_clean_all 0_run_1

``0_run_1`` directory will be created


2. copy properties

.. code-block:: bash

    python copy_properties.py 0_run_1

Copy properties from ``0_properties_base`` into ``0_run_1``

Update properties if required (properties can be passed by command line too)



3. Transform source data in common (preprocessing):

.. code-block:: bash

    python main.py -dir=./test_1/AA_618_A59 -task=preproc
    python main.py -dir=./test_1/AA_635_A45 -task=preproc
    python main.py -dir=./test_1/AA_661_A118 -task=preproc


4. Inspect which clusters are available:

.. code-block:: bash

    python main.py -dir=./test_1/AA_618_A59 -task=list
    python main.py -dir=./test_1/AA_635_A45 -task=list
    python main.py -dir=./test_1/AA_661_A118 -task=list


5. Load data, sampling & classify for the cluster(s) you are interested in:

.. code-block:: bash

    python main.py -dir=./test_1/AA_618_A59 -task="load,sampling,classify" -cluster=UBC17_a -model=all
    python main.py -dir=./test_1/AA_618_A59 -task="load,sampling,classify" -cluster=UBC17_a -model=OPTICS


6. Once the data is already loaded and sampled you can avoid those steps:

.. code-block:: bash

    python main.py -dir=./test_1/AA_618_A59 -task=classify -cluster=UBC17_a -model=all
    python main.py -dir=./test_1/AA_618_A59 -task=classify -cluster=UBC17_a -model=DBSCAN
    python main.py -dir=./test_1/AA_618_A59 -task=classify -cluster=UBC17_a -model=OPTICS -CLASSIFIER.OPTICS="min_cluster_size=0.5,xi=0.05"

7. To process default clusters (once the data and samples are already created):

(Using properties from files)

.. code-block:: bash

    python launcher.py


Directory structure and files
=============================

* 0_data_clean_all (directory containing Vizier archive data and the original works)

  * AA_661_A118

    * config.properties
    * source

      * aa42568-21_ocfinder.pdf
      * ReadMe.txt
      * table1.dat
      * table2.dat

  * AA_618_A59

    * config.properties
    * source

      * aa33390-18.pdf
      * centers.dat
      * members.dat
      * ReadMe.txt

  * AA_635_A45

    * config.properties
    * source

      * aa37386-19.pdf
      * ReadMe.txt
      * table1.dat
      * table2.dat

* 0_data_step_0 (incremento respecto de la versión anterior, con el fichero de datos estándar ‘data.csv’)

  * AA_661_A118

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_661_A118/source>

  * AA_618_A59

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_618_A59/source>

  * AA_635_A45

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_635_A45/source>

* 0_data_step_1 (incremento respecto de la versión anterior con los ficheros de datos del archivo Gaia de la Agencia Espacial Europea)

  * AA_661_A118

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_661_A118/source>

    * output

      * <datos del archivo Gaia de la ESA>

  * AA_618_A59

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_618_A59/source>

    * output

      * <datos del archivo Gaia de la ESA>

  * AA_635_A45

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_635_A45/source>

    * output

      * <datos del archivo Gaia de la ESA>

* 0_data_step_2_without_classify (incremento respecto a la versión anterior con los ficheros de muestras)

  * AA_661_A118

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_661_A118/source>

    * output

      * <datos del archivo Gaia de la ESA>
      * <contiene los ficheros de muestras>

  * AA_618_A59

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_618_A59/source>

    * output

      * <datos del archivo Gaia de la ESA>
      * <contiene los ficheros de muestras>

  * AA_635_A45

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_635_A45/source>

    * output

      * <datos del archivo Gaia de la ESA>
      * <contiene los ficheros de muestras>

* 0_properties_base (contiene las propiedades básicas)

  * AA_661_A118

    * config.properties

  * AA_618_A59

    * config.properties

  * AA_635_A45

    * config.properties

* test_1 (directorio de resultados del primer test)

  * <ver estructura más abajo>

* test_2 (directorio de resultados del segundo test)

  * <ver estructura más abajo>

* test_3 (directorio de resultados del tercer test)

  * <ver estructura más abajo>

* clone_directory.py (realiza una copia de un directorio y sus contenidos a otro)

* copy_properties.py (copia las propiedades básicas al directorio especificado)

* copy_sampling.py (copi las muestras de un directorio a otro)

* launcher.py (utilidad para procesar todos los clústeres con todos los algoritmos)

* main.py (entrada principal)

* processor.py (ejecuta las tareas requeridas, por ejemplo, descargar datos, hacer muestreo, lanzar los algoritmos de clustering...)

* README.rst (fichero con explicaciones)

* utils.py (utilidades genéricas)


Cada directorio de test contiene la siguiente estructura:

* test_n

  * AA_661_A118

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_661_A118/source>

    * output

      * <datos del archivo Gaia de la ESA>
      * <contiene los ficheros de muestras>
      * report_nnnn (resultado de la ejecución nnnn)

        * <ver contenido más abajo>

  * AA_618_A59

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_618_A59/source>

    * output

      * <datos del archivo Gaia de la ESA>
      * <contiene los ficheros de muestras>
      * report_nnnn (resultado de la ejecución nnnn)

        * <ver contenido más abajo>

  * AA_635_A45

    * config.properties
    * data.csv
    * source

      * <igual que en 0_data_clean_all/AA_635_A45/source>

    * output

      * <datos del archivo Gaia de la ESA>
      * <contiene los ficheros de muestras>
      * report_nnnn (resultado de la ejecución nnnn)

        * <ver contenido más abajo>

Cada directorio report_nnnn contiene la siguiente estructura:

* report_nnnn (resultado de la ejecución nnnn)

  * main_metrics.csv (métricas en formato CSV)
  * main_metrics.html (métricas en formato HTML con hiperenlaces)
  * main_metrics_plot.png (métricas en imagen)
  * main_metrics_new_plot.png (métricas de nuevos elementos en imagen)
  * main_metrics_new_plus_plot.png (métricas de nuevos elementos en rango en imagen)
  * main_report_nnnn (fichero en texto plano con el resultado de la ejecución nnnn)
  * <cluster>_<algoritmo>_xxxx (directorio con los datos por cluster y algoritmo)

    * Informe en HTML
    * Informe en texto plano
    * Conjunto de imágenes






