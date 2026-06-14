# ChkConfig_DisablePDULayer

> Category: `Test` | Type: `function`

## Syntax

```c
long ChkConfig_DisablePDULayer();
```

## Description

Disables the PDU layer for the current bus context. It affects the next checks that are created after calling this function.

This function has to be used for PDU networks if a check is setup on network level, i.e:

Default is enabled for a PDU network.

## Return Values

0: Successful

## Example

```c
TestCheck c1, c2;
dword bcPduNetwork;

// only needed if the test works on several networks
bcPduNetwork = getBusNameContext("My Pdu Network");
setBusContext(bcPduNetwork);

// always use short header ID
ChkConfig_SetPDUIDFormat(1);

// creates the cycle time check with a PDU header ID
c1 = TestCheck::CreateMsgAbsCycleTimeViolation(2983504, 8, 12);

ChkConfig_DisablePDULayer();
// creates the cycle time check with a CAN ID
c2 = TestCheck::CreateMsgAbsCycleTimeViolation(0x3e1, 8, 12);

// reset to default values
ChkConfig_EnablePDULayer();
ChkConfig_SetPDUIDFormat(0);
```

## Availability

| Since Version |
|---|
