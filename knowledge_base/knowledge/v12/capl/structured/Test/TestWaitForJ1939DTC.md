# TestWaitForJ1939DTC

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForJ1939DTC (dword sourceAddress, Message message, dword spn, dword timeout); // form 1
```

## Description

The function waits until a defined Parameter Group and a defined Diagnostic Trouble Code (DTC) is received or a timeout occurred.

The affected message (specified by the Parameter Group number pgn or the database object message) must be able to contain a DTC, so only this parameter groups are allowed: DM1, DM2, DM4, DM6, DM12, DM23, DM24, DM27, DM28, DM31, DM35 and DM41-DM54.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Example

```c
long result;

// waits for the occurrence of DTC with SPN=96 and FMI=12 within message DM1 (pgn=0xFECA) from node with address=0x2
result = TestWaitForJ1939DTC(0x2, 0xFECA, 96, 12, 0xFFFF, 2000);

// waits for the occurrence of DTC with SPN=98765 and OC=1 within message DM2 (pgn=0xFECB) from node with address=0x3
result = TestWaitForJ1939DTC(0x3, 0xFECB, 98765, 0xFFFF, 1, 2000);

// waits for the occurrence of DTC with OC=10 within message DM35 (pgn=0x9F00) from any node
result = TestWaitForJ1939DTC(0xFFFFFFFF, 0x9F00, 0xFFFFFFFF, 0xFFFF, 10, 2000);
```

## Availability

| Since Version |
|---|
