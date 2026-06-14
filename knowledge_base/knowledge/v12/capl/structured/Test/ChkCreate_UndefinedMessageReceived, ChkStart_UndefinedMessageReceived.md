# ChkCreate_UndefinedMessageReceived, ChkStart_UndefinedMessageReceived

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_UndefinedMessageReceived (char [] CaplCallback); // form 1
```

## Description

Observes the current bus and reports messages that are not defined.

If the CANoe configuration contains multiple buses, the current bus context has to be specified (SetBusContext) before the check configuration.

For FlexRay either only valid data frames or PDUs (according to the database type) are recognized as communication. Null Frames and Erroneous frames are ignored.

For a FlexRay PDU database this check also ignores all received frames! For a PDU database only PDUs are considered. For a FlexRay PDU database this test makes no sense, because only those PDUs, which are defined in the database, can be retrieved from frames. There cannot exist PDUs that are not defined in the database! Therefore, for a PDU database this check will always pass.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

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

| Since Version |
|---|
