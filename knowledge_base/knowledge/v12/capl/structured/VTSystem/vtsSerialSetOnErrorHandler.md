# vtsSerialSetOnErrorHandler

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSerialSetOnErrorHandler (char Target[], char onErrorCallback[]);
```

## Description

Sets the callback that notifies when an error occurred during a send or receive operation.

The set callback has to have following signature: void <OnSerialError>( dword errorFlags)

## Return Values

0: Successful call

## Availability

| Since Version |
|---|
