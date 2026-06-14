# SetSubscriptionStateIsolated

> Category: `CommunicationObjects` | Type: `function`

## Syntax

```c
void SetSubscriptionStateIsolated(providedEventRef * event, dword subscribed)
```

## Description

Sets the subscription state for an object, for a specific consumer – provider combination, independent of network communication. Normally, the subscription state will be set by the CANoe simulation depending on the observed communication. You can override the behavior if you for example want to test reaction to specific faulty behavior.

## Return Values

—

## Example

```c
SetSubscriptionStateIsolated(field1, 0);
```

## Availability

| Since Version |
|---|
