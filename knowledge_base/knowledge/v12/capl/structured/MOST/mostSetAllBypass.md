# mostSetAllBypass

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostSetAllBypass(long channel, long bypassmode)
```

## Description

This command can be used to close the MOST hardware bypass (bypassmode=1) or open it (bypassmode=0). If the bypass is closed the MOST device is invisible to other devices in the ring.

For the functionality of the AllBypass see also the description for the /ABY bit in the Transceiver Control Register of the OS8104.

## Return Values

<0: See error codes

## Availability

| Since Version |
|---|
