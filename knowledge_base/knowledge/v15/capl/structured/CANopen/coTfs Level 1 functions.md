# coTfs Level 1 functions

> Category: `CANopen` | Type: `notes`

## Description

This section contains a brief listing of all Level 1 functions that are made available by the CANopen Test Feature Set node layer.

See Also

| Quick Access |  |  |
|---|---|---|
| Guarding | Heartbeat | NMT |
| SDO |  |  |

| Functions | Short Description |
|---|---|
| coTfsGuardingRequest | Sends an user-definable guarding request. |

| Functions | Short Description |
|---|---|
| coTfsHeartbeatProducerCheckIfActive | Returns the current status of the heartbeat producer of the selected node. If this is switched on, the time settings are checked (passive test). |

| Functions | Short Description |
|---|---|
| coTfsNMTRequest | NMT request |
| coTfsNmtGetCurrentState | Returns the current device state. |

| Functions | Short Description |
|---|---|
| coTfsSDOCalcCrc | Calculates the CRC Cyclic Redundancy Check checksum for a block transfer. |
| coTfsSDOGetBlockSize | Returns the block size that is used for a block transfer. |
| coTfsSDOBlockInit | Starts a SDO block up/download. |
| coTfsSDOBlockEnd | Stops a SDO block up/download. |
| coTfsSDOBlockDownloadSegmentRequest | Sends an individual segment of a SDO block download. |
| coTfsSDOBlockUploadSegmentResponse | Sends the response to a SDO upload block request. |
| coTfsSdoBlockUploadGetCRC | Gets the CRC checksum of last successful SDO block upload. |
| coTfsSDOSegmentRequest | Sends an individual data segment of a segmented SDO transfer. |
| coTfsSDOChkCrcSupport | Returns the CRC support flag of a SDO init block download response. |
| coTfsSDOInit | Starts an expedited/segmented SDO data transfer. |
| coTfsSDOGetUploadData | Returns the received SDO data of an expedited/segmented/block upload. |
| coTfsSDOGetUploadSize | Returns the size of the received SDO data of an expedited/segmented/block upload. |
| coTfsSDOAbort | Sends an individual SDO abort message. |
| coTfsSDOInjectRawMsg | Inserts a CAN message to the following command. |
| coTfsSDOInjectAbortMsg | Inserts a SDO abort message to the following command. |

| Version 15© Vector Informatik GmbH |
|---|
