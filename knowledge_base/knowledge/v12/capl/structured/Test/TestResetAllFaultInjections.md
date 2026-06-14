# TestResetAllFaultInjections

> Category: `Test` | Type: `function`

## Syntax

```c
long TestResetAllFaultInjections (dbNode aNode);
```

## Description

Reset all fault injections setting of a node.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: No error.

## Example

```c
// set some FaultInjections and reset them all
TestDisableMsg(MsgToManipulate1);
TestSetMsgCycleTime(MsgToManipulate2, 200);

TestWaitForTimeout(2000)

TestResetAllFaultInjections(NodeToManipulate);
```

## Availability

| Since Version |
|---|
