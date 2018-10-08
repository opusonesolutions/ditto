# Equipment database

DiTTo maintains a database of known equipments from utility data with verified parameters. This database can be used to infer electrical parameters when reading incomplete models. For example, when reading a line where only the number of phases, ampacity, and nominal voltage are known, the `LINE` table can be queried to find matching known lines as well as their parameters like sequence impedances.

Alternatively, it is possible to plug your own equipment database to DiTTo assuming that you can match the following format:

## LINE TABLE

Table of the equipment database storing lines (underground and overhead).

| Column name      | Type            | Must be filled | Description                                                  | Unit                   |
| ---------------- | --------------- | -------------- | ------------------------------------------------------------ | ---------------------- |
| ID               | INT PRIMARY KEY | YES            | Primary key.                                                 | -                      |
| NAME             | TEXT            | YES            | Name of the line.                                            | -                      |
| LINETYPE         | TEXT            | YES            | Type of the line (overhead or underground).                  | -                      |
| RATING           | REAL            | YES            | Voltage rating of the line.                                  | Kilo-volt              |
| NPHASES          | INT             | YES            | Number of phases for this line.                              | -                      |
| AMPACITY         | REAL            | YES            | Ampacity normal rating of the line.                          | Amps                   |
| R0               | REAL            | YES            | Zero-sequence resistance of the line.                        | Ohms/km                |
| R1               | REAL            | YES            | Positive-sequence resistance of the line.                    | Ohms/km                |
| B0               | REAL            | YES            | Zero-sequence of the line. Specified at 3m for underground lines or 5m for overhead lines. | Micro-fahrad/km at 20C |
| B1               | REAL            | YES            | Positive-sequence of the line                                | Micro-fahrad/km at 20C |
| X0               | REAL            | YES            | Zero-sequence reactance of the line.                         | Ohms/km                |
| X1               | REAL            | YES            | Positive-sequence reactance of the line.                     | Ohms/km                |
| CONFIGURATION    | INT FOREIGN KEY | NO             | Reference a spacing configuration from the spacing table.    | -                      |
| MATERIAL         | TEXT            | NO             | Material the line is made of.                                | -                      |
| SHORTNAME        | TEXT            | NO             | Short name of the line (Sparrow, Penguin, Rucina...).        | -                      |
| SIZE             | TEXT            | NO             | Size of the wires (ex: 477kcmil, 4/0, #2...).                | -                      |
| FAILURERATE      | REAL            | NO             | The number of faults that occur per year.                    | -                      |
| PHASECONDUCTOR   | INT FOREIGN KEY | NO             | Reference a conductor or a wire from the conductor table.    | -                      |
| NEUTRALCONDUCTOR | INT FOREIGN KEY | NO             | Reference a conductor or a wire from the conductor table.    | -                      |



## CONDUCTOR TABLE

Table of the equipment database storing the conductors, wires, and cables.

| Column name                      | Type            | Must be filled | Description                                                  | Unit      |
| -------------------------------- | --------------- | -------------- | ------------------------------------------------------------ | --------- |
| ID                               | INT PRIMARY KEY | YES            | Primary key.                                                 | -         |
| NAME                             | TEXT            | YES            | Name of the wire/cable.                                      | -         |
| DIAMETER                         | REAL            | YES            | The diameter of the conductor. If the wire is a concentric neutral cable, this is the diameter of the phase conductor. | Meters    |
| GMR                              | REAL            | YES            | The geometric mean radius of the wire. If the wire is a concentric neutral cable, this is the GMR of the phase conductor. | Meters    |
| RESISTANCE                       | REAL            | YES            | The per-unit length resistance of the wire. If the wire is a concentric neutral cable, this is the per-unit resistance of the phase conductor | Ohm/meter |
| AMPACITY                         | REAL            | YES            | The ampacity rating for the wire under nomal conditions.     | Amps      |
| EMERGENCYAMPACITY                | REAL            | NO             | The ampacity rating for the wire under emergency conditions. | Amps      |
| INSULATIONTHICKNESS              | REAL            | NO             | Thickness of the insulation around the conductor.            | Meters    |
| CONCENTRICNEUTRALGMR             | REAL            | NO             | The geometric mean radius of the neutral strand for a concentric neutral cable. | Meters    |
| TYPE                             | TEXT            | YES            | Type of equipment ("conductor", "concentric-neutral-cable"...) | -         |
| CONCENTRICNEUTRALRESISTANCE      | REAL            | NO             | The per-unit length resistance of the neutral strand for a concentric neutral cable. | Meters    |
| CONCENTRICNEUTRALDIAMETER        | REAL            | NO             | The diameter of the neutral strand of the concentric neutral cable. | Meters    |
| CONCENTRICNEUTRALOUTSIDEDIAMETER | REAL            | NO             | The outside diameter of the concentric neutral cable.        | Meters    |
| NSTRAND                          | INT             | NO             | The number of strands for the concentric neutral cable.      | -         |



## TRANSFORMER TABLE

Table of the equipment database storing the transformers.

| Column name               | Type            | Must be filled | Description                                                  | Unit   |
| ------------------------- | --------------- | -------------- | ------------------------------------------------------------ | ------ |
| ID                        | INT PRIMARY KEY | YES            | Primary key.                                                 | -      |
| NAME                      | TEXT            | YES            | Name of the transformer.                                     | -      |
| NPHASES                   | INT             | YES            | Number of phases of this transformer.                        | -      |
| RATING                    | REAL            | YES            | KVA rating of this transformer.                              | KVA    |
| PRIMARYVOLTAGE            | REAL            | YES            | Voltage rating of the primary.                               | KV     |
| SECONDARYVOLTAGE          | REAL            | YES            | Voltage rating of the secondary.                             | KV     |
| REACTANCE                 | REAL            | YES            | Reactance of the transformer.                                | Ohm    |
| NOLOADLOSSES              | REAL            | YES            | The no-load loss for a zero sequence short-circuit test on the entire transformer. |        |
| SHORTCIRCUITRESISTANCELOW |                 |                |                                                              |        |
| NOUTPUTS                  | INT             | NO             | Number of outputs.                                           | -      |
| FAILURERATE               | REAL            | NO             |                                                              |        |
| PHASESHIFT                | REAL            | NO             | The degree phase shift that the transformer causes.          | Degree |
| CONNECTIONTYPE            | TEXT            | NO             | The connection type of the transformer.                      | -      |
| RESISTANCE                | REAL            | YES            | Resistance of the transformer.                               | Ohm    |



