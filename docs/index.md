# Spot Render Observability – TechDocs

## Componentes
- Exporter (`exporter/main.py`)
- Dockerfile
- Grafana dashboards (`grafana/dashboards/*.json`)
- Alert rules (`prometheus/alerts/*.yaml`)

## Métricas atuais
- `render_success_total{project,artist}`
- `render_error_total{project,artist}`
- `render_queue_total{project}`
- `render_duration_seconds`
- `render_canary_requests_total{version,status}`

## Adicionando métricas
1. Registrar no exporter.  
2. Atualizar dashboards/alerts.  
3. Build & push imagem via CI.

## Alertas
- `prometheus/alerts/canary-rules.yaml` contém regras de erro >1% e latência >600s.  
- Para novos alertas, duplica-se a estrutura e publica-se via `kubectl apply`.

## Teste local
1. `docker build -t spot-render-observability:dev .`  
2. `docker run -p 9100:9100 spot-render-observability:dev`  
3. `curl localhost:9100/metrics`

## Integração com cluster
- Use `spot-render-teste-local` para aplicar `ServiceMonitor` e dashboard.  
- Grafana import: `grafana/dashboards/rendering.json`.

## TechDocs
- `mkdocs.yml` define a navegação.
