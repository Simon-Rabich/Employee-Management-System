{{/*
Expand the name of the chart.
*/}}
{{- define "helm-employee-management-system.name" -}}
{{- default .Chart.Name .Values.nameOverride | trunc 63 | trimSuffix "-" -}}
{{- end }}

{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If the release name contains the chart name, it will be used as a full name.
*/}}
{{- define "helm-employee-management-system.fullname" -}}
{{- if .Values.fullnameOverride }}
{{ .Values.fullnameOverride }}
{{- else }}
{{- $name := default .Chart.Name .Values.nameOverride }}
{{- if contains $name .Release.Name }}
{{ .Release.Name | trunc 63 | trimSuffix "-" }}
{{- else }}
{{- printf "%s-%s" .Release.Name $name | trunc 63 | trimSuffix "-" -}}
{{- end }}
{{- end }}
{{- end }}

{{/*
Create chart name and version as used by the chart label.
*/}}
{{- define "helm-employee-management-system.chart" -}}
{{- printf "%s-%s" .Chart.Name .Chart.Version -}}
{{- end }}

{{/*
Common labels
*/}}
{{- define "helm-employee-management-system.labels" -}}
app.kubernetes.io/name: {{ include "helm-employee-management-system.name" . }}
helm.sh/chart: {{ include "helm-employee-management-system.chart" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
{{- end }}

{{/*
Selector labels
*/}}
{{- define "helm-employee-management-system.selectorLabels" -}}
{{- include "helm-employee-management-system.labels" . | indent 4 }}
{{- end }}

{{/*
Define the name of the service account to be used by the deployment.
*/}}
{{- define "helm-employee-management-system.serviceAccountName" -}}
{{- if .Values.serviceAccount.create }}
{{- default (printf "%s-%s" .Release.Name .Chart.Name) .Values.serviceAccount.name | trunc 63 | trimSuffix "-" -}}
{{- else }}
{{- default "default" .Values.serviceAccount.name -}}
{{- end }}
{{- end }}

