# Subprograms 11

### Abstraction :

**a view or representation of an entity that includes only the most significant attributes.**

### An abstract data type is a user-defined data type that satisfies the following two conditions:

                              **1**
– The representation of objects of the type is
hidden from the program units that use these
objects, so the only operations possible are
those provided in the type's definition

Advantages ⇒ 

– Reliability--by hiding the data representations, user
code cannot directly access objects of the type or
depend on the representation, allowing the
representation to be changed without affecting user
code
– Reduces the range of code and variables of which the
programmer must be aware
– Name conflicts are less likely

                              **2**
– The declarations of the type and the protocols of the operations on objects of the type are contained in a single syntactic unit. Other program units are allowed to create variables of the defined type.

Advantages ⇒ 

– Provides a method of program organization
– Aids modifiability (everything associated with a data
structure is together)
– Separate compilation

---

## Language requirements for ADTS (Abstract Data Types)

• A syntactic unit in which to encapsulate the type definition.
• A method of making type names and subprogram headers visible to clients, while hiding actual definitions.
• Some primitive operations must be built into the language processor.