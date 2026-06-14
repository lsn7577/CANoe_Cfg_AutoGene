# TestSetSendTimeout

> Category: `Test` | Type: `function`

## Syntax

```c
void TestSetSendTimeout (long aTimeout);
```

## Description

This function sets the timeout up to which the TestSendMostAMSMessage functions wait for a Tx acknowledgment for the sent message. This value is set to 5000 ms by default.

With the specification of a timeout value of 0, a wait of any length for the Tx acknowledgment is possible, while the specification of -1 means that the waiting for the acknowledgment is switched off, that is, there is no wait.

## Return Values

—

## Availability

| Since Version |
|---|
