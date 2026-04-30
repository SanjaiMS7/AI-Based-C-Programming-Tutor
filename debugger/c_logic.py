def process_query(query):
    q = query.lower()

    # Pointers
    if "pointer" in q:
        return "Pointer: stores memory address of a variable.\nExample: int *p = &x;"

    # Double pointer
    elif "double pointer" in q:
        return "Double Pointer: pointer to another pointer.\nExample: int **pp = &p;"

    # Loop
    elif "loop" in q:
        return "Loop: repeats code.\nTypes: for, while, do-while."

    # Array
    elif "array" in q:
        return "Array: stores multiple values of same type.\nExample: int a[5];"

    # Recursion
    elif "recursion" in q:
        return "Recursion: function calls itself.\nUsed in factorial, tree problems."

    # Memory
    elif "malloc" in q or "memory" in q:
        return "malloc: dynamic memory allocation.\nfree(): releases memory."

    # File
    elif "file" in q:
        return "File handling: fopen, fprintf, fscanf, fclose."

    # Error
    elif "segmentation" in q:
        return "Segmentation fault: accessing invalid memory."

    # Program
    elif "program" in q or "code" in q:
        return "#include<stdio.h>\nint main(){printf(\"Hello\");}"

    else:
        return "Ask about pointers, loops, arrays, memory, recursion."