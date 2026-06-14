# _DoIP_MessageAcknowledgeInd

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
void _DoIP_MessageAcknowledgeInd( WORD payloadType, long ackCode, WORD testerAddress, WORD ecuAddress);
```

## Description

A positive or negative acknowledgment was received in the tester. The code may provide additional information on the reason for a negative acknowledge.

## Return Values

—

## Example

```c
void _DoIP_MessageAcknowledgeInd( word payloadType, long code, word testerAddress, word ecuAddress)
{
  write( "_DoIP_MessageAcknowledgeInd type %04x, %d, tester=%04x, ecu=%04x", payloadType, code, testerAddress, ecuAddress);
}
```

## Availability

| Since Version |
|---|
