# mostApRegister

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostApRegister(long fblockID, long instIDDefault); // form 1
long mostApRegister(); // form 2
```

## Description

The first function registers the CAPL node at the Application Socket as a function block with the specified FBlockID and InstIDDefault. The function is available in the CAPL section on preStart and can be applied once per CAPL node only.

The second function re-registers a previously de-registered CAPL node.

Both functions make an entry in the device's Local FBlockList. If an FBlock with the same FBlockID and InstID has already been registered by another CAPL node the InstID of the function block to be registered is incremented until the combination {FBlockID, InstID} is unique within the simulated device.

As a result of the call of mostApRegister(), if the network status is 'ConfigOk' the device's NetBlock reports the new Local FBlockList to the NetworkMaster.

## Parameters

| Name | Description |
|---|---|
| fblockID | Function block identifier to be registered. |
| instdIDDefault | Default instance identifier. The actual registered InstID can be retrieved with mostApGetInstID(). |

## Return Values

See error codes

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.0 | — | — | — | —✔ |
| Restricted To | — | MOST25 MOST50 MOST150 While Application Socket is active | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | — | ✔ | — | N/A | — | —✔ |
| 64-Bit | — | ✔ | — | — | — | —✔ |
