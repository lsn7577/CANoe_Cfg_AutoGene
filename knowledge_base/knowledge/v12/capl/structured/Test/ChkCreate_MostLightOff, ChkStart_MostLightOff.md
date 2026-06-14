# ChkCreate_MostLightOff, ChkStart_MostLightOff

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_MostLightOff();
```

## Description

The check function monitors the occurrence of "LightOff" events.

A "LightOff" event occurs if the hardware connected to the channel no longer receives light at the input.

Consider to set always the appropriate bus context in a multibus environment before the function is called.

Further information on site MultiBus Environment.

## Return Values

0: Check could not be created and must not be referenced

## Availability

| Since Version |
|---|
