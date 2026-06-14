# output (LIN)

> Category: `LIN` | Type: `function`

## Syntax

```c
void output(linFrame msg);
```

## Description

This function can be used for two purposes:

## Parameters

| Name | Description |
|---|---|
| Msgext | Variable of type linFrame. List of available selectors for this type of objects can be found under linFrame selectors. |

## Return Values

—

## Example

```c
linFrame MotorControl frameMotorControl;
...
// Reconfigure response of the frame defined in database 
   linFrame MotorControl frameMotorControl;
frameMotorControl.RTR = 0;
frameMotorControl.byte(0)=0xDF;
frameMotorControl.byte(1)=0x20;
output(frameMotorControl);
...
// Send the frame header
frameMotorControl.RTR = 1;
output(frameMotorControl);
...
// Function to set response on channel 2 for any frame.
// The specified frame might not be defined in database.
void SetFrameResponse(byte frameID, byte frameSize)
{
int index;
linFrame 0x0 frame = {msgChannel=2}; // define frame object on channel 2
// Setting frame size in run-time possible only with this function
linChangeDLC(frameID, frameSize);
frame.ID = frameID;           // set specified frame ID
// initialize data byte fields
for (index=0; index < frameSize; ++index)
{
frame.byte(index) = 0xFF;
}
// issue request to update the configured response
frame.RTR = 0;
output(frame);
linSetRespCounter(frameID, -1); // enable unlimited number of responses
}
...
// Configuring a message in on preStart when 
 working without database.
linFrame 0x20 aLinMsg;
output(aLinMsg);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 3.2 | 3.2 | 13.0 | — | — | 1.0 |
| Restricted To | LIN | LIN | LIN | — | — | LIN |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | ✔ | ✔ | ✔ | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | ✔ | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | ✔ | ✔ | ✔ | — | — | N/A |
