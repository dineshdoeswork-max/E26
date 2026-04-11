#9.2

# Import necessary tools from the pydantic library
from pydantic import BaseModel, Field, field_validator, ValidationError

# 1. Define the rules for our data model
class StudentRegistration(BaseModel):
    name: str = Field(min_length=3)  # Name must be a string and at least 3 letters long
    roll_number: str = Field(pattern=r"^\d{10}$")  # Must be exactly 10 digits (0-9)
    email: str  # Email must be a string (we check the domain below)
    age: int = Field(ge=17, le=22)  # Age must be Greater than/Equal to 17 and Less than/Equal to 22
    percentage_12th: float = Field(ge=35.0, le=100.0)  # Decimal number between 35 and 100

    # Custom rule to check if the email ends with specific institution domains
    @field_validator('email')
    @classmethod
    def validate_email_domain(cls, v):
        # Check if the email ends with either of the two allowed domains
        if not (v.endswith("@vitstudent.ac.in") or v.endswith("@nitt.edu")):
            raise ValueError("Invalid Email Domain")  # Throw an error if it doesn't match
        return v  # Return the email if it is valid

# 2. A helper function to process and test data
def test_registration(data):
    try:
        StudentRegistration(**data)  # Try to "fit" the data into our model
        print(f"✅ Valid Student: {data['name']}")  # Runs if data follows all rules
    except ValidationError as e:
        print(f"❌ Error for {data.get('name', 'Unknown')}:")  # Runs if rules are broken
        for error in e.errors():  # Loop through every specific mistake found
            print(f"  - {error['loc'][0]}: {error['msg']}")

# 3. Create lists of test cases (3 correct, 3 incorrect)
correct_inputs = [
    {"name": "Alice", "roll_number": "1234567890", "email": "alice@nitt.edu", "age": 20, "percentage_12th": 85.5},
    {"name": "Bob Smith", "roll_number": "2110101234", "email": "bob@vitstudent.ac.in", "age": 18, "percentage_12th": 92.0},
    {"name": "Charlie", "roll_number": "9998887776", "email": "charlie@nitt.edu", "age": 22, "percentage_12th": 35.0}
]

incorrect_inputs = [
    {"name": "Al", "roll_number": "123", "email": "wrong@gmail.com", "age": 25, "percentage_12th": 30.0}, # Too short, wrong email, wrong age
    {"name": "Dave", "roll_number": "1234567890", "email": "dave@nitt.edu", "age": 16, "percentage_12th": 80.0}, # Age too young
    {"name": "Eve", "roll_number": "A1B2C3D4E5", "email": "eve@nitt.edu", "age": 19, "percentage_12th": 105.0} # Not digits, % too high
]

# 4. Run the tests and print results to the console
print("--- TESTING CORRECT INPUTS ---")
for item in correct_inputs: test_registration(item)

print("\n--- TESTING INCORRECT INPUTS ---")
for item in incorrect_inputs: test_registration(item)