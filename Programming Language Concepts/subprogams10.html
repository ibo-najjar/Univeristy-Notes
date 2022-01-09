
<html> <head> <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />    
    <link rel="stylesheet" type="text/css" href="style.css" />
    </head>
    <div id="main">
    <h2>Chapter 10 - Implementing Subprograms</h2> 
    <div class="box">
    resources:<br/>
    <a href="http://www.cs.csub.edu/~donna/PDFs/gdbrefcard.pdf">quick gdb guide</a><br>
    <a href="../examples/week10/hw10.c">hw10.c</a> 
    </div>
    <p>
    <SPAN STYLE="Background-Color : #eee;">
    SUBPROGRAM LINKAGE</span>
    </p>
    <p>
     The subprogram call and return operations of a 
     language are together called subprogram linkage. 
    </p>
      Subprogram call actions:
    <pre class="verbatim">
    + Parameter passing methods
    + Binding nonstatic local variables
    + Save return address of calling program  (address of next statement)
    + Transfer of control to callee
    + Access to nonlocal variables if subprogram nesting
    
      Subprogram return actions: 
    
    + copy outmode parameters
    + deallocate memory (including stack)
    + restore control to caller 
    </pre>
    
    <SPAN STYLE="Background-Color : #eee;">
    ACTIVATION RECORDS FOR SIMPLE SUBPROGRAMS
    </SPAN>
    <pre>
      "Simple"
    + local variables are static only (not stack-dynamic)
    + no recursion
    + subprograms are not nested
    
      Call Semantics:
    + Save the execution status of the caller
    + Carry out the parameter-passing process
    + Pass the return address to the callee
    + Transfer control to the callee
    
      Return Semantics:
    + If pass-by-value-result parameters are used, move the current values of 
        those parameters to their corresponding actual parameters
    + If a function, move the functional value to a place the caller can get it
    + Restore the execution status of the caller
    + Transfer control back to the caller
    
      Two parts of an executable: Code and Data 
      Layout of non-code part of an executing subprogram is the activation record
      An activation record instance is a concrete example of an activation 
      record (the collection of data for a particular subprogram activation)
    
      An Activation Record for Non-recursive Subprograms:
    
           ,--------------------,
           |  Local variables   |
           |--------------------|
           |   Parameters       |
           |--------------------|
           |   Return Address   |
           '--------------------'
    
      The Code and Activation Records of a Program with "Simple" Subprograms
    
            ,--------------------,
      main  |  Local variables   | \ 
            |====================|  \
        A   |  Local variables   |   \
            |--------------------|    \
            |   Parameters       |     \
            |--------------------|
            |   Return Address   |     DATA
            |====================|
        B   |  Local variables   |      /
            |--------------------|     /
            |   Parameters       |    /
            |--------------------|   /
            |   Return Address   |  /
            |====================|
      main  |                    | \
            |____________________|  \
       A    |                    |   \
            |                    |    CODE
            |____________________|   /
       B    |                    |  /
            |____________________| /
    
    
     o The compiler and linker performs all storage bindings before runtime
     o everything is part of the executable file 
    </pre>
    <SPAN STYLE="Background-Color : #eee;">
    ACTIVATION RECORDS FOR SUBPROGRAMS W/ STACK DYNAMIC VARIABLES 
    </SPAN>
    <pre>
    
    +  an activation record is also known as the "call frame"
    
    +  a more complex activation record is required to support subprograms with 
       stack-dynamic local variables.
    
    +  the compiler must generate code to cause implicit allocation and 
       de-allocation of local variables at runtime
    
    +  an activation record instance is dynamically created when a subprogram is 
       called
    
    +  the activation record format is fixed, but its size may be dynamic
    
    +  the a declaration of a stack dynamic variable does not change the size
       of the executable:
    
    Assume you compile and execute various versions of a program with and without 
    static and dynamic arrays of size 100 ints:
    
           $ gcc ./examples/week10/hw10.c   
           $ size a.out
    
    The results follow. 'Size' provides the size of the text, data and bss segments
    in the executable. The BSS (block starting symbol) segment is the data segment 
    where unitialized static variables go.
    
     <DIV class="Code">
     Stack static array 
     text	   data	    bss	    dec	    hex	filename
     1892	    532	     16	   2440	    988	a.out
    
     Stack dynamic array 
     text	   data	    bss	    dec	    hex	filename
     1940	    532	     16	   2488	    9b8	a.out
    
    
     Static array // note 416 bytes for static array
     text	   data	    bss	    dec	    hex	filename
     1876	    532	    432	   2840	    b18	a.out     
    
     No array 
     text	   data	    bss	    dec	    hex	filename
     1876	    532	     16	   2424	    978	a.out
     </div> </pre>
    
     The runtime environment varies by processor, but the general layout of 
     memory for an executing program on most processors looks like this (the
     stack grows upside down):
      <pre><tt>
      high  memory   ,---------------,
                     |    stack      |
                     |---------------|
                     |      &darr;        |
                     |               |
                     |               |
                     |      &uarr;        |
                     |     heap      |
                     |---------------|
                     |      data     |
                     |---------------|
                     |      code     |
       low memory    '---------------'
    </pre></tt>
    On a Sparc processor much of the runtime stack is loaded into registers -
    stack frames are large because they save register windows. From
    /usr/include/sys/frame.h:  
     <DIV STYLE="border: dashed 1px; width:75%;"> <tt><pre>
          
     /*
      * Copyright (c) 1987-1996, by Sun Microsystems, Inc.
      * All rights reserved.
      */
     
     #ifndef _SYS_FRAME_H
     #define  _SYS_FRAME_H
     
     #pragma ident  "@(#)frame.h  1.15  97/04/25 SMI"  /* sys4-3.2L 1.1 */
     
     #ifdef  __cplusplus
     extern "C" {
     #endif
     
     /*
      * Definition of the sparc call frame 
      */
     struct frame {
     long  fr_local[8];        /* saved locals */
     long  fr_arg[6];          /* saved arguments [0 - 5] */
     struct frame  *fr_savfp;  /* saved frame pointer */
     long  fr_savpc;           /* saved program counter */
     #if !defined(__sparcv9)
      char  *fr_stret;         /* struct return addr */
     #endif                    /* __sparcv9 */
     long  fr_argd[6];        /* arg dump area */
     long  fr_argx[1];        /* array of args past the sixth */
     };
    
     #ifdef _SYSCALL32
    /*
     * Kernels view of a 32-bit stack frame
     */
     struct frame32 {
       int  fr_local[8];      /* saved locals */
       int  fr_arg[6];        /* saved arguments [0 - 5] */
       caddr32_t fr_savfp;    /* saved frame pointer */
       int  fr_savpc;         /* saved program counter */
       caddr32_t fr_stret;    /* struct return addr */
       int  fr_argd[6];       /* arg dump area */
       int  fr_argx[1];       /* array of args past the sixth */
     };
     #endif
    
     #ifdef  __cplusplus
     }
     #endif
     #endif  /* _SYS_FRAME_H */
    </tt></pre>
    </DIV> 
    Stack frames on modern processors
     typically go from high to low memory addresses (the
    stack grows down instead of up). "UP" in normal stack terminology would mean
    moving in the direction of the last item pushed on the stack. But the runtime
    stack grows down, so "UP" moves toward the first item pushed on the stack and
    "DOWN" moves toward the last item pushed on the stack (the top of the stack).
     GDBs frame numbers reflect this: 
    <pre>
    
     #0  fac (n=1) at hw10.c:120
     #1  0x0001090c in fac (n=2) at hw10.c:121
     #2  0x0001090c in fac (n=3) at hw10.c:121
     #3  0x000108bc in main () at hw10.c:114
    </pre>
    <p>
    Terms "activation record" and "stack frame" and "call frame" are interchangeble.
    </p>
    <p>
    Typical Activation Record for a Language with Stack-Dynamic Local Variables 
    and No Recursion: <pre>
    
         ,--------------------, 
         |  Local variables   |                      
         |--------------------|                       
         |   Parameters       |                       
         |--------------------|                       
         |   Dynamic Link     |                      
         |--------------------|
         |   Return Address   |     
         '--------------------' </pre>
    <img src="../Images/stack.jpg" style="height:700px;">
    </p>
    <p>
    <SPAN STYLE="Background-Color : #eee;">
    Dynamic Chain and Local Offset Q & A
    </span>
    </p>
     <li>Q: What is a dynamic link?
    </li>
      The dynamic link (also called frame pointer)
     is an address that points to the top of the activation
      record of the calling procedure. When the current function ends, its
      activation record is popped off - the top of the stack becomes the dynamic 
      link address.
    
    <p>
     <li>Q: Why is a dynamic link necessary?
    </li>
    
      If the size of the local variables are not known at compile time (as is 
      the case of stack dynamic arrays) then the function may need memory past 
      the activation record; i.e., the call frame grows.
       The dynamic link is absolutely critical.
    <p>
     <li>Q: What is the dynamic chain (or call chain)?
    </li>
    
      The collection of dynamic links in the stack at any given time is called 
      the call chain. The call chain traces back through the activation 
      records of each function, ending in main.
    
    <p>
     <li>Q: What is the local offset?
    </li>
    
      Local variables can be accessed by their offset from the beginning of the 
      activation record. This offset is called the local_offset. The local_offset
      of a local variable can be determined by the compiler at compile time.
      
    <p>
     <li>Q: What additonal information is required to support recursion?
    </li>
    
    <p>
      Dynamic stack activation records allow for the possibility of multiple 
      simultaneous activations of the same subprogram (recursion). The stack 
      activation record must also hold the return value from the recursive call.
      Example:
    <pre>
         ----------------------
         |   Return Value     | <= return value from the recursive call 
         |--------------------|
         |  Local variables   |          
         |--------------------|     
         |   Parameters       |      
         |--------------------|     
         |   Dynamic Link     |   
         |--------------------|
         |   Return Address   |
         '--------------------' </pre>
    See runtime stack (<a href="../Code/C/fac.c">fac.c</a> 
     with <a href="../examples/week10/trace.txt">trace</a>)
    </p>
    <p>
    <SPAN STYLE="Background-Color : #eee;">
    IMPLEMENTING NESTED SUBPROGRAMS IN STATIC SCOPED LANGUAGES
    </SPAN>
    </pre>
    <p>
     Note: this is not the same topic as passing a nested subprogram as a 
     parameter (ch. 9 covers that topic)
    </p>
    <p>
     Implementing static scoping in a language that does not support nested 
     subprograms is simple: a variable is either local to its function or has 
     scope across the compilation unit or the executable (blocks are one exception 
     and are discussed below). Binding to global variables is done at compile time.
     A reference to local variable X in function foo is resolved at runtime by 
     using the local_offset to X (which the compiler determined) into foo's 
     activation record. 
    
    <p>
     If a static-scoped language (Fortran 95, Ada, JavaScript, GNU C) uses
     stack-dynamic local variables and allow subprograms to be nested, the problem
     is not so easy. Example: If func1 is nested in func2 and X is declared
     in func2, then resolving a reference to X in func1
      means binding func1:X to func2:X in the call frame of func2.
    
    <p>
     The problem becomes one of locating
      a non-static non-local reference in another frame on
     the stack. You first must find the correct activation record instance and
     then determine the correct offset within that activation record instance.
    </p>
    <p>
     Static semantic rules guarantee that all non-local variables that can be 
     referenced have been allocated in some activation record instance that is 
     on the stack when the reference is made; i.e., if function foo is nested in 
     function foobar, foo will never be called unless foobar is called first.
    <p>
    
    <em>Static Chain Method.</em>
    <br>
     Static chains are the primary method of implementing accesses to non-local 
     variables in static-scoped languages with nested subprograms.
      A static chain is a chain of static links that connects certain activation
     record instances. The static chain from an activation record instance 
     connects it to all of its static ancestors.
    The static link in an activation record instance for subprogram A points 
     to one of the activation record instances of A's static parent.
    <p>
    
     A static link is added to the activation record in addition to a
      dynamic link. Access to nonlocals is a (chain_offset,local_offset) pair
     that is known at compile time.
     The actual name of the variable is not needed to find the value on the stack.
    <pre>
     Example Pascal Program:
    
    program MAIN_2;
    |   var X : integer;
    |
    |   procedure BIGSUB;
    |   |  var A, B, C : integer;
    |   |
    |   |  procedure SUB1;
    |   |  |  var A, D : integer;
    |   |  |  begin 
    |   |  |      A := B + C;  #1 references A in SUB1 (0,2)
    |   |  |_ end;  { SUB1 }
    |   |
    |   |  procedure SUB2(X : integer);
    |   |  |  var B, E : integer;
    |   |  |
    |   |  |  procedure SUB3;
    |   |  |  |  var C, E : integer;
    |   |  |  |  begin { SUB3 }
    |   |  |  |    SUB1;
    |   |  |  |    E := B + A:    #2 references A in BIGSUB (2,3) 
    |   |  |  |_ end; { SUB3 }
    |   |  |
    |   |  |  begin { SUB2 }
    |   |  |    SUB3;
    |   |  |    A := D + E;       #3 references A in BIGSUB (1,3) 
    |   |  |_ end; { SUB2 }
    |   |
    |   |  begin { BIGSUB }
    |   |    SUB2(7);
    |   |_ end; { BIGSUB }
    |
    |   begin
    |     BIGSUB;
    |_  end; { MAIN_2 }
    
      Call sequence for MAIN_2
      
           MAIN_2 calls BIGSUB
           BIGSUB calls SUB2
           SUB2 calls SUB3
           SUB3 calls SUB1
    
     The static scoping of the above code displayed graphically:
    
     ,---------------------------------------,
     |   MAIN_2                              |  
     |   var X                               | 
     |  ,--------------------------------,   |
     |  | BIGSUB                         |   |
     |  | var A, B, C                    |   |
     |  |  ,------------------------,    |   |
     |  |  | SUB1                   |    |   |
     |  |  | var A, D               |    |   |
     |  |  | A  = B + C    <== 1    |    |   |
     |  |  '------------------------'    |   |
     |  |                                |   |
     |  |  ,-------------------------,   |   |
     |  |  | SUB2( X )               |   |   |
     |  |  | var B, E                |   |   |
     |  |  |  ,-----------------,    |   |   |
     |  |  |  | SUB3            |    |   |   |
     |  |  |  | var C, E        |    |   |   |
     |  |  |  | SUB1;           |    |   |   |
     |  |  |  | E = B + A  <==2 |    |   |   |
     |  |  |  '-----------------'    |   |   |
     |  |  |                         |   |   |
     |  |  | SUB3;                   |   |   |
     |  |  | A = D + E;  <== 3       |   |   |
     |  |  '-------------------------'   |   |
     |  | SUB2(7);                       |   |   
     |  '--------------------------------'   |
     |  BIGSUB;                              |
     '---------------------------------------'
        
    MAIN_2 calls BIGSUB
    BIGSUB calls SUB2
    SUB2 calls SUB3
    SUB3 calls SUB1
    
    The chain_offset/local_offset pairs for each access to A are: 
    (where chain_offset is the nesting depth)
     1 => (0,2)   // variables are counted starting at one from right to left  
     2 => (2,3)  
     3 => (1,3)
    </pre>
    A local_offset of 3 references the first local variable in SUB1 
    Stack Contents at Position 1 in Main_2: <br>
    <img src="../Images/stack2.jpg" style="width:800px;"><br/>
    fig. 10.9
    </p>
    <p> 
    Note that each static link points to the bottom of the prior activation
     record in the chain.
    </p>
    <p>
    <em>Display Method.</em>
    <br>
    An alternative to static chains is a "display". In this implementation
     static links are NOT stored in the activation record but in a single array.
     The contents of the display at any given time is a list of addresses of 
     the accessible activation record instances.
     Accesses to nonlocals require exactly two steps for every access:
     display_offset + local_offset takes you directly to the address.
     Displays not widely used in modern languages.
    </p>
    <p>
    <SPAN STYLE="Background-Color : #eee;">
    IMPLEMENTING BLOCKS
    </SPAN>
    <p>
      Blocks are user-specified local scopes for variables (similar to static
      scoping of nested subprograms).  An example in C:
    <pre>
      int x = 3;
      {
        int x = 5;
      }
    </pre>
    <p>
      The lifetime of inner x begins when control enters the block and ends
      when control exits the block; the scope of inner x is within block only.
      Blocks must
     be implemented so that access to x does not interfere with the variable x 
      in another scope. There are two primary methods to implement blocks.
    </p>
    <p>
    <em>Static Chain Method</em>. <br/>
     Access is by static chain process as done with nested subroutines.
          Treat blocks as parameter-less subprograms that are always called 
          from the same location.
          Each block has an activation record; i.e.,
      an instance is created each time the block is executed.
    <p>
    <em>Stack Method</em>. <br>
    Since the maximum storage required for a block can be statically 
       determined, this amount of space can be allocated after the local 
       variables in the activation record; each block is a "static" part of 
       the AR of the procedure it belongs to (ANSI C does this); block
       variables are pushed and popped off a "stack" of locals in that area; 
       access to a variable is resolved to the most recent instance of that
          variable on the stack <a href="../Code/C/blocks.c">see code</a>
          Example: What happens at reference d = 5?
    <pre>
    ____________________________     
    |main ()                    |       
    |  int d,  e                |     e <- stack top               
    | _______________________   |     d <- reference is resolved to first d 
    | |  while ()            |  |     d 
    | |  int a, b, c         |  |     c 
    | |  __________________  |  |     b 
    | |  | while ()       |  |  |     a 
    | |  | int d, e,      |  |  |     e 
    | |  | d = 5;         |  |  |  => d 
    | |  |________________|  |  |  THE STACK
    | |                      |  | 
    | |______________________|  |
    |                           |
    |  ______________________   |     f 
    |  |                     |  |     e  
    |  | while ()            |  |     e
    |  | int e, f            |  |     d
    |  |_____________________|  | THE STACK
    |___________________________| 
    </pre> </pre>
    
    <SPAN STYLE="Background-Color : #eee;">
    <B>IMPLEMENTING DYNAMIC SCOPING</B>
    </SPAN>
    
    <p><li> 
     dynamic scoping is not limited to languages with nested subroutines
    
    <p><li> 
     Access to non-local variables in dynamic-scoped languages can be 
     implemented in at least two ways (deep access and shallow access)
    
    <p><li> 
    <i>The semantics for deep and shallow access is identical</i>
    </p>
    <p>
    <em>Deep Access Method.</em> 
    <br>
     In deep access, access to nonlocal variables is facilitated by tracing 
      the scope all the way back to the first instance of 
      the variable in the call chain. The call chain consists of the 
      dynamic links (frame pointers) that are used to maintain the runtime
     stack; i.e., a non-local reference is bound to an address in some 
      activation record on the dynamic chain.
    </p>
    <p> 
      This method is
     similar to <i>static chain</i> access in nested subroutine but using
     the dynamic link and not the static link. 
    </p> 
    <p>
      Each dynamic link points to the top of the activation record instance of 
      the calling procedure and to the bottom of the activation record
     instance of the callee procedure.
    </p>
    <pre>Example: 
         void sub3() {
           int x, z
           x = u + v;
           ...
         }
         void sub2() {
           int w, x
           ...
         }
         void sub1() {
            int v, u;
            ...
         }
    
         void main() {
            int v, u, y;
            ....
         }
    
      Stack: 
    + -------+
    |  sub3  |
    |  x z   |
    | x= u+y | 
    +--------+
    |  sub2  |
    |  w x   |
    +--------+
    |  sub1  |
    |  v u   |
    +--------+
    |  sub1  |
    |  v u   |
    +--------+
    |  main  |
    |  v u y |
    +--------+
    
    What happens when sub3 references x, u, and y?
    
     By dynamic scoping the dynamic chain offset from sub3:
     Access to x is 0 to sub3
     Access to u is 2 to sub1
     Access to y is 4 to main  
    </pre>
    
    <p>
     <em>Shallow Access Method.</em> 
    <br> 
      In shallow access, a data structure separate from the runtime stack
      maintains a trace of the variables. Each variable has its own stack. 
      Access to a nonlocal variable means that the array of variable stacks is 
      searched. The top of the stack holds the most recent instantiation of that 
      variable, and is used. 
    </p>
    <p>
     The semantics is identical semantics to that of deep access but
     in this method you put 
     locals in a central table with an entry for each variable name.
     Each variable adds a stack entry for each instantiation .
     Example implementation of Shallow Access for Dynamic Scoping for same code: 
    <pre>
     --------------
     | sub1 | sub1 |
     ---------------               -------
     | sub1 | sub1 |               | sub3 |
     ---------------------------------------------
     | main | main |  main |  sub2 | sub2 | sub3 |   
     ---------------------------------------------
       v        u       y       w      x    z 
    
     From sub3
     Access to x is to sub3
     Access to u is to sub1 
     Access to y is to main 
    </pre>
     A comparison:
     Deep access provides faster subprogram linkage but slower access to
     nonlocals.
     Shallow access provides faster access to nonlocals but slower
     subprogram linkage.
    </div>
    <pre>
    
    
    </pre>
    </body>
    </html>
    