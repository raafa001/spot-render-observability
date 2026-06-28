## spot-render-observability

> Exporter Prometheus + dashboards Grafana + alertas Prometheus para acompanhar uploads, renders e deploys canário do Spot Render.

### Conteúdo

```
exporter/
  main.py
grafana/
  dashboards/
    rendering.json
prometheus/
  alerts/
    canary-rules.yaml
Dockerfile
```

### Métricas expostas
- `render_success_total{project,artist}`
- `render_error_total{project,artist}`
- `render_queue_total{project}`
- `render_duration_seconds`
- `render_canary_requests_total{version}`

### Dashboard
- Painéis para status geral, por projeto, por artista e comparativo canary vs stable.
