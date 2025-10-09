from pyspark.sql.streaming import StreamingQueryListener

"""
Example of event info:
{
  "id" : "619d4bfc-3a04-4860-863b-7c72200d97f1",
  "runId" : "d9781792-1fa6-4486-879e-b7c42af97864",
  "name" : null,
  "timestamp" : "2025-10-09T18:11:15.003Z",
  "batchId" : 1,
  "batchDuration" : 1454,
  "numInputRows" : 1,
  "inputRowsPerSecond" : 0.33311125916055967,
  "processedRowsPerSecond" : 0.687757909215956,
  "durationMs" : {
    "addBatch" : 1380,
    "commitOffsets" : 13,
    "getBatch" : 0,
    "latestOffset" : 11,
    "queryPlanning" : 12,
    "triggerExecution" : 1453,
    "walCommit" : 33
  },
  "stateOperators" : [ ],
  "sources" : [ {
    "description" : "KafkaV2[Subscribe[kafka-spark-example]]",
    "startOffset" : {
      "kafka-spark-example" : {
        "0" : 35
      }
    },
    "endOffset" : {
      "kafka-spark-example" : {
        "0" : 36
      }
    },
    "latestOffset" : {
      "kafka-spark-example" : {
        "0" : 36
      }
    },
    "numInputRows" : 1,
    "inputRowsPerSecond" : 0.33311125916055967,
    "processedRowsPerSecond" : 0.687757909215956,
    "metrics" : {
      "avgOffsetsBehindLatest" : "0.0",
      "maxOffsetsBehindLatest" : "0",
      "minOffsetsBehindLatest" : "0"
    }
  } ],
  "sink" : {
    "description" : "org.apache.spark.sql.execution.streaming.ConsoleTable$@42e4ee9a",
    "numOutputRows" : 1
  }
}
"""

class MyListener(StreamingQueryListener):
    def onQueryStarted(self, event):
        print(f"Query started: {event.id}")

    def onQueryProgress(self, event):
        print(f"Query made progress: {event.progress}")

    def onQueryTerminated(self, event):
        print(f"Query terminated: {event.id}")