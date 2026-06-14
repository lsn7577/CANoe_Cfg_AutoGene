# Event Types

> Category: `Obsolete` | Type: `notes`

## Description

See Also

| Event Type | Description |
|---|---|
| 0 | The node simulated via the node layer has completed its initialization. It if is a configuration manager, then the other nodes on the network are configured now. This event signals the beginning of this process. |
| 1 | The simulated node is initialized and was able to send its boot-up message. Now it waits for the release by the application (Bit 2 in 1F80 set) in order to become operational. The application triggers this release via the function call coAllowStart. |
| 2 | The configuration of all nodes that must be present on the network (mandatory) is completed. |
| 3 | The configuration of an individual node via SDO was completed successfully. The node-ID of the corresponding node is transmitted via the parameter nodeId. If the node-ID has the value 0, then the last node assigned to the configuration manager was configured successfully. |
| 4 | The simulated node is initialized and was able to send its boot-up message. This event is only signaled if the node is configured as NMT master (Bit 0 in 1F80 set). In this state, the functions coDownload, coDownloadExpedited, and coUpload are used, for example to update the operating software of other nodes before the boot slave process after /4/ is started. If this state should be left and the start procedure continued, then the function coAllowStart must be used. |
| 5 | Another output level than the default was specified. |
| 6 | A node that must be present on the network (mandatory) generated an error during the node monitoring (Bit 4 and Bit 0 in 1F80 set, Bit 6 not set). The simulated node has already sent a NMT Reset all Nodes command. According to /4/ the simulated node should also execute a reset. Through this event, the application should be given the control to execute a NMT Reset of the simulated node. |
| 7 | A node that must be present on the network (mandatory) generated an error during the node monitoring (Bit 6 and Bit 0 in 1F80 set). The simulated node has already sent a NMT Stop all Nodes command. According to /4/ the simulated node should also change to the state stopped. Through this event, the application should be given the control to execute the state change of the simulated node. |

| Version 15© Vector Informatik GmbH |
|---|
