# ChkCreate_UndefinedMessageReceived, ChkStart_UndefinedMessageReceived

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_UndefinedMessageReceived (char [] CaplCallback); // form 1
dword ChkStart_UndefinedMessageReceived (char [] CaplCallback); // form 2
```

## Description

Observes the current bus and reports messages that are not defined.

If the CANoe configuration contains multiple buses, the current bus context has to be specified (SetBusContext) before the check configuration.

For FlexRay either only valid data frames or PDUs (according to the database type) are recognized as communication. Null Frames and Erroneous frames are ignored.

## Parameters

| Name | Description |
|---|---|
| CaplCallback | In simulation nodes this parameter has to be set.In test modules this parameter is optional. |

## Example

```c
// observes the bus ‘CAN1’ for undefined messages
SetBusContext(getBusNameContext("CAN1"));
checkId = ChkStart_UndefinedMessageReceived();
TestAddCondition(checkId);
// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
checkId = ChkCreate_UndefinedMessageReceived("CallbackUnknownMsg");
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 5.1 7.0 SP5: method 7.2: form 2 | 13.0 | — | 14 | 1.0 |
| Restricted To | — | CAN FlexRay | CAN FlexRay | — | CAN FlexRay | CAN FlexRay |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | ✔ | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | ✔ | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | ✔ | N/A |
| 64-Bit | — | ✔ | ✔ | — | ✔ | N/A |
