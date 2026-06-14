# mostParamSetStringEnc

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamSetStringEnc (mostAmsMessage msg, char paramAdr[], long encoding, char asciiStr[]); // form 1
long mostParamSetStringEnc (mostAmsMessage msg, char paramAdr[], long arrayIndex, long encoding, char asciiStr[]); // form 2
```

## Description

Encoding and setting of parameters of the String type (for ASCII-coded strings only) in an AMS message using the parameter name from the XML function catalog. Only ASCII-coded strings are supported.

## Parameters

| Name | Description |
|---|---|
| msg | Message in which the parameter value should be described. |
| paramAdr | Identification of parameters (see Symbolic Identification of Parameters). |
| arrayIndex | Parameter index in arrays or sequences. This declaration overwrites the indexing in the brackets of <paramAdr>. |
| 0x00 | Unicode, UTF16 |
| 0x01 | ISO 8859/15 8 bit |
| 0x02 | Unicode, UTF8 |
| 0x03 | RDS |
| 0x04 | DAB Charset 0001 |
| 0x05 | DAB Charset 0010 |
| 0x06 | DAB Charset 0011 |
| 0x07 | SHIFT_JIS |
| asciiStr | String that should be encoded and copied to the message. |

## Return Values

See error codes

## Example

-> Message parameter bytes: 00 00 61 00 62 00 63 00 00

```c
mostAmsMessage AmFmTuner.RadioText.Status msg;
mostParamSetString(msg, "TextA", 0x00, "abc");
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
