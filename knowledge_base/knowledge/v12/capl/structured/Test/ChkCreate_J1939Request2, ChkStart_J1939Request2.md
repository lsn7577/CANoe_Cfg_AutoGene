# ChkCreate_J1939Request2, ChkStart_J1939Request2

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_J1939Request2(Node requestNode, Node responseNode, Message requestedMessage, dword expected, dword options, dword timeout, dword requestInhibitTime, dword retryInhibitTime, char[] callback1);
```

## Description

Observes the J1939 Request2 (C900h). It is possible to observe all Request2 messages or only the Request2 message for a specific send node.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Example

```c
TestCheck check;
  // checks the if a response from N2 is received after a J1939 Request2 from node N1
  checkId = ChkStart_J1939Request2(N1, N2, GBSD, 0x01, 0, 1250, 50, 0);
  TestAddCondition(checkId);

  // sequence of different actions and waiting conditions
  TestWaitForTimeout(1000);
  TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
