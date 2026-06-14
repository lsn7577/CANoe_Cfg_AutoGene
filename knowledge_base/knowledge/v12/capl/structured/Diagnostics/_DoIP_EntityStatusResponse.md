# _DoIP_EntityStatusResponse

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_EntityStatusResponse( char IPaddress[], WORD port, BYTE nodeType, BYTE maxConcurrentTCPsockets, BYTE currentlyOpenTCPsockets, DWORD maxDataSize);
```

## Description

A response for an entity status request was received.

## Return Values

—

## Example

```c
// Process an entity status response
void _DoIP_EntityStatusResponse( char IPaddress[], WORD port, BYTE nodeType, BYTE maxConcurrentTCPsockets, BYTE currentlyOpenTCPsockets, DWORD maxDataSize)
{
  write( "_DoIP_EntityStatusResponse( '%s', %d, %d, %d, %d, %d)",
  IPaddress, port, nodeType, maxConcurrentTCPsockets,
  currentlyOpenTCPsockets, maxDataSize);
  testSupplyTextEvent( cTE_EntityStatusRespInd);
}

Testcase TC_EntityStatus()
{
  DoIP_SendEntityStatusRequest();
  testWaitForTextEvent( cTE_EntityStatusRespInd, 500);
}
```

## Availability

| Since Version |
|---|
