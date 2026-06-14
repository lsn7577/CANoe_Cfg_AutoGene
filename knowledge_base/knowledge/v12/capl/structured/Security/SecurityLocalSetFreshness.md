# SecurityLocalSetFreshness

> Category: `Security` | Type: `function`

## Syntax

```c
long SecurityLocalSetFreshness(char freshnessIdentifierString[], dword freshnessValueId, byte freshnessData[], dword freshnessDataLength, dword flags)
```

## Description

Set the freshness for the specified Id.

As freshness values differs from Security Source to Security Source you have to refer to the Security Source specific manual to get more information about which values you have to specify as parameters.

## Return Values

1: SuccessA Value of 1 means that the action was successful. A value less than or equal to 0 means error.

## Availability

| Since Version |
|---|
