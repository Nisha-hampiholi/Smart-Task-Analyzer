## TaskMaster

A Django-based task management system featuring a "Strict Mode" priority algorithm. It aggressively scores tasks based on high-stakes importance, deadline panic, and dependency blockers.

## 🚀 Setup Instructions

1. **Clone the repository** (or extract the project folder).

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Mac/Linux
   source venv/bin/activate

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Initialize the Database**
   ```bash
   python manage.py migrate

5. **Start the Server**
   ```bash
   python manage.py runserver

6. Open your browser at http://127.0.0.1:8000/.

## Algorithm Explanation
The core priority algorithm (tasks/scoring.py) uses a "High Stakes" logic model. Unlike standard analyzers, this algorithm aggressively punishes delays and heavily rewards high-value items.

Importance (Heavy Weight):

The user's importance rating (1-10) is multiplied by 15 (instead of the standard 10). A single critical task starts with a massive 150 point baseline.

Urgency (Panic Logic):

Overdue Emergency: Past-due tasks trigger a +200 point emergency boost.

Business Days: The algorithm respects weekends. A task due on Monday is treated as having only 1 working day left on Friday.

Effort (Micro-Tasks):

Only tasks estimated at ≤ 1 hour receive the +25 point "Micro Task" bonus.

Tasks taking > 10 hours receive a penalty to encourage breaking them down.

Dependency Logic (Severe Penalty):

If a task is blocked by a dependency, it receives a crushing -50 point penalty.

Why? Blocked tasks are dead weight. They drop to the bottom so you focus only on what is actionable now.

## Design Decisions & Trade-offs
Logic Separation: The scoring logic resides in scoring.py to keep the views clean and the algorithm testable.

Client-Side vs Server-Side Sorting:

"AI Rank" runs on the Python backend to utilize the complex strict-mode logic.

"Panic Mode" / "Micro Tasks" are handled instantly in the Frontend (JavaScript) for immediate filtering.

Circular Dependencies:

Trade-off: I chose not to implement graph cycle detection for this MVP.

Reasoning: I prioritized the aggressive scoring model and UI performance. In production, input validation would prevent circular blockers.

## Bonus Challenges Completed
Date Intelligence: The algorithm calculates Business Days (excluding weekends) to accurately predict "Panic Mode" deadlines.

Unit Tests: Implemented unit tests in tasks/tests.py to verify the strict scoring logic.

Cyberpunk UI: Built a custom Dark Mode interface with neon accents, visual priority indicators, and a JSON Bulk Import feature.
