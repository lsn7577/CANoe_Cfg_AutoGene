# J1939TestCommandedAddress

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestCommandedAddress( dbNode aclNode, dword caSA, dword newAddress, dword timeout, dword options )
long J1939TestCommandedAddress( pg aclPG, dword caSA, dword newAddress, dword timeout, dword options )
```

## Description

A commanded address message (0xFED8) is sent. The addressed node must send the ACL message (0xEE00) within the timeout from the new address.

## Parameters

| Name | Description |
|---|---|
| caSA | send CA message with this source address |
| aclSender | node, which address should be changed |
| aclPG | ACL message, which contains the J1939 device name |
| newAddress | new address |
| timeout | timeout in [ms] |
| options | not used |

## Example

```c
long result;
result = J1939TestCommandedAddress( 0xf2, EMS, 1, 250, 0x00 );

if (result == 1) {
  // OK
}
else if (result == 0) {
  TestStepFail( “Timeout, ACL message not received” );
}
else {
  TestStepFail( “Error during Request for ACL test“);
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 7.1 | 13.0 | — | — | 1.1 SP2 |
| Restricted To | — | J1939 | J1939 | — | — | J1939 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
