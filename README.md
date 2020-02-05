# PersonnalData

## Context
Many applications on a global scale handle "personal data" of variable size. Data is said to be personal if it is not accessed
only by one user. In order to provide an efficient service, the storage has different system node and must place the data on these
different nodes.

Each system node can receive one or more data depending on of their size. The storage capacity of such a node is specific to it and can
differ according to the nodes. In addition, a system node can communicate with all other system nodes and some users.

Users are interested in a list of data and only access this data. They can communicate directly with a single node system and cannot communicate with other users.note: In such a context, the communication time between two nodes system or a system node and a different user depending on the users and affected system nodes. For the sake of simplification we will consider that time of communication between two nodes ni , nj is constant, but different from time communication from another couple: neither, nk.
