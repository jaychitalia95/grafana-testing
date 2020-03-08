from grafanalib.core import *

dashboard = Dashboard(
    title = "Table column style test",
    templating = Templating(list([
            {
                "allValue": "null",
                "current": {
                    "text": "node_exporter_metrics",
                    "value": "node_exporter_metrics"
                },
                "datasource": "Prometheus",
                "definition": "label_values(node_uname_info, job)",
                "hide": 0,
                "includeAll": False,
                "label": "JOB",
                "multi": False,
                "name": "job",
                "options": [],
                "query": "label_values(node_uname_info, job)",
                "refresh": 1,
                "regex": "",
                "skipUrlSync": False,
                "sort": 1,
                "tagValuesQuery": "",
                "tags": [],
                "tagsQuery": "",
                "type": "query",
                "useTags": False
            },
            {
                "allValue": "null",
                "current": {
                    "selected": False,
                    "text": "All",
                    "value": "$__all"
                },
                "datasource": "Prometheus",
                "definition": "label_values(node_uname_info{job=~\"$job\"}, nodename)",
                "hide": 0,
                "includeAll": True,
                "label": "Host",
                "multi": True,
                "name": "hostname",
                "options": [],
                "query": "label_values(node_uname_info{job=~\"$job\"}, nodename)",
                "refresh": 1,
                "regex": "",
                "skipUrlSync": False,
                "sort": 0,
                "tagValuesQuery": "",
                "tags": [],
                "tagsQuery": "",
                "type": "query",
                "useTags": False
            },
            {
                "allFormat": "glob",
                "allValue": "null",
                "current": {
                    "selected": False,
                    "text": "All",
                    "value": "$__all"
                },
                "datasource": "Prometheus",
                "definition": "label_values(node_uname_info{nodename=~\"$hostname\"},instance)",
                "hide": 0,
                "includeAll": True,
                "label": "IP",
                "multi": False,
                "multiFormat": "regex values",
                "name": "node",
                "options": [],
                "query": "label_values(node_uname_info{nodename=~\"$hostname\"},instance)",
                "refresh": 2,
                "regex": "",
                "skipUrlSync": False,
                "sort": 1,
                "tagValuesQuery": "",
                "tags": [],
                "tagsQuery": "",
                "type": "query",
                "useTags": False
            },
            {
                "allValue": "null",
                "current": {
                    "text": "/",
                    "value": "/"
                },
                "datasource": "Prometheus",
                "definition": "",
                "hide": 2,
                "includeAll": False,
                "label": "",
                "multi": False,
                "name": "maxmount",
                "options": [],
                "query": "query_result(topk(1,sort_desc (max(node_filesystem_size_bytes{instance=~'$node',fstype=~\"ext4|xfs\"}) by (mountpoint))))",
                "refresh": 2,
                "regex": "/.*\\\"(.*)\\\".*/",
                "skipUrlSync": False,
                "sort": 0,
                "tagValuesQuery": "",
                "tags": [],
                "tagsQuery": "",
                "type": "query",
                "useTags": False
            },
            {
                "allFormat": "glob",
                "allValue": "null",
                "current": {
                    "isNone": True,
                    "selected": False,
                    "text": "None",
                    "value": ""
                },
                "datasource": "Prometheus",
                "definition": "",
                "hide": 2,
                "includeAll": False,
                "label": "环境",
                "multi": False,
                "multiFormat": "regex values",
                "name": "env",
                "options": [],
                "query": "label_values(node_exporter_build_info,env)",
                "refresh": 2,
                "regex": "",
                "skipUrlSync": False,
                "sort": 1,
                "tagValuesQuery": "",
                "tags": [],
                "tagsQuery": "",
                "type": "query",
                "useTags": False
            },
            {
                "allFormat": "glob",
                "allValue": "",
                "current": {
                    "isNone": True,
                    "selected": False,
                    "text": "None",
                    "value": ""
                },
                "datasource": "Prometheus",
                "definition": "label_values(node_exporter_build_info{env=~'$env'},name)",
                "hide": 2,
                "includeAll": False,
                "label": "名称",
                "multi": True,
                "multiFormat": "regex values",
                "name": "name",
                "options": [],
                "query": "label_values(node_exporter_build_info{env=~'$env'},name)",
                "refresh": 2,
                "regex": "",
                "skipUrlSync": False,
                "sort": 1,
                "tagValuesQuery": "/.*/",
                "tags": [],
                "tagsQuery": "",
                "type": "query",
                "useTags": False
            }
    ])),
    rows = [
        Row(
            panels = [
                Table(
                    dataSource = "Prometheus",
                    targets = [
                        Target(
                            expr = "node_filesystem_size_bytes{instance=~'$node',fstype=~\"ext4|xfs\"}-0",
                            format = "table",
                            instant = True,
                            intervalFactor = 1,
                            refId = "A"
                        ),
                        Target(
                            expr = "node_filesystem_avail_bytes {instance=~'$node',fstype=~\"ext4|xfs\"}-0",
                            format = "table",
                            instant = True,
                            interval = "10s",
                            intervalFactor = 1,
                            refId = "B"
                        ),
                        Target(
                            expr = "1-(node_filesystem_free_bytes{instance=~'$node',fstype=~\"ext4|xfs\"} / node_filesystem_size_bytes{instance=~'$node',fstype=~\"ext4|xfs\"})",
                            format = "table",
                            instant = True,
                            intervalFactor = 1,
                            refId = "C"
                        ),
                    ],
                    title = "Disk Space Used Basic(EXT4/XFS)",
                    styles = [
                        ColumnStyle(
                            alias = "Mounted on",
                            align = "center",
                            link = True,
                            linkOpenInNewTab = True,
                            linkUrl = "test",
                            linkTooltip = "test tooltip",
                            pattern = "mountpoint",
                            type = StringColumnStyleType(
                                colorMode = "cell",
                                thresholds = list([
                                    "50","80"
                                ]),
                                unit = "bytes",
                                mappingType = MAPPING_TYPE_RANGE_TO_TEXT,
                                rangeMaps = list([
                                    TableRangeMaps(
                                    fr = 2,
                                    to = 10,
                                    text = "testr"
                                )])
                            )
                        )
                    ]
                )
            ]
        )]
    ).auto_panel_ids()