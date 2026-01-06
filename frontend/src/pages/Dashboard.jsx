import { useState, useEffect } from 'react'
import { getDomains } from '../api/client'
import DomainCard from '../components/DomainCard'

function Dashboard() {
  const [domains, setDomains] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getDomains(0).then((data) => {
      setDomains(data)
      setLoading(false)
    })
  }, [])

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-gray-500">Loading domains...</div>
      </div>
    )
  }

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">Life Domains</h1>
        <p className="text-gray-600 mt-1">
          7 MECE categories covering all areas of life
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {domains.map((domain) => (
          <DomainCard key={domain.id} domain={domain} />
        ))}
      </div>
    </div>
  )
}

export default Dashboard
