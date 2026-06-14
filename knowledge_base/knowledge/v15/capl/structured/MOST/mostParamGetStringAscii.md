# mostParamGetStringAscii

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamGetStringAscii(mostAmsMessage msg, char paramAdr[], char buffer[], long buffersize); // form 1
long mostParamGetStringAscii(mostAmsMessage msg, char paramAdr[], long arrayIndex, char buffer[], long buffersize); // form 2
```

## Description

Query of parameters of the String type from an AMS message and decode to ASCII format using the parameter name from the XML function catalog. Unsupported characters are ignored.

## Parameters

| Name | Description |
|---|---|
| msg | Message in which the parameter value should be described. |
| paramAdr | Identification of parameters (see Symbolic Identification of Parameters). |
| arrayIndex | Parameter index in arrays or sequences. This declaration overwrites the indexing in the brackets of <paramAdr>. |
| buffer | Buffer to which the ASCII string parameter is copied. |
| bufferSize | Maximum number of copied ASCII string parameter bytes (can be specified with (elcount(buffer))). |

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

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 | 7.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
