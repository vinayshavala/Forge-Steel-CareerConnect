# Forge Steel – CareerConnect: AI-Powered Campus Placement Portal

**Project type:** Final-year academic major project | **Team:** Four members

CareerConnect is a web-based campus placement and career-preparation platform intended to support students, training and placement officers, and recruiters. The project brings together aptitude practice, coding assessments, mock interview workflows, resume building/ATS analysis, announcements, and dashboards.

> **Academic prototype notice:** This repository is a student team project and is not production-ready. Do not deploy it with real student data. Authentication/authorization, privacy controls, API credential handling, and security testing must be reviewed before any public deployment.

## Main modules

- Student, administrator, and company-facing pages
- Aptitude tests and performance dashboards
- Coding practice and performance tracking
- Mock interview module
- Resume builder and ATS analysis module
- Announcements and placement information

## Technology mentioned in the project

HTML, CSS, JavaScript, Node.js, Python, Streamlit, MongoDB, and selected computer-vision / machine-learning libraries. Individual modules may have separate setup requirements; see their source files and dependency manifests.

## Team and contributions

This project was developed collaboratively by a four-member academic team. Add team members' names/links only with their agreement.

- **Your Name (@YOUR_GITHUB_USERNAME):** Replace this line with your actual contribution (specific modules, code, testing, documentation, or integration you personally completed).
- **Team member 2:** Add verified contribution, with permission.
- **Team member 3:** Add verified contribution, with permission.
- **Team member 4:** Add verified contribution, with permission.

Please describe only work you personally completed. Credit external templates, libraries, and reused code where applicable.

## Setup overview

### Prerequisites

- Node.js and npm
- Python 3 and pip
- MongoDB, if using database-backed modules
- Any module-specific API credentials configured locally

### Node.js backend

1. Install dependencies with `npm install`.
2. Create a local `.env` file for configuration; never commit it.
3. Configure `MONGO_URI` and any required credentials locally.
4. Start with `npm start`.

The backend and modules may need additional setup or fixes; the original project contains several independently run components. Verify each module before relying on these instructions.

### Python / Streamlit modules

Install the dependencies required by the relevant module and run its Streamlit entry point from that module's directory. Check the source code for exact filenames and package requirements.

## Security and privacy notes

- Never commit real API keys, passwords, database URLs containing credentials, or personal information.
- A previously embedded third-party API token has been replaced with a placeholder in this portfolio copy. The related country/state/city lookup may not work until it is reconfigured safely. Rotate the original token with its provider if it was real.
- Screenshot and upload-media folders were omitted from this portfolio copy because they may contain personal or identifying information. Add only reviewed, anonymized screenshots later.
- This is not a production security audit. In particular, verify authentication and authorization on every endpoint that reads, changes, or deletes student records before deployment.
- The ATS results page in the original project referenced an externally hosted application. Verify permission, ownership, and privacy practices before relying on external services.

## License and third-party material

The source archive includes an MIT licence file. Before redistributing, confirm that the team has authority to apply it to all project code and that any third-party assets/code retain their required attribution and licences.

## Repository note

This is a cleaned portfolio copy of a collaborative academic project. It intentionally excludes dependency folders, IDE metadata, uploaded preview media, and screenshots pending privacy review. These removals do not imply that the application has been fully tested or made production-safe.
