# coTfsLssSendConfigureNodeIdResponse

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssSendConfigureNodeIdResponse( dword errorCode, dword specificError );
```

## Description

This function sends the LSS configure node-ID response.

## Return Values

Error code

## Example

```c
/* send LSS configure nodeID response */

if (coTfsLssSendConfigureNodeIdResponse( 0, 0 ) != 1) {
  /* message could not be sent */
}
```
