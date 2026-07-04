"""
====================================================================
 COS202 ASSIGNMENT - SOLUTION 3
 PROJECT      : Personal Pocket CGPA Calculator (PPC)
 LANGUAGE     : Python 3
 DESCRIPTION  : Uses SELECTION CONTROL STATEMENTS (if / elif / else)
                to convert course scores into grade points, then
                calculates Quality Points, Total Credit Units,
                GPA, CGPA, and the resulting Class of Degree -
                all from the palm of your hand, without visiting
                AVERS.
 GRADING SCALE: Standard 5-point Nigerian university scale
                A (70-100) = 5.0
                B (60-69)  = 4.0
                C (50-59)  = 3.0
                D (45-49)  = 2.0
                E (40-44)  = 1.0
                F (0-39)   = 0.0
====================================================================
"""

# ---------------------------------------------------------------
# SECTION 1: INPUT VALIDATION HELPERS
# ---------------------------------------------------------------

def get_positive_int(prompt):
    """
    Repeatedly asks the user for a whole number greater than zero.
    Used for 'number of courses' and 'credit unit', where negative
    or non-numeric values would not make sense.
    """
    while True:
        raw_value = input(prompt).strip()
        try:
            value = int(raw_value)
            if value <= 0:
                print("  [Error] Please enter a whole number greater than zero.")
                continue
            return value
        except ValueError:
            print("  [Error] That is not a valid whole number. Try again.")


def get_score(prompt):
    """
    Repeatedly asks for a course score and ensures it is a number
    between 0 and 100 (inclusive), since scores outside that range
    are not valid academic scores.
    """
    while True:
        raw_value = input(prompt).strip()
        try:
            score = float(raw_value)
            if score < 0 or score > 100:
                print("  [Error] Score must be between 0 and 100.")
                continue
            return score
        except ValueError:
            print("  [Error] That is not a valid number. Try again.")


def get_course_title(prompt):
    """
    Ensures the course title entered is not left empty.
    """
    while True:
        title = input(prompt).strip()
        if title == "":
            print("  [Error] Course title cannot be empty.")
            continue
        return title


# ---------------------------------------------------------------
# SECTION 2: GRADING LOGIC (SELECTION CONTROL STATEMENTS)
# ---------------------------------------------------------------

def score_to_grade_point(score):
    """
    Converts a numeric score (0-100) into a letter grade and its
    corresponding grade point, using if / elif / else - exactly
    as required by the assignment ("powerful provision of
    selection control statements").

    Returns a tuple: (letter_grade, grade_point)
    """
    if score >= 70:
        return "A", 5.0
    elif score >= 60:
        return "B", 4.0
    elif score >= 50:
        return "C", 3.0
    elif score >= 45:
        return "D", 2.0
    elif score >= 40:
        return "E", 1.0
    else:
        return "F", 0.0


def cgpa_to_class_of_degree(cgpa):
    """
    Determines the student's class of degree from their CGPA,
    again using if / elif / else selection statements, based on
    the standard 5-point classification.
    """
    if cgpa >= 4.50:
        return "First Class Honours"
    elif cgpa >= 3.50:
        return "Second Class Honours (Upper Division)"
    elif cgpa >= 2.40:
        return "Second Class Honours (Lower Division)"
    elif cgpa >= 1.50:
        return "Third Class Honours"
    elif cgpa >= 1.00:
        return "Pass"
    else:
        return "Fail"


# ---------------------------------------------------------------
# SECTION 3: MAIN PROGRAM
# ---------------------------------------------------------------

def main():
    print("=" * 60)
    print("     PERSONAL POCKET CGPA CALCULATOR (PPC)".center(60))
    print("=" * 60)
    print("No need to visit AVERS - carry your CGPA in your pocket!\n")

    # ---- Step 1: Number of courses ----
    number_of_courses = get_positive_int("Enter the number of courses offered: ")

    courses = []          # will hold a dictionary for every course
    total_quality_points = 0.0
    total_credit_units = 0

    # ---- Step 2: Collect details for each course ----
    for index in range(1, number_of_courses + 1):
        print(f"\n--- Course {index} of {number_of_courses} ---")
        title = get_course_title("Course title: ")
        credit_unit = get_positive_int("Credit unit (e.g. 2, 3): ")
        score = get_score("Score obtained (0-100): ")

        # Selection statements do the grade conversion here:
        grade_letter, grade_point = score_to_grade_point(score)

        # Quality Point = Grade Point x Credit Unit
        quality_point = grade_point * credit_unit

        # Keep a running total for GPA calculation
        total_quality_points += quality_point
        total_credit_units += credit_unit

        # Store this course's full record for the summary table
        courses.append({
            "title": title,
            "credit_unit": credit_unit,
            "score": score,
            "grade_letter": grade_letter,
            "grade_point": grade_point,
            "quality_point": quality_point,
        })

    # ---- Step 3: Calculate GPA ----
    # GPA = Total Quality Points / Total Credit Units
    if total_credit_units == 0:
        # Defensive check - should not normally happen since credit
        # units are validated to be > 0, but guards against a
        # divide-by-zero crash regardless.
        print("\n[Error] Total credit units cannot be zero. Cannot compute GPA.")
        return

    gpa = total_quality_points / total_credit_units

    # NOTE: In this simplified single-semester tool, CGPA is treated
    # as equal to the computed GPA (since only one semester's worth
    # of results is entered). A full multi-semester version would
    # accumulate quality points and credit units across semesters.
    cgpa = gpa

    class_of_degree = cgpa_to_class_of_degree(cgpa)

    # ---- Step 4: Display the full breakdown ----
    print("\n" + "=" * 60)
    print("                 RESULT SUMMARY".center(60))
    print("=" * 60)
    print(f"{'Course':<20}{'C.U.':<6}{'Score':<8}{'Grade':<7}{'G.P.':<6}{'Q.P.':<6}")
    print("-" * 60)
    for course in courses:
        print(f"{course['title']:<20}"
              f"{course['credit_unit']:<6}"
              f"{course['score']:<8}"
              f"{course['grade_letter']:<7}"
              f"{course['grade_point']:<6}"
              f"{course['quality_point']:<6}")
    print("-" * 60)
    print(f"Total Credit Units   : {total_credit_units}")
    print(f"Total Quality Points : {total_quality_points}")
    print(f"GPA                  : {gpa:.2f}")
    print(f"CGPA                 : {cgpa:.2f}")
    print(f"Class of Degree      : {class_of_degree}")
    print("=" * 60)
    print("\nThank you for using PPC. Study smart, stay ahead!")


if __name__ == "__main__":
    main()
