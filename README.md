#  Secure Coding Review — CodeAlpha Task 3

Hey! I'm Ariba Abbasi, and this is my submission for Task 3 of the **CodeAlpha Cyber Security Internship**. The goal was to analyze insecure code, find the flaws, and apply secure coding practices to fix it.

##  What This Project Is

It’s a simple Python-based **user registration + login system** — but the original version was full of security issues (like storing passwords in plain text ). So, I reviewed the code, identified vulnerabilities, and rewrote it using more secure practices like password hashing, input validation, and better error handling.

##  Vulnerabilities I Found

| # | Issue                            | Why It’s a Problem                    | What I Did to Fix It                 |
|...|..................................|.......................................|......................................|
| 1 | Plain text password storage      | Super risky — anyone can read them    | Used `bcrypt` to hash passwords      |
| 2 | No input validation              | Could allow empty or bad data         | Added basic validation checks        |
| 3 | No duplicate user check          | Same user can register 10 times       | Now checks before saving             |
| 4 | Insecure password comparison     | Easy to bypass with string match      | Replaced with secure `bcrypt` check  |
| 5 | Weak error handling              | Could crash the app                   | Wrapped logic in `try/except`        |


##  Secure Stuff I Added

- 'bcrypt' for hashing passwords   
- Input checks to stop blank or weird inputs  
- Blocked duplicate usernames  
- Better file reading and error messages  
- Clean, readable code that’s easier to maintain

## What’s in this Repo

 CodeAlpha_SecureCodingReview/
├── vulnerable_user_system.py               # The insecure version (for audit)
├── secure_version_login_register_system.py # The improved, secure version
├── Secure_Coding_Review_Task3.md           # Audit report detailing vulnerabilities & fixes
└── README.md                               # You're reading it!

##  About Me

I'm Ariba Abbasi, currently working as a **Cyber Security Intern** with **CodeAlpha**.  
This task helped me understand how even simple apps can have serious flaws — and how secure coding can protect user data and prevent breaches. I’m excited to keep learning and growing in this field! 

-  GitHub: https://github.com/aribacodes  
-  LinkedIn: www.linkedin.com/in/ariba-abbasi-936983360

## Task Status
 Completed and Submitted  
Thanks for checking out my project — feedback is always welcome!
