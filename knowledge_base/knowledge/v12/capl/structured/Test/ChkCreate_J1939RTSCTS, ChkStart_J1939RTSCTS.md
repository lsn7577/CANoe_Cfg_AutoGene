# ChkCreate_J1939RTSCTS, ChkStart_J1939RTSCTS

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_J1939RTSCTS(dword t1, dword t2, dword t3, dword t4, char[] callback1);
```

## Description

Observes the RTS/CTS transport protocol. It is possible to observe all RTS/CTS transmissions or only the transmission of a specific send node.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks the RTS/CTS transport protocol between node N1 and node N2
checkId = ChkStart_J1939RTSCTS(N1, N2, 750, 1250, 1250, 1050);
TestAddCondition(checkId);

// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
