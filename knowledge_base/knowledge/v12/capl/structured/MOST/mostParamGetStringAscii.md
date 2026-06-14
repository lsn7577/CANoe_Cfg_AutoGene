# mostParamGetStringAscii

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamGetStringAscii(mostAmsMessage msg, char paramAdr[], char buffer[], long buffersize)
```

## Description

Query of parameters of the String type from an AMS message and decode to ASCII format using the parameter name from the XML function catalog. Unsupported characters are ignored.

The message data must contain a parameter with the given parameter address.Since the compiler is not able to validate this, errors are detected at run time of the CAPL program only. If the parameter is not part of the message or not the expected type, an error text is displayed in the Write Window and the measurement stops. The function mostParamIsAvailable can be applied to assure parameter availability.

## Return Values

>=0: number of converted characters

## Example

Input: Message parameter bytes: 00 00 61 00 62 00 63 00 00Output: Radiotext: abc

```c
on mostAmsMessage AmFmTuner.RadioText.Status
{
   char buffer[200];
   long dataLen;
   // get string parameter data
   
    datalen = mostParamGetStringAscii(this, "TextA", buffer, elcount(buffer));
   if(datalen >= 0)
   {
     write("Radiotext: %s", buffer);
   }
}
```

## Availability

| Since Version |
|---|
