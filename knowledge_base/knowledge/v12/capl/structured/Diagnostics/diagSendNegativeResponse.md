# diagSendNegativeResponse

> Category: `Diagnostics` | Type: `function`

## Syntax

```c
long diagSendNegativeResponse (diagResponse obj, DWORD code)
```

## Description

Sends a negative response to the tester, whereby the specified value is transmitted as error code.

## Return Values

Error code

## Example

```c
on diagRequest FaultMemory::FaultMemory::ReportByStatusMask
{
  // Send neg response with code 0x78 (requestCorrectlyReceived-ResponsePending)
  DiagSendNegativeResponse(this, 0x78);
  // Optionally set a timer to respond with a positive response later
  setTimer(posReq, 1);
  // pos resp after 1s
}
```

## Availability

| Since Version |
|---|
