# ChkCreate_MostPropertyProtocolError, ChkStart_MostPropertyProtocolError

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostPropertyProtocolError(char[] aProperty, int aInstanceID, unsigned long aAnswerTimeout, Callback aCallback);
```

## Description

This check monitors MOST protocol compliance for a given property. This includes monitoring the response times along with the allowable message sequences.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: Check could not be created and must not be referenced

## Availability

| Since Version |
|---|
