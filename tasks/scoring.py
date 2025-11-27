from datetime import date, timedelta

def count_business_days(start_date, end_date):
    """
    Counts weekdays (Mon-Fri) between dates.
    """
    days = 0
    current = start_date
    while current < end_date:
        if current.weekday() < 5:
            days += 1
        current += timedelta(days=1)
    return days

def calculate_priority_score(task_data):
    """
    ALTERNATIVE LOGIC: 'Strict Mode'
    Focuses heavily on high-importance items and strictly punishes overdue tasks.
    """
    
    # 1. IMPORTANCE (Heavier Weight)
    # Your version was * 10. Hers is * 15.
    # A 10/10 task starts at 150 points immediately.
    score = task_data.get('importance', 5) * 15
    
    # 2. URGENCY (Panic Logic)
    due_date_str = task_data.get('due_date')
    if due_date_str:
        today = date.today()
        try:
            if isinstance(due_date_str, str):
                due_date = date.fromisoformat(due_date_str)
            else:
                due_date = due_date_str
            
            days_until_due = (due_date - today).days
            
            if days_until_due > 0:
                business_days = count_business_days(today, due_date)
            else:
                business_days = days_until_due

            if days_until_due < 0:
                # OVERDUE: Extreme boost (+200). She treats overdue as an emergency.
                score += 200 + (abs(days_until_due) * 10)
            elif days_until_due == 0:
                score += 100 # Due Today
            elif business_days <= 3:
                score += 50  # 3 Day Warning
            elif business_days <= 5:
                score += 20  # Weekly Warning
                
        except ValueError:
            pass

    # 3. EFFORT (Micro-Task Bonus)
    # Only rewards tasks under 1 hour (Micro tasks)
    estimated_hours = task_data.get('estimated_hours', 0)
    if estimated_hours <= 1:
        score += 25  # Big bonus for very quick tasks
    elif estimated_hours >= 10:
        score -= 10  # Penalty for massive tasks

    # 4. DEPENDENCY (Severe Penalty)
    dependencies = task_data.get('dependencies')
    if dependencies and len(dependencies.strip()) > 0:
        score -= 50  # Huge penalty. Blocked tasks drop to the very bottom.

    return score