# mostApUnregisterEx

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostApUnregisterEx(long fblockID, long instID)
```

## Description

Removes the function block with functional address {fblockID, instID} from the Local FBlockList. It should be noted that CAPL nodes may only remove those function blocks you have previously registered with mostApRegisterEx.

In network status 'ConfigOk' the device's NetBlock reports the new Local FBlockList to the NetworkMaster.

## Return Values

See error codes

## Availability

| Since Version |
|---|
