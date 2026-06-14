# TestSetSendTimeout

> Category: `Test` | Type: `function`

## Syntax

```c
void TestSetSendTimeout (long aTimeout);
```

## Description

This function sets the timeout up to which the TestSendMostAMSMessage functions wait for a Tx acknowledgment for the sent message. This value is set to 5000 ms by default.

With the specification of a timeout value of 0, a wait of any length for the Tx acknowledgment is possible, while the specification of -1 means that the waiting for the acknowledgment is switched off, that is, there is no wait.

## Parameters

| Name | Description |
|---|---|
| aTimeout | Maximum time that should be waited [ms] |

## Return Values

—

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
