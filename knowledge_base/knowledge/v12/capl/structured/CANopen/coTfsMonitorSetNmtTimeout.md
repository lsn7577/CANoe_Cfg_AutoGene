# coTfsMonitorSetNmtTimeout

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsMonitorSetNmtTimeout( dword nmtTimeoutInMs );
```

## Description

This function sets the NMT timeout for the passive communication monitor.

You can start the monitoring with coTfsMonitorActivate and stop it with coTfsMonitorDeactivate.

To include node-IDs or ranges of node-IDs for monitoring you can use the functions coTfsMonitorIncludeNodeId and coTfsMonitorIncludeNodeIdRange. For exclusion you can use coTfsMonitorExcludeNodeId and coTfsMonitorExcludeNodeIdRange.

## Return Values

Error code

## Example

```c
// configure node-IDs for monitoring: monitor nodes 1..14, 21..24, 26..64 and 127
coTfsMonitorIncludeNodeIdRange( 1, 64);
coTfsMonitorExcludeNodeIdRange( 15, 20);
coTfsMonitorExcludeNodeId   ( 25);
coTfsMonitorIncludeNodeId   (127);

coTfsMonitorSetSdoTimeout( 100 ); // set SDO timeout to 100 ms
coTfsMonitorSetNmtTimeout( 2000 ); // set NMT timeout for boot-up message to 2 s

coTfsMonitorActivate();      // activate monitoring
TestWaitForTimeout(30000);     // monitor CANopen traffic for 60 seconds ...
if (coTfsMonitorDeactivate() != 1) { // deactivate monitoring and add results to report, check for errors
  TestStepFail("Monitoring", "At least one monitored response was not received in time");
}
else {
  TestStepPass("Monitoring","All monitored responses were received in time");
}
```
