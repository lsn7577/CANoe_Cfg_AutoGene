# TestGetWaitEventMostRawMsgData

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetWaitEventMostRawMsgData(mostRawMessage aRawMsg);
```

## Description

If the last (single) wait condition was resolved by a MOST control message, the function copies the data of that message into the provided CAPL variable.

The second signature can only be used for "joined events". The number of the "joined event" (return value of "testJoin...") is here being used as an index.

If the wait condition was resolved by a control message having function catalog format, it is recommended to use TestGetWaitEventMostMsgData instead.

## Return Values

0: Successful data access

## Availability

| Since Version |
|---|
