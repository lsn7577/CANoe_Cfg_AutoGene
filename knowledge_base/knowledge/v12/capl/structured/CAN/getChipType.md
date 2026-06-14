# getChipType

> Category: `CAN` | Type: `function`

## Syntax

```c
long getChipType(long channel);
```

## Description

Determines the type of CAN controller used.

## Parameters

| Name | Description |
|---|---|
| 0 | both controller |
| 1 | Channel 1 |
| 2 | Channel 2 |

## Return Values

Type of controller with the following values:
5
NEC 72005
200
Philipps PCA82C200
526
Intel 82526
527
Intel 82527
1000,1001
Philipps SJA1000
Other types may occur. DEMO versions return the result 0 or simulate one of the existing types. If an attempt is made to access a nonexistent channel (e.g. Channel 2 for CPC/PP) or if the driver used does not support this function, the functional result is 0.

## Example

```c
...
switch(getChipType(0)) {
case 200: setOcr(0,0x02);
break;
case ...
default:
write("Unknown CAN-chip %d", getChipType(0));
break;
}
...
```

## Availability

| Since Version |
|---|
