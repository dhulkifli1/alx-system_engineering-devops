## Issue summary
* Duration: 1 hour 30 minutes from 10:00 AM to 11:30 AM (UTC-8)
* Impact: Users were unable to access the login page, causing a 50% drop in traffic during the outage.
* Root Cause: A misconfiguration in the web server caused the application server to crash.

## Timeline
* 10:00 AM: We received a frantic call from our CEO, who was unable to log in and check his stock options.
* 10:01 AM: The operations team was notified and began their heroic mission to save the company from certain doom.
* 10:05 AM: The team identified that the login page was more broken than a cracked mirror and began investigating the application server.
* 10:15 AM: The team discovered that the application server was as responsive as a sleeping sloth and began investigating the web server.
* 10:25 AM: The team found a misconfiguration in the web server that was sending requests to the wrong server port and causing more chaos than a toddler in a toy store.
* 11:00 AM: The team tested the fix and confirmed that the login page was once again operational.
* 11:30 AM: The issue was resolved, and the team breathed a collective sigh of relief, knowing they had saved the day.

## Root cause and Resolution
The root cause of the outage was a misconfiguration in the web server that caused it to send requests to the wrong port on the application server, eventually causing the application server to crash. To fix the issue, the team reconfigured the web server to send requests to the correct port on the application server.

## Corrective and Preventative Measures:
To prevent similar issues in the future, the team will implement the following corrective and preventative measures:
* Add more comprehensive monitoring to the web and application servers to quickly detect similar issues.
* Implement configuration management to ensure consistent server configurations.
* Develop and test a disaster recovery plan to quickly recover from similar outages.
* Train team members on best practices for web stack configuration and management.
Overall, the team responded quickly and effectively to resolve the outage and implemented measures to prevent similar issues from occurring in the future.