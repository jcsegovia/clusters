Quick Start
===========

1. Copy source directory to destination one

.. code-block:: bash

    python clone_directory.py <src_dir> <dst_dir> <run_dir_name>

    E.g. (warm start, using already sampled files without classification)
    python clone_directory.py data_step_2_withtout_classify ../clusters_run test_1


2. Change directory to the run one

.. code-block:: bash

    cd <dst_dir>

    E.g.
    cd ../clusters_run


3. Update run properties if required

Edit each configuration properties file:

E.g.

.. code-block:: bash

    vi ./test1/AA_618_A59/config.properties
    vi ./test1/AA_635_A45/config.properties
    vi ./test1/AA_661_A118/config.properties


4. Run everything (all algorithms, all clusters)

E.g.

.. code-block:: bash

    python launcher.py ./test_1

Main Results are available at (click on the HTML file for a summary):

.. code-block:: bash

    ./main_metrics_reports/main_metrics_reports_<DdateTime>

Detailed results are available at (click on the HTML file for a summary):

.. code-block:: bash

    ./test1/AA_618_A59/output/report_<DateTime>
    ./test1/AA_635_A45/output/report_<DateTime>
    ./test1/AA_661_A118/output/report_<DateTime>


Other runs
==========

To run all default clusters for all algorithms (**preferred way**):

.. code-block:: bash

    python launcher.py <dir>

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

    python clone_directory.py data_clean_all <dst_dir> <run_dir_name>

    E.g.
    python clone_directory.py data_clean_all ./clusters_work test_1

Destination directories will be created


2. copy properties

.. code-block:: bash

    python copy_properties.py <dst_dir>

    E.g.
    python copy_properties.py ../clusters_work/test_1

Copy properties from ``properties_base`` into ``../clusters_work/test_1``

Update properties if required (properties can be passed by command line too)



3. Transform source data in common (preprocessing):

.. code-block:: bash

    cd <dst_dir>
    python main.py -dir=./test_1/AA_618_A59 -task=preproc
    python main.py -dir=./test_1/AA_635_A45 -task=preproc
    python main.py -dir=./test_1/AA_661_A118 -task=preproc


4. Inspect which clusters are available:

.. code-block:: bash

    cd <dst_dir>
    python main.py -dir=./test_1/AA_618_A59 -task=list
    python main.py -dir=./test_1/AA_635_A45 -task=list
    python main.py -dir=./test_1/AA_661_A118 -task=list


5. Load data, sampling & classify for the cluster(s) you are interested in:

.. code-block:: bash

    cd <dst_dir>
    python main.py -dir=./test_1/AA_618_A59 -task="load,sampling,classify" -cluster=UBC17_a -model=all
    python main.py -dir=./test_1/AA_618_A59 -task="load,sampling,classify" -cluster=UBC17_a -model=OPTICS


6. Once the data is already loaded and sampled you can avoid those steps:

.. code-block:: bash

    cd <dst_dir>
    python main.py -dir=./test_1/AA_618_A59 -task=classify -cluster=UBC17_a -model=all
    python main.py -dir=./test_1/AA_618_A59 -task=classify -cluster=UBC17_a -model=DBSCAN
    python main.py -dir=./test_1/AA_618_A59 -task=classify -cluster=UBC17_a -model=OPTICS -CLASSIFIER.OPTICS="min_cluster_size=0.5,xi=0.05"

7. To process default clusters (once the data and samples are already created):

(Using properties from files)

.. code-block:: bash

    cd <dst_dir>
    python launcher.py <run_dir>

    E.g.
    python launcher.py ./test_1


Directory structure and files
=============================

cluster directory
-----------------

* data_clean_all (directory containing Vizier archive data and the original works)

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

* data_step_0 (incremented version from previous one, with a ‘data.csv’ standard file)

  * AA_661_A118

    * config.properties
    * **data.csv**
    * source

      * <same as data_clean_all/AA_661_A118/source>

  * AA_618_A59

    * config.properties
    * **data.csv**
    * source

      * <same as data_clean_all/AA_618_A59/source>

  * AA_635_A45

    * config.properties
    * **data.csv**
    * source

      * <same as data_clean_all/AA_635_A45/source>

