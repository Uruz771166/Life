import { useState, useEffect } from 'react'
import { getFramework } from '../api/client'
import SpiralLadder from '../components/SpiralLadder'

function SpiralPage() {
  const [framework, setFramework] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getFramework('spiral_dynamics').then((data) => {
      setFramework(data)
      setLoading(false)
    })
  }, [])

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-gray-500">Loading Spiral Dynamics...</div>
      </div>
    )
  }

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">{framework.name}</h1>
        <p className="text-gray-600 mt-1 max-w-3xl">
          {framework.description}
        </p>
        <p className="text-gray-500 text-sm mt-2">
          By {framework.author}
        </p>
      </div>

      <div className="mb-4 text-sm text-gray-500">
        Click any stage to expand details
      </div>

      <div className="max-w-2xl">
        <SpiralLadder stages={framework.stages} />
      </div>
    </div>
  )
}

export default SpiralPage
