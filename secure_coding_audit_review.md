#  Secure Coding Review — CodeAlpha Task 3
##  Project: User Registration and Login System (Python)
##  Identified Vulnerabilities:
## 1.  Plain Text Password Storage
- **Issue**: Passwords are stored in `users.txt` as plain text.
- **Risk**: Anyone with file access can read user passwords.
- **Fix**: Implement password hashing using `bcrypt`.

...

### 2.  No Input Validation
- **Issue**: Username and password fields accept any input, including empty values.
- **Risk**: Can lead to login bypass, malformed data, or even injection.
- **Fix**: Add checks to ensure fields are not empty and properly formatted.

....

### 3.Duplicate Username Allowed
- **Issue**: The system does not check if a username is already registered.
- **Risk**: Overwriting or confusion during login.
- **Fix**: Validate against existing usernames before registering.

....

### 4. No Password Hashing
- **Issue**: Passwords are directly compared in plain text.
- **Risk**: Makes it easier for attackers to reverse-engineer credentials.
- **Fix**: Use `bcrypt.checkpw()` for secure comparison.

....

### 5. Weak Error Handling
- **Issue**: Code might crash if `users.txt` has corrupted lines.
- **Risk**: Application failure and potential info leakage.
- **Fix**: Wrap critical logic in `try/except` blocks.

....

## Secure Practices Implemented (in Fixed Code):
- Password hashing using `bcrypt`
- Duplicate check during registration
- Input validation and error handling
- Safe file read/write operations

....

##  Author: Ariba Abbasi  
**CodeAlpha Cyber Security Intern**
