# J1939TestConflictACL

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestConflictACL( dbNode aclSender, dword timeout, dword options )
```

## Description

An ACL parameter group (0xEE00) is send with the source address of the configured node. The device name is increased or decreased by one priority level. After sending the pattern waits for the ACL parameter group of the node.

The low byte of the return value contains the source address from which the ACL parameter group was sent.

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

| Since Version |
|---|
