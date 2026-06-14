# DoIP_SetTesterLogicalAddress

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SetTesterLogicalAddress(dword logicalAddress);
```

## Description

Sets logical DoIP address of the tester used for sending.

Note that ECU simulations will typically send responses to the tester address received in requests.

## Return Values

—

## Example

```c
DoIP_SetTesterLogicalAddress( 0x1000);
```

## Availability

| Since Version |
|---|
