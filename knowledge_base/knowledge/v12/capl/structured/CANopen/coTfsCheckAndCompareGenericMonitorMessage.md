# coTfsCheckAndCompareGenericMonitorMessage

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsCheckAndCompareGenericMonitorMessage( dword canId, dword dlc, qword msgData, qword msgMask, dword order );
```

## Description

This function checks if the expected message data are received.

After monitoring is started with coTfsConfigureGenericMonitor the received messages can be checked with this function. The parameter order defines to which message the comparison is executed. The check is successfully passed if the message with the expected message number and the expected data is received.

The function can be used during a monitoring started with coTfsConfigureGenericMonitor as well as after coTfsDeactivateGenericMonitor. The internal list of received messages is reset not before the monitoring is restarted with coTfsConfigureGenericMonitor.

## Return Values

Error code
