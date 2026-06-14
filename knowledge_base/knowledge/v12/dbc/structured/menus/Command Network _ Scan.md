# Command Network | Scan

> Category: `DBC` | Subcategory: `menus` | Type: `concept`

Read-out a device over the bus and generate the object tree. It tries to read all possible entries via the bus. If found entries exist in the database, the database attributes are taken over. For entries not described in the database, the basic entries are generated.

Symbol:

Shortcut: <F9>

## Databases

The databases used for the scan can be determined within the Database dialog. The dialog can be reached via the menu path Database|Edit List.

## CAN-Hardware

The scan uses the CAN channel that is assigned to CANeds in the Vector Hardware Config dialog under Application. You can open this dialog via the control panel in the start menu of your system, if you have already installed a CAN hardware.

## Settings

Node-ID

The node ID of the device to be scanned.

Master-ID

For accessing the device the scanner is a master. In that sense it is also a device and therefore needs a node ID. Just take any free number in the range 1-127.

Baudrate

The baud rate configured at your device.

1xxx,...

For reducing the scan time it is possible to select the object dictionary area.

1xxx

Communication Profile Area should always be scanned.

2xxx-5xxx

Manufacturer Specific Area - normally objects in this area are known

6xxx

part of Standardized Device Profile Area - should always be scanned

7xxx-9xxx

part of Standardized Device Profile Area - often not used

Axxx

area, where many programmable devices e.g. CiA405 devices place their network variables

Bxxx-Fxxx

reserved for further use

Include mapping test

This option enables the test for mapping facilities. For this it makes write tests to the mapping entries, trying to write all objects to all mapping entries. Also it is checked if PDO parameter objects are writeable.

Caution!

Writing to a mapping entry has some dangers: If the device is switched to Operational, the device output lines may be set active. This can lead to starting a motor or something similar. So use this feature only if you can be sure, that it does not behave this way.

Compact Storage

If this options is activated CANeds try to store objects compact. I.e.

| Node-ID | The node ID of the device to be scanned. |  |  |  |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Master-ID | For accessing the device the scanner is a master. In that sense it is also a device and therefore needs a node ID. Just take any free number in the range 1-127. |  |  |  |  |  |  |  |  |  |  |  |  |
| Baudrate | The baud rate configured at your device. |  |  |  |  |  |  |  |  |  |  |  |  |
| 1xxx,... | For reducing the scan time it is possible to select the object dictionary area. 1xxx Communication Profile Area should always be scanned. 2xxx-5xxx Manufacturer Specific Area - normally objects in this area are known 6xxx part of Standardized Device Profile Area - should always be scanned 7xxx-9xxx part of Standardized Device Profile Area - often not used Axxx area, where many programmable devices e.g. CiA405 devices place their network variables Bxxx-Fxxx reserved for further use | 1xxx | Communication Profile Area should always be scanned. | 2xxx-5xxx | Manufacturer Specific Area - normally objects in this area are known | 6xxx | part of Standardized Device Profile Area - should always be scanned | 7xxx-9xxx | part of Standardized Device Profile Area - often not used | Axxx | area, where many programmable devices e.g. CiA405 devices place their network variables | Bxxx-Fxxx | reserved for further use |
| 1xxx | Communication Profile Area should always be scanned. |  |  |  |  |  |  |  |  |  |  |  |  |
| 2xxx-5xxx | Manufacturer Specific Area - normally objects in this area are known |  |  |  |  |  |  |  |  |  |  |  |  |
| 6xxx | part of Standardized Device Profile Area - should always be scanned |  |  |  |  |  |  |  |  |  |  |  |  |
| 7xxx-9xxx | part of Standardized Device Profile Area - often not used |  |  |  |  |  |  |  |  |  |  |  |  |
| Axxx | area, where many programmable devices e.g. CiA405 devices place their network variables |  |  |  |  |  |  |  |  |  |  |  |  |
| Bxxx-Fxxx | reserved for further use |  |  |  |  |  |  |  |  |  |  |  |  |
| Include mapping test | This option enables the test for mapping facilities. For this it makes write tests to the mapping entries, trying to write all objects to all mapping entries. Also it is checked if PDO parameter objects are writeable. Caution! Writing to a mapping entry has some dangers: If the device is switched to Operational, the device output lines may be set active. This can lead to starting a motor or something similar. So use this feature only if you can be sure, that it does not behave this way. | Caution! Writing to a mapping entry has some dangers: If the device is switched to Operational, the device output lines may be set active. This can lead to starting a motor or something similar. So use this feature only if you can be sure, that it does not behave this way. |  |  |  |  |  |  |  |  |  |  |  |
| Caution! Writing to a mapping entry has some dangers: If the device is switched to Operational, the device output lines may be set active. This can lead to starting a motor or something similar. So use this feature only if you can be sure, that it does not behave this way. |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Compact Storage | If this options is activated CANeds try to store objects compact. I.e. if all sub objects have equal attributes (except the name) they are stored com-pact. if the object description of all PDOs is the same, they are stored compact. |  |  |  |  |  |  |  |  |  |  |  |  |

| 1xxx | Communication Profile Area should always be scanned. |
|---|---|
| 2xxx-5xxx | Manufacturer Specific Area - normally objects in this area are known |
| 6xxx | part of Standardized Device Profile Area - should always be scanned |
| 7xxx-9xxx | part of Standardized Device Profile Area - often not used |
| Axxx | area, where many programmable devices e.g. CiA405 devices place their network variables |
| Bxxx-Fxxx | reserved for further use |

| Caution! Writing to a mapping entry has some dangers: If the device is switched to Operational, the device output lines may be set active. This can lead to starting a motor or something similar. So use this feature only if you can be sure, that it does not behave this way. |
|---|

## Device Reset

On starting the scan the command NMT Reset is performed to ensure, that the device has its default settings. There is no command 1011h Restore factory settings. Since writing to the object dictionary may change some device settings, at the end the NMT Reset is performed again.

## Data Storage

Pressing button [Ok] at the end of a scan creates a new window. After the command has finished you should store the new EDS with the command Save. If you want to update an existing EDS, open both EDS files and move the new data to the existing one with drag & drop or via the clipboard.
