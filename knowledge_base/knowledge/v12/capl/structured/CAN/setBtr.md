# setBtr

> Category: `CAN` | Type: `function`

## Syntax

```c
long setBtr(long channel, byte btr0, byte btr1);
```

## Description

Sets another baud rate. The values do not become active until the next call of the function resetCan.

It should be noted that these values depend on the CAN controller used.

## Parameters

| Name | Description |
|---|---|
| 0 | All controllers |
| 1 - 32 | channel 1 - 32 |

## Return Values

Always 1

## Example

```c
...
setBtr(0, 0x00, 0x3a); // 500 kBaud for 82C200
resetCan(); // activate
...
```

## Availability

| Since Version |
|---|
