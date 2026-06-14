# DoIP_SendEntityStatusRequest

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void DoIP_SendEntityStatusRequest();
```

## Description

Sends an entity status request as limited broadcast or to the given address.

## Return Values

—

## Example

```c
void _DoIP_EntityStatusResponse( char IPaddress[], WORD port, BYTE nodeType, BYTE maxConcurrentTCPsockets, BYTE currentlyOpenTCPsockets, DWORD maxDataSize)
{
  write( "_DoIP_EntityStatusResponse( '%s', %d, %d, %d, %d, %d)",
    IPaddress, port, nodeType, maxConcurrentTCPsockets,
    currentlyOpenTCPsockets, maxDataSize);
  testSupplyTextEvent( cTE_EntityStatusRespInd);
}

// Send an entity status request and wait for the first response
Testcase TC_EntityStatus()
{
  DoIP_SendEntityStatusRequest();
  testWaitForTextEvent( cTE_EntityStatusRespInd, 500);
}
```

## Availability

| Since Version |
|---|
