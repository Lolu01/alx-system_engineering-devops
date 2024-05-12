Issue Summary:

Duration: The outage occurred from 10:00 PM to 12:30 AM (UTC-5).
Impact: The primary impact was on our online booking system, resulting in 30% of users experiencing slow response times or being unable to access the platform.
Root Cause: The root cause of the outage was identified as a database connection issue, leading to degraded performance and eventual service failure.

Timeline:

10:00 PM: The issue was first detected through monitoring alerts indicating a spike in database connection errors.
10:15 PM: Engineers began investigating the issue, initially suspecting a potential network issue or database overload.
10:45 PM: Further investigation revealed no abnormalities in network traffic or database load, leading to the escalation of the incident to the database administration team.
11:30 PM: Misleading investigation paths included exploring application code changes and server configurations, which were ultimately unrelated to the root cause.
12:00 AM: The incident was escalated to senior database administrators for additional support and expertise.
12:30 AM: The issue was resolved after identifying and rectifying a misconfigured database connection pool, restoring normal system functionality.

Root Cause and Resolution:

Root Cause: The issue stemmed from a misconfigured database connection pool, causing excessive connection timeouts and failed connection attempts.
Resolution: The issue was resolved by adjusting the database connection pool settings to allow for increased connection capacity and optimising connection timeout parameters to prevent future timeouts.

Corrective and Preventative Measures:

Improvements/Fixes:
  - Implement regular database connection pool health checks to proactively identify and address potential issues.
  - Enhance monitoring capabilities to detect abnormal database connection patterns and performance degradation in real-time.
Tasks to Address the Issue:
  - Update documentation to ensure proper configuration of database connection pools across all environments.
  - Conduct a thorough review of application code to identify and refactor any inefficient database connection handling practices.
  
This postmortem highlights the importance of proactive monitoring, thorough investigation, and collaboration in identifying and resolving system outages. By implementing corrective measures and preventive strategies, we aim to minimise the likelihood of similar incidents in the future, ensuring the reliability and stability of our systems for our users.

