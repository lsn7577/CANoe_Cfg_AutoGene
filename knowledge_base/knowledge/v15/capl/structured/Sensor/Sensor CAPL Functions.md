# Sensor CAPL Functions

> Category: `Sensor` | Type: `notes`

## Description

sensorSwitchSupplyVoltage

sensorQueueSerialFrames

Option .Sensor | Enumeration | Structs

| SENSOR Functions for PSI5 and SENT only available with Option Sensor. |
|---|

| Methods/Functions | Short Description |
|---|---|
| QueueSerialMessage sensorQueueSerialMessage | Inserts the given serial message into the send queue of the given time slot. |
| QueueValues sensorQueueValues | Inserts the given values into the send queue of the given sensor signal system variable. |
| ClearQueue sensorClearQueue | Clears the send queue of the given sensor system variable. |
| SwitchSupplyVoltage sensorSwitchSupplyVoltage | Enables or disables the sensor supply voltage of a simulated ECU. |
| sensorConvertUnsignedToSigned | Converts the given n bit input value from unsigned to signed using two's complement. |
| sensorExtractInteger | Extracts an integer value from the given byte array. |
| sensorInsertInteger | Inserts the given integer value into the given byte array. |
| sensorReverseBits | Reverses the given number of bits in the given array. |

| Methods/Functions | Short Description |
|---|---|
| QueueCombinedFrame sensorQueueCombinedFrame | This method/function is intended to be used for I2C master simulation. It queues a frame to write and then read the given number of bytes from the given slave. |
| QueueFrame sensorQueueFrame | This method/function is intended to be used for I2C slave simulation. It inserts the given data bytes into the response queue of the given slave. |
| QueueReadFrame sensorQueueReadFrame | This method/function is intended to be used for I2C master simulation. It queues a frame to read the given number of bytes from the given slave. |
| QueueWriteFrame sensorQueueWriteFrame | This method/function is intended to be used for I2C master simulation. It queues a frame to wite the given bytes to the given slave. |

| Methods/Functions | Short Description |
|---|---|
| QueuePsi5Frame sensorQueuePsi5Frame | Inserts the given frame into the send queue of the given channel. |

| Methods/Functions | Short Description |
|---|---|
| QueueSentFrame sensorQueueSentFrame | Inserts the given frame into the send queue of the given channel. |
| ResetClockTickLength sensorResetClockTickLength | Resets the clock tick length of a simulated sensor to the initially configured value. |
| SetClockTickLength sensorSetClockTickLength | Overwrites the clock tick length of a simulated sensor with the given value. |

| Methods/Functions | Short Description |
|---|---|
| QueueSpcTriggerPulse sensorQueueSpcTriggerPulse | Queues a single SPC trigger pulse on the specified ECU channel. |
| QueueSpcTriggerPulseSequence sensorQueueSpcTriggerPulseSequence | Queues a sequence of SPC trigger pulses on the specified ECU channel. |
| StopSpcTriggerPulseTransmission sensorStopSpcTriggerPulseTransmission | Stops any periodic trigger pulse transmission on the specified ECU channel. |

| Methods/Functions | Short Description |
|---|---|
| QueueMisoData sensorQueueMisoData | SPI slave simulation in basic mode. Inserts the given MISO data into the response queue of the given slave. |
| QueueMosiData sensorQueueMosiData | SPI master simulation. Inserts the given MOSI data into the send queue from the master to the given slave. |

| Methods/Functions | Short Description |
|---|---|
| QueueSerialFrame sensorQueueSerialFrame | Queues one frame for the given datum. |
| QueueSerialFrames sensorQueueSerialFrames | Queues one frame for each given datum. |

| Version 15© Vector Informatik GmbH |
|---|
