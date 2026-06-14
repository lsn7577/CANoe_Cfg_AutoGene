# setOcr

> Category: `CAN` | Type: `function`

## Syntax

```c
setOcr(long channel, byte ocr);
```

## Description

Sets the Output Control Register. The values do not become active until the next call of the function resetCan().

It should be noted that these values depend on the CAN platform used.

## Parameters

| Name | Description |
|---|---|
| 0 | all channels |
| > 0 | only the given channel |

## Return Values

1: success

## Example

```c
...
setOcr(0, 0x02); // set
resetCan(); // activate
...
```

## Availability

| Since Version |
|---|