* data_step_1 (incremented version from the previous one, with data files from European Space Agency Gaia Archive)

  * AA_661_A118

    * config.properties
    * data.csv
    * source

      * <same as data_clean_all/AA_661_A118/source>

    * output

      * **<data files from ESA Gaia Archive>**

  * AA_618_A59

    * config.properties
    * data.csv
    * source

      * <same as data_clean_all/AA_618_A59/source>

    * output

      * **<data files from ESA Gaia Archive>**

  * AA_635_A45

    * config.properties
    * data.csv
    * source

      * **<same as data_clean_all/AA_635_A45/source>**

    * output

      * <data files from ESA Gaia Archive>

* data_step_2_without_classify (incremented version from the previous one, with sampling files)

  * AA_661_A118

    * config.properties
    * data.csv
    * source

      * <same as data_clean_all/AA_661_A118/source>

    * output

      * <data files from ESA Gaia Archive>
      * **<sampling files>**

  * AA_618_A59

    * config.properties
    * data.csv
    * source

      * <same as data_clean_all/AA_618_A59/source>

    * output

      * <data files from ESA Gaia Archive>
      * **<sampling files>**

  * AA_635_A45

    * config.properties
    * data.csv
    * source

      * <same as data_clean_all/AA_635_A45/source>

    * output

      * <data files from ESA Gaia Archive>
      * **<sampling files>**

* properties_base (basic properties)

  * AA_661_A118

    * config.properties

  * AA_618_A59

    * config.properties

  * AA_635_A45

    * config.properties

* scripts

  * launcher.py (utility to process all clusters with all algorithms, generates metrics too)
  * main.py (main entry)
  * processor.py (executes required tasks, e.g., download data, sampling, run algorithms...)
  * utils.py (common utilities)

* README.rst (this file)

* clone_directory.py (copies all files from source directory to destination one)

* copy_properties.py (copies basic properties to the specified directory)

* copy_sampling.py (copies already sampling files to the specified directory)


working directory
-----------------

Each working directory is created by using ``clone_directory.py`` script.
You must specify destination directory as an argument, we name that directory as ``working_directory``
(in previous examples, we have used ``clusters_work``)

* working_dir

  * test_n

    * AA_661_A118

      * config.properties
      * data.csv
      * source

        * <same as data_clean_all/AA_661_A118/source>

      * output

        * <data files from ESA Gaia Archive>
        * <sampling files>
        * report_nnnn (run nnnn results)

          * <see content below>

    * AA_618_A59

      * config.properties
      * data.csv
      * source

        * <same as data_clean_all/AA_618_A59/source>

      * output

        * <data files from ESA Gaia Archive>
        * <sampling files>
        * report_nnnn (run nnnn results)

          * <see content below>

    * AA_635_A45

      * config.properties
      * data.csv
      * source

        * <same as data_clean_all/AA_635_A45/source>

      * output

        * <data files from ESA Gaia Archive>
        * <sampling files>
        * report_nnnn (run nnnn results)

          * <see content below>

Report directory
----------------

report_nnnn directory structure:

* report_nnnn (run nnnn results)

  * cluster_id.txt (cluster identifier)
  * hyper_params.txt (algorithms hyper parameters used)
  * main_metrics.csv (metrics in CSV)
  * main_metrics.html (metrics in HTML with hyperlinks)
  * main_metrics_plot.png (metrics images)
  * main_metrics_new_plot.png (new sources metrics images)
  * main_metrics_new_plus_plot.png (new in range sources metrics images)
  * main_report_nnnn (run nnnn log plain text file)
  * <cluster>_<algorithm>_xxxx (data directory per cluster and algorithm)

    * Report in HTML
    * Report in plain text
    * Images set


Main Metrics Reports
--------------------

After ``launcher.py`` is executed, a metrics summary is generated in a directory named ``main_metrics_report_<DateTime>``

main_metrics_report_<DateTime> directory structure

* main_metrics_report_<DateTime> (run <DateTime> metrics summary)

  * metrics_summary.html (HTML document with hyperlinks)
  * metrics_summary_<algorithm>_<type>.png (summary per algorithm and type)

