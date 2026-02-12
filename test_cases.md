# Test Cases - Login System

| Test Case ID | Scenario | Input | Expected Output |
|--------------|----------|--------|----------------|
| TC01 | Valid login | admin / 1234 | Login Successful |
| TC02 | Invalid password | admin / 0000 | Invalid Credentials |
| TC03 | Empty username | "" / 1234 | Fields cannot be empty |
| TC04 | Empty password | admin / "" | Fields cannot be empty |
| TC05 | Both empty | "" / "" | Fields cannot be empty |
| TC06 | Password too short | admin / 12 | Password too short |
