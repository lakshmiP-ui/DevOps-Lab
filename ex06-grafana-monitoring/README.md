# Exercise 6 - Real-Time Monitoring with Prometheus and Grafana

## Aim
Simulate delivery metrics with Python, scrape them with Prometheus, visualise them in Grafana and trigger alerts.

## Steps
1. Wrote `delivery_metrics.py`, which exposes metrics on port 8000
2. Configured Prometheus (`prometheus.yml`, `alert_rules.yml`) and ran it in Docker
3. Ran Grafana in Docker and added Prometheus as a data source
4. Built a 4-panel "Delivery Monitoring" dashboard
5. Increased pending deliveries to trigger the HighPendingDeliveries alert

## Output
![Metrics](images/01-metrics.png)
![Targets](images/02-targets.png)
![Dashboard](images/03-grafana.png)
![Alerts firing](images/04-alerts-firing.png)

