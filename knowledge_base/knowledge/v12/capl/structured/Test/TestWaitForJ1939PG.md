# TestWaitForJ1939PG

> Category: `Test` | Type: `function`

## Syntax

```c
long TestWaitForJ1939PG (dbMessage aMessage, dword aTimeout);
```

## Description

Waits for the occurrence of the specified message aMessage. Should the message not occur before the expiration of the time aTimeout, the wait condition is resolved nevertheless.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

-2: Resume due to constraint violation

## Example

```c
// waits for the occurrence of message ‚RQST’
long result;
result = TestWaitForJ1939PG(RQST, 2000);
```

## Availability

| Since Version |
|---|
