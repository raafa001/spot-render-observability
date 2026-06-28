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

### Tecnologias
- Prometheus client exporter (Python)  
- Grafana dashboards (JSON)  
- Alertas Prometheus  
- Docker/ECR + Argo Rollouts (opcional)  
- GitHub Actions para lint/build/push.

### Como adicionar novas métricas
1. Edite `exporter/main.py` e registre novos `Counter/Gauge/Histogram`.  
2. Atualize os dashboards em `grafana/dashboards/*.json`.  
3. Se necessário, crie novas regras em `prometheus/alerts/*.yaml`.  
4. Rebuild/push a imagem com o workflow do repositório.

### Como configurar novos alertas
1. Duplicate uma regra em `prometheus/alerts/canary-rules.yaml`.  
2. Ajuste a expressão Prometheus.  
3. `kubectl apply -f prometheus/alerts/canary-rules.yaml`.  
4. Referencie o alerta no blueprint e, se desejado, adicione painel no Grafana.

### Testes locais
- Rode o exporter: `docker build -t spot-render-observability:dev . && docker run -p 9100:9100 spot-render-observability:dev`.  
- Use o repositório [`spot-render-teste-local`](https://github.com/raafa001/spot-render-teste-local`) para instalar Prometheus/Grafana no cluster e aplicar `ServiceMonitor`.  
- Importe o dashboard JSON via UI do Grafana local.

### TechDocs
- Documentação detalhada em `docs/index.md` + `mkdocs.yml` para publicação no Backstage.
