"""
====================================================================
 COS202 ASSIGNMENT - SOLUTION 2
 PROJECT      : Mathematical Calculator (MC)
 LANGUAGE     : Python 3
 DESCRIPTION  : A simple, interactive, screen-based calculator that
                supports Addition, Subtraction, Multiplication,
                Division, Floor Division, Exponentiation, Modulus,
                Clear, and Off (Exit) operations.
====================================================================
"""

# ---------------------------------------------------------------
# SECTION 1: HELPER / DISPLAY FUNCTIONS
# ---------------------------------------------------------------

def show_header():
    """
    Prints the calculator's title banner.
    This runs once when the program starts, and again whenever
    the screen is 'cleared' (C option), to keep the interface
    looking clean and professional.
    """
    print("=" * 50)
    print("      SIMPLE MATHEMATICAL CALCULATOR (MC)".center(50))
    print("=" * 50)


def show_menu():
    """
    Displays the list of operations available to the user.
    Keeping this in its own function means we can call it
    repeatedly inside the main loop without repeating code
    (this follows the DRY principle - Don't Repeat Yourself).
    """
    print("\nAvailable Operations:")
    print("  +  -> Addition")
    print("  -  -> Subtraction")
    print("  *  -> Multiplication")
    print("  /  -> Division")
    print("  \\ -> Floor Division (whole-number division)")
    print("  ^  -> Exponent (power)")
    print("  %  -> Modulus (remainder)")
    print("  C  -> Clear screen")
    print("  OFF-> Exit the calculator")
    print("-" * 50)


def get_number(prompt):
    """
    Safely collects a numeric value from the user.

    WHY THIS FUNCTION EXISTS:
    Users can accidentally type letters or symbols instead of
    numbers. Rather than letting the program crash, we use a
    loop + try/except block to keep asking until valid input
    is given. This is what the assignment calls 'proper input
    validation'.
    """
    while True:
        raw_value = input(prompt).strip()
        try:
            # Try converting to a float first so decimals (e.g. 3.5)
            # are supported, not just whole numbers.
            return float(raw_value)
        except ValueError:
            print("  [Error] That is not a valid number. Please try again.")


# ---------------------------------------------------------------
# SECTION 2: CORE ARITHMETIC OPERATIONS
# ---------------------------------------------------------------
# Each operation lives in its own small function. This is called
# "modular" programming: every function does ONE clear job, which
# makes the code easier to read, test, and maintain.

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """
    Regular division. We must guard against division by zero,
    which is mathematically undefined and would otherwise crash
    the program with a ZeroDivisionError.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


def floor_divide(a, b):
    """
    Floor division (the assignment's '\\' symbol) returns the
    whole-number part of a division, discarding the remainder.
    Example: 7 // 2 = 3
    """
    if b == 0:
        raise ZeroDivisionError("Cannot floor-divide by zero.")
    return a // b


def exponent(a, b):
    """Raises 'a' to the power of 'b' (a ** b)."""
    return a ** b


def modulus(a, b):
    """
    Returns the remainder after dividing 'a' by 'b'.
    Example: 7 % 2 = 1
    """
    if b == 0:
        raise ZeroDivisionError("Cannot perform modulus with zero.")
    return a % b


# ---------------------------------------------------------------
# SECTION 3: MAIN PROGRAM LOOP
# ---------------------------------------------------------------

def main():
    """
    This is the entry point of the program. It repeatedly shows
    the menu, reads the user's chosen operation, performs the
    calculation, and loops back - until the user selects OFF.
    """
    # Dictionary mapping each symbol to its function.
    # This avoids a long chain of if/elif statements and makes
    # it easy to add new operations later.
    operations = {
        "+": ("Addition", add),
        "-": ("Subtraction", subtract),
        "*": ("Multiplication", multiply),
        "/": ("Division", divide),
        "\\": ("Floor Division", floor_divide),
        "^": ("Exponent", exponent),
        "%": ("Modulus", modulus),
    }

    show_header()

    while True:
        show_menu()
        choice = input("Select an operation (or C / OFF): ").strip()

        # ---- Handle CLEAR ----
        if choice.upper() == "C":
            # Clear the terminal screen for a fresh look.
            print("\n" * 50)  # portable "clear" that works everywhere
            show_header()
            continue

        # ---- Handle OFF (Exit) ----
        if choice.upper() == "OFF":
            print("\nThank you for using the Mathematical Calculator. Goodbye!")
            break

        # ---- Handle a valid arithmetic operation ----
        if choice in operations:
            name, func = operations[choice]
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            try:
                result = func(num1, num2)
                print(f"\n  [{name}] Result: {num1} {choice} {num2} = {result}")
            except ZeroDivisionError as error:
                # Friendly, specific error handling as required by
                # the assignment (division by zero).
                print(f"\n  [Error] {error}")
        else:
            # ---- Handle invalid menu input ----
            print("\n  [Error] Invalid choice. Please select a valid option "
                  "from the menu.")


# Standard Python entry-point guard: this ensures main() only runs
# when this file is executed directly (not when imported elsewhere).
if __name__ == "__main__":
    main()
