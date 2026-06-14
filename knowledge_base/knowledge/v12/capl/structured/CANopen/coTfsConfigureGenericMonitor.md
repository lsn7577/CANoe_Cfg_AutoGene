# coTfsConfigureGenericMonitor

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsConfigureGenericMonitor( dword canId, dword isRTR, dword dlc, dword msgData, qword msgMask, dword minOcc, dword maxOcc, char comment[], dword varContent );
```

## Description

This function configures and activates a generic message monitor. With the monitor you can check the occurrence count of a defined CAN message in the period between configuration and coTfsDeactivateGenericMonitor. The evaluation is done in the coTfsDeactivateGenericMonitor function.

Between the two functions any other test functions can be used.

The monitored message needn't sent and received cyclically, no time check is executed.

Each received message with the correct CAN-ID and DLC and that fits to the mask, is stored (independent of the given mask) and can be compared with compare data (in function coTfsCheckAndCompareGenericMonitorMessage) at runtime or after a coTfsDeactivateGenericMonitor command.

The user can specify a descriptive comment for the monitored message. This comment is written to the test report and provides a better overview.

## Return Values

Error code
