# mostAsShdEnable, mostAsShdDisable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAsShdEnable(long fblockId, long instId)
```

## Description

mostAsShdEnable() adds an entry to the list of searched function blocks. If certain network events occur, CANoe automatically sends a request to the NetworkMaster to determine the logical device address of the function block.

Registration with mostAsShdEnable(fblockId, 0xFF) causes the service to request the device addresses of all function blocks with the appropriate FBlockId at the NetworkMaster.

mostAsShdDisable() removes an entry from the list of searched function blocks.

## Return Values

See error codes

## Availability

| Since Version |
|---|
