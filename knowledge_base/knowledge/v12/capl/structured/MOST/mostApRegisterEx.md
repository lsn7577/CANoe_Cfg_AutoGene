# mostApRegisterEx

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostApRegisterEx(long fblockID, long instID)
```

## Description

mostApRegisterEx() registers the function block with the Application Socket using the functional address (fblockID, instID).

It has to be checked in advance, if the functional address already exists (mostApIsRegisteredEx). If so, another instID has to be selected.

In network status 'ConfigOk' the device's NetBlock reports the new Local FBlockList to the NetworkMaster.

## Return Values

See error codes

## Availability

| Since Version |
|---|
