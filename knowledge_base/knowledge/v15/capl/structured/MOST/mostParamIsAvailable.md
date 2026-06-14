# mostParamIsAvailable

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostParamIsAvailable(mostAmsMessage * msg, char paramadr[]); // form 1
long mostParamIsAvailable(mostAmsMessage * msg, char paramadr[], long arrayIndex); // form 2
```

## Description

Check whether a described parameter with the parameter name from the XML function catalog is in an AMS message.

PosDescription, TelLen and StreamCases are checked in addition to FblockID, FunktionID and OpType.

This function can be used to prevent erroneous access to messages that can be first identified at run time of a CAPL program.

## Parameters

| Name | Description |
|---|---|
| msg | Message to which parameter access should be applied. |
| paramAdr | Identification of parameters (see Symbolic Identification of Parameters). |
| arrayIndex | Parameter index in arrays or sequences. This declaration overwrites the indexing in the brackets of <paramAdr>. |

## Example

Assure access to a parameter

In the following sample, access to a parameter is assured in a received message. If the status message is partially transmitted, either through targeted use of the Pos parameter or erroneous assignment of TelLen, it can happen that StartTrack is not part of the received message.

```c
On mostAmsMessage DiskPlayer.MediaInfo.Status
{
   int firstTrack;
   // check whether message was transmitted including FirstTrack of third array element (third media here)
   if(mostParamIsAvailable(this, “Data.Record[].FirstTrack”, 3))
   {
      // read FirstTrack from message
      firstTrack = mostParamGet (this, “Data.Record[].FirstTrack”, 3);
   }
   else
   {
      // do error handling, either 
      // a) Pos did not indicate existence of FirstTrack (only subset transmitted)
      // b) TelLen was not sufficient (erroneous message transmission)
      // c) Message is no MediaInfo (would only be applicable if ‘On mostAmsMessage’ handler
      //    were not so specific as in this example, error in implementation of model)
      // d) Parameter description was erroneous (error in implementation of model)
      // (Hint: Check if an appropriate XML Function Catalog is assigned to the configuration)
   }
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 5.2 | 5.2 | — | — | — | —✔ |
| Restricted To | MOST25 MOST50 MOST150 | MOST25 MOST50 MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
