# vtsSetOutputMask

> Category: `VTSystem` | Type: `function`

## Syntax

```c
long vtsSetOutputMask (DWORD RowMask);
```

## Description

Activates the requested rows of a switch matrix module for dynamic stimulation (PWM, Bitstreams). The row selection is binary encoded into the call parameter.

## Parameters

| Name | Description |
|---|---|
| RowMask | Binary interpreted 32bit unsigned integer value where the least significant five bits encode the connection of the corresponding matrix row with the current matrix channel. The assignment of matrix rows to bits of RowMask is implemented as follows: Matrix Row 1 is activated with Bit0 Matrix Row 2 is activated with Bit1 Matrix Row 3 is activated with Bit2 Matrix Row 4 is activated with Bit3 Direct Switch is activated with Bit 4 (channel 5-8) |

## Example

The following example demonstrates how an identical switch sequence defined in MyBitstream.txt (e.g. a bouncing contact simulation) is applied subsequently to all rows of a VT2832 channel.

```c
ToggleMatrixRows()
{
  int iRow;

  // This calls the method SetCurveType on VTS::MyMatrixChannel
  sysvar::VTS::MyMatrixChannel_1.SetCurveType(eVTSCurveTypeBitStream);

  // This calls the method LoadWFBitStream on VTS::MyMatrixChannel_2
  sysvar::VTS::MyMatrixChannel_1.LoadWFBitStream("MyBitstream.txt");

  // Configure waveform Parameters:
      // TimeIncrement (time to hold each sample)       = 20ms
      // Pause (pause between two waveform repetitions) = 0s
      // NumberOfRepeats (number of repetitions)        = 1

  sysvar::VTS::MyMatrixChannel_1.SetWFParams(0.020, 0.0, 1);

  // Start stimulation
  vtsStartStimulation("VTS::MyMatrixChannel_1");

  for (iRow = 1; iRow < 16; iRow = iRow << 1)
  {
    // This calls the method SetOutputMask on VTS::MyMatrixChannel_1
    vtsSetOutputMask("VTS::MyMatrixChannel_1", iRow);
  }

  // Stop the simulation
  vtsStopStimulation("VTS::MyMatrixChannel_1");
}
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 11.0 | 13.0 | — | — | 3.0 |
| Restricted To | — | — | VT offline | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | — | — | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
