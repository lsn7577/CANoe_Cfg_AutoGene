# valueEntity::GetUpdateCount

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
dword <value>::GetUpdateCount()
```

## Description

Returns the update count of the value. The update count is reset to zero at start of measurement and with each call to valueEntity::ResetValueState. It is then increased each time the value is updated, even if the value does not change.

For some values, the count is only initialized when the value is accessed the first time for performance reasons. This means that if you want to use it as a ‘global’ count over the whole measurement, you should call valueEntity::ResetValueState at the start of the measurement explicitly.

## Return Values

The current update count.

## Example

```c
MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition.ResetValueState();
testWaitForTimeout(1000);
write("Updates during the last second: %d", MirrorAdjustment.consumerSide[CANoe,LeftMirror].CurrentPosition.GetUpdateCount());
```

## Availability

| Since Version |
|---|
