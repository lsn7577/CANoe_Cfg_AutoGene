# Error Codes of coGetLastError

> Category: `Obsolete` | Type: `notes`

## Description

Error Handling with the CANopen Node Layer | See Also

| Error Code | Description |
|---|---|
| 0 | No error, function was executed successfully. |
| 1 | When loading an EDS Electronic Data Sheet or DCF Device Configuration File file, not all objects were generated. |
| 100 | Object dictionary error |
| 101 | Invalid parameter, the value range of a parameter was not adhered to. |
| 102 | The object does not exist. |
| 103 | The object does not have the correct size. |
| 104 | The object cannot be "mapped." |
| 105 | The object dictionary cannot be changed. Objects can only be generated before coStartUp is called. |
| 106 | The node was already started by executing coStartUp. |
| 107 | The node was not started yet, it must be started with coStartUp in order to be able to execute the desired function. |
| 108 | Data for the coThisGet functions are only available in the event function coOnUploadResponse. |
| 109 | The data does not have the correct size for the coThisGet function. |
| 110 | The object could not be connected with the environment variable. |
| 112 | The EDS/DCF file contains a data type that is not supported. |
| 113 | The EDS/DCF file could not be opened. |
| 114 | The object is not permitted. |
| 115 | No SDO transfer was initiated. |
| 116 | A SDO transfer is already running. |
| 117 | The environment variable is not defined in the database. |
| 118 | The environment variable has an incorrect data type. |
| 119 | The incorrect function for the data type of this object was used. |
| 120 | There is not enough buffer storage available to execute the transfer. |
| 121 | The data buffer that was given to the function coThisGetData is too small. |
| 122 | The environment variable is already associated with another object or the object is already associated with another environment variable. |
| 123 | No valid SDO client found. |
| 124 | No valid SDO server found. |
| 125 | Invalid PDO |
| 126 | Wrong transmission type |
| 127 | PDO inhibit time active |
| 128 | Invalid mapping |
| 129 | Wrong communication state |
| 130 | Object or environment variable is not connected. |
| 150 | The selected access type is not supported for the object. |
| 151 | There was an attempt to read an object that can only be written. |
| 152 | There was an attempt to write an object that can only be read. |
| 153 | The number and/or length of the objects to be mapped would exceed the capacity of a PDO. |
| 154 | The sub index does not exist. |
| 155 | The data type does not fit. The length of the service parameter does not fit. |
| 156 | The data type does not fit. The length of the service parameter is too large. |
| 157 | The data type does not fit. The length of the service parameter is too small. |
| 158 | The value range of the parameter was exceeded. |
| 159 | The value of the written parameter is too large. |
| 160 | The value of the written parameter is too small. |
| 161 | General error |
| 162 | It is not possible to transmit the data to the application or to save it there. |
| 163 | The local control does not permit the transmission of the data to the application or its storage there. |
| 164 | The current device state does not permit the transmission of the data to the application or its storage there. |
| 165 | The object dictionary could not be generated or no object is available. |
| 166 | No data available. |
| 200 | Error while using an internal interface function (fatal error). |
| 201 | Error while accessing the error/warning logging file. |
| 202 | Invalid CANopen® node reference. |
| 203 | Internal signal list processing error. |
| 4096 | Internal general error. The size of the object does not correspond to the number of data bytes read. |
| 4097 | Invalid node layer configuration. |
| 4098 | Internal command memory full. Too many function calls were probably executed one after another. |

| Version 15© Vector Informatik GmbH |
|---|
