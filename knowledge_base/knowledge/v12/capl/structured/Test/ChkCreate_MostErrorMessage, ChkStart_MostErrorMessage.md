# ChkCreate_MostErrorMessage, ChkStart_MostErrorMessage

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostErrorMessage(dword aSourceDeviceAddress, char[] aName, dword aInstanceId, dword aErrorCode, Callback aCallback);
```

## Description

This check can be used to monitor the occurrence of MOST error messages (OpType 0xF or 0x9).

The check can be implemented for a MOST device address, function block or function. In addition, monitoring can be limited to error messages with a specific error code.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: Check was not created and may not be referenced.

## Availability

| Since Version |
|---|
