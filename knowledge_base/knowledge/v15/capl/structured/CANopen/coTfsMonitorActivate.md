# coTfsMonitorActivate

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsMonitorActivate( void );
```

## Description

This function activates the passive communication monitor and resets the statistics. Furthermore the active nodes are written to the test report.

You can stop the monitoring with coTfsMonitorDeactivate. To include node-IDs or ranges of node-IDs for monitoring you can use the functions coTfsMonitorIncludeNodeId and coTfsMonitorIncludeNodeIdRange. For exclusion you can use coTfsMonitorExcludeNodeId and coTfsMonitorExcludeNodeIdRange. With coTfsMonitorSetNmtTimeout and coTfsMonitorSetSdoTimeout you can set NMT and SDO timeouts.

## Return Values

Error code

## Example

```c
// configure node-IDs for monitoring: monitor nodes 1..14, 21..24, 26..64 and 127
coTfsMonitorIncludeNodeIdRange(1, 64);
coTfsMonitorExcludeNodeIdRange(15, 20);
coTfsMonitorExcludeNodeId(25);
coTfsMonitorIncludeNodeId(127);

coTfsMonitorSetSdoTimeout(100); // set SDO timeout to 100 ms
coTfsMonitorSetNmtTimeout(2000); // set NMT timeout for boot-up message to 2 s

coTfsMonitorActivate(); // activate monitoring
TestWaitForTimeout(30000); // monitor CANopen traffic for 60 seconds ...
if (coTfsMonitorDeactivate() != 1) { // deactivate monitoring and add results to report, check for errors
  TestStepFail("Monitoring", "At least one monitored response was not received in time");
}
else {
  TestStepPass("Monitoring", "All monitored responses were received in time");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.2 | 13.0 | — | — | 2.1 SP3 |
| Restricted To | — | CANopen | CANopen | — | — | CANopen |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
