# J1939TestConflictACL

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestConflictACL( dbNode aclSender, dword timeout, dword options )
long J1939TestConflictACL( pg aclMsg, dword timeout, dword options )
```

## Description

An ACL parameter group (0xEE00) is send with the source address of the configured node. The device name is increased or decreased by one priority level. After sending the pattern waits for the ACL parameter group of the node.

The low byte of the return value contains the source address from which the ACL parameter group was sent.

## Parameters

| Name | Description |
|---|---|
| aclSender | node, which device name and address is used |
| aclMsg | device name and address of this ACL parameter group is used |
| timeout | timeout in [ms] |
| Bit 0 | 1: higher priority 0: lower priority |
| Bit 1 | 1: uses NMT Address table to identify the nodes actual address (dynamic) 0: uses NmStationAddress attribute in the database to get the nodes address (static) |

## Example

```c
long result;
result = J1939TestConflictACL( EMS, 250, 0x00 );

if (result >= 0x100) {
  // check address
  if ((result & 0xff) == EMS.NmStationAddress)) {
    TestStepPass( "ACL conflict test OK" );
  }
  else {
    TestStepFail( "Received ACL from wrong SA" );
  }
}
else if (result == 0) {
  TestStepFail( "Timeout, ACL message not receive" );
}
else {
  TestStepFail( "Error during ACL conflict test");
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
