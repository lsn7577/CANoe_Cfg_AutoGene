# J1939TestRequestACL

> Category: `J1939` | Type: `function`

## Syntax

```c
long J1939TestRequestACL( dword requestSA, dbNode aclSender, dword timeout, dword options )
```

## Description

A request for ACL is sent. The configured node must respond with the ACL message (0xEE00).

## Return Values

>0: ACL was received from the configured node (aclSender); return value is equal to the number of received ACLs

## Example

```c
long result;
result = J1939TestRequestACL( 254, EMS, 250, 0x00 );

if (result == 1) {
  TestStepPass( "ACL received" );
}
else if (result == 0) {
  TestStepFail( “Timeout, ACL message not receive” );
}
else {  
  TestStepFail( “Error during Request for ACL test“);
}
```

## Availability

| Since Version |
|---|
