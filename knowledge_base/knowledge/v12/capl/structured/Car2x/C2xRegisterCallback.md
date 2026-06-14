# C2xRegisterCallback

> Category: `Car2x` | Type: `function`

## Syntax

```c
long C2xRegisterCallback(long callbackType, char* callbackFunction);
```

## Description

Register a callback function.

The callback can be registered for all or for a specific message. If the dbMessage parameter is present, the function can be called earliest in the On Start event handler. With multiple calls of this function it is possible to register several callback functions for the same message or to register the same callback function for several messages.

## Return Values

0 or error code

## Availability

| Since Version |
|---|
