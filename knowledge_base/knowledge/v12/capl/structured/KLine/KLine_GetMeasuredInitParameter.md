# KLine_GetMeasuredInitParameter

> Category: `KLine` | Type: `function`

## Syntax

```c
long KLine_GetMeasuredValue(dword parameterID)
```

## Description

Retrieves the different parameters of the init patterns.

## Return Values

Parameter value or error code.

## Example

```c
DiagRequest StartDiagnosticSession req;
enum eMeasuredValues
{
   KeyByte1            = 0,
   KeyByte2            = 1,
   TiniL               = 2,
   Twup                = 3,
   W4Time1             = 4,
   InvertedAddressByte = 5,
   W1Time              = 6,
   W2Time              = 7,
   W3Time              = 8,
   W4Time2             = 9,
   BaudRateSyncByte    = 10
};

long pKeyByte1;
long pKeyByte2;
long pW4Time1;
long pInvertedAddressByte;
long pW1Time;
long pW2Time;
long pW3Time;
long pW4Time2;
long pBaudRateSyncByte;

DiagSetTarget(“DUT”);
DiagConnectChannel();
   if (1 == TestWaitForDiagChannelConnected(3000))
   {
      TestStepPass("Channel connected successfully");
   }
   else
   {
      TestStepFail("Could not connect channel");
   }

req.SendRequest();
   if (1 == testWaitForDiagKLineFrameTransmitted(1000))
   {
      TestStepPass("Request transmitted successfully.");
   }
   else
   {
      TestStepFail("No request transmitted.");
   }

pKeyByte1 = KLine_GetMeasuredInitParameter(KeyByte1);
pKeyByte2 = KLine_GetMeasuredInitParameter(KeyByte2);
pW4Time1 = KLine_GetMeasuredInitParameter(W4Time1);
pInvertedAddressByte = KLine_GetMeasuredInitParameter(InvertedAddressByte);
pW1Time = KLine_GetMeasuredInitParameter(W1Time);
pW2Time = KLine_GetMeasuredInitParameter(W2Time);
pW3Time = KLine_GetMeasuredInitParameter(W3Time);
pW4Time2 = KLine_GetMeasuredInitParameter(W4Time2);
pBaudRateSyncByte = KLine_GetMeasuredInitParameter(BaudRateSyncByte);

write("KeyByte1: 0x%x", pKeyByte1);
write("KeyByte2: 0x%x", pKeyByte2);
write("W4Time 1: %.2f", pW4Time1/toMs);
write("InvertedAddressByte: 0x%x", pInvertedAddressByte);
write("W1Time: %.2f", pW1Time/toMs);
write("W2Time: %.2f", pW2Time/toMs);
write("W3Time: %.2f", pW3Time/toMs);
write("W4Time 2: %.2f", pW4Time2/toMs);
write("BaudRateSyncByte: %d", pBaudRateSyncByte);

DiagCloseChannel();
   if (1 == testWaitforDiagChannelClosed(1000))
   {
      TestStepPass("Diag channel closed successfully");
   }
   else
   {
      TestStepFail("Diag channel could not be closed.");
   }
```

## Availability

| Since Version |
|---|
