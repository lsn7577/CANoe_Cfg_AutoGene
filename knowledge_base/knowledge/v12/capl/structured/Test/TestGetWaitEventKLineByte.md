# TestGetWaitEventKLineByte

> Category: `Test` | Type: `function`

## Syntax

```c
long TestGetKLineByte();
```

## Description

If a byte is the last event that triggers a wait instruction, the content can be called up with the first function.

The second function allows to call the content and the end of byte time stamp.

## Return Values

Value of the byte

## Example

```c
DiagRequest EcuIdentification_Read req;
int64 timeStamps;
Byte byteValue;

DiagSetTarget(“DUT”);
req.SendRequest();

   if (1 == TestWaitForDiagKLinebyteTransmitted(5000))
   {
      TestStepPass("Transmitted KLine frame.");
      byteValue =  TestGetWaitEventKLineByte( timeStamp) ;
      write( "TRANSMITTED BYTE VALUE: 0x%x. TIMESTAMP [%.3f]", byteValue, timeStamp/1000000000.0);
   }
   else
   {
   TestStepFail("No confirmation of transmitted K-Line byte.");
   }
```

## Availability

| Since Version |
|---|
