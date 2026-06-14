# valueEntity::ResetValueState

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void <value>::ResetValueState()
```

## Description

Resets the state of the value:

## Return Values

—

## Example

```c
testcase MirrorTest1()
{
// at the start of the testcase, reset all states
MirrorAdjustment.consumerSide[0,0].CurrentPosition.ResetValueState();
// ...
}
```

## Availability

| Since Version |
|---|
