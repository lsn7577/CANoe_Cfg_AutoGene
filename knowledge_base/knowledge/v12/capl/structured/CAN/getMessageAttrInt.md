# getMessageAttrInt

> Category: `CAN` | Type: `function`

## Syntax

```c
long GetMessageAttrInt(message canMessage, char attributeName[]);
```

## Description

Gets the value of a message attribute from the database.

A user-defined attribute with the name specified in the parameter, and of the Integer type, must be defined in the database. If no such attribute is defined, the function returns 0. If no attribute value is assigned to the message in the database, the default value of the attribute definition is returned.

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

| Since Version |
|---|
