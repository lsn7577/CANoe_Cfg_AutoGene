# GetNrOfCOProviders

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword GetNrOfCOProviders(communicationObject co)
```

## Description

Returns the current number of provider endpoints at a (service-oriented) communication object. Note the number of endpoints may vary over time for some objects. The function is particularly useful to iterate over all providers.

## Return Values

The current number of provider endpoints.

## Example

```c
for (i = 0; i < GetNrOfCOProviders(MirrorAdjustment); ++i)
{
  svc = MirrorAdjustment.consumerSide[CANoe,i];
  // ...
}
```

## Availability

| Since Version |
|---|
