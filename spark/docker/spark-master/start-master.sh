#!/bin/bash
set -x
export SPARK_MASTER_HOST=`hostname`

. "${SPARK_HOME}/sbin/spark-config.sh"

. "${SPARK_HOME}/bin/load-spark-env.sh"

mkdir -p $SPARK_MASTER_LOG

ln -sf /dev/stdout $SPARK_MASTER_LOG/spark-master.out

cd ${SPARK_HOME}/bin && ${SPARK_HOME}/sbin/../bin/spark-class org.apache.spark.deploy.master.Master -h $SPARK_MASTER_HOST -p $SPARK_MASTER_PORT --webui-port $SPARK_MASTER_WEBUI_PORT >> $SPARK_MASTER_LOG/spark-master.out
