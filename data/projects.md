# Pratyush Maurya — Developer Knowledge Base

> **Comprehensive Technical Profile for Personal Digital Twin / RAG System**
> Generated: June 2026 | Developer: pratyushmaurya01 | Purpose: AI-readable knowledge base for RAG chatbot

---

## Table of Contents

1. [High-Priority Projects](#high-priority-projects)
   - [Quiesy — Assessment Platform](#1-quiesy--assessment-platform)
   - [Project ARIES](#2-project-aries)
   - [Tic Tac Toe BOT](#3-tic-tac-toe-bot)
   - [Fake Job Detection](#4-fake-job-detection)
   - [Blog Project](#5-blog-project)
2. [Developer Profile](#developer-profile)
3. [Technical Skills Assessment](#technical-skills-assessment)
4. [Learning Journey](#learning-journey)
5. [Project Index & Ranking](#project-index--ranking)
6. [Digital Twin Summary](#digital-twin-summary)

---

# High-Priority Projects

---

## 1. Quiesy — Assessment Platform

**Priority:** HIGH | **Complexity:** ADVANCED | **Status:** Active Development

### Project Summary

Quiesy is a sophisticated full-stack assessment platform designed for educators, trainers, and bootcamps to create, manage, and evaluate quizzes and coding challenges. The platform provides a dual-mode experience:

- **Student Interface:** Clean, distraction-free UI for taking assessments
- **Teacher Dashboard:** Powerful content creation and analytics tools

Supports MCQ, MSQ, subjective questions, and live coding challenges with real-time code execution. Features include hidden test cases, analytics-driven performance insights, and secure access management through quiz codes and optional passwords.

**Stack:** React + Vite (frontend) · Django REST Framework (backend) · JWT Authentication · PostgreSQL · Monaco Editor · Netlify (deployment)

---

### Problem Statement

Educational institutions and training bootcamps struggle with assessment tools that:

- Lack support for both MCQ and coding challenges in a unified platform
- Provide poor user experience with distractions or clunky interfaces
- Don't support hidden test cases for fair code evaluation
- Lack comprehensive analytics for educator insights
- Don't provide secure, shareable assessment links with access control

---

### Key Features

#### For Educators / Teachers

| Feature                  | Description                                                       |
| ------------------------ | ----------------------------------------------------------------- |
| Multiple Question Types  | MCQ, MSQ, subjective, and coding questions in a single quiz       |
| Hidden Test Cases        | Auto-evaluate student code without revealing test cases           |
| Secure Quiz Distribution | Unique UUID quiz codes with optional password protection          |
| Quick Sharing            | One-click copy/share of quiz links                                |
| Student Review Toggle    | Control whether students can review their answers post-submission |
| Comprehensive Analytics  | Track scores, trends, and student performance                     |
| Time Tracking            | Monitor time taken per student                                    |
| Score Statistics         | View average, max, and min scores across all attempts             |
| Results Export           | Export assessment data for reporting                              |
| Question Management      | Edit questions, test cases, and quiz parameters                   |

#### For Students

| Feature                    | Description                                         |
| -------------------------- | --------------------------------------------------- |
| Distraction-Free Interface | Clean, minimal UI focused on assessment content     |
| Monaco Code Editor         | Syntax highlighting for Python, Java, and C++       |
| Live Test Execution        | Run code against test cases in real-time            |
| Split-Pane Layout          | Problem statement (left) + code editor (right)      |
| Auto-Save                  | Automatic saving of responses and code              |
| Smooth Navigation          | Seamless question navigation with progress tracking |
| Dark/Light Mode            | User preference persisted across sessions           |
| Countdown Timer            | Visual time-limit awareness                         |
| Starter Code Support       | Pre-populated code templates for coding questions   |
| Review Mode                | Post-submission review with correctness indicators  |

---

### User Workflow

#### Teacher Workflow

1. **Register/Login** → Create account with email and password
2. **Create Quiz** → Enter title, subject, description, number of questions, optional password, time limit
3. **Add Questions** → For each question:
   - Select type (MCQ / MSQ / Subjective / Coding)
   - For MCQ/MSQ: Add options and mark correct answer(s)
   - For Coding: Provide starter code and add hidden test cases (input + expected output)
   - Set marks per question
4. **Publish Quiz** → Auto-generated UUID quiz code
5. **Share Quiz** → Copy link or distribute quiz code
6. **Monitor Submissions** → Real-time dashboard
7. **Review Results** → Individual scores, leaderboard (by score then time), aggregate stats
8. **Toggle Review Access** → Enable/disable student review
9. **Manage Quizzes** → Edit, delete, or duplicate

#### Student Workflow

1. **Access Quiz** → Via link or quiz code
2. **Enter Info** → Name, email, roll number, password (if required)
3. **Take Assessment** → MCQ options / Monaco code editor with live test execution
4. **Submit Quiz** → Click finish
5. **View Score** → Immediate feedback with score breakdown
6. **Review Answers** (if enabled) → See correctness, submitted code, test case results

---

### System Architecture

#### Frontend

| Item        | Detail                                    |
| ----------- | ----------------------------------------- |
| Framework   | React 19.2.4 with Vite 7.3.1              |
| Styling     | Tailwind CSS 4.2.2 with @tailwindcss/vite |
| Routing     | React Router DOM 7.13.1                   |
| Code Editor | @monaco-editor/react 4.7.0                |
| HTTP Client | Axios 1.13.6                              |
| Charting    | Recharts 3.8.0                            |

**Key Components:**

- `ProtectedRoute` — Auth wrapper, redirects unauthenticated users
- `TeacherDashboard` — Lists all teacher quizzes with edit/delete/results
- `CreateQuiz` — Quiz metadata form
- `AddQuestions` — Dynamic multi-type question form
- `EditQuiz` — Update existing quiz
- `StartQuiz` — Pre-assessment student credential entry
- `QuizAttempt` — Main quiz interface with Monaco editor
- `Review` — Post-submission correctness review
- `QuizResult` — Teacher analytics dashboard

#### Backend

| Item           | Detail                                       |
| -------------- | -------------------------------------------- |
| Framework      | Django 5.2.12 + Django REST Framework 3.16.1 |
| Authentication | JWT via djangorestframework_simplejwt 5.5.1  |
| CORS           | django-cors-headers 4.9.0                    |
| Database       | SQLite (dev) / PostgreSQL (prod)             |
| Server         | Gunicorn 25.2.0                              |

---

### Database Schema

```
User (Custom AbstractBaseUser)
├── email (unique)
├── name
├── password (hashed)
├── is_active, is_staff, is_superuser

Quiz
├── teacher (FK → User)
├── title, subject, description
├── review_on (boolean)
├── quiz_code (UUID, unique)
├── password (optional, nullable)
├── num_of_qus, time_limit (minutes)
├── created_at (timestamp)

Question
├── quiz (FK → Quiz)
├── text
├── type (enum: mcq | msq | subjective | coding)
├── marks
├── starter_code (for coding)

Option
├── question (FK → Question)
├── text
├── is_correct (boolean)

TestCase
├── question (FK → Question)
├── input_data
├── expected_output

QuizAttempt
├── quiz (FK → Quiz)
├── student_name, email, roll_number
├── started_at, completed_at
├── score (nullable until completion)
├── unique_together: [quiz, email]

Answer
├── attempt (FK → QuizAttempt)
├── question (FK → Question)
├── code (for coding questions)
├── selected_option (FK → Option, nullable)
├── is_correct (boolean)
├── language (python | java | cpp)
├── unique_together: [attempt, question]
```

---

### API Endpoints

#### Authentication

```
POST /api/register/           → Teacher registration
POST /api/login/              → Login, returns access/refresh tokens
POST /api/token/refresh/      → Refresh access token
```

#### Quiz Management *(Auth required)*

```
POST   /api/create-quiz/                      → Create new quiz
GET    /api/teacher-quizzes/                  → List teacher's quizzes
GET    /api/quiz/<id>/                        → Get quiz details
DELETE /api/quiz/<id>/delete/                 → Delete quiz
POST   /api/quiz/<id>/toggle-review/          → Toggle review_on flag
GET    /api/quiz/<id>/results/                → All attempts + stats
```

#### Question Management *(Auth required)*

```
POST /api/create-question/                    → Add question to quiz
GET  /api/quiz/<id>/questions-list/           → Questions with answers
PUT  /api/update-question/                    → Update question
```

#### Student Assessment

```
POST /api/start-quiz/                         → Initialize attempt
GET  /api/quiz/<quiz_code>/questions/         → Fetch questions + time limit
GET  /api/quiz-info/<uuid:quiz_code>/         → Quiz metadata
POST /api/submit-answer/                      → Save answer
POST /api/finish_quiz/                        → Finalize + calculate score
POST /api/test-code/                          → Preview code against input
POST /api/get-attempt/                        → Retrieve attempt by email + code
GET  /api/review/<attempt_id>/               → Full review with correct answers
```

---

### Code Execution System

```python
# Language-specific runners with timeout protection
run_python(code, input_data)  → subprocess, 3s timeout
run_java(code, input_data)    → javac compile (4s) → execute (3s)
run_cpp(code, input_data)     → g++ compile (4s) → execute (3s)

# Evaluation
evaluate_code(question, code, language)
→ Runs all test cases
→ Returns (passed / total) * question_marks  # Partial credit support
```

Key safety features:

- Temporary file creation for code isolation
- Timeout protection (4s compile, 3s execute)
- Exception handling for compile/runtime/timeout errors
- Threading lock (`execution_lock`) for concurrent request safety

---

### Authentication Flow

1. **Registration** → Email/password → `set_password()` (hashed)
2. **Login** → `django authenticate()` → verify credentials
3. **Token Generation** → `RefreshToken.for_user()` → access + refresh tokens
4. **Protected Endpoints** → `@permission_classes([IsAuthenticated])`
5. **Token Usage** → `Authorization: Bearer <access_token>` header

---

### Technical Challenges & Solutions

**Challenge 1 — Code Execution Safety**

- Problem: Arbitrary student code could compromise server or run infinitely
- Solution: Subprocess with timeout, temp files for isolation, threading lock, output capture

**Challenge 2 — Duplicate Quiz Attempts**

- Problem: Students could re-attempt the same quiz
- Solution: `unique_together: [quiz, email]` + explicit `.exists()` check in `start_quiz()` → returns 400

**Challenge 3 — Optional Password Protection**

- Problem: Supporting passwordless quizzes while also allowing password-protected ones
- Solution: Nullable password field + conditional validation in `QuizStartSerializer`

**Challenge 4 — Partial Credit for Coding**

- Problem: Award marks based on test case pass rate, not binary pass/fail
- Solution: `(passed / total) * question_marks` in `evaluate_code()`

**Challenge 5 — Multi-type Question Submission**

- Problem: Same endpoint handling MCQ, MSQ, subjective, and coding submissions
- Solution: `if/else` branching on `question.type`, `update_or_create()` for idempotency

**Challenge 6 — CORS Between Frontend and Backend**

- Problem: Vite (localhost:5173) and Django (localhost:8000) on different origins
- Solution: `django-cors-headers` with `CORS_ALLOW_ALL_ORIGINS = True` (restricted in prod)

**Challenge 7 — Theme Persistence**

- Problem: Dark/light mode lost on page refresh
- Solution: `localStorage` save on change + `useEffect` on init → `document.documentElement.classList`

---

### Evidence of Skill

| Skill            | Confidence | Key Evidence                                                                      |
| ---------------- | ---------- | --------------------------------------------------------------------------------- |
| Python           | 9/10       | Django ORM, subprocess management, exception handling, serializer data transforms |
| JavaScript/React | 9/10       | Hooks, React Router, Axios, Monaco Editor, Recharts, localStorage                 |
| Django           | 9/10       | Custom user model, nested serializers, permission decorators, JWT config          |
| APIs             | 9/10       | 20+ RESTful endpoints, proper HTTP codes, JWT, versioning structure               |
| Databases        | 8/10       | 7-model schema, cascade deletes, unique constraints, prefetch_related             |
| Frontend Dev     | 8/10       | Responsive UI, dark mode, split-pane editor, analytics charts                     |

---

### Repository Insights

| Metric               | Score | Notes                                                             |
| -------------------- | ----- | ----------------------------------------------------------------- |
| Development Maturity | 7/10  | Well-structured, production security, missing CI/CD and tests     |
| Code Quality         | 7/10  | Good Django patterns, some repeated logic, missing type hints     |
| Maintainability      | 7/10  | Clear structure, but missing constants file and full docs         |
| Scalability          | 6/10  | JWT enables horizontal scaling; code execution is sync bottleneck |

---

### Future Improvements

**Features:** Live collaborative mode · Question randomization · Proctoring integration · Mobile-first responsive · Audio/video questions · Plagiarism detection · LLM for auto question generation

**Performance:** Redis caching · Celery async code execution · Database indexing · CDN integration · API rate limiting · Load balancing

**Security:** 2FA · Encryption at rest · Audit logging · RBAC roles · IP whitelisting

**DevEx:** Swagger/OpenAPI docs · Docker Compose · GitHub Actions CI/CD · Bulk CSV import · PDF/Excel export

---

## 2. Project ARIES

**Priority:** HIGH | **Complexity:** INTERMEDIATE | **Status:** In Progress

### Project Summary

ARIES is a full-stack web application with React on the frontend and a RESTful backend (technology TBD from limited docs). Demonstrates modern web application architecture with clear frontend/backend separation.

**Stack:** React 19.2.4 · Vite 8.0.4 · Tailwind CSS 4.2.2 · React Router DOM 7.14.0 · Axios 1.14.0

### Key Features (Inferred from Dependencies)

- React 19.2.4 component-based UI
- Client-side routing with React Router
- HTTP API communication via Axios
- Responsive UI with Tailwind CSS
- RESTful backend (technology unknown)

### Evidence of Skill

| Skill           | Confidence | Notes                                                     |
| --------------- | ---------- | --------------------------------------------------------- |
| React           | 7/10       | Modern version, Vite setup, Router integration            |
| JavaScript      | 7/10       | Modern tooling, dependency management, build scripts      |
| Frontend Dev    | 7/10       | React + Tailwind + Router, missing source code assessment |
| API Integration | 6/10       | Axios dependency, no interceptor evidence visible         |

### Repository Insights

| Metric               | Score | Notes                                           |
| -------------------- | ----- | ----------------------------------------------- |
| Development Maturity | 5/10  | Modern setup, missing docs and tests            |
| Maintainability      | 5/10  | Clean frontend/backend split, missing API specs |

---

## 3. Tic Tac Toe BOT

**Priority:** HIGH | **Complexity:** INTERMEDIATE | **Status:** Complete

### Project Summary

A Python/Django game application implementing an AI opponent for Tic Tac Toe using game theory algorithms (likely minimax). Showcases understanding of game logic, AI algorithms, state management, and web application architecture for interactive apps.

**Stack:** Python 3.9+ · Django 5.2.11 · Django REST Framework 3.16.1 · django-cors-headers · SQLite · HTML/CSS/JS

### Key Features

- Intelligent AI opponent with strategic decision-making
- Complete game rules and move validation
- Win/loss/draw detection
- API-driven game engine
- Web interface for gameplay

### User Workflow

1. **Start Game** → Player initializes new game
2. **Player Move** → Click board cell to place X
3. **API Call** → Move submitted to backend
4. **Server Processing** → Validate move, update board state
5. **AI Response** → Backend computes optimal AI move
6. **Board Update** → Frontend receives new state
7. **Win Check** → System determines game outcome
8. **Game Over** → Display result, option to replay

### Game AI Concepts

- **Minimax Algorithm** — Optimal move selection via game tree search
- **Alpha-Beta Pruning** — Search space optimization
- **Heuristic Evaluation** — Scoring board positions
- **Recursive Depth-First Search** — Exploring future game states

### Inferred API Endpoints

```
POST /api/game/new/       → Initialize new game
POST /api/game/move/      → Submit player move
GET  /api/game/state/     → Get current board state
POST /api/game/ai-move/   → Get AI response
GET  /api/game/status/    → Check game status
```

### Evidence of Skill

| Skill            | Confidence | Notes                                                      |
| ---------------- | ---------- | ---------------------------------------------------------- |
| Python           | 8/10       | Django app, game logic, algorithm design, state management |
| Django           | 7/10       | Project structure, REST endpoints, CORS config             |
| Algorithms       | 7/10       | Minimax/game tree, decision tree evaluation                |
| Game Development | 7/10       | State management, turn logic, win detection, AI opponent   |

### Repository Insights

| Metric               | Score | Notes                                         |
| -------------------- | ----- | --------------------------------------------- |
| Development Maturity | 5/10  | Basic Django setup, minimal docs              |
| Maintainability      | 5/10  | Good Django structure, missing tests and docs |
| Scalability          | 4/10  | Single-player, no concurrency needs           |

---

## 4. Fake Job Detection

**Priority:** HIGH | **Complexity:** INTERMEDIATE | **Status:** Complete

### Project Summary

A machine learning classification project that identifies fraudulent job postings. Trains on a 50MB+ CSV dataset, builds a classification model, and exposes predictions through a Flask/Streamlit web app.

**Stack:** Python 3.x · pandas · numpy · scikit-learn · NLTK/spaCy · TF-IDF · pickle · Flask or Streamlit · matplotlib/seaborn

### ML Pipeline

```
Data Loading (50MB+ CSV)
        ↓
Data Preprocessing (missing values, duplicates, normalization)
        ↓
Feature Engineering (TF-IDF, word count, linguistic patterns, categorical vars)
        ↓
Model Training (multiple classifiers, GridSearchCV, cross-validation)
        ↓
Evaluation (Accuracy, Precision, Recall, F1, ROC-AUC, confusion matrix)
        ↓
Serialization (pickle → fake_job_detector.pkl)
        ↓
Web App (Flask/Streamlit, loads model, accepts input, returns prediction)
```

### Technical Challenges & Solutions

**Challenge 1 — Large Dataset**

- Problem: 50MB+ CSV is computationally expensive
- Solution: Efficient pandas ops, chunked processing, feature selection, data sampling

**Challenge 2 — Imbalanced Classes**

- Problem: Fewer fake postings than real ones in dataset
- Solution: Class weight adjustment, stratified sampling, F1/precision-recall metrics, oversampling

**Challenge 3 — Text Feature Engineering**

- Problem: Converting unstructured job posting text to numerical features
- Solution: TF-IDF vectorization + structural features (word count, URLs, urgency words, formatting)

**Challenge 4 — Model Persistence**

- Problem: Model must be saved and reloaded for web app
- Solution: Pickle serialization + versioned preprocessing pipeline + consistent random seeds

### Evidence of Skill

| Skill                 | Confidence | Notes                                                               |
| --------------------- | ---------- | ------------------------------------------------------------------- |
| Python                | 8/10       | pandas, model training, serialization, web app                      |
| Machine Learning      | 8/10       | End-to-end pipeline, hyperparameter tuning, evaluation metrics      |
| Data Science          | 8/10       | EDA, preprocessing, feature engineering, visualization              |
| NLP / Text Processing | 7/10       | TF-IDF, tokenization, stop words — no advanced models (BERT, etc.) |
| Flask/Streamlit       | 7/10       | Model integration, prediction UI                                    |

### Repository Insights

| Metric               | Score | Notes                                                        |
| -------------------- | ----- | ------------------------------------------------------------ |
| Development Maturity | 6/10  | Complete pipeline, pickle model, web app; missing docs/tests |
| Code Quality         | 7/10  | Clear Jupyter notebook; missing type hints                   |
| Scalability          | 5/10  | Single process; suitable for low-medium volume               |

---

## 5. Blog Project

**Priority:** HIGH | **Complexity:** INTERMEDIATE | **Status:** Complete

### Project Summary

A Django-based blogging platform with full CRUD operations, user authentication, Cloudinary media storage, PostgreSQL production database, and Heroku deployment. Complete CMS experience for authors and readers.

**Stack:** Python 3.x · Django 4.2.18 · Bootstrap 5 · PostgreSQL · Cloudinary · Gunicorn · WhiteNoise · Heroku

### Database Schema

```
User (Django built-in)
├── username, email, password (hashed)

BlogPost
├── author (FK → User)
├── title, slug, content, excerpt
├── featured_image
├── created_at, updated_at
├── is_published

Comment
├── post (FK → BlogPost)
├── author (FK → User)
├── content, created_at
├── is_approved

Category
├── name
```

### Key Technical Challenges

**Image Upload at Scale**

- Cloudinary cloud storage + CDN + `django-cloudinary-storage` integration

**Dev/Prod Environment Config**

- `.env` + `python-dotenv` + `dj-database-url` + `DEBUG`-based conditional settings

**Static Files in Production**

- WhiteNoise middleware with `STATIC_ROOT` and compression/caching headers

**Heroku Deployment**

- Procfile → Gunicorn · `dj-database-url` · environment-based config

### Evidence of Skill

| Skill             | Confidence | Notes                                                        |
| ----------------- | ---------- | ------------------------------------------------------------ |
| Python            | 8/10       | Django models, views, forms, decorators, ORM                 |
| Django            | 8/10       | Models, views, templates, admin, auth, URL routing           |
| Database Design   | 7/10       | FK relationships, timestamps, slugs, published flag          |
| DevOps/Deployment | 7/10       | Heroku, Gunicorn, WhiteNoise, environment config             |
| Cloudinary        | 7/10       | Image upload, CDN, django-cloudinary-storage                 |
| Frontend Dev      | 6/10       | Bootstrap, HTML templates, forms — limited JS interactivity |

---

# Developer Profile

## Professional Identity

Pratyush Maurya is a **full-stack developer** with strong expertise in Python, JavaScript, and modern web frameworks. Capable across the entire application stack — from database design to frontend UI/UX — with experience in Django, React, and ML.

## Technical Interests

**Primary:**

- Full-Stack Web Development (database → UI)
- Educational Technology / EdTech (Quiesy is primary focus)
- Machine Learning in Practice (real-world problems)
- Game Development (algorithmic problem-solving)
- System Design (scalable, multi-user platforms)

**Emerging:**

- AI/LLM integration
- DevOps and deployment automation
- Performance optimization
- Code quality and testing

## Preferred Languages

| Tier                 | Languages                             |
| -------------------- | ------------------------------------- |
| Tier 1 — Proficient | Python, JavaScript, SQL               |
| Tier 2 — Competent  | TypeScript, HTML/CSS, Bash/Shell      |
| Tier 3 — Learning   | Java, C++ (via Quiesy code execution) |

## Preferred Frameworks

**Backend:** Django 4.x/5.x + Django REST Framework

**Frontend:** React 19.x + Vite + React Router + Tailwind CSS

**Emerging:** Flask/Streamlit (rapid prototyping), Astro (static sites)

## Problem-Solving Style

- **Pragmatic** — Chooses proven technologies (Django, React) over experimental ones
- **Complete** — Builds end-to-end solutions including deployment
- **User-focused** — Distraction-free UX, responsive design, dark mode
- **Architecture-first** — Plans system design before coding
- **Production-oriented** — Considers deployment, config, and scaling early

## Coding Habits

**Positive:**

- Meaningful variable/function names
- Business logic separated from framework code
- Proper error handling
- Security-conscious (password hashing, JWT, CORS)
- Environment variables for configuration

**Areas for Improvement:**

- Test coverage (no visible test files)
- Documentation (README files often minimal)
- TypeScript adoption
- CI/CD automation

---

# Technical Skills Assessment

## Expert Level (8–10/10)

| Skill              | Confidence | Key Evidence                                                                     |
| ------------------ | ---------- | -------------------------------------------------------------------------------- |
| Django Backend     | 9/10       | Custom user models, ORM, DRF, JWT, complex serializers, permission decorators    |
| React Frontend     | 9/10       | Hooks, React Router, Axios, Monaco Editor, Recharts, dark mode, protected routes |
| Python             | 9/10       | OOP, subprocess, file I/O, exception handling, data manipulation, serialization  |
| REST APIs          | 9/10       | 20+ endpoints, HTTP conventions, JWT auth, status codes, error formatting        |
| Database Design    | 8/10       | 7-entity schemas, FKs, cascade deletes, unique constraints, query optimization   |
| Tailwind CSS       | 8/10       | Utility-first, responsive breakpoints, dark mode, PostCSS                        |
| Authentication     | 8/10       | JWT, custom user models, password hashing, CORS, permission decorators           |
| JavaScript Tooling | 8/10       | Vite setup, npm, ESLint, HMR, production builds                                  |

## Intermediate Level (6–8/10)

| Skill                 | Confidence | Key Evidence                                                                |
| --------------------- | ---------- | --------------------------------------------------------------------------- |
| Machine Learning      | 8/10       | End-to-end pipeline, feature engineering, hyperparameter tuning, evaluation |
| Data Science          | 8/10       | EDA, preprocessing, text processing, model evaluation                       |
| NLP / Text Processing | 7/10       | TF-IDF, tokenization, stop words — no transformers/BERT                    |
| Deployment / DevOps   | 7/10       | Heroku, Netlify, Gunicorn, environment config, WhiteNoise                   |
| Game Dev / Algorithms | 7/10       | Minimax, game state management, win detection                               |
| Media Handling        | 7/10       | Cloudinary, django-cloudinary-storage, CDN                                  |
| TypeScript            | 6/10       | Chatbot project; limited usage overall                                      |

## Beginner Level (1–4/10)

| Skill              | Confidence | Notes                                           |
| ------------------ | ---------- | ----------------------------------------------- |
| Automated Testing  | 2/10       | No visible test files in any repository         |
| CI/CD Automation   | 2/10       | No GitHub Actions workflows visible             |
| Docker             | 3/10       | No containerization evidence                    |
| Advanced ML (DL)   | 1/10       | No neural networks, TensorFlow, or transformers |
| Mobile Development | 1/10       | No React Native or Flutter projects             |
| Microservices      | 1/10       | All backends are monolithic Django apps         |

## Summary Matrix

| Category         | Confidence | Level        |
| ---------------- | ---------- | ------------ |
| Django Backend   | 9/10       | Expert       |
| React Frontend   | 9/10       | Expert       |
| Python           | 9/10       | Expert       |
| REST APIs        | 9/10       | Expert       |
| Database Design  | 8/10       | Strong       |
| JavaScript       | 8/10       | Strong       |
| Tailwind CSS     | 8/10       | Strong       |
| Authentication   | 8/10       | Strong       |
| Machine Learning | 8/10       | Strong       |
| Deployment       | 7/10       | Intermediate |
| TypeScript       | 6/10       | Intermediate |
| DevOps/Docker    | 4/10       | Beginner     |
| Testing          | 2/10       | Beginner     |
| CI/CD            | 2/10       | Beginner     |
| Deep Learning    | 1/10       | Beginner     |

---

# Learning Journey

## Phase 1 — Foundation (Early 2024)

**Projects:** codsoft-calculator · codsoft-landing · codsoft-portfolio · animate · draw · todo

**Focus:** HTML/CSS, JavaScript DOM manipulation, browser APIs, basic state management

**Skill Progression:** HTML/CSS (Beginner → Intermediate) · JavaScript (Beginner → Beginner-Intermediate)

---

## Phase 2 — Framework Exploration (Mid-2024)

**Projects:** mytennis · project_blog (early version)

**Focus:** Django basics — models, views, ORM, forms, authentication, admin interface, MVC/MTV architecture

**Key Transition:** Vanilla JS → Framework-based development; introduced backend and server-side logic

**Skill Progression:** Python (Beginner → Intermediate) · Django (Beginner → Intermediate)

---

## Phase 3 — Full-Stack Integration (Late 2024 – Early 2025)

**Projects:** Blog Project (complete) · Fake Job Detection

**Focus:** Complete full-stack development, PostgreSQL, Heroku deployment, Cloudinary, ML pipeline, feature engineering, model training

**Key Transition:** Beyond learning frameworks → Building production applications with external services

**Skill Progression:** Django (Intermediate → Advanced) · Python (Intermediate → Advanced) · ML (N/A → Intermediate)

---

## Phase 4 — Advanced Full-Stack & Real-World Problems (Early 2025 – Present)

**Projects:** Quiesy · Project ARIES · Tic Tac Toe BOT

**Focus:** Complex system architecture, multi-user RBAC, 20+ API endpoints, safe code execution, performance thinking, advanced React patterns, game AI

**Key Achievement: Quiesy** — 10x complexity jump from Blog Project. Demonstrates:

- 7 interconnected database models
- Code execution with safety isolation
- 20+ permission-based API endpoints
- Dark/light mode, split-pane editor, real-time feedback
- Production deployment with environment management

**Skill Progression:** Django (Expert) · React (Advanced) · System Design (Intermediate-Advanced) · API Design (Advanced)

---

## Evolution of Complexity

```
Phase 1: Static HTML/CSS Pages
         ↓
Phase 2: Interactive JavaScript Features
         ↓
Phase 3: Single-Technology Django Backend
         ↓
Phase 4: Integrated React + Django Full-Stack
         ↓
Phase 5: Complex Multi-User Systems (Current)
         ↓
Phase 6: Optimization & Scaling (Next)
```

---

## Recurring Mistakes & Improvements

| Mistake                    | Recognition                                   | Current Status  |
| -------------------------- | --------------------------------------------- | --------------- |
| Minimal documentation      | Added comprehensive README to Quiesy          | Still improving |
| No automated testing       | Not yet addressed                             | Next priority   |
| Deployment as afterthought | Now included early (Procfile, Netlify config) | Fixed           |

---

## Predicted Next Projects & Learning Gaps

**High Priority Gaps:**

- Automated Testing (pytest, Jest, TDD)
- CI/CD Pipelines (GitHub Actions)
- Docker & Containerization
- Async Task Processing (Celery/RabbitMQ)
- Advanced Caching (Redis)

**Medium Priority:**

- TypeScript adoption
- Redux / Zustand state management
- Advanced PostgreSQL (JSON fields, full-text search)
- Kubernetes

---

# Project Index & Ranking

## High-Priority Projects

| Rank | Project            | Complexity            | Technologies                                | Status      |
| ---- | ------------------ | --------------------- | ------------------------------------------- | ----------- |
| 1    | Quiesy             | Advanced              | React, Django, PostgreSQL, Monaco, Recharts | Active      |
| 2    | Project ARIES      | Advanced              | React, Vite, Backend TBD                    | In Progress |
| 3    | Tic Tac Toe BOT    | Intermediate-Advanced | Python, Django, Game AI                     | Complete    |
| 4    | Fake Job Detection | Intermediate          | Python, scikit-learn, Flask/Streamlit       | Complete    |
| 5    | Blog Project       | Intermediate          | Django, PostgreSQL, Cloudinary, Bootstrap   | Complete    |

## Medium-Priority Projects

| Rank | Project                     | Technologies        | Status      |
| ---- | --------------------------- | ------------------- | ----------- |
| 6    | Advanced Django Cheat Sheet | Django, Markdown    | Maintained  |
| 7    | Chatbot                     | TypeScript, Node.js | In Progress |
| 8    | My Site / Portfolio         | React, JavaScript   | Complete    |
| 9    | Guardian Chrome Extension   | JavaScript          | Complete    |

## Learning / Foundational Projects

| Rank | Project              | Technologies             | Status   |
| ---- | -------------------- | ------------------------ | -------- |
| 10   | Draw                 | HTML5 Canvas, JavaScript | Complete |
| 11   | Todo List            | JavaScript, CSS          | Complete |
| 12   | Codsoft Calculator   | HTML, CSS, JavaScript    | Complete |
| 13   | Codsoft Portfolio    | HTML, CSS                | Complete |
| 14   | Codsoft Landing      | HTML                     | Complete |
| 15   | Animate              | CSS                      | Complete |
| 16   | Netlify Feature Tour | Astro, CSS               | Complete |

## ML & Data Science Projects

| Rank | Project             | Technologies                | Status   |
| ---- | ------------------- | --------------------------- | -------- |
| 17   | Fake Job Detection  | scikit-learn, pandas, Flask | Complete |
| 18   | ML Assign 01        | Jupyter, Python, pandas     | Complete |
| 19   | AccuKnox Assignment | Python, Django              | Complete |

---

# Digital Twin Summary

> This section is optimized for AI assistant / RAG retrieval.

## Core Identity

Pratyush Maurya is a **full-stack developer and data scientist** with advanced proficiency in Python and JavaScript. Can independently design, build, and deploy complete production-ready systems. Specializes in Django backend, React frontend, and system design.

## Quick Reference — What They Build

| Type                          | Example            | Key Traits                                  |
| ----------------------------- | ------------------ | ------------------------------------------- |
| EdTech / Assessment Platforms | Quiesy             | Multi-user RBAC, code execution, analytics  |
| Content Management Systems    | Blog Project       | CRUD, media handling, production deployment |
| ML Applications               | Fake Job Detection | End-to-end pipeline, web interface          |
| Interactive Web Apps          | General            | Tailwind UI, dark mode, responsive design   |
| Game / Algorithm Apps         | Tic Tac Toe BOT    | Game AI, state management                   |

## When to Ask Pratyush About…

**Definitely Ask:**

- Django application architecture
- React component design
- Full-stack system design
- Database schema design
- REST API design
- Production deployment strategies
- UI/UX decisions

**Probably Ask:**

- Machine learning pipelines
- JavaScript/TypeScript patterns
- Vite build tools
- Authentication systems
- Cloudinary / cloud service integration

**Don't Ask:**

- Deep learning / neural networks
- Mobile app development (React Native, Flutter)
- Microservices architecture
- Kubernetes / advanced DevOps
- Low-level systems programming

## Predicted Career Path

| Stage   | Timeline   | Description                                                                          |
| ------- | ---------- | ------------------------------------------------------------------------------------ |
| Current | Now        | Mid-Level Full-Stack Developer — can architect and ship complete products solo      |
| Next    | 1–2 years | Senior Dev / Tech Lead — architectural responsibility, mentoring, potential startup |
| Later   | 2–5 years | Startup CTO / Engineering Lead — building teams, commercial products                |

## Key RAG Retrieval Points

- **Expert:** Django, React, Python, full-stack development, system design
- **Strong:** Database design, REST APIs, authentication, deployment, ML basics
- **Learning:** Testing, CI/CD, Docker, advanced ML, DevOps
- **Not experienced:** Deep learning, mobile, microservices, advanced DevOps

**Behavioral context:**

- Prefers complete, production-ready projects over prototypes
- Rapid learner who integrates new tech quickly
- Quality-conscious with attention to UX and deployment
- Independent contributor capable of solo product development
- Likely building toward a startup or major commercial product

---
