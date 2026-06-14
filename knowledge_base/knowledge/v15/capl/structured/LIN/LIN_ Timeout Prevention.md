# LIN: Timeout Prevention

> Category: `LIN` | Type: `notes`

## Description

The 7259-transceiver implements a dominant timeout of 6 to 20 ms to prevent a faulty slave from disturbing the LIN bus for a prolonged time. This timeout, however, can lead to problems with low baud rates. For example, a timeout of 6 ms means that only 6 dominant bits can be sent at 1 kBaud. This excludes a null byte as well as any valid synch break. It is also impossible to create a dominant disturbance on the bus using the transceiver alone.

To bypass these limitations, the 7259mag-cab and the 7259mag-piggy contain an auxiliary circuit that is able to keep the bus level dominant. When using this auxiliary circuit, however, LIN conformant signal edges can not be guaranteed, particularly for the rising edge of a dominant signal that is longer than 6 ms.

| Version 15© Vector Informatik GmbH |
|---|
