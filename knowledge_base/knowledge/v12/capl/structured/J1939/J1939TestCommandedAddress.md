# J1939TestCommandedAddress

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestCommandedAddress( dbNode aclNode, dword caSA, dword newAddress, dword timeout, dword options )
```

## Description

A commanded address message (0xFED8) is sent. The addressed node must send the ACL message (0xEE00) within the timeout from the new address.

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

| Since Version |
|---|
