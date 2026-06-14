# DiagSendRequestPDU

> Category: `KLine` | Type: `function`

## Syntax

```c
long DiagSendRequestPDU(BYTE rawPDU[], WORD rawPDULength)
```

## Description

Sends a raw byte buffer. Allows also to send invalid requests.

## Return Values

On success 0, otherwise a value less than 0.

## Example

```c
BYTE request[5];
write ("EXECUTE: Send Tester Present request");
request[0] = 0x81;
request[1] = 0x12;
request[2] = 0xF1;
request[3] = 0x3E;
request[4] = 0xC2;
   if (0 == DiagSendRequestPDU(request, elcount(request)))
   {
      TestStepPass( "Test DiagSendRequestPDU()", "Sending of raw request PDU reports OK.");
   }
   else
   {
      TestStepFail( "Test DiagSendRequestPDU()", "Sending of raw request PDU did not work!");
   }
   if (1 == TestWaitForDiagKLineFrameTransmitted( 1000))
   {
      TestStepPass("Raw request was sent");
   }
   else
   {
      TestStepFail("Error sending raw request");
   }
```

## Availability

| Since Version |
|---|
