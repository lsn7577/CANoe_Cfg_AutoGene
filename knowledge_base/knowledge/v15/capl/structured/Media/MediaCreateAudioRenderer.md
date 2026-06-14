# MediaCreateAudioRenderer

> Category: `Media` | Type: `function`

## Syntax

```c
dword MediaCreateAudioRenderer();
```

## Description

Creates the streaming audio renderer (SAR) which is a media sink that renders audio in an output device, e.g. a headphone or speaker. Each instance of the SAR renders a single audio stream. To render multiple streams, use multiple instances of the SAR.

The SAR can receive uncompressed audio in either PCM or IEEE floating-point format.

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 8.5 | 13.0 | — | — | — |
| Restricted To | — | — | — | — | — | — |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | — |
| CANoe Simulation Setup | N/A | ✔ | ✔ | — | N/A | — |
| CANoe System and Communication Setup | N/A | ✔ | ✔ | — | — | — |
| CANoe Test Setup for Test Modules | N/A | ✔ | ✔ | — | N/A | — |
| CANoe Test Setup for Test Units | N/A | ✔ | ✔ | — | — | — |
| 32-Bit | — | ✔ | ✔ | N/A | — | — |
| 64-Bit | — | ✔ | ✔ | — | — | — |
