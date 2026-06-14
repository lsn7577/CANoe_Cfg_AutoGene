# ChkCreate_J1939BAM, ChkStart_J1939BAM

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_J1939BAM(dword min, dword max, char[] callback1);
```

## Description

Observes the BAM transport protocol. It is possible to observe all BAM transmissions or only the transmission of a specific originator node.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
// checks the BAM transport protocol of node N1
checkId = ChkStart_J1939BAM(N1, 100, 200);
TestAddCondition(checkId);

// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
