# mostGenerateBypassToggle

> Category: `MOST` | Type: `function`

## Syntax

```c
long mostGenerateBypassToggle(long channel, long invistime, long vistime, long repeat);
```

## Description

Starts (repeat > 0) or stops (repeat = 0) generation of Bypass-open-close transitions.

VN2640: The bypass of the INIC used for simulation and stimulation is toggled. The node has to be in slave mode. The range for timing values is 10…65535 ms.

OptoLyzer: The bypass of the additional stress network interface controller (NIC) in the OptoLyzer G2 3150o is switched. The bypass of the main NIC (which is responsible for sending and receiving) is not affected.

The stress network interface controller (NIC) must have active bypass or bypass opened (see mostSetStressNodeParameter ).

## Parameters

| Name | Description |
|---|---|
| channel | Channel of the connected interface |
| invistime | Time during which node has its bypass closed (in ms) |
| vistime | Time with opened bypass (in ms) |
| repeat | 0: Stop stress >0: Number of transitions0xFFFF: Generate transitions continually |

## Return Values

See error codes

## Example

```c
// prepare stress NIC: set "active" bypass
mostSetStressNodeParameter(1, 3, 2);
// make the stress NIC visible two times for 50 ms each
mostGenerateBypassToggle(1, 100, 50, 2);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | 7.2 | 7.2 | — | — | — | —✔ |
| Restricted To | MOST150 | MOST150 | — | — | — | —✔ |
| CANalyzer Measurement Setup (Transmit Branch) | ✔ | N/A | N/A | N/A | N/A | — |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | —✔ |
| CANoe Simulation Setup | N/A | ✔ | — | — | N/A | —✔ |
| CANoe System and Communication Setup | N/A | ✔ | — | — | — | —✔ |
| CANoe Test Setup for Test Modules | N/A | ✔ | — | — | N/A | —✔ |
| CANoe Test Setup for Test Units | N/A | ✔ | — | — | — | —✔ |
| 32-Bit | ✔ | ✔ | — | N/A | — | —✔ |
| 64-Bit | ✔ | ✔ | — | — | — | —✔ |
