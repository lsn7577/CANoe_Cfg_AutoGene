# Chk_AddNode

> Category: `Test` | Type: `function`

## Syntax

```c
dword Chk_AddNode (dword aCheckId, Node aNode, dword aAddress, dword aac, dword ig, dword sys, dword sysi, dword fct, dword fcti, dword ecui, dword mc, dword in);
```

## Description

Adds a J1939 node to an existing check.

## Return Values

0: Check could not be created and must not be referenced.

## Example

```c
// checks the address claim violation of node N1
checkId = ChkCreate_J1939AddressClaimViolation ( N1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 200, 0x01);

// add node N2 to the check
Chk_AddNode (checkId, N2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1);
TestAddCondition(checkId);

// Start check
ChkControl_Start(checkId);

// sequence of different actions and waiting conditions
TestWaitForTimeout(1000);
TestRemoveCondition(checkId);
```

## Availability

| Since Version |
|---|
