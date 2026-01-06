const API_BASE = '/api/v1'

export async function getDomains(level = null) {
  const url = level !== null
    ? `${API_BASE}/domains?level=${level}`
    : `${API_BASE}/domains`
  const response = await fetch(url)
  return response.json()
}

export async function getDomainTree() {
  const response = await fetch(`${API_BASE}/domains/tree`)
  return response.json()
}

export async function getDomain(code) {
  const response = await fetch(`${API_BASE}/domains/${code}`)
  return response.json()
}

export async function getDomainChildren(code) {
  const response = await fetch(`${API_BASE}/domains/${code}/children`)
  return response.json()
}

export async function getFrameworks() {
  const response = await fetch(`${API_BASE}/frameworks`)
  return response.json()
}

export async function getFramework(code) {
  const response = await fetch(`${API_BASE}/frameworks/${code}`)
  return response.json()
}

export async function getFrameworkStages(code) {
  const response = await fetch(`${API_BASE}/frameworks/${code}/stages`)
  return response.json()
}
