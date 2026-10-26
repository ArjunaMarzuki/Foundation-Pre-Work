"""
Programming Fundamentals for IC Design and EDA Workflows
Companion Python examples for the 2-hour training module.

These examples use simulated data for learning. They do not run real EDA tools.
Run with Python 3.
"""

# 1. Variables, data types, and operators
design_name = "Core_Block"
cell_count = 1200
clock_mhz = 500.0
design_ready = True

print("Design:", design_name)
print("Cell count:", cell_count)
print("Clock frequency:", clock_mhz, "MHz")
print("Ready:", design_ready)
print("Large design?", cell_count > 1000)


# 2. Conditional statements
timing_slack = -0.05

if timing_slack > 0:
    print("Positive timing margin")
elif timing_slack == 0:
    print("No timing margin")
else:
    print("Timing violation")


# 3. Loops
blocks = ["CPU", "Memory", "Controller"]

for block in blocks:
    print("Checking:", block)

attempt = 1
while attempt <= 3:
    print("Run", attempt)
    attempt += 1


# 4. Functions
def classify_design(cell_count):
    """Return a simple design-size category using an example threshold."""
    if cell_count > 1000:
        return "Large design"
    return "Small design"


print(classify_design(1200))


# 5. Reading and modifying source code
def report_design(name, count):
    print("Design:", name)
    print("Cell count:", count)
    if count > 1000:
        print("Category: Large")
    else:
        print("Category: Small")


report_design("Block_A", 800)


# 6. Mini-project: process multiple simulated design records
def check_design(name, cell_count, clock_mhz):
    print("\\nDesign:", name)
    print("Cell count:", cell_count)
    print("Clock:", clock_mhz, "MHz")

    if cell_count > 1000:
        print("Size: Large")
    else:
        print("Size: Small")


designs = [
    ("Block_A", 800, 400),
    ("Block_B", 1500, 500),
    ("Block_C", 600, 300),
]

for design in designs:
    check_design(design[0], design[1], design[2])


# Practice:
# - Change the size threshold from 1000 to 700.
# - Add a fourth design record.
# - Try timing_slack values of 0.15, 0.0, and -0.05.
