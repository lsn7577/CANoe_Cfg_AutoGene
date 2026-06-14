# mostAmsSetSizePrefixed

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostAmsSetSizePrefixed(long channel, long minlength);
```

## Description

Configures the minimum length of an AMS message above which an initiating message with TelID==4 is sent.

## Return Values

0: OK

## Example

Activate special size prefix length for exactly one AMS message.

Activate special size prefix length for AMS messages with more than 200 bytes payload.

```c
mostAmsSetSizePrefixed(1, 46);
mostAmsOutput(1, "Telephone.List.Status(0,1,2,3,4,5,6,7)");
mostAmsSetSizePrefixed(1, -1);
mostAmsSetSizePrefixed(1, 200);
```

## Availability

| Since Version |
|---|
