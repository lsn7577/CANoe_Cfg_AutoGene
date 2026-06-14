# GetNrOfCOConsumers

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword GetNrOfCOConsumers(communicationObject co)
```

## Description

Returns the current number of consumer endpoints at a (service-oriented) communication object. Note the number of endpoints may vary over time for some objects. The function is particularly useful to iterate over all consumers.

## Return Values

The current number of consumer endpoints.

## Example

```c
for (i = 0; i < GetNrOfCOConsumers(MirrorAdjustment); ++i)
{
  svc = MirrorAdjustment.providerSide[i,LeftMirror];
  // ...
}
```

## Availability

| Since Version |
|---|
