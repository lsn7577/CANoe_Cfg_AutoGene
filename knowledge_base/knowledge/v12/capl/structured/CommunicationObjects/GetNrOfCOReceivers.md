# GetNrOfCOReceivers

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword GetNrOfCOReceivers(communicationObject co)
```

## Description

Returns the current number of receiver endpoints at a signal or PDU communication object. Note the number of endpoints may vary over time for some objects. The function is particularly useful to iterate over all receivers.

## Return Values

The current number of receiver endpoints.

## Example

```c
for (i = 0; i < GetNrOfCOReceivers(MirrorState); ++i)
{
  MirrorState.receiverSide[i].ResetValueState();
  // ...
}
```

## Availability

| Since Version |
|---|
