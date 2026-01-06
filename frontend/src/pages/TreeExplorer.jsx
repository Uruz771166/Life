import { useState, useEffect } from 'react'
import { getDomainTree } from '../api/client'
import DomainTree from '../components/DomainTree'

function TreeExplorer() {
  const [tree, setTree] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    getDomainTree().then((data) => {
      setTree(data)
      setLoading(false)
    })
  }, [])

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-gray-500">Loading domain tree...</div>
      </div>
    )
  }

  return (
    <div>
      <div className="mb-8">
        <h1 className="text-2xl font-bold text-gray-900">Domain Tree Explorer</h1>
        <p className="text-gray-600 mt-1">
          Full MECE hierarchy of life domains - click to expand/collapse
        </p>
      </div>

      <DomainTree domains={tree} />
    </div>
  )
}

export default TreeExplorer
