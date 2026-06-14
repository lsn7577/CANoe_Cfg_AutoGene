# A664SetStringSignal

> Category: `ADFX` | Type: `function`

## Syntax

```c
long A664SetStringSignal (dbSignal aSignal, char val[]) (1)
long A664SetStringSignal (dbSignal aSignal, char val[], a664Message aMessage) (2)
```

## Description

This function can be used to set a string-signal within a specific a664Message (form 2) or to set the Tx-signal of the CANoe-subsystem (form 1).

For AFDX the usual string format contains the string length information at the first 2 bytes of the signal position, so the usual string operations won’t work correct on string signal.

## Parameters

| Name | Description |
|---|---|
| dbSignal | The signal. |
| val | The string to be used. |
| aMessage | The message object where the signal value should be set for variant 2. |

## Example

```c
a664Message TESTMSG_ALLTYPES testMsg = { msgChannel = 1};
a664SetStringSignal(TEST_STRING14_CITY, "STR126"); // set signal value on signalServer
a664InitPayload (testMsg); 	// set payload to last known signal values
a664TriggerMessage(testMsg, 1);
a664Message TESTMSG_ALLTYPES testMsg = { msgChannel = 1};
testMsg.VFG_OIL_TEMP_AB_32 = 86;
a664SetStringSignal(TEST_STRING14_CITY, "STR126", testMsg);
a664TriggerMessage(testMsg, 1);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 9.0 SP4 | 9.0 SP4 | — | — | — | — |
| Restricted To | AFDX | AFDX | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | N/A |
| 32-Bit | ✔ | ✔ | — | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | — | — | — | N/A |
