{{/*
Common labels for the application.
*/}}
{{- define "fastapi-app.labels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end -}}

{{/*
Common selector labels for the application.
*/}}
{{- define "fastapi-app.selectorLabels" -}}
app.kubernetes.io/name: {{ .Chart.Name }}
app.kubernetes.io/instance: {{ .Release.Name }}
{{- end -}}

{{/*
Full name template.
*/}}
{{- define "fastapi-app.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end -}}

{{/*
Chart name template.
*/}}
{{- define "fastapi-app.name" -}}
{{ .Chart.Name }}
{{- end -}}
