# Postmortem: Nginx Web Server Performance Under Load on May 15, 2024

## Issue Summary:

- Duration: May 15, 2024, 02:00 PM - 03:00 PM (UTC)
- Impact: The web server experienced a high rate of failed requests during a load test. Out of 2000 simulated HTTP requests, 943 failed, resulting in a failure rate of approximately 47.15%. Users experienced slow response times and failures in accessing the service.
- Root Cause: The root cause was identified as a misconfiguration in the Nginx server settings, specifically the insufficient allocation of resources to handle a high volume of concurrent requests.

## Timeline:
* ***02:00 PM:*** The load test began using ApacheBench (ab) with 2000 requests at a concurrency level of 100.

* ***02:10 PM:*** Monitoring alerts indicated a significant number of failed requests.

* ***02:15 PM:*** I began investigating the issue, starting with a review of Nginx logs.

* ***02:20 PM:*** Initial suspicion fell on the backend application, but no issues were found there.

* ***02:30 PM:*** Focus shifted to the Nginx server configuration after noticing errors related to worker processes.

* ***02:40 PM:*** Misleadingly, I temporarily adjusted the timeout settings, which did not resolve the issue.

* ***03:00 PM:*** The I identified the misconfiguration in the worker processes and connections settings of Nginx.

* ***03:05 PM:*** Configuration changes were applied to increase the number of worker processes and connections.

* ***03:10 PM:*** A subsequent load test showed 0 failed requests, confirming the resolution of the issue.

## Root Cause and Resolution:

### - Root Cause: 
The Nginx server was not configured to handle high concurrency, leading to worker processes being overwhelmed and causing request failures.
 
#### Specific Misconfigurations:
- Insufficient number of worker processes.
- Low worker connections limit.

#### Resolution:
- Updated Nginx configuration:

```
worker_processes auto;
events {
    worker_connections 1024;
}
```

- Restarted the Nginx service to apply the new configuration:
```
sudo systemctl restart nginx
```

### - Corrective and Preventative Measures:
#### Improvements/Fixes:

- Regularly review and optimize server configurations based on anticipated load.
Implement automated load testing as part of the deployment pipeline to identify performance issues early.
- Enhance monitoring to detect resource exhaustion issues promptly.

#### Tasks:

- **Review Server Configuration:**
Conduct a comprehensive review of Nginx and backend server configurations to ensure optimal settings.
- **Automate Load Testing:**
Integrate ApacheBench or a similar load-testing tool into the CI/CD pipeline for regular performance assessments.
- **Enhance Monitoring:**
Set up alerts for high resource usage on Nginx worker processes and connections.
- **Document Best Practices:**
Create documentation outlining best practices for configuring web servers to handle high concurrency.
- **Training and Knowledge Sharing:**
Organize training sessions for the engineering team on performance tuning and debugging techniques.
