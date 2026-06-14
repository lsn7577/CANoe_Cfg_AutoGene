# ChkCreate_J1939AddressClaimViolation, ChkStart_J1939AddressClaimViolation

> Category: `Test` | Type: `function`

## Syntax

```c
dword ChkCreate_J1939AddressClaimViolation (Node aNode, dword aAddress, dword aac, dword ig, dword sys, dword sysi, dword fct, dword fcti, dword ecui, dword mc, dword in, dword aTimeout, dword aFlags, Callback aCallback);
```

## Description

Observes the Address Claiming of a J1939 node. The specified node must respond to a Request for Address Claim.

Optionally the check allows sending other messages, only if an Address Claim message (0xEE00) of the node is received first.

You can add further nodes to this check with Chk_AddNode.

Dependent on the used parameter type the appropriate bus context in a multibus environment has only to be set before the function is called if the corresponding database object will be ambiguous.

Further information on site MultiBus Environment.

## Return Values

0: Check could not be created and must not be referenced.

## Example

```c
TestCheck c;
// checks the address claim violation of node N1
c = TestCheck::CreateJ1939AddressClaimViolation( N1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 200, 0x01);

// add node N2 to the check
c.AddNode (N2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1);
TestAddCondition(c);

// Start check
c.start();

// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(c);
```

## Availability

| Since Version |
|---|
