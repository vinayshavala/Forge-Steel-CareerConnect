# Security notes for portfolio publication

- The exposed token in `form.js` was replaced with a placeholder. Rotate the original token with the provider if it was genuine. Do not put replacement secrets in browser-side JavaScript.
- Do not deploy the backend with real student records until every student-data endpoint has authentication, role-based authorization, input validation, and appropriate response-field filtering.
- Screenshots and upload media were excluded pending review for personal data.
- The `ResumeATS/results.html` page points to an externally hosted service; confirm ownership, permission, and data handling before using it.
- This archive has no original Git history, so removed secrets in earlier commits could not be checked.
