# coTfsLssWaitForMasterRequestMessage

> Category: `CANopen` | Type: `function`

## Syntax

```c
long coTfsLssWaitForMasterRequestMessage( void );
```

## Description

This function waits for one of the LSS Master requests which have been configured before. Depending on the request, an appropriate response is sent.

If several requests occur during the wait process, all requests are handled. After a single event the function waits for a further event (standard timeout) if at least one wait condition is available. So the whole wait time of the function can exceed the standard timeout.

To configure LSS Master requests, you can use the following functions:

## Return Values

Error code

## Example

```c
/* clear internal check list */
if (coTfsLssClearMasterResponseList() != 1) {
  write("Clear list failed");
  return;
} 

/* add one or more test functions */

if (coTfsLssAddMasterResponseActivateBitTiming( 1000, 0xFFFFFFFF ) != 1) {
  write("could not add request");
  return;
} 

/* wait for any of the events configured before */
if (coTfsLssWaitForMasterRequestMessage() != 1) {
  write("no event received");
} 
else {
  write("event received");
}
```
