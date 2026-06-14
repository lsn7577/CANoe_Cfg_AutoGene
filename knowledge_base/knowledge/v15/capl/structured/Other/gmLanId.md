# gmLanId

> Category: `Other` | Type: `function`

## Syntax

```c
dword gmLanId (dbMsg aMessage, dword aSourceId); // form 1
dword gmLanId (dbMsg aMessage, Node aTxNode); // form 2
```

## Description

This function can be used to create a message ID for a GMLAN message. In addition to the message, you must specify the transmission node or its source ID.

The message ID returned can be used, for example, to wait for a specific GMLAN message with the TestWaitForMessage function.

## Parameters

| Name | Description |
|---|---|
| aMessage | GMLAN message for which a message ID is to be created. |
| aSourceId | Source ID of the node to be coded as the transmission node in the message ID. |
| aTxNode | Node to be coded as the transmission node in the message ID. |

## Return Values

If the message is a GMLAN message, a GMLAN message ID will be returned containing the correct source address and priority. Otherwise, the message ID will be returned.

## Example

```c
dword gmID = 0;
long result = 0;
gmID = gmLanId(Comfort::Console_1, 48);
waitResult = TestWaitForMessage(gmID, 5000);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 6.1 | 6.1 | 13.0 | — | — | 1.0 |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
