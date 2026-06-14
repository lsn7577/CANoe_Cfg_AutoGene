# GetNrOfCOSenders

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword GetNrOfCOSenders(communicationObject co)
```

## Description

Returns the current number of sender endpoints at a signal or PDU communication object. Note the number of endpoints may vary over time for some objects. The function is particularly useful to iterate over all senders.

## Return Values

The current number of sender endpoints.

## Example

```c
for (i = 0; i < GetNrOfCOSenders(MirrorState); ++i)
{
  MirrorState.senderSide[i].ResetValueState();
  // ...
}
```

## Availability

| Since Version |
|---|
