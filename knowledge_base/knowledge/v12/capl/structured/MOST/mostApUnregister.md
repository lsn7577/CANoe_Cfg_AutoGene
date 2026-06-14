# mostApUnregister

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostApUnregister()
```

## Description

mostApUnregister() removes the function block assigned to the CAPL node by CANdb or mostApRegister(fblockID, instIDDefault) from the Local FBlockList.

In network status 'ConfigOk' the device's NetBlock reports the new Local FBlockList to the NetworkMaster.

## Return Values

See error codes

## Availability

| Since Version |
|---|
