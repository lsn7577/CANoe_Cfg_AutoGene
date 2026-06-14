# FSIL_ConnectRemovableDevice

> Category: `ISO11783` | Type: `function`

## Syntax

```c
long FSIL_ConnectRemovableDevice(char volumeName[], char pathOfWindowsFolder[], byte maxTimeForRemoval); // form 1
long FSIL_ConnectRemovableDevice(dbNode* fs, char volumeName[], char pathOfWindowsFolder[], byte maxTimeForRemoval); // form 2
```

## Description

Connects a virtual removeable device to the File Server.

A common application is to connect a removeable device (e.g. a USB stick) to the File Server. With this function you can define a Windows folder which is used by the File Server IL as a virtual removable device.

As a result of the function call, the File Server sends a Volume Status Response with the name of the volume (parameter volumeName), maximum time for removal (parameter maxTimeForRemoval) and with volume status Present to all clients.

If there is no other removable volume available (either a physical media, e.g. an USB stick, or a virtual removable device) and no primary volume is set by FSIL_SetNodeProperty then the first virtual removable device is used as a primary volume.

You can disconnect the removable device with FSIL_DisconnectRemovableDevice.

## Parameters

| Name | Description |
|---|---|
| volumeName | Name of the removable volume (without leading “\\”). |
| pathOfWindowsFolder | Path to the Windows folder that is used as a removable virtual disk. Path has to be absolute or relative relating to the folder of the CANoe configuration. Path shall be no subfolder of the root directory. The folder is created if it does not already exist. |
| maxTimeForRemoval | Maximum time a volume can be held off from being removed [s], 0..255. |
| fs | FS simulation node to apply the function. |

## Example

```c
// use folder ‘MyRemovableDevices\Device1’
//Path is relative to the folder of the CANoe configuration
FSIL_ConnectRemovableDevice(“VOL_A”, “MyRemovableDevices\Device1”);
…
// now a File Server client can access files via the volume name e.g.  “\\VOL_A\MyFile.txt”
…
// disconnect removable file File Server is not busy
result = FSIL_DisconnectRemovableDevice(“\\VOL_A”);
```

## Availability

| CANalyzer | CANoe | CANoe4SW Server Edition (Windows) | CANoe4SW Server Edition (Linux) | CANoe4SW | vTESTstudio |  |
|---|---|---|---|---|---|---|
| Since Version | — | 13.0 | 13.0 | — | — | 4.0 |
| Restricted To | — | ISO11783 | ISO11783 | — | — | form 2 ISO11783 |
| CANalyzer Measurement Setup (Transmit Branch) | — | N/A | N/A | N/A | N/A | N/A |
| CANoe Measurement Setup / CANalyzer Analysis Branch | — | — | — | — | N/A | N/A |
| CANoe Simulation Setup | N/A | ✔ (form 1) | ✔ (form 1) | — | N/A | N/A |
| CANoe System and Communication Setup | N/A | — | — | — | — | N/A |
| CANoe Test Setup for Test Modules | N/A | ✔ (form 2) | ✔ (form 2) | — | N/A | N/A |
| CANoe Test Setup for Test Units | N/A | ✔ (form 2) | ✔ (form 2) | — | — | N/A |
| 32-Bit | — | ✔ | ✔ | N/A | — | N/A |
| 64-Bit | — | ✔ | ✔ | — | — | N/A |
