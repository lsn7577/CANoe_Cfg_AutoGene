# Class: CanDisturbanceBitSequence

> Category: `CANDisturbance` | Type: `notes`

## Description

Each object of CanDisturbanceBitSequence represents one bit within a CanDisturbanceFrameSequenceField.

—

You can access control information of a CanDisturbanceBitSequence object with the following attributes:

Digital Disturbance

| Keyword | Description | Type | Access Limitations |
|---|---|---|---|
| SegmentCount | The number of segments for the bit. | dword | — |
| SegmentValue | The value of each segment Possible values: d: dominant level r: recessive level R: recessive stress level | char[8] | — |
| SegmentLength | The length of each segment in FPGA ticks. | word[8] | — |

| Version 15© Vector Informatik GmbH |
|---|
