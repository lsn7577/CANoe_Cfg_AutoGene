# getMessageAttrInt

> Category: `CAN` | Type: `function`

## Syntax

```c
long GetMessageAttrInt(message canMessage, char attributeName[]);
long GetMessageAttrInt(pg parameterGroup, char attributeName[]);
```

## Description

Gets the value of a message attribute from the database.

A user-defined attribute with the name specified in the parameter, and of the Integer type, must be defined in the database. If no such attribute is defined, the function returns 0. If no attribute value is assigned to the message in the database, the default value of the attribute definition is returned.

## Parameters

| Name | Description |
|---|---|
| canMessage | Message variable |
| attributeName | Attribute name |

## Return Values

Value of the attribute (or default value) from the database.

## Example

This example outputs the value of the message attribute GenMsgCycleTime in the Write Window when the message is received.

The attribute name must be written as defined in the database. You can find the attribute name in the attribute window of the database.

```c
on message *
{
long cycleTimeValue1;
long cycleTimeValue2;
cycleTimeValue1 = getMessageAttrInt(this, "GenMsgCycleTime");
write("CycleTime of message id %x = %d", this.id, cycleTimeValue1);
message EngineData gMsgEngineData;
cycleTimeValue2 = getMessageAttrInt(gMsgEngineData, "GenMsgCycleTime");
write("CycleTime of message id %x = %d", this.id, cycleTimeValue2);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.1 | 3.1 | 13.0 | — | — | 1.0 |
| Restricted To | CAN | CAN | CAN | — | — | CAN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
