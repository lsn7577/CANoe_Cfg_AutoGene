# TestWaitForMessage

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForMessage(dbMessage aMessage, dword aTimeout);
```

## Description

Waits for the occurrence of the specified message aMessage. Should the message not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

When no message is specified the wait condition is resolved on any message.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Example

```c
// waits for the occurrence of message ‚VehicleMotion’
long result;
result = TestWaitForMessage(VehicleMotion, 2000);
```

## Availability

| Since Version |
|---|
